import random
import time
import math

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains


class CreateRequestPage:
    def __init__(self, driver):
        self.driver = driver

    CREATE_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[42]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView[6]/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    CREATE_REQUEST_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("請領")')
    QA_TEST_REQUESTER_SELECT = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SALLY_REQUESTER_SELECT = (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲')
    REQUEST_PERSONNEL_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請領人員")')
    ITEM_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商品")')
    SELECT_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇商品")')
    
    REQUESTER_SAVE_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
    AUTO_TEST_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試商品")')
    SAVE_PRODUCT_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    SAVE_PRODUCT_BTN_2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    
    CONFIRM_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("請領商品")')
    PERSONNEL_SIGN_BTN = (AppiumBy.ACCESSIBILITY_ID, '請領人員進行簽名')
    CONFIRM_REQUEST_BTN = (AppiumBy.ACCESSIBILITY_ID, '確認請領')
    CLEAR_ITEMS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部清除")')
    QUANTITY_INPUT = (AppiumBy.ACCESSIBILITY_ID, '數量輸入')
    AMOUNT_EDIT_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="pen-to-square"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    AMOUNT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    AMOUNT_CLEAR_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")')
    AMOUNT_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    EDIT_ITEM_QUANTITY_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)')
    QUANTITLY_PLUS_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@resource-id, "plus")]')
    QUANTITY_REVISE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")')
    QUANTITY_REVISE_INPUT2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    QUANTITY_REVISE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    
    REMOVE_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    REMOVE_CONFIRM_BTN = (AppiumBy.ACCESSIBILITY_ID, '移除')
    BACK_TO_PREVIOUS_PAGE_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    SIGNATURE_PAD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.webkit.WebView")')
    CLEAR_SIGNATURE_BTN = (AppiumBy.ACCESSIBILITY_ID, '清除簽名')

    def click_create_request(self):
        try:
          time.sleep(1.5)
          create_button = self.driver.find_element(*self.CREATE_BTN)
          if create_button.is_displayed() and create_button.is_enabled():
              create_button.click()
              
          self.driver.find_element(*self.CREATE_REQUEST_BTN).click()
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create appointment button after multiple attempts")
      
        return self

    def select_requester(self, change=False):
        if change is False:
            self.driver.find_element(*self.QA_TEST_REQUESTER_SELECT).click()       
        else:
            self.driver.find_element(*self.REQUEST_PERSONNEL_SECTION).click()
            self.driver.find_element(*self.SALLY_REQUESTER_SELECT).click()
            
        self.driver.find_element(*self.REQUESTER_SAVE_BUTTON).click()

    def select_item(self):
        try:
            tab_container = self.driver.find_element(*self.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 5
            found_target = False

            for _ in range(max_attempts):
                self.driver.swipe(start_x, y, end_x, y, 100)
                time.sleep(0.5)
                try:
                    auto_test_tab = self.driver.find_element(*self.AUTO_TEST_TAB)
                    if auto_test_tab.is_displayed():
                        auto_test_tab.click()
                        found_target = True
                        break
                except NoSuchElementException:
                    continue

            if not found_target:
                print("Could not find AUTO_TEST_TAB after maximum attempts")
                return self

        except Exception as e:
            print(f"Error swiping tabs: {str(e)}")
            return self

        # Select specific services under AUTO_TEST_TAB
        try:
            test_product_options = [
              'new UiSelector().text("測試1")',
              'new UiSelector().text("測試2")',
              'new UiSelector().text("測試3")',
              'new UiSelector().text("測試4")',
              'new UiSelector().text("測試5")',
            ]
            
            
            num_selections = random.randint(2,4)
            selected_options = random.sample(test_product_options, num_selections)
            
            for option in selected_options:
                service = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, option)
                service.click()
                time.sleep(0.5)
            
            try:
                save_button = self.driver.find_element(*self.SAVE_PRODUCT_BTN)
                save_button.click()
            except:
                save_button = self.driver.find_element(*self.SAVE_PRODUCT_BTN_2)
                save_button.click()
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")

        return self
      

    def submit_signing(self):
        self.driver.find_element(*self.CONFIRM_ITEM_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.PERSONNEL_SIGN_BTN).click()

    def confirm_request(self):
        self.driver.find_element(*self.CONFIRM_REQUEST_BTN).click()

    def clear_all_items(self):
        time.sleep(0.5)
        self.driver.find_element(*self.ITEM_SECTION).click()
        time.sleep(0.5)
        self.driver.find_element(*self.SELECT_ITEM_BTN).click()
        self.driver.find_element(*self.CLEAR_ITEMS_BTN).click()

    def reselect_items(self):
        # 後續做商品加減使用
        quantity_plus = [
              'new UiSelector().className("com.horcrux.svg.PathView").instance(4)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(7)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(10)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(13)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(16)'
            ]
        
        existing_elements = []
        for selector in quantity_plus:
            try:
                element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                if element.is_displayed():
                    existing_elements.append(selector)
            except:
                continue

        if not existing_elements:
            raise Exception("No elements found on the page")

        
                        
        click_times = random.randint(3,5)
            
        for _ in range(click_times):
            selector = random.choice(quantity_plus)
            ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
            ele.click()
            time.sleep(0.5)
            

    def update_items_amount(self):
        amount_edit_icon = self.driver.find_element(*self.AMOUNT_EDIT_ICON)
        amount_edit_icon.click()
        amount_input = self.driver.find_element(*self.AMOUNT_INPUT)
        random_amount = str(random.randint(10, 1000))
        amount_input.send_keys(random_amount)
        self.driver.find_element(*self.AMOUNT_CLEAR_BTN).click()

        amount_input.send_keys(random_amount)
        time.sleep(1.5)
        self.driver.find_element(*self.AMOUNT_SAVE_BTN).click()
        

    def update_items_quantity(self):
        time.sleep(0.5)
        self.driver.find_element(*self.EDIT_ITEM_QUANTITY_ICON).click()
        try:
          if random.choice([True, False]):
             plus_button = self.driver.find_element(*self.QUANTITLY_PLUS_BUTTON)
             click_times = random.randint(5,8)
             for _ in range(click_times):
                plus_button.click()
                time.sleep(0.5)
          else:
             quantity_input = self.driver.find_element(*self.QUANTITY_REVISE_INPUT)
             quantity_input.click()
             random_quantity = str(random.randint(5, 100))
             quantity_input2 = self.driver.find_element(*self.QUANTITY_REVISE_INPUT2)
             quantity_input2.click()
             quantity_input2.send_keys(random_quantity)
          
          self.driver.find_element(*self.QUANTITY_REVISE_SAVE_BTN).click()
        
        except Exception as e:
            print(f"Error updating items quantity: {str(e)}")
            raise
        
        

    def remove_item(self):
        time.sleep(0.5)
        self.driver.find_element(*self.REMOVE_ITEM_BTN).click()
        remove_confirm_btn = self.driver.find_element(*self.REMOVE_CONFIRM_BTN)
        if remove_confirm_btn.is_displayed() and remove_confirm_btn.is_enabled():
            remove_confirm_btn.click()
        
        time.sleep(0.5)
        back_to_previous_page_icon = self.driver.find_element(*self.BACK_TO_PREVIOUS_PAGE_ICON)
        back_to_previous_page_icon.click()
        

    def sign_request(self):
        """Simulate signature with large continuous strokes in the center"""
        try:
            signature_pad = self.driver.find_element(*self.SIGNATURE_PAD)
            location = signature_pad.location
            size = signature_pad.size
            
            # 計算中心區域
            center_x = location['x'] + size['width'] * 0.15
            center_y = location['y'] + size['height'] * 0.2
            
            # 使用較大的範圍但仍在安全區域內
            range_x = size['width'] * 0.15
            range_y = size['height'] * 0.15

            # 創建一個大的橢圓形簽名
            def generate_oval_points():
                points = []
                # 生成橢圓形的點
                for i in range(8): 
                    angle = (i / 8.0) * 2 * 3.14  # 2π
                    x = center_x + range_x * 1.5 * math.cos(angle)
                    y = center_y + range_y * 1.3 * math.sin(angle)
                    points.append((x, y))
                return points

            # 執行主要簽名筆劃
            actions = ActionChains(self.driver)
            
            # 第一筆：大橢圓
            oval_points = generate_oval_points()
            actions.move_to_element_with_offset(signature_pad,
                                             oval_points[0][0] - location['x'],
                                             oval_points[0][1] - location['y'])
            actions.click_and_hold()
            for point in oval_points[1:]:
                actions.move_to_element_with_offset(signature_pad,
                                                 point[0] - location['x'],
                                                 point[1] - location['y'])
                time.sleep(0.1)
            actions.release()
            actions.perform()

            # 第二筆：中間的裝飾線
            actions = ActionChains(self.driver)
            start_x = center_x - range_x * 0.2
            start_y = center_y
            actions.move_to_element_with_offset(signature_pad,
                                             start_x - location['x'],
                                             start_y - location['y'])
            actions.click_and_hold()
            
            # 創建波浪形狀
            for i in range(4):
                x = start_x + range_x * 0.3 * i
                y = start_y + (range_y * 0.3 * math.sin(i * 3.14))
                actions.move_to_element_with_offset(signature_pad,
                                                 x - location['x'],
                                                 y - location['y'])
                time.sleep(0.1)
            
            actions.release()
            actions.perform()

        except Exception as e:
            print(f"Error during signing: {str(e)}")
            raise

    def clear_signature(self):
        self.driver.find_element(*self.CLEAR_SIGNATURE_BTN).click()
