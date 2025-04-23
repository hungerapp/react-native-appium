from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.invitation_code_locators import InvitationCodePageLocators
from pages.shared_components.common_action import CommonActions

# noinspection DuplicatedCode
class InvitationCodePage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.common_use_section = CommonUseSection(driver)
        self.invitation_code_page_locators = InvitationCodePageLocators()

    def verify_invitation_code_page(self):
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.TITLE_IN_INVITATION_CODE_PAGE)
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.INVITATION_CODE_IN_INVITATION_CODE_PAGE)
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.DESCRIPTION_IN_INVITATION_CODE_PAGE)
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.SHARE_INVITATION_CODE_BUTTON_IN_INVITATION_CODE_PAGE)
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.INVITED_LIST_IN_INVITATION_CODE_PAGE)
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.CLOSE_BUTTON_IN_INVITATION_CODE_PAGE)
        return self

    def tap_invitation_code_share_button(self):
        self.common_actions.click_element(*self.invitation_code_page_locators.SHARE_INVITATION_CODE_BUTTON_IN_INVITATION_CODE_PAGE)
        self.common_actions.wait_for_element_clickable(*self.invitation_code_page_locators.COPY_INVITATION_BUTTON)
        self.common_actions.click_element(*self.invitation_code_page_locators.COPY_INVITATION_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.invitation_code_page_locators.COPY_INVITATION_BUTTON)
        return self

    def tap_invited_list_button(self):
        self.common_actions.click_element(*self.invitation_code_page_locators.INVITED_LIST_IN_INVITATION_CODE_PAGE)
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.TITLE_IN_INVITED_LIST)
        self.common_actions.is_element_visible(*self.invitation_code_page_locators.CLOSE_BUTTON_IN_INVITED_LIST)
        return self

    def tap_invited_list_close_button(self):
        self.common_actions.click_element(*self.invitation_code_page_locators.CLOSE_BUTTON_IN_INVITED_LIST)
        self.common_actions.wait_for_element_disappear(*self.invitation_code_page_locators.CLOSE_BUTTON_IN_INVITED_LIST)
        return self

