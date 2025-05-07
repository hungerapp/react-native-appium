from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.service_personnel import ServicePersonnelPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../../features/navigation/setting/service_personnel.feature')

# Scenario: Successfully add new service personnel
@given("I am on the Branch Settings page")
def on_branch_setting_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the Service Personnel")
def tap_service_personnel_button(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_service_personnel_button(), "Service Personnel button not found in Branch Settings page"

@when("I tap on Add Service Personnel button")
def tap_add_service_personnel_button(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_add_service_personnel_button(), "Add Service Personnel button is not found"

@when(parsers.parse('I enter "{service_personnel_name}" in the Name field'))
def enter_service_personnel_name(driver, service_personnel_name):
    service_personnel_name = CommonUseSection.replace_current_datetime(service_personnel_name)
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.enter_service_personnel_name(service_personnel_name), "Service Personnel Name field is not found"

@when(parsers.parse('I select color "{color_num}" from the Color list'))
def select_color(driver, color_num):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.select_color(color_num), "Color selection is not found"

@when(parsers.parse('I enter "{service_personnel_introduction}" in the Introduction field'))
def enter_service_personnel_introduction(driver, service_personnel_introduction):
    service_personnel_introduction = CommonUseSection.replace_current_datetime(service_personnel_introduction)
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.enter_service_personnel_introduction(service_personnel_introduction), "Service Personnel Introduction field is not found"

@when(parsers.parse('I enter "{simultaneous_service_count}" in the Simultaneous Service Count field'))
def enter_simultaneous_service_count(driver, simultaneous_service_count):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.enter_simultaneous_service_count(simultaneous_service_count), "Simultaneous Service Count field is not found"

@when("I tap on the Confirm button in service personnel modal")
def tap_confirm_button(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_confirm_button(), "Confirm button in service personnel modal is not found"

@when(parsers.parse('I delete "{service_personnel_name}" from the Service Personnel list'))
def delete_service_personnel(driver, service_personnel_name):
    service_personnel_name = CommonUseSection.replace_current_datetime(service_personnel_name)
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.delete_service_personnel(service_personnel_name), f"Service Personnel name {service_personnel_name} is not found in the list"

@when("I tap on the close button in service personnel Page")
def tap_close_button(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_close_button(), "Close button in service personnel page is not found"

@then("I should see the branch settings page")
def verify_branch_settings_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_branch_settings_page(), "Branch Settings page not found"






    
