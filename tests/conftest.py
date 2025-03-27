import pytest
import os
import requests
import subprocess
import time

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
    """Add custom markers for tagging tests."""
    config.addinivalue_line("markers", "onboarding: Mark test as onboarding")
    config.addinivalue_line("markers", "login: Mark test as login")
    
    # start recording screen
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # recording_path = f"screen_records/Test_{timestamp}.mp4"
    # os.makedirs("screen_records", exist_ok=True)
    
    # use adb to start recording, store the process object in the config for later stopping
    # config.recording_process = Popen(['adb', 'shell', 'screenrecord', f'/sdcard/{os.path.basename(recording_path)}'])
    # config.recording_path = recording_path


def pytest_bdd_apply_tag(tag, function):
    if tag == 'order':
        marker = pytest.mark.run(order=int(function.__doc__.split('order=')[1]))
        marker(function)
        return True
    return None

def pytest_collection_modifyitems(items):
    items.sort(key=lambda x: x.get_closest_marker('run').args[0] if x.get_closest_marker('run') else 999)
    
    
def pytest_sessionfinish(session, exitstatus):
    """
    Test session finish after the test
    """
    try:
        # stop recording
        # if hasattr(session.config, 'recording_process'):
        #     session.config.recording_process.terminate()
        #     import time
        #     time.sleep(3)
            
        #     # copy recording file from device to local
        #     run(['adb', 'pull', f'/sdcard/{os.path.basename(session.config.recording_path)}', 
        #          session.config.recording_path])
        #     # delete recording file from device
        #     run(['adb', 'shell', 'rm', f'/sdcard/{os.path.basename(session.config.recording_path)}'])
            
        #     # check if file exists and size is not 0
        #     if os.path.exists(session.config.recording_path) and os.path.getsize(session.config.recording_path) > 0:
        #         try:
        #             # ensure allure environment is initialized
        #             if hasattr(session.config.option, 'allure_report_dir'):
        #                 import allure
        #                 # copy video to allure report directory
        #                 allure_video_path = os.path.join(
        #                     session.config.option.allure_report_dir,
        #                     f"Screen_Recording_{time.strftime('%Y%m%d_%H%M%S')}.mp4"
        #                 )
        #                 import shutil
        #                 shutil.copy2(session.config.recording_path, allure_video_path)
                        
        #                 # add video as file path to allure report
        #                 allure.attach.file(
        #                     allure_video_path,
        #                     name="Test Execution Video",
        #                     attachment_type=allure.attachment_type.MP4
        #                 )
        #         except Exception as e:
        #             print(f"Error adding video to allure report: {str(e)}")
        #     else:
        #         print("Recording video file does not exist or is empty")

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
    
    # Clean app state before onboarding test
    if request.node.get_closest_marker('onboarding'):
        # force stop the app
        run(['adb', 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'])
        # uninstall the app
        run(['adb', 'uninstall', 'com.hunger.hotcakeapp.staging'])
    
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

# @pytest.fixture(scope="function", autouse=True)
# def screen_recorder(request):
#     """Screen recorder fixture for test cases with segmented recording"""
#     import threading
#     import time
#     import os
    
#     # Create directory for temporary recordings
#     os.makedirs('allure-results', exist_ok=True)
    
#     # Flag to control recording
#     recording = True
#     segment_count = 0
    
#     def record_segment():
#         nonlocal segment_count
#         while recording:
#             try:
#                 # Start a new segment
#                 segment_file = f'/sdcard/recording_segment_{segment_count}.mp4'
#                 process = subprocess.Popen([
#                     'adb', 'shell', 'screenrecord',
#                     '--time-limit', '6000',  # 10 minutes per segment
#                     '--size', '1280x720',
#                     '--bit-rate', '4000000',
#                     segment_file
#                 ])
#                 process.wait()  # Wait for the segment to complete
                
#                 # Pull the segment file
#                 subprocess.run(['adb', 'pull', segment_file, 
#                               f'allure-results/recording_segment_{segment_count}.mp4'])
#                 subprocess.run(['adb', 'shell', 'rm', segment_file])
                
#                 segment_count += 1
#             except Exception as e:
#                 print(f"Segment recording error: {str(e)}")
    
#     # Start recording thread
#     record_thread = threading.Thread(target=record_segment)
#     record_thread.start()
    
#     yield
    
#     # Stop recording
#     recording = False
#     record_thread.join(timeout=5)
    
#     try:
#         # Combine all segments if there are multiple segments
#         if segment_count > 1:
#             # Create a file list
#             with open('allure-results/segments.txt', 'w') as f:
#                 for i in range(segment_count):
#                     f.write(f"file 'recording_segment_{i}.mp4'\n")
            
#             # Combine segments using ffmpeg
#             subprocess.run([
#                 'ffmpeg', '-f', 'concat', '-safe', '0',
#                 '-i', 'allure-results/segments.txt',
#                 '-c', 'copy',
#                 'allure-results/recording.mp4'
#             ])
            
#             # Clean up segment files
#             for i in range(segment_count):
#                 os.remove(f'allure-results/recording_segment_{i}.mp4')
#             os.remove('allure-results/segments.txt')
#         elif segment_count == 1:
#             # If only one segment, just rename it
#             os.rename('allure-results/recording_segment_0.mp4', 
#                      'allure-results/recording.mp4')
#     except Exception as e:
#         print(f"Error combining video segments: {str(e)}")
    
    
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "login: login related tests"
    )
    config.addinivalue_line(
        "markers",
        "personal: personal related tests"
    )
    config.addinivalue_line(
        "markers",
        "create: create related tests"
    )
    config.addinivalue_line(
        "markers",
        "calendar: calendar related tests"
    )
    config.addinivalue_line(
        "markers",
        "navigation: navigation related tests"
    )
    
    