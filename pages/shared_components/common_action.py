import time

from typing import Tuple, Union
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder

class CommonActions:
    def __init__(self, driver: WebDriver, default_timeout: int = 10):
        """
        Args:
            driver: WebDriver instance
            default_timeout: default timeout (seconds)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, default_timeout)
        self.default_timeout = default_timeout

    def find_element(self, locator_type: str, locator_value: str, timeout: int = None):
        """
        使用顯式等待查找元素並返回
        增加重試機制以提高穩定性

        Args:
            locator_type: 定位方式
            locator_value: 定位值
            timeout: 可選的等待時間，如果不指定則使用默認值

        Returns:
            WebElement: 找到的元素

        Raises:
            TimeoutException: 如果在指定時間內未找到元素
        """
        if timeout is None:
            timeout = self.default_timeout

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((locator_type, locator_value))
                )
            except (TimeoutException, StaleElementReferenceException) as e:
                if attempt == max_attempts - 1:
                    raise TimeoutException(
                        f"Element ({locator_type}={locator_value}) not found after {max_attempts} attempts"
                    ) from e
                time.sleep(1) 

    def is_element_visible(self, locator_type: str, locator_value: str, timeout: int = None):
        """
        檢查元素是否存在且可見
        """
        if timeout is None:
            timeout = self.default_timeout

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((locator_type, locator_value))
                )
                return True
            except (TimeoutException, StaleElementReferenceException):
                if attempt == max_attempts - 1:
                    return False
                time.sleep(1)
        return False

    def is_element_present(self, locator_type: str, locator_value: str) -> bool:
        """
        檢查元素是否存在
        """
        try:
            self.driver.find_element(locator_type, locator_value)
            return True
        except NoSuchElementException:
            return False

    def click_element(self, locator_type: str, locator_value: str, timeout: int = None):
        """
        點擊可點擊的元素
        """
        if timeout is None:
             timeout = self.default_timeout

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((locator_type, locator_value))
                )
                element.click()
                return
            except (TimeoutException, StaleElementReferenceException) as e:
                if attempt == max_attempts - 1:
                    raise TimeoutException(
                        f"Element ({locator_type}={locator_value}) not clickable after {max_attempts} attempts"
                    ) from e
                time.sleep(1)

    def click_if_exists(self, locator_type: str, locator_value: str) -> bool:
        """
        如果元素存在則點擊
        """
        if self.is_element_visible(locator_type, locator_value):
            self.click_element(locator_type, locator_value)
            return True
        return False

    def send_keys_to_element(self, locator_or_element, text: str = None, locator_value: str = None):
        """
        向指定元素發送鍵盤輸入
        支援兩種使用方式：
        1. 傳入定位器: send_keys_to_element(*LoginLocators.EMAIL_INPUT, "text")
        2. 傳入元素: send_keys_to_element(element, "text")
        """
        if isinstance(locator_or_element, WebElement):
            element = locator_or_element
            element.clear()
            element.send_keys(text)
        else:
            element = self.wait.until(
                EC.visibility_of_element_located((locator_or_element, locator_value))
            )
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
        快速檢查元素是否可見
        如果元素不存在則立即返回 False

        Args:
            locator_type: 定位方式
            locator_value: 定位值
            timeout: 最大等待時間（秒）

        Returns:
            WebElement: 如果元素可見返回 WebElement，否則返回 False

        Raises:
            TimeoutException: 如果元素在指定時間內未可見
        """
        try:
            self.driver.implicitly_wait(0)
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(
                EC.visibility_of_element_located((locator_type, locator_value))
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
                EC.element_to_be_clickable((locator_type, locator_value))
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
            bool: 如果找到並且元件可見返回 True，否則返回 False
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

    def tap(self, x_ratio: float, y_ratio: float):
        """
        使用 W3C Actions API 在螢幕指定比例位置點擊
        
        Args:
        x_ratio (float): x 座標的螢幕比例 (0.0 ~ 1.0)
        y_ratio (float): y 座標的螢幕比例 (0.0 ~ 1.0)
        Ex. 
        self.common_actions.tap(0.5, 0.9)
        """
        size = self.get_screen_size()
        x = int(size[0] * x_ratio)
        y = int(size[1] * y_ratio)
        actions = ActionChains(self.driver)
        pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
        
        actions.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1) 
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()

    def hide_keyboard(self):
        """
        隱藏鍵盤
        """
        self.driver.hide_keyboard()

    def get_screen_size(self) -> Tuple[int, int]:
        """
        獲取螢幕尺寸
        """
        size = self.driver.get_window_size()
        return size['width'], size['height']

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
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_disappear(self, locator_type: str, locator_value: str, timeout: int = 30) -> Union[WebElement, bool]:
        """
        快速檢查元素是否存在且可見
        如果元素不存在則立即返回 True

        Args:
            locator_type: 定位方式
            locator_value: 定位值
            timeout: 最大等待時間（秒）

        Returns:
            Union[WebElement, bool]: 如果元素消失返回 True，否則返回 False

        Raises:
            TimeoutException: 如果元素在指定時間內未消失
        """
        try:
            self.driver.implicitly_wait(0)
            return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((locator_type, locator_value)))
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

    def get_element_attribute(self, locator_type: str, locator_value: str, attribute: str) -> str:
        """
        獲取元素屬性值

        Args:
            locator_type: 定位方式
            locator_value: 定位值
            attribute: 屬性名稱

        Returns:
            str: 屬性值
        """
        element = self.find_element(locator_type, locator_value)
        return element.get_attribute(attribute)


    def get_element_location(self, locator_type: str, locator_value: str) -> Tuple[int, int]:
        """
        獲取元素位置

        Args:
            locator_type: 定位方式
            locator_value: 定位值

        Returns:
            Tuple[int, int]: 元素的 x, y 座標
        """
        element = self.find_element(locator_type, locator_value)
        location = element.location
        return location['x'], location['y']

    def get_element_size(self, locator_type: str, locator_value: str) -> Tuple[int, int]:
        """
        獲取元素尺寸

        Args:
            locator_type: 定位方式
            locator_value: 定位值

        Returns:
            Tuple[int, int]: 元素的寬度和高度
        """
        element = self.find_element(locator_type, locator_value)
        size = element.size
        return size['width'], size['height']

    def is_toggle_on(self, locator_type: str, locator_value: str) -> bool:
        """
        根據 checked 屬性判斷 toggle 狀態
        checked="true" 表示 ON，checked="false" 表示 OFF
        """
        try:
            element = self.find_element(locator_type, locator_value)
            checked = element.get_attribute("checked")
            print(f"Toggle checked attribute: {checked}")
            return checked == "true"
        except (NoSuchElementException, TimeoutException):
            return False

    def toggle_switch(self, locator_type: str, locator_value: str, should_be_on: bool = True) -> bool:
        """
        切換 Toggle（Switch）的狀態

        Args:
            locator_type: 定位方式
            locator_value: 定位值
            should_be_on: 期望的狀態，True 表示開啟，False 表示關閉

        Returns:
            bool: 如果成功切換到期望狀態返回 True，否則返回 False
        """
        try:
            current_state = self.is_toggle_on(locator_type, locator_value)
            if current_state != should_be_on:
                self.click_element(locator_type, locator_value)
                # 等待狀態改變
                time.sleep(0.5)
                return self.is_toggle_on(locator_type, locator_value) == should_be_on
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def toggle_switch_state(self, locator_type: str, locator_value: str, should_be_on: bool = True) -> bool:
        """
        切換 Toggle（Switch）的狀態
        - 強制將 Toggle 切換到指定的狀態（should_be_on）
        - 如果當前狀態與期望狀態不同，則進行切換
        - 如果當前狀態與期望狀態相同，則保持不變

        使用範例：
        # 切換到開啟狀態
        common_actions.toggle_switch_state(By.ID, "my_toggle", should_be_on=True)
        # 輸出：
        # Toggle Current State: Off
        # Toggle New State: On
        # Toggle switched to On state successfully

        # 切換到關閉狀態
        common_actions.toggle_switch_state(By.ID, "my_toggle", should_be_on=False)
        # 輸出：
        # Toggle Current State: On
        # Toggle New State: Off
        # Toggle switched to Off state successfully

        Args:
            locator_type: 定位方式
            locator_value: 定位值
            should_be_on: 期望的狀態，True 表示開啟，False 表示關閉

        Returns:
            bool: 如果成功切換到期望狀態返回 True，否則返回 False
        """
        try:
            current_state = self.is_toggle_on(locator_type, locator_value)
            print(f"Toggle Current State:{'On' if current_state else 'Off'}")
            
            # 如果當前狀態與期望狀態不同，進行切換
            if current_state != should_be_on:
                print(f"Switching toggle to {'On' if should_be_on else 'Off'} state")
                
                max_attempts = 3
                for attempt in range(max_attempts):
                    try:
                        element = self.wait.until(
                            EC.element_to_be_clickable((locator_type, locator_value))
                        )
                        element.click()
                        time.sleep(1) 
                        
                        new_state = self.is_toggle_on(locator_type, locator_value)
                        print(f"Toggle New State (Attempt {attempt + 1}):{'On' if new_state else 'Off'}")
                        
                        if new_state == should_be_on:
                            print(f"Toggle switched to {'On' if should_be_on else 'Off'} state successfully")
                            return True
                            
                        if attempt < max_attempts - 1:
                            print(f"Attempt {attempt + 1} failed, trying again...")
                            time.sleep(1)  # 等待一下再試
                            
                    except Exception as e:
                        print(f"Error during attempt {attempt + 1}: {str(e)}")
                        if attempt < max_attempts - 1:
                            time.sleep(1)
                            continue
                
                print(f"Warning: Failed to switch toggle to {'On' if should_be_on else 'Off'} state after {max_attempts} attempts")
                return False
            else:
                print(f"Toggle is already {'On' if should_be_on else 'Off'}, no need to switch")
                return True
            
        except NoSuchElementException:
            print(f"Error: Toggle element not found ({locator_type}={locator_value})")
            return False
        except TimeoutException:
            print(f"Error: Waiting for Toggle element timeout ({locator_type}={locator_value})")
            return False
        except Exception as e:
            print(f"Error: Unknown error occurred while switching toggle state: {str(e)}")
            return False

    def get_element_count(self, locator_type: str, locator_value: str) -> int:
        """
        找到所有匹配的元素並返回數量
        """
        elements = self.driver.find_elements(locator_type, locator_value)
        return len(elements)