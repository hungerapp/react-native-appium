from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.service_personnel import ServicePersonnelPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../features/navigation/setting/service_personnel.feature')

# Scenario: Successfully add new service personnel
@given("I am on the Branch Settings page")
def on_branch_setting_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the Service Personnel")
def tap_service_personnel_button(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_service_personnel_button(), "Service Personnel button not found in Branch Settings page"

@when("I delete all service personnel")
def delete_all_service_personnel(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.delete_service_personnel(delete_all=True), "Service Personnel list is not empty"

@when(parsers.parse('I add service personnel "{service_personnel_name}" and select color "{color_num}" and enter "{service_personnel_introduction}" and the Simultaneous Service Count "{simultaneous_service_count}"'))
def add_service_personnel(driver, service_personnel_name, color_num, service_personnel_introduction, simultaneous_service_count):
    service_personnel_name = CommonUseSection.replace_current_datetime(service_personnel_name)
    service_personnel_introduction = CommonUseSection.replace_current_datetime(service_personnel_introduction)
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_add_service_personnel_button(), "Add Service Personnel button is not found"
    assert service_personnel_page.enter_service_personnel_name(service_personnel_name), "Service Personnel Name field is not found"
    assert service_personnel_page.select_color(color_num), "Color selection is not found"
    assert service_personnel_page.enter_service_personnel_introduction(service_personnel_introduction), "Service Personnel Introduction field is not found"
    assert service_personnel_page.enter_simultaneous_service_count(simultaneous_service_count), "Simultaneous Service Count field is not found"
    assert service_personnel_page.tap_confirm_button(), "Confirm button in service personnel modal is not found"

@when(parsers.parse('I edit service personnel "{old_service_personnel_name}" to "{new_service_personnel_name}" and select color "{color_num}" and enter "{service_personnel_introduction}" and the Simultaneous Service Count "{simultaneous_service_count}"'))
def edit_service_personnel(driver, old_service_personnel_name, new_service_personnel_name, color_num, service_personnel_introduction, simultaneous_service_count):
    old_service_personnel_name = CommonUseSection.replace_current_datetime(old_service_personnel_name)
    new_service_personnel_name = CommonUseSection.replace_current_datetime(new_service_personnel_name)
    service_personnel_introduction = CommonUseSection.replace_current_datetime(service_personnel_introduction)
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_edit_service_personnel_button(old_service_personnel_name), f"Service Personnel name {old_service_personnel_name} is not found in the list"
    assert service_personnel_page.enter_service_personnel_name(new_service_personnel_name), "Service Personnel Name field is not found"
    assert service_personnel_page.select_color(color_num), "Color selection is not found"
    assert service_personnel_page.enter_service_personnel_introduction(service_personnel_introduction), "Service Personnel Introduction field is not found"
    assert service_personnel_page.enter_simultaneous_service_count(simultaneous_service_count), "Simultaneous Service Count field is not found"
    assert service_personnel_page.tap_confirm_button(), "Confirm button in service personnel modal is not found"

@when(parsers.parse('I delete "{service_personnel_name}" from the Service Personnel list'))
def delete_service_personnel(driver, service_personnel_name):
    service_personnel_name = CommonUseSection.replace_current_datetime(service_personnel_name)
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.delete_service_personnel(service_personnel_name), f"Service Personnel name {service_personnel_name} is not found in the list"

@when(parsers.parse('I add service personnel "{service_personnel_name}" and select color "{color_num}" and enter "{service_personnel_introduction}" and the Simultaneous Service Count "{simultaneous_service_count}"'))
def add_service_personnel(driver, service_personnel_name, color_num, service_personnel_introduction, simultaneous_service_count):
    service_personnel_name = CommonUseSection.replace_current_datetime(service_personnel_name)
    service_personnel_introduction = CommonUseSection.replace_current_datetime(service_personnel_introduction)
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_add_service_personnel_button(), "Add Service Personnel button is not found"
    assert service_personnel_page.enter_service_personnel_name(service_personnel_name), "Service Personnel Name field is not found"
    assert service_personnel_page.select_color(color_num), "Color selection is not found"
    assert service_personnel_page.enter_service_personnel_introduction(service_personnel_introduction), "Service Personnel Introduction field is not found"
    assert service_personnel_page.enter_simultaneous_service_count(simultaneous_service_count), "Simultaneous Service Count field is not found"
    assert service_personnel_page.tap_confirm_button(), "Confirm button in service personnel modal is not found"

@when("I tap on the close button in service personnel Page")
def tap_close_button(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_close_button(), "Close button in service personnel page is not found"

@then("I should see the branch settings page")
def verify_branch_settings_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_branch_settings_page(), "Branch Settings page not found"






    
