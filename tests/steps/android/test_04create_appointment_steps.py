import allure
import pytest
from pytest_bdd import scenarios, given, when, then

from pages.android.create.create_appointment_page import CreateAppointmentPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../features/create/create_appointment.feature')

# Test data
TEST_CONTACT_NAME = "王貝克"
TEST_PARTIAL_NAME = "B"
TEST_VALID_PHONE = "0972205690"
TEST_INVALID_PHONE = "#90"
TEST_PARTIAL_PHONE = "09722"

# Scenario: Successfully create an appointment with anonymous nickname
@allure.feature('Create Appointment for anonymous nickname')
@allure.story('Successfully create an appointment with anonymous nickname')
@pytest.mark.run(order=20)
@pytest.mark.create_appointment
@given('I click the back button to go to calendar page')
def click_back_to_calendar(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.personal_page_back_to_calendar()

@when('I click the create appointment option')
def create_appointment_from_calendar(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()
  
@then('I fill in the contact with anonymous nickname')
def fill_anonymous_contact(driver):
    """Fill contact info as anonymous"""
    create_page = CreateAppointmentPage(driver)
    create_page.fill_anonymous_contact()

@then('I select a service person')
def select_service_person(driver):
    common_use = CommonUseSection(driver)
    common_use.select_service_person()

@then('I select a service')
def select_service(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()
    create_page.save_service1_button()
    
@then('I change service time and service person')
def change_service_time_and_service_person(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.change_service_time_and_service_person()
    

@then('I select a valid appointment time')
def select_appointment_time(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_appointment_time()
    
@then('I input the note in the note section')
def input_note(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.note_input()

@then('I click create appointment and should see the appointment created successfully')
def click_create_button(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_create_button()
    
    
  
    
    
# Scenario: Successfully create an appointment with one more service
@allure.feature('Create Appointment with one more service')
@allure.story('Successfully create an appointment with one more service')
@pytest.mark.run(order=21)
@pytest.mark.create_appointment
@given('I click the create appointment option')
def click_create_appointment_for_one_more_service(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()
  
@when('I select a service person')
def select_service_person(driver):
    common_use = CommonUseSection(driver)
    common_use.select_service_person()

@then('I select a service')
def select_service(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()
    create_page.save_service1_button()

@then('I select a valid appointment time')
def select_appointment_time(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_appointment_time()


@then('I click one more service button')
def click_one_more_service(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_one_more_service()

@then('I change the reservation time and add one more service')
def change_reservation_time(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_appointment_time()
    create_page.one_more_service()
 
@then('I choose which deposit should be selected')    
def choose_deposit(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_deposit_options()


@then('I can successfully create an appointment with one more service')
def verify_success(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_create_button()
    
    
 
 
 
    
# Scenario: Successfully create an appointment with one more service then delete
@allure.feature('Create Appointment with one more service then delete') 
@allure.story('Successfully create an appointment with one more service then delete')
@pytest.mark.run(order=22)
@pytest.mark.create_appointment
@given('I click the create appointment option')
def click_create_appointment_for_one_more_service_then_delete(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I select a service person')
def select_service_person(driver):
    common_use = CommonUseSection(driver)
    common_use.select_service_person()

@then('I select a service')
def select_service(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()
    create_page.save_service1_button()
    
    
@then('I select a valid appointment time')
def select_appointment_time(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_appointment_time()

@then('I add one more service')
def add_one_more_service(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_one_more_service()
    
@then('I delete one service')
def delete_one_service(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.delete_service()

@then('I can go back to calendar page after delete')
def go_back_to_calendar(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.work_as_expected_then_back_to_calendar()
    
    


  

# Scenario: Successfully create an appointment with existing name and phone number
@allure.feature('Create Appointment for existing name and phone number')
@allure.story('Successfully create an appointment with existing name and phone number')
@pytest.mark.run(order=23)
@pytest.mark.create_appointment
@given('I click the create appointment option')
def click_create_appointment_option(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I fill in the contact with existing name and phone number')
def fill_existing_contact(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.fill_existing_contact(TEST_CONTACT_NAME, TEST_VALID_PHONE)
    
@then('I check the member passport and back')
def check_member_passport(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.check_member_passport()

@then('I select a service person')
def select_service_person_existing(driver):
    common_use = CommonUseSection(driver)
    common_use.select_service_person()

@then('I select a service')
def select_service_existing(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()
    create_page.save_service1_button()
    
@then('I select a valid appointment time')
def select_appointment_time_existing(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_appointment_time()

@then('I click create appointment and should see the appointment created successfully')
def click_create_button_existing(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_create_button()

 
    

# Scenario: Show error for invalid phone number format
@allure.feature('Create Appointment for invalid phone number')
@allure.story('Show error for invalid phone number format')
@pytest.mark.run(order=24)
@pytest.mark.create_appointment
@given('I click the create appointment option')
def click_create_appointment_for_invalid(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_invalid(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info_section()

@then('I enter an invalid phone number')
def enter_invalid_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.enter_phone_number(TEST_INVALID_PHONE)

@then('I should see an error message for invalid phone number')
def verify_phone_error(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.verify_invalid_phone_error_message()
    
 
 
# Scenario: Create Appointment for selecting and searching country code
@allure.feature('Create Appointment for selecting and searching country code')
@pytest.mark.run(order=25)
@pytest.mark.create_appointment
@given('I am on the contact page')
def contact_page(driver):
    pass

@when('I select random country code')
def select_country_code(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_random_country_code()

@then('I should see different country code in the phone number input field')
def verify_country_code_changed(driver):
    common_use = CommonUseSection(driver)
    common_use.is_country_code_changed()
    
@when('I search different country code')
def search_different_country_code(driver):
    common_use = CommonUseSection(driver)
    common_use.search_country_code()

@then('I should see different country code in the phone number input field')
def verify_country_code_changed(driver):
    common_use = CommonUseSection(driver)
    common_use.is_country_code_changed()
    
    


# Scenario: Search contact by partial phone number
@allure.feature('Create Appointment for partial phone number')
@allure.story('Search contact by partial phone number')
@pytest.mark.run(order=26)
@pytest.mark.create_appointment
@given('I click contact back button to appointment page')
def click_contact_back_btn_to_appointment(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_back_btn_to_appointment()

@when('I click contact info section')
def click_contact_info_partial_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info_section()

@then('I enter a partial phone number')
def enter_partial_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.enter_phone_number(TEST_PARTIAL_PHONE)

@then('I click the phone search button for partial phone number')
def click_phone_search(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.search_by_phone()

@then('I should see search results and select the contact then save')
def select_and_save_contact_partial_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()
    


    
# Scenario: Create Appointment for modify contact
@allure.feature('Create Appointment for modifying contact')
@allure.story('Create Appointment for modifying contact')
@pytest.mark.run(order=27)
@pytest.mark.create_appointment
@given('I have chosen a contact')
def create_appointment_page(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.contact_has_chosen()
    

@when('I change the contact info section')
def change_contact_info(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.change_contact_info()

@then('I should save then back to calendar')
def select_and_save_contact_full_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.work_as_expected_then_back_to_calendar()
  




# Scenario: Search contact by full phone number
@allure.feature('Create Appointment for full phone number')
@allure.story('Search contact by full phone number')
@pytest.mark.run(order=28)
@pytest.mark.create_appointment
@given('I click the create appointment option')
def click_create_appointment_for_full_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_full_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info_section()

@then('I enter a full phone number')
def enter_full_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.enter_phone_number(TEST_VALID_PHONE)

@then('I click the phone search button for full phone number')
def click_phone_search_full(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.search_by_phone()

@then('I should see search results and save then back to calendar')
def select_and_save_contact_full_phone(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()
    create_page.work_as_expected_then_back_to_calendar()
    
    
    
    

# Scenario: Search contact by partial name
@allure.feature('Create Appointment for partial name')
@allure.story('Search contact by partial name')
@pytest.mark.run(order=29)
@pytest.mark.create_appointment
@given('I click the create appointment option')
def click_create_appointment_for_partial_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_partial_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info_section()

@then('I enter a partial name')
def enter_partial_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.enter_name(TEST_PARTIAL_NAME)

@then('I click the name search button for partial name')
def click_name_search(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.search_by_name()

@then('I should see search results and save then back to calendar')
def select_and_save_contact_partial_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()
    create_page.work_as_expected_then_back_to_calendar()
    

    

# Scenario: Search contact by full name
@allure.feature('Create Appointment for full name')
@allure.story('Search contact by full name')
@pytest.mark.run(order=30)
@pytest.mark.create_appointment
@given('I click the create appointment option')
def click_create_appointment_for_full_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_full_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info_section()

@when('I enter a full name')
def enter_full_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.enter_name(TEST_CONTACT_NAME)

@then('I click the name search button for full name')
def click_name_search_full(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.search_by_name()

@then('I should see search results and save then back to calendar')
def select_and_save_contact_full_name(driver):
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()
    create_page.work_as_expected_then_back_to_calendar()


