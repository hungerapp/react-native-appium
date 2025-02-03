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

options = XCUITestOptions()
options.platform_name = platform
options.set_capability('language', 'zh')
options.set_capability('locale', 'TW')

if options.platform_name == 'android':
    #options = UiAutomator2Options()
    options.automation_name = 'UiAutomator2'
    # options.set_capability('platformVersion', '34.0')
    # options.set_capability('deviceName', 'Android Emulator')
    options.set_capability('app', '/Users/ouhiroshishi/Downloads/20241231 application-a987e8b1-5efb-44c5-a812-187862fb75e0.apk')
    options.set_capability('noReset', noReset_bool)
    #options.set_capability('useNewWDA', False)
    options.set_capability('autoGrantPermissions', auto_accept_alerts_bool)

elif options.platform_name == 'ios':
    #options = XCUITestOptions()
    options.automation_name = 'XCUITest'
    options.set_capability('platformVersion', '17.5')
    # options.set_capability('deviceName', 'iPhone 15 Pro')
    options.set_capability('simulatorStartupTimeout', '90000')
    options.set_capability('app', '/Users/ouhiroshishi/Downloads/Runner.app')
    # device: iPhone 15 pro
    #options.set_capability('udid', '9CB10BB7-489C-421B-AAEA-27EEDAF86195')
    options.set_capability('noReset', noReset_bool)
    options.set_capability('autoAcceptAlerts', auto_accept_alerts_bool)
    #options.set_capability('useNewWDA', False)
    # autoFillPassword works only above iOS 16.4 
    options.set_capability('autoFillPassword', False)



appium_server_url = 'http://127.0.0.1:4723'

#@pytest.mark.usefixtures("method", "auth_path")
class AppiumSetup(unittest.TestCase):
    def setUp(self) -> Remote:
        # Setting global variables
        self.config = config
        self.auto_accept_alerts_bool = auto_accept_alerts_bool
        self.noReset_bool = noReset_bool
        self.platform = platform

        self.driver = Remote(appium_server_url, options=options)
        #self.driver.switch_to.context('NATIVE_APP')
        self.driver.implicitly_wait(config['IMPLICIT_WAIT'] or 25)
        
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