import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pages.locators.android.navigation.more.member_apply_locators import MemberApplyLocators
from pages.shared_components.common_use import CommonUseSection

class MemberApplyPage(CommonUseSection):
    def __init__(self, driver):
        self.driver = driver
        self.member_apply_locators = MemberApplyLocators()
        
    def tap_member_apply(self):
        self.driver.find_element(*self.member_apply_locators.MEMBER_APPLY).click()
        time.sleep(0.5)
        return self

    def tap_voucher_management(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.VOUCHER_MANAGEMENT).click()
        return self

    def switch_to_bonus_point_tab(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_TAB).click()
        return self

    def switch_to_membership_gift_tab(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.MEMBERSHIP_GIFT_TAB).click()
        return self

    def switch_to_birthday_gift_tab(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.BIRTHDAY_GIFT_TAB).click()
        return self

    def add_general_voucher(self):
        
        self.driver.find_element(*self.member_apply_locators.ADD_GENERAL_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
        # enter voucher title
        voucher_title = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.VOUCHER_TITLE_INPUT).send_keys(voucher_title)
        
        # enter voucher content
        self.driver.find_element(*self.member_apply_locators.VOUCHER_CONTENT).click()
        time.sleep(0.5)
        voucher_content = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=10)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.VOUCHER_CONTENT_INPUT).send_keys(voucher_content)
        self.driver.find_element(*self.member_apply_locators.VOUCHER_CONTENT_INPUT_SAVE_BUTTON).click()
        
        # sale setting section
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.SALES_TOGGLE).click()
        
        sales_amount = str(random.randint(10, 1000))
        self.driver.find_element(*self.member_apply_locators.SALES_AMOUNT_INPUT).clear()
        self.driver.find_element(*self.member_apply_locators.SALES_INPUT_FIELD).send_keys(sales_amount)
        time.sleep(0.5)
        
        # discount setting section
        self.discount_setting_section()
        
        # other section
        self.other_section()
        
        # performance setting section
        self.performance_setting_section()
        
        
        # save button
        self.driver.find_element(*self.member_apply_locators.ADD_NEW_VOUCHER_SAVE_BUTTON).click()
        time.sleep(0.5)
        
    def discount_setting_section(self):
        # discount setting section
        self.driver.find_element(*self.member_apply_locators.AUTO_DISCOUNT_TOGGLE).click()
        time.sleep(1)
        
        self.driver.find_element(*self.member_apply_locators.DISCOUNT_TYPE_BLOCK).click()
        
        selected_option = random.choice(self.member_apply_locators.DISCOUNT_OPTIONS)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_option}').click()
           
        if selected_option == self.member_apply_locators.DISCOUNT_OPTIONS[0]:
            discount_amount = str(random.randint(10, 1000))
            self.driver.find_element(*self.member_apply_locators.DISCOUNT_AMOUNT_INPUT).send_keys(discount_amount)
        else:
            discount_list = self.member_apply_locators.DISCOUNT_PERCENTAGE_LIST
            discount_percentage = random.choice(discount_list)
            self.driver.find_element(*self.member_apply_locators.DISCOUNT_PERCENTAGE_INPUT).send_keys(discount_percentage)
        
        # scroll to the bottom of the page to continue doing the next step
        self.driver.swipe(start_x=500, start_y=1800, end_x=500, end_y=300, duration=800)
        time.sleep(1)
        
    def usage_period_section(self):
        # scroll to the bottom of the page to continue doing the next step
        self.driver.swipe(start_x=500, start_y=1800, end_x=500, end_y=300, duration=800)
        time.sleep(1)
        
        # usage period section
        self.driver.find_element(*self.member_apply_locators.USAGE_PERIOD).click()
        
        selected_usage = random.choice(self.member_apply_locators.USAGE_OPTIONS)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_usage}').click()
        
        # no limit
        if selected_usage == self.member_apply_locators.USAGE_OPTIONS[0]:
            pass
        # days
        elif selected_usage == self.member_apply_locators.USAGE_OPTIONS[1]:
            random_days = str(random.randint(1, 30))
            input_field = self.driver.find_element(*self.member_apply_locators.USAGE_PERIOD_TIME_INPUT)
            input_field.send_keys(random_days)
            
        # expire time
        else:
            self.driver.find_element(*self.member_apply_locators.USAGE_PERIOD_CHOOSE_TIME).click()
            time.sleep(1)
            self.add_gift_voucher_choose_date()
            
    def performance_setting_section(self):
        # scroll to the bottom of the page to find the created voucher
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=200, duration=800)
        time.sleep(1)
        
        # performance setting section
        self.driver.find_element(*self.member_apply_locators.INCLUDE_PERFORMANCE_TOGGLE).click()
        time.sleep(0.5)
        
        performance_amount = str(random.randint(10, 1000))
        self.driver.find_element(*self.member_apply_locators.INPUT_PERFORMANCE_AMOUNT).send_keys(performance_amount)
        
        self.driver.hide_keyboard()

    def other_section(self):
        # scroll to the bottom of the page to find the created voucher
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=200, duration=800)
        time.sleep(1)
        
        # other section
        self.driver.find_element(*self.member_apply_locators.OTHER_TICKET_TRANSFER_TOGGLE).click()
        time.sleep(0.5)
        

    def edit_and_delete_general_voucher(self):
        # scroll to the bottom of the page to find the created voucher
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=200, duration=800)
        time.sleep(1)
        
        # edit voucher toggle
        self.driver.find_element(*self.member_apply_locators.EDIT_GENERAL_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
        # toggle
        toggle_elements = [
            self.driver.find_element(*self.member_apply_locators.SALES_TOGGLE),
            self.driver.find_element(*self.member_apply_locators.AUTO_DISCOUNT_TOGGLE)
        ]
        
        for toggle in toggle_elements:
            toggle.click()
            time.sleep(0.5)
        
        # scroll down again
        self.driver.swipe(start_x=500, start_y=1800, end_x=500, end_y=300, duration=800)
        time.sleep(1)
        
        self.driver.find_element(*self.member_apply_locators.OTHER_TICKET_TRANSFER_TOGGLE).click()
        
        
        # delete voucher
        self.driver.find_element(*self.member_apply_locators.DELETE_GENERAL_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.DELETE_CONFIRM_BUTTON).click()
        return self

    def add_bonus_point_voucher(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.ADD_BONUS_POINT_VOUCHER_BUTTON).click()
        
        # open to change toggle
        self.driver.find_element(*self.member_apply_locators.OPEN_TO_CHANGE_TOGGLE).click()
        time.sleep(0.5)
        
        # enter bonus point title
        bonus_point_title = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_TITLE_INPUT).send_keys(bonus_point_title)
        
        # enter bonus point content
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT).click()
        time.sleep(0.5)
        bonus_point_content = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=10)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT_INPUT).send_keys(bonus_point_content)
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT_INPUT_SAVE_BUTTON).click()
        
        # input required amount
        self.driver.find_element(*self.member_apply_locators.REQUIRED_AMOUNT).clear()
        required_amount = str(random.randint(10, 1000))
        self.driver.find_element(*self.member_apply_locators.REQUIRED_AMOUNT_INPUT).send_keys(required_amount)
        
        # discount setting section
        self.discount_setting_section()
        
        # usage period section
        self.usage_period_section()
        
        # other section
        self.other_section()
        
        # performance setting section
        self.performance_setting_section()
        
        # save button
        self.driver.find_element(*self.member_apply_locators.ADD_NEW_VOUCHER_SAVE_BUTTON).click()
        time.sleep(0.5)
        
        return self

    def edit_and_delete_bonus_point_voucher(self):
        self.driver.find_element(*self.member_apply_locators.EDIT_BONUS_POINT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
        # toggle
        toggle_elements = [
            self.driver.find_element(*self.member_apply_locators.OPEN_TO_CHANGE_TOGGLE),
            self.driver.find_element(*self.member_apply_locators.AUTO_DISCOUNT_TOGGLE),
        ]
        
        for toggle in toggle_elements:
            toggle.click()
            time.sleep(0.5)
            
        
        
        # scroll down again
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=200, duration=800)
        time.sleep(1)
        
        # click transfer toggle
        self.driver.find_element(*self.member_apply_locators.OTHER_TICKET_TRANSFER_TOGGLE).click()
        
        # delete voucher
        self.driver.find_element(*self.member_apply_locators.DELETE_BONUS_POINT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.DELETE_CONFIRM_BUTTON).click()
        return self
      
      
    def add_membership_gift_voucher(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.ADD_MEMBERSHIP_GIFT_VOUCHER_BUTTON).click()
        
        
        # enter membership gift title
        membership_gift_title = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_TITLE_INPUT).send_keys(membership_gift_title)
        
        # enter membership gift content
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT).click()
        time.sleep(0.5)
        membership_gift_content = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=10)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT_INPUT).send_keys(membership_gift_content)
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT_INPUT_SAVE_BUTTON).click()
        
        # discount setting section
        self.discount_setting_section()
        
        # scroll down 
        self.driver.swipe(start_x=500, start_y=1800, end_x=500, end_y=300, duration=800)
        time.sleep(1)
        
        # usage period section
        self.usage_period_section()
        
        # scroll down again
        self.driver.swipe(start_x=500, start_y=1800, end_x=500, end_y=300, duration=800)
        time.sleep(1)
        
        # other section
        time.sleep(0.5)
        self.other_section()
        
        # performance setting section
        time.sleep(0.5)
        self.performance_setting_section()
        
        # save button
        self.driver.find_element(*self.member_apply_locators.ADD_NEW_VOUCHER_SAVE_BUTTON).click()
        time.sleep(0.5)
        
        
        return self
      
    def edit_and_delete_membership_gift_voucher(self):
        self.driver.find_element(*self.member_apply_locators.EDIT_MEMBERSHIP_GIFT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
        # toggle
        toggle_elements = [
            self.driver.find_element(*self.member_apply_locators.AUTO_DISCOUNT_TOGGLE),
            self.driver.find_element(*self.member_apply_locators.INCLUDE_PERFORMANCE_TOGGLE)
        ]
        
        for toggle in toggle_elements:
            toggle.click()
            time.sleep(0.5)
            
        # scroll down again
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=200, duration=800)
        time.sleep(1)
        
        # delete voucher
        self.driver.find_element(*self.member_apply_locators.DELETE_MEMBERSHIP_GIFT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.DELETE_CONFIRM_BUTTON).click()
        return self
      
      
    def add_birthday_gift_voucher(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.ADD_BIRTHDAY_GIFT_VOUCHER_BUTTON).click()
        
        # enter birthday gift title
        birthday_gift_title = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_TITLE_INPUT).send_keys(birthday_gift_title)
        
        # enter birthday gift content
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT).click()
        time.sleep(0.5)
        birthday_gift_content = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=10)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT_INPUT).send_keys(birthday_gift_content)
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_CONTENT_INPUT_SAVE_BUTTON).click()
        
        # discount setting section
        self.discount_setting_section()
        
        # scroll down 
        self.driver.swipe(start_x=500, start_y=1800, end_x=500, end_y=300, duration=800)
        time.sleep(1)
        
        
        # other section
        self.other_section()
        
        # performance setting section
        self.performance_setting_section()
        
        # save button
        self.driver.find_element(*self.member_apply_locators.ADD_NEW_VOUCHER_SAVE_BUTTON).click()
        time.sleep(0.5)
        
        return self
      
    def edit_and_delete_birthday_gift_voucher(self):
        self.driver.find_element(*self.member_apply_locators.EDIT_BIRTHDAY_GIFT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
        # toggle
        toggle_elements = [
            self.driver.find_element(*self.member_apply_locators.AUTO_DISCOUNT_TOGGLE),
            self.driver.find_element(*self.member_apply_locators.INCLUDE_PERFORMANCE_TOGGLE)
        ]
        
        for toggle in toggle_elements:
            toggle.click()
            time.sleep(0.5)
            
        # scroll down again
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=200, duration=800)
        time.sleep(1)
        
        # delete voucher
        self.driver.find_element(*self.member_apply_locators.DELETE_BIRTHDAY_GIFT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.DELETE_CONFIRM_BUTTON).click()
        return self
      
   

    def back_to_membership_application(self):
        self.driver.back()
        time.sleep(0.5)
        return self


####### DOCUMENT MANAGEMENT #######

    def tap_document_management(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.DOCUMENT_MANAGEMENT).click()
        return self
    
    def add_document(self):
        time.sleep(2)
        self.driver.find_element(*self.member_apply_locators.ADD_DOCUMENT_BUTTON).click()
        
        # member auto sign toggle
        self.driver.find_element(*self.member_apply_locators.MEMBER_AUTO_SIGN_TOGGLE).click()
        time.sleep(0.5)
        
        # document name input
        random_input = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.DOCUMENT_NAME_INPUT).send_keys(random_input)
        
        # click text paragraph & problem btn
        self.driver.find_element(*self.member_apply_locators.ADD_TEXT_PARAGRAPH_BUTTON).click()
        time.sleep(0.5)
        

        selected_option = random.choice(self.member_apply_locators.ADD_TEXT_PROBLEM_OPTIONS)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_option}').click()
  
        if selected_option == self.member_apply_locators.ADD_TEXT_PROBLEM_OPTIONS[0]:
            # add text paragraph
            self.driver.find_element(*self.member_apply_locators.ADD_TEXT_PARAGRAPH_CONTENT_INPUT).send_keys(random_input)
            time.sleep(0.5)
            self.driver.find_element(*self.member_apply_locators.ADD_TEXT_PARAGRAPH_SAVE_BUTTON).click()
            time.sleep(0.5)
        else:
            # add problem
            self.driver.find_element(*self.member_apply_locators.NEW_PROBLEM_INPUT).send_keys(random_input)
            time.sleep(0.5)
            
            self.option_type_question_section(is_add_document_question_save_button=True)
             
        self.driver.find_element(*self.member_apply_locators.CUSTOMER_NEED_TO_SIGN_TOGGLE).click()    
        self.driver.find_element(*self.member_apply_locators.DOCUMENT_SAVE_BUTTON).click()
        
        return self
    
    def option_type_question_section(self, is_add_document_question_save_button=None):
        option_type_section = self.driver.find_element(*self.member_apply_locators.OPTION_TYPE_SECTION)
        option_type_section.click()
        time.sleep(0.5)
            
        selected_option = random.choice(self.member_apply_locators.OPTION_TYPE_OPTIONS)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_option}').click()
            
            
        if selected_option == self.member_apply_locators.OPTION_TYPE_OPTIONS[0] or selected_option == self.member_apply_locators.OPTION_TYPE_OPTIONS[1]:
            # add new option
            self.driver.find_element(*self.member_apply_locators.NEW_OPTION).click()
            time.sleep(0.5)
                
            # input random option name
            random_option = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
            self.driver.find_element(*self.member_apply_locators.NEW_OPTION_INPUT).send_keys(random_option)
            time.sleep(0.5)
                
            if is_add_document_question_save_button:
              self.driver.find_element(*self.member_apply_locators.ADD_DOCUMENT_ADD_NEW_QUESTION_SAVE_BUTTON).click()
              
              # CLICK QUESTION TYPE SECTION
              time.sleep(1)
              question_type_section = self.driver.find_element(*self.member_apply_locators.QUESTION_TYPE_SECTION)
              question_type_section.click()
        
              selected_option = random.choice(self.member_apply_locators.QUESTION_TYPE_OPTIONS)
              self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_option}').click()
            
              self.driver.find_element(*self.member_apply_locators.ADD_DOCUMENT_ADD_NEW_QUESTION_SAVE_BUTTON).click()
            else:
              # add custom column save button locator
              self.driver.find_element(*self.member_apply_locators.ADD_CUSTOM_COLUMN_NEW_QUESTION_SAVE_BUTTON).click()
              
              # CLICK QUESTION TYPE SECTION
              time.sleep(1)
              question_type_section = self.driver.find_element(*self.member_apply_locators.QUESTION_TYPE_SECTION)
              question_type_section.click()
        
              selected_option = random.choice(self.member_apply_locators.QUESTION_TYPE_OPTIONS)
              self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_option}').click()
            
              self.driver.find_element(*self.member_apply_locators.ADD_NEW_COLUMN_SAVE_BUTTON).click()
                
        else:
            if is_add_document_question_save_button:
                self.driver.find_element(*self.member_apply_locators.ADD_DOCUMENT_ADD_NEW_QUESTION_SAVE_BUTTON).click()
            else:
                self.driver.find_element(*self.member_apply_locators.ADD_NEW_COLUMN_SAVE_BUTTON).click()
        return self
    
    def edit_preview_share_document(self):
        # Scroll down to continue editing
        for _ in range(7):
            self.driver.swipe(
                 start_x=500,
                 start_y=1800,
                 end_x=500,
                 end_y=300,
                 duration=1000
        )
        time.sleep(0.5)
        
        # click edit document button
        self.driver.find_element(*self.member_apply_locators.EDIT_DOCUMENT_BUTTON).click()
        time.sleep(0.5)
        
        # randomly choose one of the options
        selected_option = random.choice(self.member_apply_locators.EDIT_DOCUMENT_OPTIONS)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_option}').click()
        
        
        if selected_option == self.member_apply_locators.EDIT_DOCUMENT_OPTIONS[0]:
            # edit document
            self.driver.find_element(*self.member_apply_locators.MEMBER_AUTO_SIGN_TOGGLE).click()
            random_input = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
            self.driver.find_element(*self.member_apply_locators.EDIT_DOCUMENT_TITLE_INPUT).clear()
            self.driver.find_element(*self.member_apply_locators.EDIT_DOCUMENT_TITLE_INPUT).send_keys(random_input)
            self.driver.find_element(*self.member_apply_locators.DOCUMENT_SAVE_BUTTON).click()
        elif selected_option == self.member_apply_locators.EDIT_DOCUMENT_OPTIONS[1]:
            # preview document
            time.sleep(0.5)
            self.driver.find_element(*self.member_apply_locators.PREVIEW_DOCUMENT_BACK_BUTTON).click()
        elif selected_option == self.member_apply_locators.EDIT_DOCUMENT_OPTIONS[2]:
            # share document
            time.sleep(0.5)
            self.driver.find_element(*self.member_apply_locators.SHARE_DOCUMENT_COPY_BUTTON).click()
        else:
            # sign record
            time.sleep(0.5)
            self.driver.find_element(*self.member_apply_locators.SIGN_RECORD_BACK_BUTTON).click()
        
        return self
    
    def disable_document(self):
        time.sleep(2)
        disable_document_button = self.driver.find_element(*self.member_apply_locators.DISABLE_DOCUMENT_BUTTON)
        if disable_document_button.is_displayed():
            disable_document_button.click()
            time.sleep(0.5)
            self.driver.find_element(*self.member_apply_locators.DISABLE_DOCUMENT_CONFIRM_BUTTON).click()
        else:
            print("Disable Document is not displayed")
        return self
    
    def click_disabled_tab(self):
        self.driver.find_element(*self.member_apply_locators.DISABLE_TAB).click()
        time.sleep(0.5)
        return self
    
    def reactivate_disabled_document(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.REACTIVATE_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.REACTIVATE_CONFIRM_BUTTON).click()
        return self
    
    def edit_and_reactivate_disabled_document(self):
        time.sleep(2)
        self.driver.find_element(*self.member_apply_locators.RANDOMLY_EDIT_DISABLE_DOCUMENT_BUTTON).click()
        self.driver.find_element(*self.member_apply_locators.MEMBER_AUTO_SIGN_TOGGLE).click()
        
        # click reactivate document button
        self.driver.find_element(*self.member_apply_locators.REACTIVATE_DOCUMENT_BUTTON).click()
        self.driver.find_element(*self.member_apply_locators.REACTIVATE_CONFIRM_BUTTON).click()
        return self
    
    
    
####### BONUS POINT RATIO MANAGEMENT #######

    def tap_bonus_points(self):
        time.sleep(2)
        self.driver.find_element(*self.member_apply_locators.BONUS_POINTS).click()
        return self

    def set_bonus_point_ratio(self):
        
        # click toggle 2 times
        for _ in range(2):
            self.driver.find_element(*self.member_apply_locators.CHECKOUT_AUTO_SEND_TOGGLE).click()
            time.sleep(0.5)
            
        # set bonus point ratio
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_RATIO_SECTION).click()
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_RATIO_INPUT).send_keys(random.randint(1, 100))
        time.sleep(0.5)
        
        # click save button
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_RATIO_SAVE_BUTTON).click()
        return self


####### CUSTOM MEMBERSHIP REGISTRATION #######

    def tap_custom_membership_registration_fields(self):
        time.sleep(1)
        self.driver.find_element(*self.member_apply_locators.CUSTOM_MEMBERSHIP_REGISTRATION_FIELDS).click()
        return self
    
    def add_new_field(self):
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.ADD_NEW_FIELD_BUTTON).click()
        
        # open to member input toggle
        self.driver.find_element(*self.member_apply_locators.MEMBER_INPUT_TOGGLE).click()
    
        # input random field name
        random_field_name = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+", k=5)) + "自動化測試"
        self.driver.find_element(*self.member_apply_locators.FIELD_TITLE_INPUT).send_keys(random_field_name)
        time.sleep(0.5)
        
        # option type & question type section
        self.option_type_question_section(is_add_document_question_save_button=False)
        
        # click add new field button
        self.driver.find_element(*self.member_apply_locators.ADD_NEW_COLUMN_BUTTON).click()
        time.sleep(0.5)
        
        
    
    def edit_and_delete_field(self):
        time.sleep(0.5)
        self.driver.find_element(*self.member_apply_locators.EDIT_FIELD_BUTTON).click()
        
        # click open to member input toggle
        self.driver.find_element(*self.member_apply_locators.MEMBER_INPUT_TOGGLE).click()
        
        # click save button
        self.driver.find_element(*self.member_apply_locators.EDIT_FIELD_SAVE_BUTTON).click()
        
        # click edit confirm button
        self.driver.find_element(*self.member_apply_locators.EDIT_CONFIRM_BUTTON).click()
        
        # click delete button
        self.driver.find_element(*self.member_apply_locators.DELETE_BUTTON).click()
        
        # input delete text then click delete confirm button
        self.driver.find_element(*self.member_apply_locators.DELETE_INPUT).send_keys("Delete")
        self.driver.find_element(*self.member_apply_locators.DELETE_CONFIRM_BUTTON).click()
        
        return self
    
    def return_to_membership_application(self):
        self.driver.find_element(*self.member_apply_locators.RETURN_TO_CALENDAR_BUTTON).click()
        time.sleep(0.5)
        return self
        
    def add_gift_voucher_choose_date(self):
        # click right arrow multiple times
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*self.member_apply_locators.RIGHT_ARROW).click()
            time.sleep(0.5)
    
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
    
        random.choice(dates).click()
    
        # click outside to close the date window
        size = self.driver.get_window_size()
        x = int(size['width'] * 0.5)
        y = int(size['height'] * 0.9)
        
        # 使用 W3C Actions API 進行點擊
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
        
        