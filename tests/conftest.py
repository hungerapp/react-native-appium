import os
import pytest
import requests
import subprocess
import time
import allure


from dotenv import load_dotenv

# load .env file
load_dotenv()

from subprocess import run, Popen
from datetime import datetime

from setup import AppiumSetup
from utils.send_report_to_slack import send_report_to_slack
from utils.logger import logger
from screenshot_hooks import pytest_runtest_makereport
from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection
from tests.steps.android.test_setup import setup_flow


@pytest.fixture(scope="session")
def driver():
    """Set up and tear down Appium driver for the test session."""
    appium_setup = AppiumSetup()
    driver = appium_setup.setUp()
    yield driver
    appium_setup.tearDown()

def pytest_configure(config):
    """Configure test collection and markers"""
    config.addinivalue_line("markers", "onboarding: Mark test as onboarding")
    config.addinivalue_line("markers", "login: login related tests run on port 4723")
    config.addinivalue_line("markers", "personal: personal related tests run on 4724")
    config.addinivalue_line("markers", "create: create related tests")
    config.addinivalue_line("markers", "calendar: calendar related tests")
    config.addinivalue_line("markers", "navigation: navigation related tests")
    
    if not config.args:
        platform = os.getenv('APPIUM_OS', 'android').lower()
        logger.info(f"Configuring test collection for platform: {platform}")
        
        if platform == 'ios':
            config.args = ['tests/steps/ios']
        else:
            config.args = ['tests/steps/android']


def pytest_bdd_apply_tag(tag, function):
    if tag == 'order':
        marker = pytest.mark.run(order=int(function.__doc__.split('order=')[1]))
        marker(function)
        return True
    return None

def pytest_collection_modifyitems(items):
    """Filter tests based on the platform specified in .env"""
    platform = os.getenv('APPIUM_OS', 'android').lower()
    logger.info(f"Running tests for platform: {platform}")
    
    filtered_items = []
    for item in items:
        file_path = str(item.fspath)
        if platform == 'ios' and '/ios/' in file_path:
            filtered_items.append(item)
        elif platform == 'android' and '/android/' in file_path:
            filtered_items.append(item)
    
    items[:] = filtered_items
    logger.info(f"Filtered test count: {len(filtered_items)}")

def pytest_sessionfinish(session):
    """
    Test session finish after the test
    """
    try:
        # only send report to slack if allure_report_dir is used
        if hasattr(session.config.option, 'allure_report_dir') and session.config.option.allure_report_dir:  
            print("開始處理 Allure 報告...")
            
            all_tests = session.items
            
            skipped_tests = 0
            total_scenarios = 0
            
            for item in all_tests:
                
                total_scenarios += 1
                if item.get_closest_marker('skip'):
                    skipped_tests += 1

                elif hasattr(item, 'function') and hasattr(item.function, '__scenario__'):
                    scenario = item.function.__scenario__
                    if hasattr(scenario, 'tags') and '@skip' in scenario.tags:
                        skipped_tests += 1
            
            allure_report_path = 'allure-report'
            
            # Get the Webhook URL from GitHub secrets
            webhook_url = "${{ secrets.SLACK_WEBHOOK_URL }}"
            if not webhook_url:
                print("Warning: SLACK_WEBHOOK_URL not set")
                return
            print("Slack webhook URL configured")
            
            # Generate Allure report
            subprocess.run(['allure', 'generate', 'allure-results', '-o', allure_report_path, '--clean'], check=True)
            print("Allure 報告生成完成")
            
            with open('allure-report/widgets/summary.json', 'r') as f:
                import json
                summary = json.load(f)
                
           
            total_duration_seconds = summary.get('time', {}).get('duration', 0) / 1000  
            minutes = int(total_duration_seconds // 60)
            seconds = int(total_duration_seconds % 60)
            
        
            statistic = summary.get('statistic', {})
            passed = statistic.get('passed', 0)
            failed = statistic.get('failed', 0)
            

            skipped = skipped_tests
            total = total_scenarios
            
            print(f"測試統計：")
            print(f"總測試案例數: {total}")
            print(f"通過測試數: {passed}")
            print(f"失敗測試數: {failed}")
            print(f"跳過測試數: {skipped}")
            
            message = {
                "text": "APP自動化測試報告 📱",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*APP自動化測試報告 📱*\n執行時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*測試結果:*\n總數: {total}\n通過: {passed}  ✅\n"
                                       f"失敗: {failed}  ❌\n跳過-開發中: {skipped}  ⏭️\n"
                                       f"執行時間: {minutes}分{seconds}秒 ⏱️"
                            }
                        ]
                    }
                ]
            }
            
            print("開始發送報告到 Slack...")
            send_report_to_slack(webhook_url, allure_report_path, message)
            

    except Exception as e:
        print(f"Error processing and sending report: {str(e)}")
        import traceback
        print(traceback.format_exc())

@pytest.fixture(autouse=True)
def clean_app_state(driver, common_actions, request):
    """每個測試前都重新安裝 App 並執行 onboarding + login（包含 CI）"""

    test_name = request.node.name
    print(f"\n🔁 Preparing test: {test_name}")

    platform = os.getenv('APPIUM_OS', 'android').lower()
    email = os.getenv('TEST_EMAIL', 'test@example.com')
    ver_code = os.getenv('VERIFICATION_CODE', '123456')

    print(f"🧪 Platform: {platform}")

    # --- App 清理流程（包含 CI） ---
    try:
        if platform == 'android':
            print("📱 Cleaning Android app...")
            run(['adb', 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'], check=True)
            run(['adb', 'uninstall', 'com.hunger.hotcakeapp.staging'], check=True)
        elif platform == 'ios':
            print("🍎 Cleaning iOS app...")
            app_path = os.getenv('IOS_APP_PATH')
            if app_path:
                run(['xcrun', 'simctl', 'uninstall', 'booted', 'com.hunger.hotcakeapp.staging'], check=True)
                run(['xcrun', 'simctl', 'install', 'booted', app_path], check=True)
            else:
                print("⚠️ Please set IOS_APP_PATH in your .env")
    except Exception as e:
        print(f"⚠️ App cleanup failed: {e}")

    # --- Onboarding + login 流程 ---
    print("🚀 Running onboarding & login setup flow...")
    try:
        setup_flow(driver, common_actions, email, ver_code)
    except Exception as e:
        print(f"❌ Onboarding/Login flow failed: {e}")

    yield
        
    """
    # TODO: 本地環境的重試邏輯，暫時註解掉
    # 等待穩定後再討論是否需要重新啟用
    try:
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            if request.node.retry_count >= 3:
                print(f"Test {request.node.name} 已達到最大重試次數 (3次)，不再重試")
                return
                
            request.node.retry_count += 1
            print(f"Test {request.node.name} failed, 第 {request.node.retry_count} 次重試...")
            
            if platform == 'android':
                try:
                    print("正在停止 app...")
                    run(['adb', 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'])
                    
                    print("正在啟動 app...")
                    run(['adb', 'shell', 'am', 'start', '-n', 'com.hunger.hotcakeapp.staging/com.hunger.hotcakeapp.staging.MainActivity'])
                    
                    print("開始重新登入...")
                    try:
                        from pages.android.login_page import LoginPage 
                        login_page = LoginPage(driver)
                        
                        time.sleep(5)
                        
                        TEST_EMAIL = "ann@hunger.ai" 
                        TEST_VER = "5556666"  
                        
                        login_page.click_logout_button()
                        login_page.login(TEST_EMAIL, TEST_VER)
                        
                        login_page.is_logged_in()
                        print("重新登入完成")
                        
                    except Exception as e:
                        print(f"登入過程發生錯誤: {str(e)}")
                        import traceback
                        print(traceback.format_exc())
                        raise
                except Exception as e:
                    print(f"重試過程發生錯誤: {str(e)}")
            
    except Exception as e:
        print(f"Error during cleanup and relogin: {str(e)}")
    """
        
@pytest.fixture
def common_actions(driver):
    return CommonActions(driver)

@pytest.fixture
def common_use(driver):
    return CommonUseSection(driver) 
        