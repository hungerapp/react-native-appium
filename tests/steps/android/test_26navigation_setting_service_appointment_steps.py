from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.service_appointment import ServiceAppointmentPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../features/navigation/setting/service_appointment.feature')

# Scenario: Navigate to Service Appointment Page
@given("I am on the branch settings page")
def on_branch_settings_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_branch_settings_page(), "Branch settings page is not displayed"

@when("I tap on the service appointment")
def tap_service_appointment(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_service_appointment(), "Service appointment is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"




# Scenario: Share the appointment link
@given('I am on the service appointment page')
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"

@when("I share the appointment link")
def share_appointment_link(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.share_appointment_link(), "Share appointment link is not displayed"

@when("I click to apply for a LINE Official Account")
def click_apply_line_official_account(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.click_apply_line_official_account(), "Apply for LINE Official Account is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"




# Scenario: Service Item
@given("I am on the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"

@when("I tap on the service items")
def tap_service_items(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_service_items(), "Service items are not displayed"

@when("I delete all service category")
def delete_service_category(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_service_category(delete_all=True), "Delete service category is not displayed"

@when(parsers.parse('I add a new service category named "{category_name}"'))
def add_service_category(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_service_category(category_name), "Add service category is not displayed"

@when(parsers.parse('I edit the service category named "{old_category}" to "{new_category}"'))
def edit_service_category(driver, old_category, new_category):
    old_category = CommonUseSection.replace_current_datetime(old_category)
    new_category = CommonUseSection.replace_current_datetime(new_category)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.edit_service_category(old_category, new_category), "Edit service category is not displayed"

@when(parsers.parse('I delete the service category named "{category_name}"'))
def delete_service_category(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_service_category(category_name), "Delete service category is not displayed"

@when(parsers.parse('I add a new service category named "{category_name}"'))
def add_service_category(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_service_category(category_name), "Add service category is not displayed"

@when(parsers.parse('I select a service category named "{category_name}"'))
def select_service_category(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_service_category(category_name), "Select service category is not displayed"

@when("I click the add service item button")
def click_add_service_item_button(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.click_add_service_item_button(), "Add service item button is not displayed"
    
@when(parsers.parse('I enter the service item name "{item_name}"'))
def enter_service_item_name(driver, item_name):
    item_name = CommonUseSection.replace_current_datetime(item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_item_name(item_name), "Service item name input is not displayed"

@when(parsers.parse('I enter the service code name "{code_name}"'))
def enter_service_code_name(driver, code_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_code_name(code_name), "Service code name input is not displayed"

@when(parsers.parse('I enter the service introduction "{introduction}"'))
def enter_service_introduction(driver, introduction):
    introduction = CommonUseSection.replace_current_datetime(introduction)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_introduction(introduction), "Service introduction input is not displayed"

@when(parsers.parse('I select the service category "{category_name}" in the add service item'))
def select_service_category_in_add_service_item(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_service_category_in_add_service_item(category_name), "Select service category in add service item is not displayed"

@when(parsers.parse('I enter the service duration "{duration}" minutes'))
def select_service_duration(driver, duration):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_duration(duration), "Service duration selection is not displayed"

@when(parsers.parse('I enter the service price "{price}"'))
def enter_service_price(driver, price):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_price(price), "Service price input is not displayed"

@when(parsers.parse('I select the service display type "{display_price_method}"'))
def select_display_price_method(driver, display_price_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_display_price_method(display_price_method),  "Select display price method is not displayed"

@when(parsers.parse('I select the sub service type "{sub_service_type}"'))
def select_sub_service_type(driver, sub_service_type):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_sub_service_type(sub_service_type), "Select sub service type is not displayed"

@when(parsers.parse('I add sub service items name "{sub_item_name}" and duration "{duration}" minutes and price "{price}"'))
def add_sub_service_items(driver, sub_item_name, duration, price):
    sub_item_name = CommonUseSection.replace_current_datetime(sub_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_sub_service_items(sub_item_name, duration, price), "Add sub service items is not displayed"

@when(parsers.parse('I edit the sub service items "{old_sub_item_name}" to "{new_sub_item_name}" and duration "{duration}" minutes and price "{price}"'))
def edit_sub_service_items(driver, old_sub_item_name, new_sub_item_name, duration, price):
    old_sub_item_name = CommonUseSection.replace_current_datetime(old_sub_item_name)
    new_sub_item_name = CommonUseSection.replace_current_datetime(new_sub_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.edit_sub_service_items(old_sub_item_name, new_sub_item_name, duration, price), "Edit sub service items is not displayed"

@when(parsers.parse('I delete the sub service items "{sub_item_name}"'))
def delete_sub_service_items(driver, sub_item_name):
    sub_item_name = CommonUseSection.replace_current_datetime(sub_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_sub_service_items(sub_item_name), "Delete sub service items is not displayed"

@when(parsers.parse('I add sub service items name "{sub_item_name}" and duration "{duration}" minutes and price "{price}"'))
def add_sub_service_items(driver, sub_item_name, duration, price):
    sub_item_name = CommonUseSection.replace_current_datetime(sub_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_sub_service_items(sub_item_name, duration, price), "Add sub service items is not displayed"

@when(parsers.parse('I add sub service items name "{sub_item_name}" and duration "{duration}" minutes and price "{price}"'))
def add_sub_service_items(driver, sub_item_name, duration, price):
    sub_item_name = CommonUseSection.replace_current_datetime(sub_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_sub_service_items(sub_item_name, duration, price), "Add sub service items is not displayed"

@when('I click the save add service item button')
def click_save_add_service_item_button(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.click_save_add_service_item_button(), "Save add service item button is not displayed"

@when(parsers.parse('I copy the service item name "{item_name}"'))
def copy_service_item_name(driver, item_name):
    item_name = CommonUseSection.replace_current_datetime(item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.copy_service_item_name(item_name), "Copy service item name is not displayed"

@when(parsers.parse('I delete the service item "{item_name}"'))
def delete_service_item(driver, item_name):
    item_name = CommonUseSection.replace_current_datetime(item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_service_item(item_name), "Delete service item is not displayed"

@when(parsers.parse('I copy the service item name "{item_name}"'))
def copy_service_item_name(driver, item_name):
    item_name = CommonUseSection.replace_current_datetime(item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.copy_service_item_name(item_name), "Copy service item name is not displayed"

@when(parsers.parse('I edit the service item "{item_name}"'))
def edit_service_item(driver, item_name):
    item_name = CommonUseSection.replace_current_datetime(item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.edit_service_item(item_name), "Edit service item is not displayed"

@when(parsers.parse('I enter the service item name "{item_name}"'))
def enter_service_item_name(driver, item_name):
    item_name = CommonUseSection.replace_current_datetime(item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_item_name(item_name), "Service item name input is not displayed"

@when(parsers.parse('I enter the service code name "{code_name}"'))
def enter_service_code_name(driver, code_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_code_name(code_name), "Service code name input is not displayed"

@when(parsers.parse('I enter the service introduction "{introduction}"'))
def enter_service_introduction(driver, introduction):
    introduction = CommonUseSection.replace_current_datetime(introduction)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_introduction(introduction), "Service introduction input is not displayed"

@when(parsers.parse('I select the service category "{category_name}" in the add service item'))
def select_service_category_in_add_service_item(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_service_category_in_add_service_item(category_name), "Select service category in add service item is not displayed"

@when(parsers.parse('I enter the service duration "{duration}" minutes'))
def select_service_duration(driver, duration):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_duration(duration), "Service duration selection is not displayed"

@when(parsers.parse('I enter the service price "{price}"'))
def enter_service_price(driver, price):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_service_price(price), "Service price input is not displayed"

@when(parsers.parse('I select the service display type "{display_price_method}"'))
def select_display_price_method(driver, display_price_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_display_price_method(display_price_method),  "Select display price method is not displayed"

@when(parsers.parse('I select the sub service type "{sub_service_type}"'))
def select_sub_service_type(driver, sub_service_type):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_sub_service_type(sub_service_type), "Select sub service type is not displayed"

@when(parsers.parse('I add sub service items name "{sub_item_name}" and duration "{duration}" minutes and price "{price}"'))
def add_sub_service_items(driver, sub_item_name, duration, price):
    sub_item_name = CommonUseSection.replace_current_datetime(sub_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_sub_service_items(sub_item_name, duration, price), "Add sub service items is not displayed"

@when('I click the save add service item button')
def click_save_add_service_item_button(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.click_save_add_service_item_button(), "Save add service item button is not displayed"

@when("I tap on the close button on the service item page")
def tap_close_service_item_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_service_item_page(), "Close service item page button is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"


    
    
    

# Scenario: Online Booking
@given('I am on the service appointment page')
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"

@given(parsers.parse('I have a service personnel named "{service_personnel}"'))
def verify_service_personnel(driver, service_personnel):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_personnel(service_personnel), "Service personnel is not displayed"

@given(parsers.parse('I have a service personnel named "{service_personnel}"'))
def verify_service_personnel(driver, service_personnel):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_personnel(service_personnel), "Service personnel is not displayed"

@given(parsers.parse('I have a service item "{category_name}" and "{service_item_name}"'))
def verify_service_item(driver, category_name, service_item_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_item(category_name, service_item_name), "Service item is not displayed"

@given(parsers.parse('I have a service item "{category_name}" and "{service_item_name}"'))
def verify_service_item(driver, category_name, service_item_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_item(category_name, service_item_name), "Service item is not displayed"

@when('I tap on the online booking')
def tap_online_booking(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_online_booking(), "Online booking is not displayed"

@when("I delete all appointment combinations")
def delete_appointment_combination(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_appointment_combination(delete_all=True), "Delete appointment combination is not displayed"

@when(parsers.parse('I add a new appointment combination named "{combination_name}" and introduction "{combination_introduction}" and service personnel "{service_personnel}"'))
def add_appointment_combination(driver, combination_name, combination_introduction, service_personnel):
    combination_name = CommonUseSection.replace_current_datetime(combination_name)
    combination_introduction = CommonUseSection.replace_current_datetime(combination_introduction)
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_add_appointment_combination(), "Add appointment combination is not displayed"
    assert service_appointment_page.enter_appointment_combination_name(combination_name), "Appointment combination name input is not displayed"
    assert service_appointment_page.enter_appointment_combination_introduction(combination_introduction), "Appointment combination introduction input is not displayed"
    assert service_appointment_page.select_appointment_combination_service_personnel(service_personnel), "Appointment combination service personnel selection is not displayed"
    assert service_appointment_page.tap_confirm_add_appointment_combination(), "Confirm add appointment combination button is not displayed"
    assert service_appointment_page.verify_appointment_combination_name(combination_name), "Appointment combination name is not displayed"

@when(parsers.parse('I delete the appointment combination named "{combination_name}"'))
def delete_appointment_combination(driver, combination_name):
    combination_name = CommonUseSection.replace_current_datetime(combination_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_appointment_combination(combination_name), "Delete appointment combination button is not displayed"

@when(parsers.parse('I add a new appointment combination named "{combination_name}" and introduction "{combination_introduction}" and service personnel "{service_personnel}"'))
def add_appointment_combination(driver, combination_name, combination_introduction, service_personnel):
    combination_name = CommonUseSection.replace_current_datetime(combination_name)
    combination_introduction = CommonUseSection.replace_current_datetime(combination_introduction)
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_add_appointment_combination(), "Add appointment combination is not displayed"
    assert service_appointment_page.enter_appointment_combination_name(combination_name), "Appointment combination name input is not displayed"
    assert service_appointment_page.enter_appointment_combination_introduction(combination_introduction), "Appointment combination introduction input is not displayed"
    assert service_appointment_page.select_appointment_combination_service_personnel(service_personnel), "Appointment combination service personnel selection is not displayed"
    assert service_appointment_page.tap_confirm_add_appointment_combination(), "Confirm add appointment combination button is not displayed"
    assert service_appointment_page.verify_appointment_combination_name(combination_name), "Appointment combination name is not displayed"

@when(parsers.parse('I edit the appointment combination "{combination_name}" and select the main service item "{service_item_category}" "{service_item_name}" and the online booking type "{online_booking_type}" and select the additional service item "{additional_service_item_category}" "{additional_service_item_name}"'))
def edit_appointment_combination(driver, combination_name, service_item_category, service_item_name, online_booking_type, additional_service_item_category, additional_service_item_name):
    combination_name = CommonUseSection.replace_current_datetime(combination_name)
    service_item_category = CommonUseSection.replace_current_datetime(service_item_category)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    additional_service_item_category = CommonUseSection.replace_current_datetime(additional_service_item_category)
    additional_service_item_name = CommonUseSection.replace_current_datetime(additional_service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_appointment_combination(combination_name), "Edit appointment combination is not displayed"
    assert service_appointment_page.tap_open_item_tab(), "Open item tab is not displayed"
    assert service_appointment_page.select_main_service_item(service_item_category, service_item_name, clear_all=True), "Main service item selection and clear all options is not displayed"
    assert service_appointment_page.select_online_booking_type(online_booking_type), "Online booking type selection is not displayed"
    assert service_appointment_page.select_additional_service_item(additional_service_item_category, additional_service_item_name, clear_all=True), "Additional service item selection is not displayed"
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"
    assert service_appointment_page.verify_appointment_combination_name(combination_name), "Appointment combination name is not displayed"

@when(parsers.parse('I modify the service personnel "{service_personnel}" open settings to set available date "{specific_day}" "{open_month}" and latest booking time "{latest_booking_time}" and online booking quantity range "{min_quantity}" to "{max_quantity}"'))
def modify_service_personnel_open_settings(driver, service_personnel, specific_day, open_month, latest_booking_time, min_quantity, max_quantity):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_service_personnel(service_personnel), "Edit service personnel is not displayed"
    assert service_appointment_page.set_available_date(specific_day, open_month), "Set available date is not displayed"
    assert service_appointment_page.set_online_booking_quantity_range(min_quantity,max_quantity), "Set online booking quantity range is not displayed"
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"

@when(parsers.parse('I modify the service personnel "{service_personnel}" open time to set today open time "{times}"'))
def modify_service_personnel_open_time(driver, service_personnel, times):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_service_personnel(service_personnel), "Edit service personnel is not displayed"
    assert service_appointment_page.set_open_time(times), "Set open time is not displayed"
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"

@when(parsers.parse('I modify the service personnel "{service_personnel}" open item to set the main service item "{service_item_category}" "{service_item_name}" and the online booking type "{online_booking_type}" and select the additional service item "{additional_service_item_category}" "{additional_service_item_name}"'))
def modify_service_personnel_open_item(driver, service_personnel, service_item_category, service_item_name, online_booking_type, additional_service_item_category, additional_service_item_name):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_item_category = CommonUseSection.replace_current_datetime(service_item_category)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    additional_service_item_category = CommonUseSection.replace_current_datetime(additional_service_item_category)
    additional_service_item_name = CommonUseSection.replace_current_datetime(additional_service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_service_personnel(service_personnel), "Edit service personnel is not displayed"
    assert service_appointment_page.tap_open_item_tab(), "Open item tab is not displayed"
    assert service_appointment_page.select_main_service_item(service_item_category, service_item_name, clear_all=True), "Main service item selection and clear all options is not displayed"
    assert service_appointment_page.select_online_booking_type(online_booking_type), "Online booking type selection is not displayed"
    assert service_appointment_page.select_additional_service_item(additional_service_item_category, additional_service_item_name, clear_all=True), "Additional service item selection is not displayed"
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"

@when(parsers.parse('I modify the service personnel "{service_personnel}" open settings to set available date "{specific_day}" "{open_month}" and latest booking time "{latest_booking_time}" and online booking quantity range "{min_quantity}" to "{max_quantity}"'))
def modify_service_personnel_open_settings(driver, service_personnel, specific_day, open_month, latest_booking_time, min_quantity, max_quantity):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_service_personnel(service_personnel), "Edit service personnel is not displayed"
    assert service_appointment_page.set_available_date(specific_day, open_month), "Set available date is not displayed"
    assert service_appointment_page.set_online_booking_quantity_range(min_quantity,max_quantity), "Set online booking quantity range is not displayed"
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"

@when(parsers.parse('I modify the service personnel "{service_personnel}" open time to set today open time "{times}"'))
def modify_service_personnel_open_time(driver, service_personnel, times):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_service_personnel(service_personnel), "Edit service personnel is not displayed"
    assert service_appointment_page.set_open_time(times), "Set open time is not displayed"
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"

@when(parsers.parse('I modify the service personnel "{service_personnel}" open item to set the main service item "{service_item_category}" "{service_item_name}" and the online booking type "{online_booking_type}" and select the additional service item "{additional_service_item_category}" "{additional_service_item_name}"'))
def modify_service_personnel_open_item(driver, service_personnel, service_item_category, service_item_name, online_booking_type, additional_service_item_category, additional_service_item_name):
    service_personnel = CommonUseSection.replace_current_datetime(service_personnel)
    service_item_category = CommonUseSection.replace_current_datetime(service_item_category)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    additional_service_item_category = CommonUseSection.replace_current_datetime(additional_service_item_category)
    additional_service_item_name = CommonUseSection.replace_current_datetime(additional_service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_service_personnel(service_personnel), "Edit service personnel is not displayed"
    assert service_appointment_page.tap_open_item_tab(), "Open item tab is not displayed"
    assert service_appointment_page.select_main_service_item(service_item_category, service_item_name, clear_all=True), "Main service item selection and clear all options is not displayed"
    assert service_appointment_page.select_online_booking_type(online_booking_type), "Online booking type selection is not displayed"
    assert service_appointment_page.select_additional_service_item(additional_service_item_category, additional_service_item_name, clear_all=True), "Additional service item selection is not displayed"
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"

@when("I tap on the close button on the online booking page")
def tap_close_online_booking_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_online_booking_page(), "Close online booking page button is not displayed"

@then('I should see the online booking page')
def verify_online_booking_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_online_booking_page(), "Online booking page is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"





# Scenario: Booking Note Settings
@given('I am on the service appointment page')
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"

@when("I tap on the booking note")
def tap_booking_note(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_booking_note(), "Booking note is not displayed"

@when("I turn off the booking note switch")
def turn_off_booking_note_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_booking_note_switch(), "Booking note switch is not displayed"

@when("I turn on the booking note switch")
def turn_on_booking_note_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_booking_note_switch(), "Booking note switch is not displayed"

@when(parsers.parse('I enter the booking note "{booking_note}"'))
def enter_booking_note(driver, booking_note):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_booking_note(booking_note), "Booking note input is not displayed"

@when("I tap on the confirm button in the booking note")
def tap_confirm_booking_note(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_confirm_booking_note(), "Confirm booking note button is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"




# Scenario: Deposit Management Settings
@given('I am on the service appointment page')
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"

@given(parsers.parse('I have a service item "{category_name}" and "{service_item_name}"'))
def verify_service_item(driver, category_name, service_item_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_item(category_name, service_item_name), "Service item is not displayed"

@given(parsers.parse('I have a service item "{category_name}" and "{service_item_name}"'))
def verify_service_item(driver, category_name, service_item_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_item(category_name, service_item_name), "Service item is not displayed"

@when("I tap on the deposit management")
def tap_deposit_management(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_deposit_management(), "Deposit management is not displayed"

@when("I tap on the general deposit settings")
def tap_general_deposit_settings(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_general_deposit_settings(), "General deposit settings is not displayed"

@when("I turn off the general date deposit switch")
def turn_off_general_date_deposit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_general_date_deposit_switch(), "General date deposit switch is not displayed"

@when("I turn on the general date deposit switch")
def turn_on_general_date_deposit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_general_date_deposit_switch(), "General date deposit switch is not displayed"

@when("I set the default member status to no receive deposit")
def set_default_member_status_no_receive_deposit(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_default_member_status_no_receive_deposit(), "Default member status no receive deposit is not displayed"

@when(parsers.parse('I set the default member status to receive deposit and set the receive type "{receive_type}"'))
def set_default_member_status_receive_deposit(driver, receive_type):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_default_member_status_receive_deposit(receive_type), "Default member status receive deposit is not displayed"

@when(parsers.parse('I set the payable service item scope to "{service_scope}"'))
def set_payable_service_item_scope(driver, service_scope):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payable_service_item(service_scope), "Payable service item scope is not displayed"

@when(parsers.parse('I set the payable service item scope to "{service_scope}" and service item "{category_name}" "{service_item_name}" and clear all'))
def set_payable_service_item_scope(driver, service_scope, category_name, service_item_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payable_service_item(service_scope, category_name, service_item_name, clear_all=True), "Payable service item scope is not displayed"

@when("I go to integration payment method")
def go_to_integration_payment_method(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.go_to_integration_payment_method(), "Integration payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment amount pricing method to "{pricing_method}" and amount "{amount}"'))
def set_payment_amount_pricing_method(driver, pricing_method, amount):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_amount_pricing_method(pricing_method, amount), "Payment amount pricing method is not displayed"

@when(parsers.parse('I set the payment amount pricing method to "{pricing_method}" and minimum amount "{amount}" and percentage "{percentage}"'))
def set_payment_amount_pricing_method(driver, pricing_method, amount, percentage):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_amount_pricing_method(pricing_method, amount, percentage), "Payment amount pricing method is not displayed"

@when(parsers.parse('I set the auto cancel if unpaid to "{unpaid_time}"'))
def set_auto_cancel_if_unpaid(driver, unpaid_time):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_auto_cancel_if_unpaid(unpaid_time), "Auto cancel if unpaid is not displayed"

@when(parsers.parse('I set the payment instructions to "{instruction}"'))
def set_payment_instructions(driver, instruction):
    instruction = CommonUseSection.replace_current_datetime(instruction)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_instructions(instruction), "Payment instructions is not displayed"

@when("I tap on the confirm button in the deposit settings page")
def tap_confirm_deposit_settings(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_confirm_deposit_settings(), "Confirm deposit settings button is not displayed"

@when("I tap on the specific date deposit settings")
def tap_specific_date_deposit_settings(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_specific_date_deposit_settings(), "Specific date deposit settings is not displayed"

@when("I turn off the specific date deposit switch")
def turn_off_specific_date_deposit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_specific_date_deposit_switch(), "Specific date deposit switch is not displayed"

@when("I turn on the specific date deposit switch")
def turn_on_specific_date_deposit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_specific_date_deposit_switch(), "Specific date deposit switch is not displayed"

@when(parsers.parse('I set the specific date name "{name}" "{start_day}" to "{end_day}"'))
def set_specific_date(driver, name, start_day, end_day):
    name = CommonUseSection.replace_current_datetime(name)
    start_day = CommonUseSection.replace_current_datetime(start_day)
    end_day = CommonUseSection.replace_current_datetime(end_day)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_specific_date(name, start_day, end_day), "Specific date is not displayed"

@when(parsers.parse('I set the default member status to receive deposit and set the receive type "{receive_type}"'))
def set_default_member_status_receive_deposit(driver, receive_type):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_default_member_status_receive_deposit(
        receive_type), "Default member status receive deposit is not displayed"

@when(parsers.parse('I set the payable service item scope to "{service_scope}"'))
def set_payable_service_item_scope(driver, service_scope):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payable_service_item(
        service_scope), "Payable service item scope is not displayed"

@when(parsers.parse('I set the payable service item scope to "{service_scope}" and service item "{category_name}" "{service_item_name}" and clear all'))
def set_payable_service_item_scope(driver, service_scope, category_name, service_item_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payable_service_item(service_scope, category_name, service_item_name, clear_all=True), "Payable service item scope is not displayed"

@when("I go to integration payment method")
def go_to_integration_payment_method(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.go_to_integration_payment_method(), "Integration payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment method to "{payment_method}"'))
def set_payment_method(driver, payment_method):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_method(payment_method), "Payment method is not displayed"

@when(parsers.parse('I set the payment amount pricing method to "{pricing_method}" and amount "{amount}"'))
def set_payment_amount_pricing_method(driver, pricing_method, amount):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_amount_pricing_method(pricing_method, amount), "Payment amount pricing method is not displayed"

@when(parsers.parse(
    'I set the payment amount pricing method to "{pricing_method}" and minimum amount "{amount}" and percentage "{percentage}"'))
def set_payment_amount_pricing_method(driver, pricing_method, amount, percentage):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_amount_pricing_method(pricing_method, amount, percentage), "Payment amount pricing method is not displayed"

@when(parsers.parse('I set the auto cancel if unpaid to "{unpaid_time}"'))
def set_auto_cancel_if_unpaid(driver, unpaid_time):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_auto_cancel_if_unpaid(unpaid_time), "Auto cancel if unpaid is not displayed"

@when(parsers.parse('I set the payment instructions to "{instruction}"'))
def set_payment_instructions(driver, instruction):
    instruction = CommonUseSection.replace_current_datetime(instruction)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_payment_instructions(instruction), "Payment instructions is not displayed"

@when("I tap on the confirm button in the deposit settings page")
def tap_confirm_deposit_settings(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_confirm_deposit_settings(), "Confirm deposit settings button is not displayed"

@when("I tap on the close button in the deposit management page")
def tap_close_deposit_management_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_deposit_management_page(), "Close deposit management page button is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"




# Scenario: Advanced Feature Settings
@when("I tap on the advanced feature settings")
def tap_advanced_feature_settings(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_advanced_feature_settings(), "Advanced feature settings is not displayed"

@when("I tap on the reservation restriction")
def tap_reservation_restriction(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_reservation_restriction(), "Reservation restriction is not displayed"

@when(parsers.parse('I set the cancellation time to "{restriction}"'))
def set_cancellation_time(driver, restriction):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_cancellation_time(restriction), "Cancellation time is not displayed"

@when("I turn off the upcoming reservation switch")
def turn_off_upcoming_reservation_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_upcoming_reservation_switch(), "Upcoming reservation switch is not displayed"

@when("I turn on the upcoming reservation switch")
def turn_on_upcoming_reservation_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_upcoming_reservation_switch(), "Upcoming reservation switch is not displayed"

@when(parsers.parse('I set the upcoming reservation count to "{count}"'))
def set_upcoming_reservation_count(driver, count):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_upcoming_reservation_count(count), "Upcoming reservation count is not displayed"

@when("I turn off the no show switch")
def turn_off_no_show_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_no_show_switch(), "No show switch is not displayed"

@when("I turn on the no show switch")
def turn_on_no_show_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_no_show_switch(), "No show switch is not displayed"

@when(parsers.parse('I set the no show count to "{count}"'))
def set_no_show_count(driver, count):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_no_show_count(count), "No show count is not displayed"

@when("I turn off the monthly reservation cancellation limit switch")
def turn_off_monthly_reservation_cancellation_limit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_monthly_reservation_cancellation_limit_switch(), "Monthly reservation cancellation limit switch is not displayed"

@when("I turn on the monthly reservation cancellation limit switch")
def turn_on_monthly_reservation_cancellation_limit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_monthly_reservation_cancellation_limit_switch(), "Monthly reservation cancellation limit switch is not displayed"

@when(parsers.parse('I set the monthly reservation cancellation limit to "{limit}"'))
def set_monthly_reservation_cancellation_limit(driver, limit):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_monthly_reservation_cancellation_limit(limit), "Monthly reservation cancellation limit is not displayed"

@when("I turn off customer score limit switch")
def turn_off_customer_score_limit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_customer_score_limit_switch(), "Customer score limit switch is not displayed"

@when("I turn on customer score limit switch")
def turn_on_customer_score_limit_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_customer_score_limit_switch(), "Customer score limit switch is not displayed"

@when(parsers.parse('I set the customer score limit to "{limit}"'))
def set_customer_score_limit(driver, limit):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_customer_score_limit(limit), "Customer score limit is not displayed"

@when("I tap on the confirm button in the reservation restriction page")
def tap_confirm_reservation_restriction(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_confirm_reservation_restriction(), "Confirm reservation restriction button is not displayed"

@when("I tap on the post reservation buffer")
def tap_post_reservation_buffer(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_post_reservation_buffer(), "Post reservation buffer is not displayed"

@when("I turn off the post reservation buffer switch")
def turn_off_post_reservation_buffer_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_post_reservation_buffer_switch(), "Post reservation buffer switch is not displayed"

@when("I turn on the post reservation buffer switch")
def turn_on_post_reservation_buffer_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_post_reservation_buffer_switch(), "Post reservation buffer switch is not displayed"

@when(parsers.parse('I set the post reservation buffer time to "{time}" minutes'))
def set_post_reservation_buffer_time(driver, time):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_post_reservation_buffer_time(time), "Post reservation buffer time is not displayed"

@when(parsers.parse('I set the need post reservation buffer service item to "{category_name}" "{service_item_name}"'))
def set_need_post_reservation_buffer_service_item(driver, category_name, service_item_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_need_post_reservation_buffer_service_item(category_name, service_item_name, clear_all=True), "Need post reservation buffer service item is not displayed"

@when("I tap on the confirm button in the post reservation buffer page")
def tap_confirm_post_reservation_buffer(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_confirm_post_reservation_buffer(), "Confirm post reservation buffer button is not displayed"

@when("I tap on the business hours")
def tap_business_hours(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_business_hours(), "Business hours is not displayed"

@when("I turn off the business hours switch")
def turn_off_business_hours_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_off_business_hours_switch(), "Business hours switch is not displayed"

@when("I turn on the business hours switch")
def turn_on_business_hours_switch(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.turn_on_business_hours_switch(), "Business hours switch is not displayed"

@when(parsers.parse('I set the business hours to "{weekdays}" 9:00-21:00'))
def set_business_hours(driver, weekdays):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_business_hours(weekdays), "Business hours is not displayed"

@when("I tap on the close button in the business hours page")
def tap_close_business_hours_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_business_hours_page(), "Close business hours page button is not displayed"

@when("I tap on the equipment management")
def tap_equipment_management(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_equipment_management(), "Equipment management is not displayed"

@when("I Delete the equipment")
def delete_equipment(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_equipment(), "Delete equipment is not displayed"

@when(parsers.parse('I add a new equipment named "{equipment_name}" and set the equipment number to "{equipment_num}" and select the service item "{service_item_category}" "{service_item_name}"'))
def add_equipment(driver, equipment_name, equipment_num, service_item_category, service_item_name):
    equipment_name = CommonUseSection.replace_current_datetime(equipment_name)
    service_item_category = CommonUseSection.replace_current_datetime(service_item_category)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.add_equipment(equipment_name, equipment_num, service_item_category, service_item_name, clear_all=True), "Add equipment is not displayed"

@when(parsers.parse('I edit the equipment "{old_equipment_name}" to "{new_equipment_name}" and set the equipment number to "{equipment_num}" and select the service item "{service_item_category}" "{service_item_name}"'))
def edit_equipment(driver, old_equipment_name, new_equipment_name, equipment_num, service_item_category, service_item_name):
    old_equipment_name = CommonUseSection.replace_current_datetime(old_equipment_name)
    new_equipment_name = CommonUseSection.replace_current_datetime(new_equipment_name)
    service_item_category = CommonUseSection.replace_current_datetime(service_item_category)
    service_item_name = CommonUseSection.replace_current_datetime(service_item_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.edit_equipment(old_equipment_name, new_equipment_name, equipment_num, service_item_category, service_item_name), "Edit equipment is not displayed"

@when("I tap on the close button in the equipment management page")
def tap_close_equipment_management_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_equipment_management_page(), "Close equipment management page button is not displayed"

@when("I tap on the close button in the advanced feature settings page")
def tap_close_advanced_feature_settings_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_advanced_feature_settings_page(), "Close advanced feature settings page button is not displayed"

@when("I tap on the close button in the service appointment page")
def tap_close_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_service_appointment_page(), "Close service appointment page button is not displayed"

@then("I should see the Branch Settings page")
def verify_branch_settings_page_after_close(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_branch_settings_page(), "Branch settings page is not displayed"