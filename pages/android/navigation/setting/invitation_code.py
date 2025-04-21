import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.invitation_code_locators import InvitationCodePageLocators

class InvitationCodePage(CommonUseSection):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.invitation_code = None
        #todo: 用super()初始化父類會設置 self.driver = driver, 這邊可以刪除
        # todo: invitation_code目前不清楚功用, 是否需要刪除？

    def tap_invitation_code_in_branch_settings_page(self):
        self.driver.find_element(*InvitationCodePageLocators.INVITATION_CODE_IN_BRANCH_SETTING_PAGE).click()
        time.sleep(2)
        return self

    def verify_invitation_code_page(self):
        self.driver.find_element(*InvitationCodePageLocators.TITLE_IN_INVITATION_CODE_PAGE)
        self.driver.find_element(*InvitationCodePageLocators.INVITATION_CODE_IN_INVITATION_CODE_PAGE)
        self.driver.find_element(*InvitationCodePageLocators.DESCRIPTION_IN_INVITATION_CODE_PAGE)
        self.driver.find_element(*InvitationCodePageLocators.SHARE_BUTTON_IN_INVITATION_CODE_PAGE)
        self.driver.find_element(*InvitationCodePageLocators.INVITED_LIST_IN_INVITATION_CODE_PAGE)
        self.driver.find_element(*InvitationCodePageLocators.CLOSE_BUTTON_IN_INVITATION_CODE_PAGE)
        return self
    
        #todo: 加is_displayed

    def tap_invitation_code_sharing(self):
        self.driver.find_element(*InvitationCodePageLocators.SHARE_BUTTON_IN_INVITATION_CODE_PAGE).click()
        time.sleep(2)
        return self

    def verify_invitation_code_sharing_dialog(self):
        self.driver.find_element(*InvitationCodePageLocators.INVITATION_CODE_SHARING_DIALOG)
        self.driver.find_element(*InvitationCodePageLocators.SHARE_TEXT_IN_INVITATION_CODE_SHARING_DIALOG)
        self.driver.find_element(*InvitationCodePageLocators.COPY_BUTTON_IN_INVITATION_CODE_SHARING_DIALOG)
        return self
        
        #todo: 加is_displayed

    def tap_copy_button_in_invitation_code_sharing_dialog(self):
        self.driver.find_element(*InvitationCodePageLocators.COPY_BUTTON_IN_INVITATION_CODE_SHARING_DIALOG).click()
        time.sleep(2)
        return self

    def verify_invitation_code_sharing_dialog_dismissed(self):
        try:
            self.driver.find_element(*InvitationCodePageLocators.INVITATION_CODE_SHARING_DIALOG)
            return False
        #todo: 這邊可以直接寫 return not self.driver.find_element(
        #    *InvitationCodePageLocators.INVITATION_CODE_SHARING_DIALOG
        #    ).is_displayed()
        except NoSuchElementException:
            return True

    def tap_invited_list_in_invitation_code_page(self):
        self.driver.find_element(*InvitationCodePageLocators.INVITED_LIST_IN_INVITATION_CODE_PAGE).click()
        time.sleep(2)
        return self

    def verify_invited_list_page(self):
        self.driver.find_element(*InvitationCodePageLocators.TITLE_IN_INVITED_LIST_PAGE)
        self.driver.find_element(*InvitationCodePageLocators.CLOSE_BUTTON_IN_INVITED_LIST_PAGE)
        return self
    
        #todo: 加is_displayed

    def tap_close_button_in_invited_list_page(self):
        self.driver.find_element(*InvitationCodePageLocators.CLOSE_BUTTON_IN_INVITED_LIST_PAGE).click()
        time.sleep(2)
        return self

    def tap_close_button_in_invitation_code_page(self):
        self.driver.find_element(*InvitationCodePageLocators.CLOSE_BUTTON_IN_INVITATION_CODE_PAGE).click()
        time.sleep(2)
        return self