from pytest_bdd import scenarios, given, when, then, parsers
from pages.shared_components.common_use import CommonUseSection
from pages.android.navigation.setting.web_layout_management import WebLayoutManagementPage
from pages.android.calendar.calendar_page import CalendarPage
from pages.android.personal_page import PersonalPage

scenarios('../../../features/navigation/setting/web_layout_management.feature')

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






# Scenario: Setting the web layout
@given("I am on the branch settings page")
def on_branch_settings_page(driver):
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.verify_branch_settings_page(), "Branch settings page is not displayed"

@when("I tap on the Web Layout")
def tap_web_layout_management(driver):
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.tap_web_layout_management(), "Failed to tap on Web Layout Management"

@when(parsers.parse("I select the web layout color {color}"))
def select_web_layout_color(driver, color):
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.select_web_layout_color(color), f"Failed to select the web layout color {color}"

@when(parsers.parse('I set week start day to "{day}"'))
def set_week_start_day(driver, day):
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.set_week_start_day(day), f"Failed to set week start day to {day}"

@when(parsers.parse('I set the google tracking code to "{tracking_code}"'))
def set_google_tracking_code(driver, tracking_code):
    tracking_code = CommonUseSection.replace_current_datetime(tracking_code)
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.set_google_tracking_code(tracking_code), f"Failed to set Google tracking code to {tracking_code}"

@when("I tap on the confirm button")
def tap_confirm_button(driver):
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.tap_confirm_button(), "Failed to tap on the confirm button"

@when("I tap on the close button in the web layout page")
def tap_close_button(driver):
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.tap_close_button(), "Failed to tap on the close button in the web layout page"

@when("I tap on the close button in the branch settings page")
def tap_close_button_in_branch_settings_page(driver):
    web_layout_management_page = WebLayoutManagementPage(driver)
    assert web_layout_management_page.tap_close_button_in_branch_settings_page(), "Failed to tap on the close button in the branch settings page"