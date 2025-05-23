from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.third_party_tools_locators import ThirdPartToolsPageLocators

# noinspection DuplicatedCode
class ThirdPartToolsPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = ThirdPartToolsPageLocators()
        self.common_actions = CommonActions(driver)
        self.common_use_section = CommonUseSection(driver)

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE)
        return self

    def verify_subscription_plan(self, subscription_name):
        self.common_actions.wait_for_element_visible(*self.locators.SUBSCRIPTION_PLAN_IN_BRANCH_SETTINGS_PAGE(subscription_name))
        return self

    def tap_third_party_tools(self):
        self.common_actions.wait_for_element_visible(*self.locators.THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE)
        return self

    def tap_sms_button(self):
        self.common_actions.wait_for_element_visible(*self.locators.SMS_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.SMS_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        return self

    def turn_on_appointment_success_sms(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_SUCCESS_SMS_SWITCH_IN_SMS_SETTINGS_PAGE)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_SUCCESS_SMS_SWITCH_IN_SMS_SETTINGS_PAGE, should_be_on=True)
        return self

    def turn_off_appointment_success_sms(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_SUCCESS_SMS_SWITCH_IN_SMS_SETTINGS_PAGE)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_SUCCESS_SMS_SWITCH_IN_SMS_SETTINGS_PAGE, should_be_on=False)
        return self

    def turn_on_appointment_reminder_sms(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_REMINDER_SMS_SWITCH_IN_SMS_SETTINGS_PAGE)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_REMINDER_SMS_SWITCH_IN_SMS_SETTINGS_PAGE, should_be_on=True)
        return self

    def turn_off_appointment_reminder_sms(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_REMINDER_SMS_SWITCH_IN_SMS_SETTINGS_PAGE)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_REMINDER_SMS_SWITCH_IN_SMS_SETTINGS_PAGE, should_be_on=False)
        return self

    def tap_close_button_in_sms_settings(self):
        self.common_actions.wait_for_element_visible(*self.locators.CLOSE_BUTTON_IN_SMS_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.CLOSE_BUTTON_IN_SMS_SETTINGS_PAGE)
        return self

    def tap_back_to_calendar_button_in_third_party_tools(self):
        self.common_actions.wait_for_element_visible(*self.locators.BACK_TO_CALENDAR_BUTTON_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.BACK_TO_CALENDAR_BUTTON_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        return self

    def tap_line_oa_button(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_OA_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.LINE_OA_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        return self

    def tap_line_liff_integration(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_LIFF_INTEGRATION_IN_LINE_OA_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.LINE_LIFF_INTEGRATION_IN_LINE_OA_SETTINGS_PAGE)
        return self

    def tap_close_button_in_line_liff_integration(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_LIFF_INTEGRATION_CLOSE_BUTTON)
        self.common_actions.click_element(*self.locators.LINE_LIFF_INTEGRATION_CLOSE_BUTTON)
        return self

    def tap_line_widget_integration(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_WIDGETS_IN_LINE_OA_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.LINE_WIDGETS_IN_LINE_OA_SETTINGS_PAGE)
        return self

    def turn_on_hotcake_rich_menu(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_WIDGETS_INTEGRATION_HOTCAKE_RICH_MENU_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.LINE_WIDGETS_INTEGRATION_HOTCAKE_RICH_MENU_SWITCH, should_be_on=True)
        return self

    def turn_off_hotcake_rich_menu(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_WIDGETS_INTEGRATION_HOTCAKE_RICH_MENU_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.LINE_WIDGETS_INTEGRATION_HOTCAKE_RICH_MENU_SWITCH, should_be_on=False)
        return self

    def tap_close_button_in_line_widget(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_WIDGETS_INTEGRATION_CLOSE_BUTTON)
        self.common_actions.click_element(*self.locators.LINE_WIDGETS_INTEGRATION_CLOSE_BUTTON)
        return self

    def tap_notification_settings(self):
        self.common_actions.wait_for_element_visible(*self.locators.NOTIFICATION_SETTINGS_IN_LINE_OA_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.NOTIFICATION_SETTINGS_IN_LINE_OA_SETTINGS_PAGE)
        return self

    def turn_on_appointment_reminder_notification(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_REMINDER_NOTIFICATION_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_REMINDER_NOTIFICATION_SWITCH, should_be_on=True)
        return self

    def turn_off_appointment_reminder_notification(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_REMINDER_NOTIFICATION_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_REMINDER_NOTIFICATION_SWITCH, should_be_on=False)
        return self

    def set_appointment_reminder_time(self, time):
        self.common_actions.wait_for_element_visible(*self.locators.NOTIFICATION_TIME)
        self.common_actions.click_element(*self.locators.NOTIFICATION_TIME)
        self.common_actions.click_element(*self.locators.NOTIFICATION_TIME_SELECT(time))
        return self

    def set_appointment_reminder_custom_message(self, message):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_REMINDER_NOTIFICATION_CUSTOM_MESSAGE)
        self.common_actions.click_element(*self.locators.APPOINTMENT_REMINDER_NOTIFICATION_CUSTOM_MESSAGE)
        self.common_actions.wait_for_element_visible(*self.locators.CUSTOM_MESSAGE_DIALOG_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.CUSTOM_MESSAGE_DIALOG_SWITCH, should_be_on=True)
        if not self.common_actions.wait_for_element_present(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE, timeout=1):
            self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_SWITCH)
        self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE)
        self.common_actions.wait_for_element_visible(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_FIELD)
        # self.common_actions.send_keys_to_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_FIELD, message)
        message_field = self.common_actions.find_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_FIELD)
        message_field.send_keys(message)
        self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.locators.CUSTOM_MESSAGE_DIALOG_CONFIRM_BUTTON)
        return self

    def turn_on_appointment_success_notification(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_SUCCESS_NOTIFICATION_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_SUCCESS_NOTIFICATION_SWITCH, should_be_on=True)
        return self

    def turn_off_appointment_success_notification(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_SUCCESS_NOTIFICATION_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_SUCCESS_NOTIFICATION_SWITCH, should_be_on=False)
        return self

    def set_appointment_success_custom_message(self, message):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_SUCCESS_NOTIFICATION_CUSTOM_MESSAGE)
        self.common_actions.click_element(*self.locators.APPOINTMENT_SUCCESS_NOTIFICATION_CUSTOM_MESSAGE)
        self.common_actions.wait_for_element_visible(*self.locators.CUSTOM_MESSAGE_DIALOG_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.CUSTOM_MESSAGE_DIALOG_SWITCH, should_be_on=True)
        if not self.common_actions.wait_for_element_present(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE, timeout=1):
            self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_SWITCH)
        self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE)
        self.common_actions.wait_for_element_visible(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_FIELD)
        # self.common_actions.send_keys_to_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_FIELD, message)
        message_field = self.common_actions.find_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_FIELD)
        message_field.send_keys(message)
        self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.locators.CUSTOM_MESSAGE_DIALOG_MESSAGE_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.locators.CUSTOM_MESSAGE_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.locators.CUSTOM_MESSAGE_DIALOG_CONFIRM_BUTTON)
        return self

    def turn_on_appointment_cancellation_notification(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_CANCELLATION_NOTIFICATION_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_CANCELLATION_NOTIFICATION_SWITCH, should_be_on=True)
        return self

    def turn_off_appointment_cancellation_notification(self):
        self.common_actions.wait_for_element_visible(*self.locators.APPOINTMENT_CANCELLATION_NOTIFICATION_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.APPOINTMENT_CANCELLATION_NOTIFICATION_SWITCH, should_be_on=False)
        return self

    def turn_on_ticket_notification_on_manual_send(self):
        self.common_actions.wait_for_element_visible(*self.locators.TICKET_NOTIFICATION_ON_MANUAL_SEND_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.TICKET_NOTIFICATION_ON_MANUAL_SEND_SWITCH, should_be_on=True)
        return self

    def turn_off_ticket_notification_on_manual_send(self):
        self.common_actions.wait_for_element_visible(*self.locators.TICKET_NOTIFICATION_ON_MANUAL_SEND_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.TICKET_NOTIFICATION_ON_MANUAL_SEND_SWITCH, should_be_on=False)
        return self

    def turn_on_ticket_notification_on_auto_send(self):
        self.common_actions.wait_for_element_visible(*self.locators.TICKET_NOTIFICATION_ON_AUTO_SEND_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.TICKET_NOTIFICATION_ON_AUTO_SEND_SWITCH, should_be_on=True)
        return self

    def turn_off_ticket_notification_on_auto_send(self):
        self.common_actions.wait_for_element_visible(*self.locators.TICKET_NOTIFICATION_ON_AUTO_SEND_SWITCH)
        self.common_actions.toggle_switch_state(*self.locators.TICKET_NOTIFICATION_ON_AUTO_SEND_SWITCH, should_be_on=False)
        return self

    def tap_close_button_in_notification_settings(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_OA_NOTIFICATION_SETTINGS_CLOSE_BUTTON)
        self.common_actions.click_element(*self.locators.LINE_OA_NOTIFICATION_SETTINGS_CLOSE_BUTTON)
        return self

    def tap_close_button_in_line_oa_settings(self):
        self.common_actions.wait_for_element_visible(*self.locators.CLOSE_BUTTON_IN_LINE_OA_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.CLOSE_BUTTON_IN_LINE_OA_SETTINGS_PAGE)
        return self

    def tap_payment_integration_button(self):
        self.common_actions.wait_for_element_visible(*self.locators.PAYMENT_INTEGRATION_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.PAYMENT_INTEGRATION_IN_THIRD_PART_TOOLS_SETTINGS_PAGE)
        return self

    def tap_insto_integration(self):
        self.common_actions.wait_for_element_visible(*self.locators.INSTO_INTEGRATION_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.INSTO_INTEGRATION_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE)
        return self

    def tap_close_button_in_insto_integration(self):
        self.common_actions.wait_for_element_visible(*self.locators.INSTO_INTEGRATION_CLOSE_BUTTON)
        self.common_actions.click_element(*self.locators.INSTO_INTEGRATION_CLOSE_BUTTON)
        return self

    def tap_line_pay_integration(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_PAY_INTEGRATION_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.LINE_PAY_INTEGRATION_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE)
        return self

    def tap_close_button_in_line_pay_integration(self):
        self.common_actions.wait_for_element_visible(*self.locators.LINE_PAY_INTEGRATION_CLOSE_BUTTON)
        self.common_actions.click_element(*self.locators.LINE_PAY_INTEGRATION_CLOSE_BUTTON)
        return self

    def tap_close_button_in_payment_integration_settings(self):
        self.common_actions.wait_for_element_visible(*self.locators.BACK_BUTTON_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.BACK_BUTTON_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE)
        return self