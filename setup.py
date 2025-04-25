import time
import pytest
import unittest
import os
from dotenv import dotenv_values
from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from utils.helpers import GetTestHelper

# TODO: Move the config and options to a separate file
config = dotenv_values(".env")

# 設置默認值
noReset_bool = True if config.get('NO_RESET', 'True') == 'True' else False
platform = config.get('APPIUM_OS', 'android')
auto_accept_alerts_bool = True if config.get('AUTO_ACCEPT_ALERTS', 'True') == 'True' else False
is_ci = config.get('IS_CI', 'false').lower() == 'true'

# 根據環境選擇配置
if is_ci:
    # BrowserStack 配置
    browserstack_options = {
        'userName': config.get('BROWSERSTACK_USERNAME'),
        'accessKey': config.get('BROWSERSTACK_ACCESS_KEY'),
        'projectName': config.get('BROWSERSTACK_PROJECT_NAME', 'App E2E Tests'),
        'buildName': config.get('BROWSERSTACK_BUILD_NAME', 'GitHub Actions Build'),
        'sessionName': config.get('BROWSERSTACK_SESSION_NAME', 'E2E Test Session'),
        'deviceName': config.get('BROWSERSTACK_DEVICE_NAME', 'Google Pixel 8'),
        'osVersion': config.get('BROWSERSTACK_OS_VERSION', '14.0'),
        'interactiveDebugging': True,
        'debug': True,
        'networkLogs': True,
        'appiumLogs': True,
        'deviceLogs': True,
        'video': True
    }

    if platform == 'android':
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.app = config.get('BROWSERSTACK_APP_ID')
        options.set_capability('autoGrantPermissions', True) 
        options.set_capability('bstack:options', browserstack_options)
        # BrowserStack 特定配置
        options.set_capability('disableAnimation', False)
        options.set_capability('uiautomator2ServerInstallTimeout', 60000)
        options.set_capability('androidDeviceReadyTimeout', 60)
        options.set_capability('newCommandTimeout', 300)
        options.set_capability('androidInstallTimeout', 90000)
        options.set_capability('adbExecTimeout', 60000)
    
    else:  # iOS
        options = XCUITestOptions()
        options.platform_name = 'iOS'
        options.automation_name = 'XCUITest'
        options.deviceName = config.get('BROWSERSTACK_DEVICE_NAME', 'iPhone 15 Pro')
        options.os_version = config.get('BROWSERSTACK_OS_VERSION', '17.5')
        options.app = config.get('BROWSERSTACK_APP_ID')
        options.set_capability('autoAcceptAlerts', True) 
        options.set_capability('bstack:options', browserstack_options)
        options.set_capability('simulatorStartupTimeout', 60000)
        options.set_capability('disableAnimation', False)
    appium_server_url = config.get('BROWSERSTACK_HUB_URL', 'https://hub-cloud.browserstack.com/wd/hub')
else:
    # 本地配置
    if platform == 'android':
        options = UiAutomator2Options()
        options.platform_name = platform
        options.automation_name = 'UiAutomator2'
        options.set_capability('language', 'zh')
        options.set_capability('locale', 'TW')
        options.set_capability('app', config.get('ANDROID_APP_PATH'))
        options.set_capability('noReset', noReset_bool)
        options.set_capability('autoGrantPermissions', auto_accept_alerts_bool)
    else:  # iOS
        options = XCUITestOptions()
        options.platform_name = platform
        options.automation_name = 'XCUITest'
        options.set_capability('language', 'zh')
        options.set_capability('locale', 'TW')
        options.set_capability('platformVersion', '17.5')
        options.set_capability('simulatorStartupTimeout', '90000')
        options.set_capability('app', config.get('IOS_APP_PATH'))
        options.set_capability('noReset', noReset_bool)
        options.set_capability('autoAcceptAlerts', auto_accept_alerts_bool)
        options.set_capability('autoFillPassword', False)
    appium_server_url = config.get('APPIUM_SERVER_URL', 'http://127.0.0.1:4723')

# 本地設備配置（僅在非 CI 環境中使用）
'''
if not is_ci and platform == 'android':
    ANDROID_DEVICES = [
        {
            'name': 'device1',
            'port': 4723,
            'udid': 'emulator-5554',
            'systemPort': 8200,
        },
        {
            'name': 'device2',
            'port': 4724,
            'udid': 'emulator-5556',
            'systemPort': 8201,
        },
        {
            'name': 'device3',
            'port': 4725,
            'udid': 'emulator-5558',
            'systemPort': 8202,
        }
    ]
'''

class AppiumSetup(unittest.TestCase):
    def setUp(self) -> Remote:
        # Setting global variables
        self.config = config
        self.auto_accept_alerts_bool = auto_accept_alerts_bool
        self.noReset_bool = noReset_bool
        self.platform = platform

        # Create screenshots directory only in local environment
        if not is_ci:
            screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

        self.driver = Remote(appium_server_url, options=options)
        #self.driver.switch_to.context('NATIVE_APP')
        self.driver.implicitly_wait(int(config.get('IMPLICIT_WAIT', '25')))
        
        # Save BrowserStack session ID if running in CI
        if is_ci:
            with open('browserstack_session_id.txt', 'w') as f:
                f.write(self.driver.session_id)
        
        # Initialize  TestHelper
        self.helper = GetTestHelper(self.driver)
        return self.driver
    
    def screen_shot(self, name: str):
        self.driver.save_screenshot(f'{name}-{time.time()}.png')

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
            time.sleep(10)

if __name__ == '__main__':
    unittest.main()