from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.third_party_tools import ThirdPartToolsPage
from pages.android.calendar.calendar_page import CalendarPage
from pages.android.personal_page import PersonalPage

scenarios('../../../features/navigation/setting/third_party_tools.feature')

# Background: Select the target branch for testing
@given(parsers.parse('I have selected the target branch "{branch_name}"'))
def verify_current_branch(driver, branch_name):
    calendar_page = CalendarPage(driver)
    personal_page = PersonalPage(driver)
    calendar_page.tap_branch_button()
    personal_page.select_branch(branch_name)
    calendar_page.click_close_tutorial_popup()

@given("I Navigate to the branch settings page")
def navigate_to_branch_settings_page(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.tap_navigation_bar_settings_icon()





# Scenario: SMS Settings
@given(parsers.parse('This branch is subscribed to "{plan_name}"'))
def subscribed_to_free_plan(driver, plan_name):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.verify_subscription_plan(plan_name), "Plan is not displayed"

@when("I tap on the Third Party Tools")
def tap_third_party_tools(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_third_party_tools(), "Failed to tap on Third Party Tools"

@when("I tap on the SMS button")
def tap_sms_button(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_sms_button(), "Failed to tap on SMS button"

@when("I turn on the appointment success SMS")
def turn_on_appointment_success_sms(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_appointment_success_sms(), "Failed to turn on appointment success SMS"

@when("I turn off the appointment success SMS")
def turn_off_appointment_success_sms(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_appointment_success_sms(), "Failed to turn off appointment success SMS"

@when("I turn on the appointment reminder SMS")
def turn_on_appointment_reminder_sms(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_appointment_reminder_sms(), "Failed to turn on appointment reminder SMS"

@when("I turn off the appointment reminder SMS")
def turn_off_appointment_reminder_sms(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_appointment_reminder_sms(), "Failed to turn off appointment reminder SMS"

@when("I tap on the close button in the SMS settings")
def tap_close_button_in_sms_settings(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_sms_settings(), "Failed to tap on close button in SMS settings"

@when("I tap on the back to calendar button in the third party tools")
def tap_back_to_calendar_button_in_third_party_tools(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_back_to_calendar_button_in_third_party_tools(), "Failed to tap on back to calendar button in third party tools"

@then("I should see the calendar page")
def verify_calendar_page(driver):
    calendar_page = CalendarPage(driver)
    assert calendar_page.verify_calendar_page(), "Calendar page is not displayed"




# Scenario: LINE OA Settings
@given(parsers.parse('This branch is subscribed to "{plan_name}"'))
def subscribed_to_free_plan(driver, plan_name):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.verify_subscription_plan(plan_name), "Plan is not displayed"

@when("I tap on the Third Party Tools")
def tap_third_party_tools(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_third_party_tools(), "Failed to tap on Third Party Tools"

@when("I tap on the LINE OA button")
def tap_line_oa_button(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_line_oa_button(), "Failed to tap on LINE OA button"

@when("I tap on the LINE LIFF integration")
def tap_line_liff_integration(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_line_liff_integration(), "Failed to tap on LINE LIFF integration"

@when("I tap on the close button in the LINE LIFF integration")
def tap_close_button_in_line_liff_integration(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_line_liff_integration(), "Failed to tap on close button in LINE LIFF integration"

@when("I tap on the LINE widget integration")
def tap_line_widget_integration(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_line_widget_integration(), "Failed to tap on LINE widget integration"

@when("I turn on the Hotcake rich menu")
def turn_on_hotcake_rich_menu(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_hotcake_rich_menu(), "Failed to turn on Hotcake rich menu"

@when("I turn off the Hotcake rich menu")
def turn_off_hotcake_rich_menu(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_hotcake_rich_menu(), "Failed to turn off Hotcake rich menu"

@when("I tap on the close button in the LINE widget")
def tap_close_button_in_line_widget(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_line_widget(), "Failed to tap on close button in LINE widget"

@when("I tap on the notification settings")
def tap_notification_settings(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_notification_settings(), "Failed to tap on notification settings"

@when("I turn on the appointment reminder notification")
def turn_on_appointment_reminder_notification(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_appointment_reminder_notification(), "Failed to turn on appointment reminder notification"

@when("I turn off the appointment reminder notification")
def turn_off_appointment_reminder_notification(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_appointment_reminder_notification(), "Failed to turn off appointment reminder notification"

@when(parsers.parse('I set the appointment reminder time to "{time}"'))
def set_appointment_reminder_time(driver, time):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.set_appointment_reminder_time(time), "Failed to set appointment reminder time"

@when(parsers.parse('I set the appointment reminder custom message to "{message}"'))
def set_appointment_reminder_custom_message(driver, message):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.set_appointment_reminder_custom_message(message), "Failed to set appointment reminder custom message"

@when("I turn on the appointment success notification")
def turn_on_appointment_success_notification(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_appointment_success_notification(), "Failed to turn on appointment success notification"

@when("I turn off the appointment success notification")
def turn_off_appointment_success_notification(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_appointment_success_notification(), "Failed to turn off appointment success notification"

@when(parsers.parse('I set the appointment success custom message to "{message}"'))
def set_appointment_success_custom_message(driver, message):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.set_appointment_success_custom_message(message), "Failed to set appointment success custom message"

@when("I turn on the appointment cancellation notification")
def turn_on_appointment_cancellation_notification(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_appointment_cancellation_notification(), "Failed to turn on appointment cancellation notification"

@when("I turn off the appointment cancellation notification")
def turn_off_appointment_cancellation_notification(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_appointment_cancellation_notification(), "Failed to turn off appointment cancellation notification"

@when("I turn on the ticket notification on manual send")
def turn_on_ticket_notification_on_manual_send(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_ticket_notification_on_manual_send(), "Failed to turn on ticket notification on manual send"

@when("I turn off the ticket notification on manual send")
def turn_off_ticket_notification_on_manual_send(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_ticket_notification_on_manual_send(), "Failed to turn off ticket notification on manual send"

@when("I turn on the ticket notification on auto send")
def turn_on_ticket_notification_on_auto_send(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_on_ticket_notification_on_auto_send(), "Failed to turn on ticket notification on auto send"

@when("I turn off the ticket notification on auto send")
def turn_off_ticket_notification_on_auto_send(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.turn_off_ticket_notification_on_auto_send(), "Failed to turn off ticket notification on auto send"

@when("I tap on the close button in the notification settings")
def tap_close_button_in_notification_settings(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_notification_settings(), "Failed to tap on close button in notification settings"

@when("I tap on the close button in the LINE OA settings")
def tap_close_button_in_line_oa_settings(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_line_oa_settings(), "Failed to tap on close button in LINE OA settings"

@when("I tap on the back to calendar button in the third party tools")
def tap_back_to_calendar_button_in_third_party_tools(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_back_to_calendar_button_in_third_party_tools(), "Failed to tap on back to calendar button in third party tools"

@then("I should see the calendar page")
def verify_calendar_page(driver):
    calendar_page = CalendarPage(driver)
    assert calendar_page.verify_calendar_page(), "Calendar page is not displayed"




# Scenario: Payment Integration Settings
@given(parsers.parse('This branch is subscribed to "{plan_name}"'))
def subscribed_to_free_plan(driver, plan_name):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.verify_subscription_plan(plan_name), "Plan is not displayed"

@when("I tap on the Third Party Tools")
def tap_third_party_tools(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_third_party_tools(), "Failed to tap on Third Party Tools"

@when("I tap on the Payment Integration button")
def tap_payment_integration_button(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_payment_integration_button(), "Failed to tap on Payment Integration button"

@when("I tap on the INSTO Integration")
def tap_insto_integration(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_insto_integration(), "Failed to tap on INSTO Integration"

@when("I tap on the close button in the INSTO integration")
def tap_close_button_in_insto_integration(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_insto_integration(), "Failed to tap on close button in INSTO integration"

@when("I tap on the LINE Pay integration")
def tap_line_pay_integration(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_line_pay_integration(), "Failed to tap on LINE Pay integration"

@when("I tap on the close button in the LINE Pay integration")
def tap_close_button_in_line_pay_integration(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_line_pay_integration(), "Failed to tap on close button in LINE Pay integration"

@when("I tap on the close button in the Payment Integration settings")
def tap_close_button_in_payment_integration_settings(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_close_button_in_payment_integration_settings(), "Failed to tap on close button in Payment Integration settings"

@when("I tap on the back to calendar button in the third party tools")
def tap_back_to_calendar_button_in_third_party_tools(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_back_to_calendar_button_in_third_party_tools(), "Failed to tap on back to calendar button in third party tools"

@then("I should see the calendar page")
def verify_calendar_page(driver):
    calendar_page = CalendarPage(driver)
    assert calendar_page.verify_calendar_page(), "Calendar page is not displayed"