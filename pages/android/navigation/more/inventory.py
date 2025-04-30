import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from pages.locators.android.navigation.more.inventory_locators import InventoryLocators
from pages.shared_components.common_use import CommonUseSection


class InventoryPage(CommonUseSection):
    def __init__(self, driver):
        self.driver = driver
        self.inventory_locators = InventoryLocators()
        
    def tap_inventory_management(self):
        self.driver.find_element(*self.inventory_locators.INVENTORY_MANAGEMENT).click()
        time.sleep(0.5)
        return self
      
    def tap_products_tab(self):
        try:
            tab_container = self.driver.find_element(*self.inventory_locators.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 3
            found_target = False

            for _ in range(max_attempts):
                self.driver.swipe(start_x, y, end_x, y, 100)
                time.sleep(0.5)
                try:
                    products_tab = self.driver.find_element(*self.inventory_locators.AUTO_TEST_TAB)
                    if products_tab.is_displayed():
                        products_tab.click()
                        found_target = True
                        break
                except NoSuchElementException:
                    continue

            if not found_target:
                print("Could not find PRODUCTS_TAB after maximum attempts")
                return self

        except Exception as e:
            print(f"Error swiping tabs: {str(e)}")
            return self
          
        # click test product 1
        self.driver.find_element(*self.inventory_locators.TEST_PRODUCT_1).click()
        time.sleep(0.5)
        return self
    
    def add_inventory(self):
        self.driver.find_element(*self.inventory_locators.ADD_INVENTORY).click()
        time.sleep(0.5)
        
        # click inventory date
        self.driver.find_element(*self.inventory_locators.INVENTORY_DATE).click()
        self.swipe_calendar_component()
        
        # input inventory quantity
        self.driver.find_element(*self.inventory_locators.INVENTORY_QUANTITY).send_keys(random.randint(1, 100))
        
        # input inventory price
        self.driver.find_element(*self.inventory_locators.INVENTORY_PRICE).send_keys(random.randint(1, 100))
        
        # save inventory
        self.driver.find_element(*self.inventory_locators.SAVE_BUTTON).click()
        time.sleep(1)
        return self
      
    def set_safety_stock_level(self):
        self.driver.find_element(*self.inventory_locators.SAFETY_STOCK_LEVEL).click()
        
        # stock remind toggle
        self.driver.find_element(*self.inventory_locators.STOCK_REMIND_TOGGLE).click()
        
        try:
            # input safety stock amount
            self.driver.find_element(*self.inventory_locators.SAFETY_STOCK_AMOUNT).send_keys(random.randint(1, 100))
        except NoSuchElementException:
            pass
        
        # save safety stock
        self.driver.find_element(*self.inventory_locators.SAVE_BUTTON).click()
        time.sleep(0.5)
        return self
      
    def process_return_to_warehouse_action(self):
        self.driver.find_element(*self.inventory_locators.RETURN_TO_WAREHOUSE_ACTION).click()
        time.sleep(0.5)
        
        # click return to warehouse
        self.driver.find_element(*self.inventory_locators.RETURN_TO_WAREHOUSE_BUTTON).click()
        time.sleep(1)
        
        # click confirm return to warehouse
        self.driver.find_element(*self.inventory_locators.CONFIRM_RETURN_TO_WAREHOUSE_BUTTON).click()
        time.sleep(0.5)
        
        # click back button
        self.driver.find_element(*self.inventory_locators.RETURN_TO_WAREHOUSE_BACK_BUTTON).click()
        time.sleep(0.5)
        return self
    
    def view_inventory_records(self):
        self.driver.find_element(*self.inventory_locators.INVENTORY_RECORDS).click()
        time.sleep(1)
        self.driver.find_element(*self.inventory_locators.INVENTORY_RECORDS_BACK_BUTTON).click()
        return self
      
    def return_to_calendar(self):
        self.driver.find_element(*self.inventory_locators.RETURN_TO_INVENTORY_MANAGEMENT_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.inventory_locators.BACK_BUTTON).click()
        return self
    
    
    
    