import time
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

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

    def wait_for_element_visible(self, locator_type: str, locator_value: str, timeout: int = 30):
        """
        Quick check if an element is visible
        Returns False immediately if an element does not exist

        Args:
            locator_type: The type of locator strategy
            locator_value: The value of the locator
            timeout: Maximum time to wait in seconds (only used if an element is found)

        Returns:
            WebElement: The visible WebElement if found
            False: If the element is not found

        Raises:
            TimeoutException: If the element is not visible after the timeout period
        """
        try:
            self.driver.implicitly_wait(0)
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(
                expected_conditions.visibility_of_element_located((locator_type, locator_value))
            )
        except NoSuchElementException:
            return False
        except TimeoutException:
            actual_timeout = timeout
            raise TimeoutException(
                f"Element ({locator_type}={locator_value}) still not visible after {actual_timeout} seconds"
            )

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

    def scroll_to_element(self, locator_type: str, locator_value: str, scroll_container: str = "//android.widget.ScrollView", max_swipes: int = 5, timeout: float = 0.5) -> bool:
        """
        在 ScrollView 內垂直滾動直到找到指定元件

        Args:
            locator_type: 定位方式（例如：AppiumBy.ID）
            locator_value: 定位值
            scroll_container: 滾動容器的xpath，默認為"//android.widget.ScrollView"
            max_swipes: 最大滑動次數，默認3次
            timeout: 每次滑動後的等待時間（秒），默認0.5秒

        Returns:
            bool: 如果找到並且元件可見返回True，否則返回False
        """
        self.driver.implicitly_wait(0)
        try:
            element = self.driver.find_element(locator_type, locator_value)
            if element.is_displayed():
                return True
        except (NoSuchElementException, StaleElementReferenceException):
            pass

        try:
            # 尋找 ScrollView 容器
            container = self.driver.find_element(By.XPATH, scroll_container)
            container_rect = container.rect

            # 使用容器的尺寸和位置
            start_y = container_rect['y'] + int(container_rect['height'] * 0.8)
            end_y = container_rect['y'] + int(container_rect['height'] * 0.2)
            start_x = container_rect['x'] + (container_rect['width'] // 2)

        except NoSuchElementException:
            print("找不到 ScrollView 容器，改用整個螢幕範圍")
            # 找不到容器時使用整個螢幕的尺寸
            screen_width, screen_height = self.get_screen_size()
            start_y = int(screen_height * 0.8)
            end_y = int(screen_height * 0.2)
            start_x = screen_width // 2

        for _ in range(max_swipes):
            self.swipe(start_x, start_y, start_x, end_y)
            time.sleep(timeout)
            try:
                element = self.driver.find_element(locator_type, locator_value)
                if element.is_displayed():
                    return True
            except (NoSuchElementException, StaleElementReferenceException):
                continue

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

    def wait_for_element_present(self, locator_type: str, locator_value: str, timeout: int = 30) -> bool:
        """
        等待元素在DOM中出現並可見

        Args:
            locator_type: 定位方式
            locator_value: 定位值
            timeout: 最大等待時間（秒）

        Returns:
            bool: 如果元素出現並可見返回True，否則返回False
        """
        try:
            # 暫時禁用隱式等待，避免與顯式等待發生衝突
            self.driver.implicitly_wait(0)
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_disappear(self, locator_type: str, locator_value: str, timeout: int = 30):
        """
        Quick check if an element exists and is visible
        Returns True immediately if an element is not found

        Args:
            locator_type: The type of locator strategy
            locator_value: The value of the locator
            timeout: Maximum time to wait in seconds (only used if an element is found and visible)

        Returns:
            bool: True if an element is not visible or not found
        """
        try:
            self.driver.implicitly_wait(0)
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.invisibility_of_element_located((locator_type, locator_value))
            )
        except NoSuchElementException:
            return True
        except TimeoutException:
            raise TimeoutException(f"Element ({locator_type}={locator_value}) still visible after {timeout} seconds")

    def scroll_to_element_left(self, locator_type: str, locator_value: str, scroll_container: str = "//android.widget.HorizontalScrollView", max_swipes: int = 3, timeout: float = 0.5) -> bool:
        """
        在指定的 HorizontalScrollView 內向左滑動直到找到指定元件

        Args:
            locator_type: 定位方式（例如：AppiumBy.ID）
            locator_value: 定位值
            scroll_container: 滾動容器的xpath，默認為"//android.widget.HorizontalScrollView"
            max_swipes: 最大滑動次數，默認3次
            timeout: 每次滑動後的等待時間（秒），默認0.5秒

        Returns:
            bool: 如果找到並且元件可見返回True，否則返回False
        """

        self.driver.implicitly_wait(0)
        try:
            element = self.driver.find_element(locator_type, locator_value)
            if element.is_displayed():
                return True
        except (NoSuchElementException, StaleElementReferenceException):
            pass

        # 獲取 HorizontalScrollView 的位置和尺寸
        try:
            scroll_view = self.driver.find_element(By.XPATH, scroll_container)
            container_rect = scroll_view.rect

            # 取得滾動容器的座標和尺寸
            container_x = container_rect['x']
            container_y = container_rect['y']
            container_width = container_rect['width']
            container_height = container_rect['height']

            # 計算滑動的起點和終點
            start_x = container_x + int(container_width * 0.8)  # 容器右側80%位置
            end_x = container_x + int(container_width * 0.2)    # 容器左側20%位置
            swipe_y = container_y + (container_height // 2)     # 容器垂直中心位置

            for _ in range(max_swipes):
                self.swipe(start_x, swipe_y, end_x, swipe_y)
                time.sleep(timeout)
                try:
                    element = self.driver.find_element(locator_type, locator_value)
                    if element.is_displayed():
                        return True
                except (NoSuchElementException, StaleElementReferenceException):
                    continue

        except NoSuchElementException:
            print("找不到指定的 HorizontalScrollView")
            return False

        return False