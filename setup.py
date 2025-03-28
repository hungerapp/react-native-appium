import time
import pytest
import unittest
from dotenv import dotenv_values
from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from utils.helpers import GetTestHelper

# TODO: Move the config and options to a separate file
config = dotenv_values(".env")

noReset_bool = True if config['NO_RESET'] == 'True' else False
platform = config['APPIUM_OS']
auto_accept_alerts_bool = True if config['AUTO_ACCEPT_ALERTS'] == 'True' else False

# Android devices
ANDROID_DEVICES = {
    'gw0': {  # worker ID
        'udid': 'emulator-5554',
        'systemPort': 8200,
        'marker': 'login',  
        'avd': 'Pixel_8a_API_35',
        'appium_port': 4723
    },
    'gw1': {
        'udid': 'emulator-5556',
        'systemPort': 8201,
        'marker': 'personal',  
        'avd': 'Pixel_8a_API_35-2',
        'appium_port': 4724 
    }
}

# basic options setup
options = XCUITestOptions()
options.platform_name = platform
options.set_capability('language', 'zh')
options.set_capability('locale', 'TW')

if options.platform_name == 'android':
    options = UiAutomator2Options()
    options.automation_name = 'UiAutomator2'
    # options.set_capability('platformVersion', '34.0')
    # options.set_capability('deviceName', 'Android Emulator')
    options.set_capability('app', config['ANDROID_APP_PATH'])
    options.set_capability('noReset', noReset_bool)
    #options.set_capability('useNewWDA', False)
    options.set_capability('autoGrantPermissions', auto_accept_alerts_bool)

elif options.platform_name == 'ios':
    #options = XCUITestOptions()
    options.automation_name = 'XCUITest'
    options.set_capability('platformVersion', '17.5')
    # options.set_capability('deviceName', 'iPhone 15 Pro')
    options.set_capability('simulatorStartupTimeout', '90000')
    options.set_capability('app', config['IOS_APP_PATH'])
    # device: iPhone 15 pro
    #options.set_capability('udid', '9CB10BB7-489C-421B-AAEA-27EEDAF86195')
    options.set_capability('noReset', noReset_bool)
    options.set_capability('autoAcceptAlerts', auto_accept_alerts_bool)
    #options.set_capability('useNewWDA', False)
    # autoFillPassword works only above iOS 16.4 
    options.set_capability('autoFillPassword', False)



class AppiumSetup(unittest.TestCase):
    def setUp(self) -> Remote:
        worker_id = getattr(self, 'worker_id', None)
        appium_port = getattr(self, 'appium_port', None)
        
        # decide which device to use
        device_config = None
        
        # 1. first check if there is a specified appium_port
        if appium_port:
            for device_id, device in ANDROID_DEVICES.items():
                if device['appium_port'] == appium_port:
                    device_config = device
                    break
        
        # 2. if no config found through port, check marker
        if not device_config and hasattr(self, '_pytest_request'):
            for marker in self._pytest_request.node.iter_markers():
                for device_id, device in ANDROID_DEVICES.items():
                    if device['marker'] == marker.name:
                        device_config = device
                        break
        
        # 3. if still no config found, use gw0
        if not device_config:
            device_config = ANDROID_DEVICES['gw0']
        
        # Setting Appium server URL
        appium_server_url = f'http://127.0.0.1:{device_config["appium_port"]}'
        print(f"Using device config: {device_config}")
        print(f"Connecting to Appium server at: http://127.0.0.1:{device_config['appium_port']}")

        
        if platform == 'android':
            options.set_capability('udid', device_config['udid'])
            options.set_capability('systemPort', device_config['systemPort'])
            options.set_capability('platformName', 'Android')
            options.set_capability('automationName', 'UiAutomator2')
            options.set_capability('deviceName', device_config['avd'])
        
        # Setting global variables
        self.config = config
        self.auto_accept_alerts_bool = auto_accept_alerts_bool
        self.noReset_bool = noReset_bool
        self.platform = platform

        self.driver = Remote(appium_server_url, options=options)
        self.driver.implicitly_wait(config['IMPLICIT_WAIT'] or 25)
        
        # Initialize TestHelper
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