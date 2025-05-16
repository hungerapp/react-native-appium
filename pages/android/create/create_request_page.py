import random
import time

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

from pages.locators.android.create.create_request_locators import CreateRequestLocators
from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions


class CreateRequestPage(CommonUseSection):
    def __init__(self, driver):
        super().__init__(driver)
        self.common_actions = CommonActions(driver)
        
        
    def click_create_request(self):
        try:
          self.common_actions.is_element_visible(*CreateRequestLocators.CREATE_BTN)
          self.common_actions.click_element(*CreateRequestLocators.CREATE_BTN)
          self.common_actions.click_element(*CreateRequestLocators.CREATE_REQUEST_BTN)
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create appointment button after multiple attempts")
      
        return self

    def select_requester(self, change=False):
        if change is False:
            self.common_actions.click_element(*CreateRequestLocators.QA_TEST_REQUESTER_SELECT)       
        else:
            self.common_actions.click_element(*CreateRequestLocators.REQUEST_PERSONNEL_SECTION)
            self.common_actions.click_element(*CreateRequestLocators.SALLY_REQUESTER_SELECT)
            
        self.common_actions.click_element(*CreateRequestLocators.REQUESTER_SAVE_BUTTON)

    def select_item(self):
        self.swipe_and_find_tab(CreateRequestLocators.AUTO_TEST_TAB)
        
        # Select specific services under AUTO_TEST_TAB
        try:
            num_selections = random.randint(2,4)
            selected_options = random.sample(CreateRequestLocators.TEST_PRODUCT_OPTIONS, num_selections)
            
            for option in selected_options:
                service = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, option)
                service.click()
                time.sleep(0.5)
            
            self.common_actions.click_element(*CreateRequestLocators.SAVE_PRODUCT_BTN)
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")

        return self
    
    def remove_item(self):
        self.common_actions.click_element(*CreateRequestLocators.REMOVE_ITEM_BTN)
        self.common_actions.is_element_visible(*CreateRequestLocators.REMOVE_CONFIRM_BTN)
        self.common_actions.click_element(*CreateRequestLocators.REMOVE_CONFIRM_BTN)
        self.common_actions.click_element(*CreateRequestLocators.BACK_TO_PREVIOUS_PAGE_ICON)
      
    def submit_signing(self):
        self.common_actions.click_element(*CreateRequestLocators.CONFIRM_ITEM_BTN)
        self.common_actions.click_element(*CreateRequestLocators.PERSONNEL_SIGN_BTN)

    def confirm_request(self):
        self.common_actions.click_element(*CreateRequestLocators.CONFIRM_REQUEST_BTN)

    def clear_all_items(self):
        self.common_actions.click_element(*CreateRequestLocators.ITEM_SECTION)
        self.common_actions.click_element(*CreateRequestLocators.SELECT_ITEM_BTN)
        self.common_actions.click_element(*CreateRequestLocators.CLEAR_ITEMS_BTN)

    def reselect_items(self):
        existing_elements = []
        for selector in CreateRequestLocators.QUANTITY_PLUS:
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
            selector = random.choice(CreateRequestLocators.QUANTITY_PLUS)
            ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
            ele.click()
            time.sleep(0.5)
            
    def clear_signature(self):
        self.common_actions.click_element(*CreateRequestLocators.CLEAR_SIGNATURE_BTN)
