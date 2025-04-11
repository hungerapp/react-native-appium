# Description: This file contains helper functions that are used in the test cases.
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from dotenv import dotenv_values

class GetTestHelper():

    config = dotenv_values(".env")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def android_textfield_send_keys(self, value:str, text: str):
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=value)
        el.click()
        el.send_keys(text)

    # TODO: Maybe change the driver capability to accept the save password alert and save time during test
    def ios_accept_save_password(self):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Save Password').click()
        except Exception:
            print("Save password alert not found.")
            pass

    def set_config_implicitly_wait(self):
        self.driver.implicitly_wait(self.config['IMPLICIT_WAIT'] or 15)

