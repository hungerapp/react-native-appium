from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.service_appointment import ServiceAppointmentPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../../features/navigation/setting/service_appointment.feature')

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

@when(parsers.parse('I delete the service category named "{category_name}"'))
def delete_service_category(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_service_category(category_name), "Delete service category is not displayed"

@when("I tap on the close button on the service item page")
def tap_close_service_item_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_service_item_page(), "Close service item page button is not displayed"

@then("I should see the service appointment page")
def verify_service_appointment_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_service_appointment_page(), "Service appointment page is not displayed"


    
    
    

# TODO: 每一條test都建議標記是跑哪一條scenario的, 每條test之間建議留有空白, 這樣比較好debug
# TODO: 少寫了Given I am on the Service Appointment page 這句
@when('I tap on the online booking')
def tap_online_booking(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_online_booking(), "Online booking is not displayed"

@then('I should see the online booking page')
def verify_online_booking_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_online_booking_page(), "Online booking page is not displayed"
    
    
    


# TODO: 每一條test都建議標記是跑哪一條scenario的, 每條test之間建議留有空白, 這樣比較好debug
# TODO: 少寫了Given I am on the Service Appointment page 這句
@given('I am on the online booking page')
def verify_online_booking_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_online_booking_page(), "Online booking page is not displayed"

@when('I tap on the add unspecified appointment combination')
def tap_add_appointment_combination(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_add_appointment_combination(), "Add appointment combination is not displayed"

@when(parsers.parse('I enter the appointment combination name "{combination_name}"'))
def enter_appointment_combination_name(driver, combination_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_appointment_combination_name(combination_name), "Appointment combination name input is not displayed"

@when(parsers.parse('I enter the appointment combination introduction "{combination_introduction}"'))
def enter_appointment_combination_introduction(driver, combination_introduction):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.enter_appointment_combination_introduction(combination_introduction), "Appointment combination introduction input is not displayed"

@when(parsers.parse('I select the appointment combination service personnel "{service_personnel}"'))    #全部選取
def select_appointment_combination_service_personnel(driver, service_personnel):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_appointment_combination_service_personnel(service_personnel), "Appointment combination service personnel selection is not displayed"

@when('I tap on the confirm button on the add appointment combination')
def tap_confirm_add_appointment_combination(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_confirm_add_appointment_combination(), "Confirm add appointment combination button is not displayed"

@then(parsers.parse('I should see the appointment combination name "{combination_name}" on the online booking page'))
def verify_appointment_combination_name(driver, combination_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_appointment_combination_name(combination_name), "Appointment combination name is not displayed"
    
    
    


# TODO: 每一條test都建議標記是跑哪一條scenario的, 每條test之間建議留有空白, 這樣比較好debug
# TODO: 少寫了Given I am on the Service Appointment page 這句
@when(parsers.parse('I tap on the edit appointment combination named "{combination_name}"'))
def tap_edit_appointment_combination(driver, combination_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_appointment_combination(combination_name), "Edit appointment combination is not displayed"

@when("I tap on the open item tab")
def tap_open_item_tab(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_open_item_tab(), "Open item tab is not displayed"

@when(parsers.parse('I select the main service item and clear all options "{service_item_category}" "{service_item_name}"'))
def select_main_service_item_and_clear_all(driver, service_item_category, service_item_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_main_service_item(service_item_category, service_item_name, clear_all=True), "Main service item selection and clear all options is not displayed"

@when(parsers.parse('I select the main service item "{service_item_category}" "{service_item_name}"'))
def select_main_service_item(driver, service_item_category, service_item_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    #TODO: 這邊要確認前置條件main service都有存在, 不然會fail
    assert service_appointment_page.select_main_service_item(service_item_category, service_item_name), "Main service item selection is not displayed"

@when(parsers.parse('I select the online booking type "{online_booking_type}"'))
def select_online_booking_type(driver, online_booking_type):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_online_booking_type(online_booking_type), "Online booking type selection is not displayed"

@when(parsers.parse('I select the additional service item "{service_item_category}" "{service_item_name}"'))
def select_additional_service_item(driver, service_item_category, service_item_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_additional_service_item(service_item_category, service_item_name), "Additional service item selection is not displayed"

@when(parsers.parse('I select the additional service item and clear all options "{service_item_category}" "{service_item_name}"'))
def select_additional_service_item(driver, service_item_category, service_item_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.select_additional_service_item(service_item_category, service_item_name, clear_all=True), "Additional service item selection is not displayed"

@when("I tap on the close button on the edit appointment combination")
def tap_close_edit_appointment_combination(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_close_edit_appointment_combination(), "Close edit appointment combination button is not displayed"

@when("I delete the appointment combination")
def delete_appointment_combination(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.delete_appointment_combination(), "Delete edit appointment combination button is not displayed"

@then(parsers.parse('I should not see the appointment combination name "{combination_name}" on the online booking page'))
def verify_appointment_combination_name_not_visible(driver, combination_name):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_appointment_combination_name_not_visible(combination_name), "Appointment combination name is still displayed"
    
    
    
    

# TODO: 每一條test都建議標記是跑哪一條scenario的, 每條test之間建議留有空白, 這樣比較好debug
# TODO: 少寫了Given I am on the Service Appointment page 這句
@when(parsers.parse('I tap on the edit service personnel "{service_personnel}"'))
def tap_edit_service_personnel(driver, service_personnel):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_edit_service_personnel(service_personnel), "Edit service personnel is not displayed"

@when(parsers.parse('I set the available date to "{specific_day}" "{open_month}"'))
def set_available_date(driver, specific_day, open_month):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_available_date(specific_day, open_month), "Set available date is not displayed"

@when(parsers.parse('I set the latest booking time to "{latest_booking_time}"'))
def set_latest_booking_time(driver, latest_booking_time):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_latest_booking_time(latest_booking_time), "Set latest booking time is not displayed"

@when(parsers.parse('I set the range of online booking quantity "{min_quantity}" to "{max_quantity}"'))
def set_online_booking_quantity_range(driver, min_quantity, max_quantity):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_online_booking_quantity_range(min_quantity, max_quantity), "Set online booking quantity range is not displayed"

@when(parsers.parse('I set today open time "{times}"'))
def set_open_time(driver, times):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.set_open_time(times), "Set open time is not displayed"
#TODO: 這邊最後結束要返回服務預約頁, 這樣下一條case才是given I am on the Service Appointment page


# TODO: 每一條test都建議標記是跑哪一條scenario的, 每條test之間建議留有空白, 這樣比較好debug
# TODO: 少寫了Given I am on the Service Appointment page 這句
@when("I tap on the booking note")
def tap_booking_note(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_booking_note(), "Booking note is not displayed"

@then("I should see the booking note page")
def verify_booking_note_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_booking_note_page(), "Booking note page is not displayed"

@given("I am on the booking note page")
def verify_booking_note_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_booking_note_page(), "Booking note page is not displayed"

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

@when("I tap on the deposit management")
def tap_deposit_management(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.tap_deposit_management(), "Deposit management is not displayed"

@then("I should see the deposit management page")
def verify_deposit_management_page(driver):
    service_appointment_page = ServiceAppointmentPage(driver)
    assert service_appointment_page.verify_deposit_management_page(), "Deposit management page is not displayed"