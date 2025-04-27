from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.service_appointment import ServiceAppointmentPage

scenarios('../../../../features/navigation/setting/service_appointment.feature')
@given('I am on the service appointment page')
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"


@when("I share the appointment link")
def share_appointment_link(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.share_appointment_link(), "Share appointment link is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"

@when("I tap on the service items")
def tap_service_items(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_service_items(), "Service items are not displayed"

@then("I should see the service items page")
def verify_service_items_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_items_page(), "Service items page is not displayed"

@given("I am on the service items page")
def verify_service_items_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_items_page(), "Service items page is not displayed"

@when(parsers.parse('I Add a new service category named "{category_name}"'))
def add_service_category(driver, category_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_service_category(category_name), "Add service category is not displayed"

@then(parsers.parse('I should see the service category named "{category_name}"'))
def verify_service_category(driver, category_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_category(category_name), "Service category is not displayed"

@when(parsers.parse('I edit the service category named "{old_category}" to "{new_category}"'))
def edit_service_category(driver, old_category, new_category):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.edit_service_category(old_category, new_category), "Edit service category is not displayed"

@when(parsers.parse('I delete the service category named "{category_name}"'))
def delete_service_category(driver, category_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_service_category(category_name), "Delete service category is not displayed"

@then(parsers.parse('I should not see the service category named "{category_name}"'))
def verify_service_category_not_visible(driver, category_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_category_not_visible(category_name), "Service category is still displayed"

@when(parsers.parse('I select a service category named "{category_name}"'))
def select_service_category(driver, category_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_service_category(category_name), "Select service category is not displayed"

@when("I click the add service item button")
def click_add_service_item_button(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.click_add_service_item_button(), "Add service item button is not displayed"

@when(parsers.parse('I enter the service item name "{item_name}"'))
def enter_service_item_name(driver, item_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_item_name(item_name), "Service item name input is not displayed"

@when(parsers.parse('I enter the service code name "{code_name}"'))
def enter_service_code_name(driver, code_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_code_name(code_name), "Service code name input is not displayed"

@when(parsers.parse('I enter the service introduction "{introduction}"'))
def enter_service_introduction(driver, introduction):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_introduction(introduction), "Service introduction input is not displayed"

@when(parsers.parse('I enter the service duration "{duration}" minutes'))
def select_service_duration(driver, duration):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_duration(duration), "Service duration selection is not displayed"

@when(parsers.parse('I enter the service price "{price}"'))
def enter_service_price(driver, price):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_price(price), "Service price input is not displayed"

@when('I select the service display type fixed price')
def select_fixed_price(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_fixed_price(), "Select fixed price is not displayed"

@when('I select the service display type starting price')
def select_starting_price(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_starting_price(), "Select starting price is not displayed"

@when('I select the sub service type single choice')
def select_single_choice(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_single_choice(), "Select single choice is not displayed"

@when('I select the sub service type multiple choice')
def select_multiple_choice(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_multiple_choice(), "Select multiple choice is not displayed"

@when(parsers.parse('I add sub service items name "{sub_item_name}" and duration "{duration}" minutes and price "{price}"'))
def add_sub_service_items(driver, sub_item_name, duration, price):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_sub_service_items(sub_item_name, duration, price), "Add sub service items is not displayed"

@when(parsers.parse('I select the service category "{category_name}" in the add service item'))
def select_service_category_in_add_service_item(driver, category_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_service_category_in_add_service_item(category_name), "Select service category in add service item is not displayed"

@when('I click the save add service item button')
def click_save_add_service_item_button(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.click_save_add_service_item_button(), "Save add service item button is not displayed"

@then(parsers.parse('I should see the service item name "{item_name}"'))
def verify_service_item_name(driver, item_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_item_name(item_name), "Service item name is not displayed"

@when('I tap on the online booking')
def tap_online_booking(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_online_booking(), "Online booking is not displayed"

@then('I should see the online booking page')
def verify_online_booking_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_online_booking_page(), "Online booking page is not displayed"

