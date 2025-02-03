import pytest
from subprocess import run, Popen
from setup import AppiumSetup
from utils.send_report_to_slack import send_report_to_slack
from datetime import datetime
import os

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
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    recording_path = f"screen_records/Test_{timestamp}.mp4"
    os.makedirs("screen_records", exist_ok=True)
    
    # use adb to start recording, store the process object in the config for later stopping
    config.recording_process = Popen(['adb', 'shell', 'screenrecord', f'/sdcard/{os.path.basename(recording_path)}'])
    config.recording_path = recording_path
    

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
        if hasattr(session.config, 'recording_process'):
            session.config.recording_process.terminate()
            import time
            time.sleep(3)
            
            # copy recording file from device to local
            run(['adb', 'pull', f'/sdcard/{os.path.basename(session.config.recording_path)}', 
                 session.config.recording_path])
            # delete recording file from device
            run(['adb', 'shell', 'rm', f'/sdcard/{os.path.basename(session.config.recording_path)}'])
            
            # check if file exists and size is not 0
            if os.path.exists(session.config.recording_path) and os.path.getsize(session.config.recording_path) > 0:
                try:
                    # ensure allure environment is initialized
                    if hasattr(session.config.option, 'allure_report_dir'):
                        import allure
                        # copy video to allure report directory
                        allure_video_path = os.path.join(
                            session.config.option.allure_report_dir,
                            f"Screen_Recording_{time.strftime('%Y%m%d_%H%M%S')}.mp4"
                        )
                        import shutil
                        shutil.copy2(session.config.recording_path, allure_video_path)
                        
                        # add video as file path to allure report
                        allure.attach.file(
                            allure_video_path,
                            name="Test Execution Video",
                            attachment_type=allure.attachment_type.MP4
                        )
                except Exception as e:
                    print(f"Error adding video to allure report: {str(e)}")
            else:
                print("Recording video file does not exist or is empty")

        # check if --alluredir parameter is used
        if hasattr(session.config.option, 'allure_report_dir'):
            print("開始處理 Allure 報告...")
            
            # Get the Webhook URL
            webhook_url = "https://hooks.slack.com/services/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"
            print(f"使用 Webhook URL: {webhook_url}")
            
            # Generate Allure report
            import subprocess
            subprocess.run(['allure', 'generate', 'allure-results', '-o', 'allure-report', '--clean'], check=True)
            print("Allure 報告生成完成")
            
            # Send report to Slack
            allure_report_path = "allure-report"
            print("開始發送報告到 Slack...")
            send_report_to_slack(webhook_url, allure_report_path)

    except Exception as e:
        print(f"Error processing and sending report: {str(e)}")
        import traceback
        print(traceback.format_exc())

@pytest.fixture(autouse=True)        
def clean_app_state(request):
    '''Each test will re-install when we run the test'''
    print(f"Current test name: {request.node.name}")
    print(f"Module name: {request.node.module.__name__}")
    print(f"Module file path: {request.node.module.__file__}")
    
    # only clean the app state before the first test
    if request.node.get_closest_marker('onboarding'): # or use the exact name of your first test
        # force stop the app
        run(['adb', 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'])
        # uninstall the app
        run(['adb', 'uninstall', 'com.hunger.hotcakeapp.staging'])
    
    yield
    
    # only clean the app state after the test
    if request.session.testsfailed > 0:
        # force stop the app
        run(['adb', 'shell', 'am', 'force-stop', 'com.hunger.hotcakeapp.staging'])
        # uninstall the app
        run(['adb', 'uninstall', 'com.hunger.hotcakeapp.staging'])
    