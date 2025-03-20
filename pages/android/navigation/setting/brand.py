import time

from appium.webdriver.common.appiumby import AppiumBy


class BrandPage:
    def __init__(self, driver):
        self.driver = driver
        # 定義直接在類別內的定位元素
        self.SETTINGS_OPTION = (AppiumBy.ACCESSIBILITY_ID, '設定')

    def tap_settings_option(self):
        self.driver.find_element(*self.SETTINGS_OPTION).click()
        time.sleep(0.5)
        return self