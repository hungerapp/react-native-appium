import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy

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
        self.driver.find_element(*self.member_apply_locators.VOUCHER_MANAGEMENT).click()
        time.sleep(0.5)
        return self

    def switch_to_bonus_point_tab(self):
        self.driver.find_element(*self.member_apply_locators.BONUS_POINT_TAB).click()
        time.sleep(0.5)
        return self

    def switch_to_membership_gift_tab(self):
        self.driver.find_element(*self.member_apply_locators.MEMBERSHIP_GIFT_TAB).click()
        time.sleep(0.5)
        return self

    def switch_to_birthday_gift_tab(self):
        self.driver.find_element(*self.member_apply_locators.BIRTHDAY_GIFT_TAB).click()
        time.sleep(0.5)
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
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{selected_option}")').click()
           
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
        # usage period section
        self.driver.find_element(*self.member_apply_locators.USAGE_PERIOD).click()
        
        selected_usage = random.choice(self.member_apply_locators.USAGE_OPTIONS)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{selected_usage}")').click()
        
        # no limit
        if selected_usage == self.member_apply_locators.USAGE_OPTIONS[0]:
            pass
        # days
        elif selected_usage == self.member_apply_locators.USAGE_OPTIONS[1]:
            self.driver.find_element(*self.member_apply_locators.USAGE_PERIOD_TIME_INPUT).click()
            time.sleep(1)
            self.driver.find_element(*self.member_apply_locators.USAGE_PERIOD_TIME_INPUT).send_keys(str(random.randint(1, 30)))
        # expire time
        else:
            self.driver.find_element(*self.member_apply_locators.USAGE_PERIOD_CHOOSE_TIME).click()
            time.sleep(1)
            self.choose_date()
            
    def performance_setting_section(self):
        # performance setting section
        self.driver.find_element(*self.member_apply_locators.INCLUDE_PERFORMANCE_TOGGLE).click()
        time.sleep(0.5)
        
        performance_amount = str(random.randint(10, 1000))
        self.driver.find_element(*self.member_apply_locators.INPUT_PERFORMANCE_AMOUNT).send_keys(performance_amount)

    def other_section(self):
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
        self.driver.find_element(*self.member_apply_locators.ADD_BONUS_POINT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
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
        self.driver.find_element(*self.member_apply_locators.ADD_MEMBERSHIP_GIFT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
        
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
        
        # other section
        self.other_section()
        
        # performance setting section
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
        self.driver.find_element(*self.member_apply_locators.ADD_BIRTHDAY_GIFT_VOUCHER_BUTTON).click()
        time.sleep(0.5)
        
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
