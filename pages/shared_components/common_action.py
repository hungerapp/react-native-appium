import time
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

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

    def is_element_visible(self, locator_type: str, locator_value: str):
        """
        檢查元素是否存在且可見
        """
        element = self.driver.find_element(locator_type, locator_value)
        return self.wait.until(
            expected_conditions.visibility_of(element)
        )

    def is_element_present(self, locator_type: str, locator_value: str) -> bool:
        """
        檢查元素是否存在
        """
        try:
            self.driver.find_element(locator_type, locator_value)
            return True
        except NoSuchElementException:
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

    def clear_text(self, locator_type: str, locator_value: str):
        """
        清除指定元素的文本
        """
        element = self.find_element(locator_type, locator_value)
        element.clear()

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



    def scroll_to_element(self, locator_type: str, locator_value: str, max_swipes: int = 3, timeout: int = 2) -> bool:
        """
        滾動螢幕直到指定元素可見

        Args:
            locator_type: 定位器類型 (例如 AppiumBy.ID)
            locator_value: 定位器的值
            max_swipes: 最大滑動嘗試次數，默認3次
            timeout: 每次滑動後的等待時間（秒），默認2秒

        Returns:
            bool: 找到並可見元素時返回True，否則返回False
        """
        from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

        try:
            element = self.driver.find_element(locator_type, locator_value)
            if element.is_displayed():
                return True
        except (NoSuchElementException, StaleElementReferenceException):
            pass

        screen_width, screen_height = self.get_screen_size()
        start_y = int(screen_height * 0.8)
        end_y = int(screen_height * 0.2)
        start_x = screen_width // 2

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(locator_type, locator_value)
                if element.is_displayed():
                    return True
                self.swipe(start_x, start_y, start_x, end_y)
                time.sleep(timeout)
            except (NoSuchElementException, StaleElementReferenceException):
                self.swipe(start_x, start_y, start_x, end_y)
                time.sleep(timeout)

        return False

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
        return self.driver.get_window_size()['width'], self.driver.get_window_size()['height']

    def wait_for_element_present(self, locator_type: str, locator_value: str, timeout: int = 30):
        """
        Wait for an element to be present in the DOM and visible

        Args:
            locator_type: The type of locator strategy
            locator_value: The value of the locator
            timeout: Maximum time to wait in seconds

        Returns:
            WebElement: The found element

        Raises:
            TimeoutException: When an element is not present within a specified timeout
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element ({locator_type}={locator_value}) not present within {timeout} seconds")

    def wait_for_element_disappear(self, locator_type: str, locator_value: str, timeout: int = 30):
        """
        Wait for an element to disappear from the page (either not visible or not in DOM)

        Args:
            locator_type: The type of locator strategy
            locator_value: The value of the locator
            timeout: Maximum time to wait in seconds

        Returns:
            bool: True if an element successfully disappeared

        Raises:
            TimeoutException: When an element remains visible within specified timeout
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.invisibility_of_element_located((locator_type, locator_value))
            )
        except TimeoutException:
            raise TimeoutException(f"Element ({locator_type}={locator_value}) still visible after {timeout} seconds")