import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.allow_appointment import AllowAppointmentPage

scenarios('../../../features/navigation/more/allow_appointment.feature')

# TEST DATA



# [ALLOW APPOINTMENT SETTINGS] ACCESS_RESERVATION_SETTINGS
@allure.feature('Allow Appointment')
@allure.story('Allow Appointment - Access Reservation Settings')
@pytest.mark.navigation_more_allow_appointment
@pytest.mark.run(order=89)
@given('I click on the more option in the bottom navigation bar')
def click_more_option(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.click_more_option()
    
@when('I click on the allow appointment settings')
def click_allow_appointment_settings(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.click_allow_appointment_settings()
    
@then('I can click the toggle and select open times')
def click_toggle_and_select_open_times(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.click_toggle_and_select_open_times()
    
@then('I can select the latest reservation time')
def select_latest_reservation_time(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.select_latest_reservation_time()
    
@when('I click on the expand advanced settings')
def click_expand_advanced_settings(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.click_expand_advanced_settings()
    
@then('I can enter the quantity selection')
def enter_quantity_selection(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.enter_quantity_selection()
    
    
    
    
# [ALLOW APPOINTMENT SETTINGS] OPEN_TIME_MANAGEMENT
@allure.feature('Allow Appointment')
@allure.story('Allow Appointment - Open Time Management')
@pytest.mark.navigation_more_allow_appointment
@pytest.mark.run(order=90)
@when('I click on the open time tab')
def click_open_time_tab(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.click_open_time_tab()
    
@then('I can select the display date')
def select_display_date(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.select_display_date()
    
@then('I can add a new open time')
def add_new_open_time(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.add_new_open_time()
    
@when('I click on edit then copy today')
def click_edit_then_copy_today(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.click_edit_then_copy_today()
    
@then('I can edit the open time and quick close')
def edit_open_time_and_quick_close(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.quick_close()
    
    

# [ALLOW APPOINTMENT SETTINGS] OPEN_ITEMS_MANAGEMENT
@allure.feature('Allow Appointment')
@allure.story('Allow Appointment - Open Items Management')
@pytest.mark.navigation_more_allow_appointment
@pytest.mark.run(order=91)
@when('I click on the open items tab')
def click_open_items_tab(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.click_open_items_tab()
    
@then('I can select the main item')
def select_main_item(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.select_main_item()
    
@then('I can select the online reservation type')
def select_online_reservation_type(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.select_online_reservation_type()
    
@then('I can select the add-on service items')
def select_add_on_service_items(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.select_add_on_service_items()
    
@then('I can return to the calendar page')
def return_to_calendar_page(driver):
    allow_appointment_page = AllowAppointmentPage(driver)
    allow_appointment_page.return_to_calendar_page()
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    