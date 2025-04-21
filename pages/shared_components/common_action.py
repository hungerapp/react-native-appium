from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy

class CommonActions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator_type: str, locator_value: str):
        """
        使用顯式等待查找元素並返回
        """
        return self.wait.until(
            expected_conditions.presence_of_element_located((locator_type, locator_value))
        )

    def is_element_visible(self, locator_type: str, locator_value: str) -> bool:
        """
        檢查元素是否可見並返回布林值
        """
        try:
            self.wait.until(
                expected_conditions.visibility_of_element_located((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False

    def click_element(self, locator_type: str, locator_value: str):
        """
        點擊可點擊的元素
        """
        element = self.wait.until(
            expected_conditions.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()

    def click_if_exists(self, locator_type: str, locator_value: str) -> bool:
        """
        如果元素存在則點擊
        """
        if self.is_element_visible(locator_type, locator_value):
            self.click_element(locator_type, locator_value)
            return True
        return False

    def send_keys_to_element(self, locator_type: str, locator_value: str, text: str):
        """
        向指定元素發送鍵盤輸入
        """
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator_type: str, locator_value: str) -> str:
        """
        獲取元素文本
        """
        element = self.find_element(locator_type, locator_value)
        return element.text

    def wait_for_element_visible(self, locator_type: str, locator_value: str) -> bool:
        """
        等待直到指定元素可見
        """
        try:
            self.wait.until(
                expected_conditions.visibility_of_element_located((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_clickable(self, locator_type: str, locator_value: str) -> bool:
        """
        等待直到指定元素可點擊
        """
        try:
            self.wait.until(
                expected_conditions.element_to_be_clickable((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False

    def verify_element_text(self, locator_type: str, locator_value: str, expected_text: str) -> bool:
        """
        驗證元素文本
        """
        actual_text = self.get_element_text(locator_type, locator_value)
        return actual_text == expected_text

    def verify_element_visible(self, locator_type: str, locator_value: str) -> bool:
        """
        驗證元素是否可見
        """
        return self.is_element_visible(locator_type, locator_value)

    def scroll_to_element(self, locator_type: str, locator_value: str):
        """
        滾動頁面直到指定元素可見
        """
        element = self.find_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 800):
        """
        執行滑動手勢
        """
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def tap(self, x: int, y: int):
        """
        點擊指定座標
        """
        self.driver.tap([(x, y)])

    def hide_keyboard(self):
        """
        隱藏鍵盤
        """
        self.driver.hide_keyboard()

    def get_screen_size(self) -> tuple:
        """
        獲取螢幕尺寸
        """
        return self.driver.get_window_size()
