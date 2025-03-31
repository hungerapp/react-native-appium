import pytest
import os
import requests
import subprocess
import time

from subprocess import run, Popen
from datetime import datetime
from xdist.workermanage import WorkerController
from xdist.scheduler import LoadScheduling, LoadScopeScheduling
from dotenv import load_dotenv

from setup import ANDROID_DEVICES, AppiumSetup
from utils.send_report_to_slack import send_report_to_slack
from utils.logger import logger


# load .env file
load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--appium-port", action="store", default=None, type=int,
                    help="Appium server port")

@pytest.fixture
def driver(request):
    """Set up and tear down Appium driver for the test session."""
    appium_setup = AppiumSetup()
    appium_setup._pytest_request = request
    
    # check if running in xdist worker
    if hasattr(request.config, 'workerinput'):
        worker_id = request.config.workerinput['workerid']
        port = request.config.workerinput['port']
    else:
        # logic for running separately
        markers = [marker.name for marker in request.node.iter_markers()]
        if "personal" in markers:
            worker_id = "gw1"
            port = 4724
        else:
            worker_id = "gw0"
            port = 4723
    
    appium_setup.appium_port = port
    appium_setup.worker_id = worker_id
    
    device_config = ANDROID_DEVICES[worker_id]
    print(f"Setting up driver for worker {worker_id} on port {port} with device {device_config['udid']}")
    driver = appium_setup.setUp()
    yield driver
    appium_setup.tearDown()
    
def pytest_collection_modifyitems(config, items):
    """Process test item collection and sorting"""
    selected_items = []
    for item in items:
        module_name = item.module.__name__
        if ('test_02login_steps' in module_name or 
            'test_01onboarding_steps' in module_name or 
            'test_03personal_page_steps' in module_name):
            selected_items.append(item)
    
    items[:] = selected_items
    
    # Filter tests based on the platform specified in .env
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

def pytest_configure(config):
    """Configure pytest markers"""
    config.addinivalue_line("markers", "login: login related tests run on port 4723")
    config.addinivalue_line("markers", "personal: personal related tests run on port 4724")
    config.addinivalue_line("markers", "create: create related tests")
    config.addinivalue_line("markers", "calendar: calendar related tests")
    config.addinivalue_line("markers", "navigation: navigation related tests")
    config.addinivalue_line("markers", "onboarding: onboarding related tests")
    
    # set xdist allocation strategy to loadfile
    config.option.dist = "loadfile"

def pytest_bdd_apply_tag(tag, function):
    if tag == 'order':
        marker = pytest.mark.run(order=int(function.__doc__.split('order=')[1]))
        marker(function)
        return True
    return None

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

@pytest.fixture(autouse=True)        
def clean_app_state(request):
    '''Each test will re-install when we run the test'''
    print(f"Current test name: {request.node.name}")
    print(f"Module name: {request.node.module.__name__}")
    print(f"Module file path: {request.node.module.__file__}")
    
    if not hasattr(request.node, 'retry_count'):
        request.node.retry_count = 0
    
    # check environment variable
    platform = os.getenv('APPIUM_OS', 'android').lower()
    print(f"Current platform from .env: {platform}")
    
    # Clean app state before onboarding test
    if request.node.get_closest_marker('onboarding'):
        if platform == 'android':
            # 決定使用哪個設備
            if hasattr(request.config, 'workerinput'):
                worker_id = request.config.workerinput['workerid']
                port = request.config.workerinput['port']
            else:
                markers = [marker.name for marker in request.node.iter_markers()]
                if "personal" in markers:
                    worker_id = "gw1"
                    port = 4724
                else:
                    worker_id = "gw0"
                    port = 4723
            
            device_config = ANDROID_DEVICES[worker_id]
            print(f"Cleaning app state for worker {worker_id} on port {port} with device {device_config['udid']}")
            
            # Android cleanup
            run(['adb', '-s', device_config['udid'], 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'])
            run(['adb', '-s', device_config['udid'], 'uninstall', 'com.hunger.hotcakeapp.staging'])
            
        elif platform == 'ios':
            # iOS cleanup
            device_id = os.getenv('UDID')
            app_path = os.getenv('IOS_APP_PATH')
            
            print(f"iOS device ID: {device_id}")
            print(f"iOS app path: {app_path}")
            
            if device_id and app_path:
                # reset simulator
                run(['xcrun', 'simctl', 'erase', device_id])
                # install app
                run(['xcrun', 'simctl', 'install', device_id, app_path])
            else:
                print("Warning: Please ensure UDID and IOS_APP_PATH are set in .env")
    
    yield
    
    """
    # TODO: 先保留並註解, 等有需要再討論fail rerun 方式
    try:
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            if request.node.retry_count >= 3:
                print(f"Test {request.node.name} 已達到最大重試次數 (3次)，不再重試")
                return
                
            request.node.retry_count += 1
            print(f"Test {request.node.name} failed, 第 {request.node.retry_count} 次重試...")
            
            print("正在停止 app...")
            run(['adb', 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'])
           
            
        
            print("正在啟動 app...")
            run(['adb', 'shell', 'am', 'start', '-n', 'com.hunger.hotcakeapp.staging/com.hunger.hotcakeapp.staging.MainActivity'])
            #time.sleep(8) 
            
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
            
            print(f"準備進行下一次測試...")
            time.sleep(10)
        
    except Exception as e:
        print(f"Error during cleanup and relogin: {str(e)}")
        
    """

def pytest_configure_node(node):
    """這個 hook 會在 worker 節點配置時被調用"""
    worker_id = node.gateway.id
    if worker_id == "gw0":
        node.workerinput['port'] = 4723
        node.workerinput['marker'] = 'login'
        node.workerinput['workerid'] = 'gw0'
    elif worker_id == "gw1":
        node.workerinput['port'] = 4724
        node.workerinput['marker'] = 'personal'
        node.workerinput['workerid'] = 'gw1'
    print(f"Configuring node {worker_id} with port {node.workerinput['port']}")

def pytest_runtest_setup(item):
    """Setup a test item"""
    if hasattr(item.config, 'workerinput'):
        worker_id = item.config.workerinput['workerid']
        port = item.config.workerinput['port']
        module_name = item.module.__name__
        print(f"Setting up test {item.name} on worker {worker_id} (port {port}) from module {module_name}")
        
        # 確保測試在正確的 worker 上執行
        if worker_id == 'gw0' and ('test_02login_steps.py' in module_name or 'test_01onboarding_steps.py' in module_name):
            pytest.skip(f"Test {item.name} should run on gw1")
        elif worker_id == 'gw1' and 'test_03personal_page_steps.py' in module_name:
            pytest.skip(f"Test {item.name} should run on gw0")

def pytest_xdist_node_collection_finished(node, ids):
    """determine which tests to run based on worker"""
    worker_id = node.gateway.id
    filtered_ids = []
    
    # ensure all workers collect the same tests
    for test_id in ids:
        if 'test_02login_steps.py' in test_id or 'test_01onboarding_steps.py' in test_id or 'test_03personal_page_steps.py' in test_id:
            filtered_ids.append(test_id)
    
    print(f"Worker {worker_id} will run tests: {filtered_ids}")
    return filtered_ids
