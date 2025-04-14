import pytest
import os
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
        print(f"Configuring test collection for platform: {platform}")
        
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
    print(f"Running tests for platform: {platform}")
    
    filtered_items = []
    for item in items:
        file_path = str(item.fspath)
        if platform == 'ios' and '/ios/' in file_path:
            filtered_items.append(item)
        elif platform == 'android' and '/android/' in file_path:
            filtered_items.append(item)
    
    items[:] = filtered_items
    print(f"Filtered test count: {len(filtered_items)}")

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
            
            # Get the Webhook URL
            webhook_url = "https://hooks.slack.com/services/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"
            print(f"使用 Webhook URL: {webhook_url}")
            
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs.get('driver')
            if driver is not None:
                # make sure the artifacts/screenshots directory exists
                os.makedirs('artifacts/screenshots', exist_ok=True)
                
                # generate the screenshot file name
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                screenshot_path = f"artifacts/screenshots/{item.name}_{timestamp}.png"
                
                # save the screenshot to the file
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved to: {screenshot_path}")
                
                # if you want to display the screenshot in the Allure report, uncomment the following code
                # screenshot = driver.get_screenshot_as_png()
                # if screenshot:
                #     allure.attach(
                #         screenshot,
                #         name=f"screenshot_{item.name}",
                #         attachment_type=allure.attachment_type.PNG
                #     )
            else:
                print(f"No driver instance found for test: {item.name}")
        except Exception as e:
            print(f"Failed to take screenshot: {str(e)}")

@pytest.fixture(autouse=True)        
def clean_app_state(request):
    '''Each test will re-install when we run the test'''
    print(f"Current test name: {request.node.name}")
    print(f"Module name: {request.node.module.__name__}")
    print(f"Module file path: {request.node.module.__file__}")
    
    # check environment variable
    platform = os.getenv('APPIUM_OS', 'android').lower()
    is_ci = os.getenv('IS_CI', 'false').lower() == 'true'
    print(f"Current platform from .env: {platform}")
    print(f"Running in CI environment: {is_ci}")
    
    if not hasattr(request.node, 'retry_count'):
        request.node.retry_count = 0
    
    # if running in CI, skip local cleanup
    if is_ci:
        print("Running in BrowserStack - skipping local cleanup")
        yield
    else:
        # local cleanup
        if request.node.get_closest_marker('onboarding'):
            if platform == 'android':
                try:
                    # Android cleanup
                    run(['adb', 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'])
                    run(['adb', 'uninstall', 'com.hunger.hotcakeapp.staging'])
                except Exception as e:
                    print(f"Warning: Local cleanup failed - {str(e)}")
            elif platform == 'ios':
                # iOS cleanup
                app_path = os.getenv('IOS_APP_PATH')
                if app_path:
                    try:
                        # For simulator
                        run(['xcrun', 'simctl', 'uninstall', 'booted', 'com.hunger.hotcakeapp.staging'])
                        run(['xcrun', 'simctl', 'install', 'booted', app_path])
                    except Exception as e:
                        print(f"Warning: Local cleanup failed - {str(e)}")
                else:
                    print("Warning: Please ensure IOS_APP_PATH is set in .env")
        
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
                
                print(f"準備進行下一次測試...")
                time.sleep(10)
            
        except Exception as e:
            print(f"Error during cleanup and relogin: {str(e)}")
        """
