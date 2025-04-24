from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.service_personnel import ServicePersonnelPage

scenarios('../../../../features/navigation/setting/service_personnel.feature')

@given("I am on the Service Personnel page")
def verify_on_service_personnel_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_page(), "Service Personnel page is not found"

@when("I tap on Add Service Personnel button")
def tap_add_service_personnel_button(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.tap_add_service_personnel_button(), "Add Service Personnel button is not found"

@then("I should see the service personnel Modal")
def verify_service_personnel_modal(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_modal(), "Service Personnel Modal is not found"

@when(parsers.parse('I enter "{service_personnel_name}" in the Name field'))
def enter_service_personnel_name(driver, service_personnel_name):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.enter_service_personnel_name(service_personnel_name), "Service Personnel Name field is not found"

@when(parsers.parse('I select color "{color_num}" from the Color list'))
def select_color(driver, color_num):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.select_color(color_num), "Color selection is not found"

@when(parsers.parse('I enter "{service_personnel_introduction}" in the Introduction field'))
def enter_service_personnel_introduction(driver, service_personnel_introduction):
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

@then("I should see the Service Personnel page")
def verify_service_personnel_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_page(), "Service Personnel page is not found"

@then(parsers.parse('I should see "{service_personnel_name}" in the Service Personnel list'))
def verify_service_personnel_name(driver, service_personnel_name):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_name(service_personnel_name), f"Service Personnel name {service_personnel_name} is not found in the list"

@given(parsers.parse('I should see "{service_personnel_name}" in the Service Personnel list'))
def verify_service_personnel_name(driver, service_personnel_name):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_name(service_personnel_name), f"Service Personnel name {service_personnel_name} is not found in the list"

@when(parsers.parse('I delete "{service_personnel_name}" from the Service Personnel list'))
def delete_service_personnel(driver, service_personnel_name):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.delete_service_personnel(service_personnel_name), f"Service Personnel name {service_personnel_name} is not found in the list"