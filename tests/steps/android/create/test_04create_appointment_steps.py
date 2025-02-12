import time
import allure
import pytest
from pytest_bdd import scenarios, given, when, then

from pages.android.create.create_appointment_page import CreateAppointmentPage

scenarios('../../../../features/create/create_appointment.feature')

# Test data
TEST_CONTACT_NAME = "測試用戶"
TEST_PARTIAL_NAME = "測試"
TEST_VALID_PHONE = "0912345678"
TEST_INVALID_PHONE = "123"
TEST_PARTIAL_PHONE = "0912"

# Scenario: Successfully create an appointment with anonymous nickname
@allure.feature('Create Appointment for anonymous nickname')
@allure.story('Successfully create an appointment with anonymous nickname')
@pytest.mark.run(order=19)
@given('I click the back button to go to calendar page')
def click_back_to_calendar(driver):
    """Click back to calendar button"""
    create_page = CreateAppointmentPage(driver)
    create_page.personal_page_back_to_calendar()

@when('I click the create appointment option')
def create_appointment_from_calendar(driver):
    """Initial step to create appointment from calendar page"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()
  
@then('I fill in the contact with anonymous nickname')
def fill_anonymous_contact(driver):
    """Fill contact info as anonymous"""
    create_page = CreateAppointmentPage(driver)
    create_page.fill_anonymous_contact()

@then('I select a service person')
def select_service_person(driver):
    """Select service person"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service_person()

@then('I select a service')
def select_service(driver):
    """Select service"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()

@then('I select a valid appointment time')
def select_appointment_time(driver):
    """Select appointment time"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_appointment_time()

@then('I click create appointment and should see the appointment created successfully')
def click_create_button(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_create_button()
    
    
    
    
    
# Scenario: Successfully create an appointment with change time and service person
@allure.feature('Create Appointment with change time and service person')
@allure.story('Successfully create an appointment with change time and service person')
@pytest.mark.run(order=20)1
@given('I click the create appointment option')
def click_create_appointment_for_change_time(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I fill in the contact with anonymous nickname')
def fill_anonymous_contact(driver):
    """Fill contact info as anonymous"""
    create_page = CreateAppointmentPage(driver)
    create_page.fill_anonymous_contact()

@then('I select a service person')
def select_service_person(driver):
    """Select service person"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service_person()

@then('I select a service')
def select_service(driver):
    """Select service"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()
    
@then('I change service time and service person')
def change_service_time_and_service_person(driver):
    """Change service time and service person"""
    create_page = CreateAppointmentPage(driver)
    create_page.change_service_time_and_service_person()

@then('I input the note in the note section')
def input_note(driver):
    """Input note"""
    create_page = CreateAppointmentPage(driver)
    create_page.input_note()

@then('I click create appointment and should see the appointment created successfully')
def click_create_button(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_create_button()
    
    
    
    
    
# Scenario: Successfully create an appointment with one more service
@allure.feature('Create Appointment with one more service')
@allure.story('Successfully create an appointment with one more service')
@pytest.mark.run(order=21)
@given('I click the create appointment option')
def click_create_appointment_for_one_more_service(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I fill in the contact with anonymous nickname')
def fill_anonymous_contact(driver):
    """Fill contact info as anonymous"""
    create_page = CreateAppointmentPage(driver)
    create_page.fill_anonymous_contact()
    
@then('I select a service person')
def select_service_person(driver):
    """Select service person"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service_person()

@then('I select a service')
def select_service(driver):
    """Select service"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()

@then('I add one more service')
def add_one_more_service(driver):
    """Add one more service"""
    create_page = CreateAppointmentPage(driver)
    create_page.add_one_more_service()

@then('I click create appointment and should see the appointment created successfully')
def click_create_button(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_create_button()
    
    
    
    
    
# Scenario: Successfully create an appointment with one more service then delete
@allure.feature('Create Appointment with one more service then delete') 
@allure.story('Successfully create an appointment with one more service then delete')
@pytest.mark.run(order=22)
@given('I click the create appointment option')
def click_create_appointment_for_one_more_service_then_delete(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I fill in the contact with anonymous nickname')
def fill_anonymous_contact(driver):
    """Fill contact info as anonymous"""
    create_page = CreateAppointmentPage(driver)
    create_page.fill_anonymous_contact()
    
@then('I select a service person')
def select_service_person(driver):
    """Select service person"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service_person()

@then('I select a service')
def select_service(driver):
    """Select service"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()
    
@then('I add one more service')
def add_one_more_service(driver):
    """Add one more service"""
    create_page = CreateAppointmentPage(driver)
    create_page.add_one_more_service()

@then('I delete one service')
def delete_one_service(driver):
    """Delete one service"""
    create_page = CreateAppointmentPage(driver)
    create_page.delete_one_service()

@then('I can go back to calendar page after delete')
def go_back_to_calendar(driver):
    """Go back to calendar page after delete"""
    create_page = CreateAppointmentPage(driver)
    create_page.go_back_to_calendar()
    
    
    

# Scenario: Successfully create an appointment with existing nickname
@allure.feature('Create Appointment for existing nickname')
@allure.story('Successfully create an appointment with existing nickname')
@pytest.mark.run(order=23)
@given('I click the create appointment option')
def click_create_appointment_option(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I fill in the contact with existing nickname')
def fill_existing_contact(driver):
    """Fill contact info with existing contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.fill_existing_contact(TEST_CONTACT_NAME)

@then('I select a service person')
def select_service_person_existing(driver):
    """Select service person for existing contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service_person()

@then('I select a service')
def select_service_existing(driver):
    """Select service for existing contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()

@then('I select a valid appointment time')
def select_appointment_time_existing(driver):
    """Select appointment time for existing contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_appointment_time()

@then('I click create appointment button')
def click_create_button_existing(driver):
    """Click create appointment button for existing contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_create_button()

@then('I should see the appointment created successfully')
def verify_success_existing(driver):
    """Verify appointment creation success for existing contact"""
    create_page = CreateAppointmentPage(driver)
    assert create_page.verify_success_message()
    
    
    
    

# Scenario: Add a new contact with valid phone number
@allure.feature('Create Appointment for valid phone number')
@allure.story('Add a new contact with valid phone number')
@pytest.mark.run(order=24)
@given('I click the create appointment option')
def click_create_appointment_for_contact(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info(driver):
    """Click contact info section"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info()

@then('I enter a valid phone number')
def enter_valid_phone(driver):
    """Enter valid phone number"""
    create_page = CreateAppointmentPage(driver)
    create_page.enter_phone_number(TEST_VALID_PHONE)

@then('I click the save button')
def click_save_button(driver):
    """Click save button"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_save_button()

@then('the contact should be saved successfully')
def verify_contact_saved(driver):
    """Verify contact saved successfully"""
    create_page = CreateAppointmentPage(driver)
    assert create_page.verify_contact_saved()
    
    
    
    

# Scenario: Show error for invalid phone number format
@allure.feature('Create Appointment for invalid phone number')
@allure.story('Show error for invalid phone number format')
@pytest.mark.run(order=25)
@given('I click the create appointment option')
def click_create_appointment_for_invalid(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_invalid(driver):
    """Click contact info section for invalid phone"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info()

@then('I enter an invalid phone number')
def enter_invalid_phone(driver):
    """Enter invalid phone number"""
    create_page = CreateAppointmentPage(driver)
    create_page.enter_phone_number(TEST_INVALID_PHONE)

@then('I should see an error message for invalid phone number')
def verify_phone_error(driver):
    """Verify invalid phone error message"""
    create_page = CreateAppointmentPage(driver)
    assert create_page.verify_invalid_phone_error()
    
    
    
    

# Scenario: Save contact as anonymous when no information is entered
@allure.feature('Create Appointment for no information')
@allure.story('Save contact as anonymous when no information is entered')
@pytest.mark.run(order=26)
@given('I click the create appointment option')
def click_create_appointment_for_anonymous(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_anonymous(driver):
    """Click contact info section for anonymous save"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info()

@then('I click the save button without entering any information')
def click_save_empty(driver):
    """Click save button without entering information"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_save_button()

@then('the contact should be saved as anonymous')
def verify_anonymous_contact(driver):
    """Verify contact saved as anonymous"""
    create_page = CreateAppointmentPage(driver)
    assert create_page.verify_anonymous_contact()




# Scenario: Search contact by partial phone number
@allure.feature('Create Appointment for partial phone number')
@allure.story('Search contact by partial phone number')
@pytest.mark.run(order=27)
@given('I click the create appointment option')
def click_create_appointment_for_partial_phone(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_partial_phone(driver):
    """Click contact info section for partial phone search"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info()

@then('I enter a partial phone number')
def enter_partial_phone(driver):
    """Enter partial phone number"""
    create_page = CreateAppointmentPage(driver)
    create_page.enter_phone_number(TEST_PARTIAL_PHONE)

@then('I click the phone search button')
def click_phone_search(driver):
    """Click phone search button"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_phone_search()

@then('I should see search results and select the contact then save')
def select_and_save_contact_partial_phone(driver):
    """Select search result and save contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()
    
    
    
    

# Scenario: Search contact by full phone number
@allure.feature('Create Appointment for full phone number')
@allure.story('Search contact by full phone number')
@pytest.mark.run(order=28)
@given('I click the create appointment option')
def click_create_appointment_for_full_phone(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_full_phone(driver):
    """Click contact info section for full phone search"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info()

@then('I enter a full phone number')
def enter_full_phone(driver):
    """Enter full phone number"""
    create_page = CreateAppointmentPage(driver)
    create_page.enter_phone_number(TEST_VALID_PHONE)

@then('I click the phone search button')
def click_phone_search_full(driver):
    """Click phone search button for full number"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_phone_search()

@then('I should see search results and select the contact then save')
def select_and_save_contact_full_phone(driver):
    """Select search result and save contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()
    
    
    
    
    

# Scenario: Search contact by partial name
@allure.feature('Create Appointment for partial name')
@allure.story('Search contact by partial name')
@pytest.mark.run(order=29)
@given('I click the create appointment option')
def click_create_appointment_for_partial_name(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_partial_name(driver):
    """Click contact info section for partial name search"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info()

@then('I enter a partial name')
def enter_partial_name(driver):
    """Enter partial name"""
    create_page = CreateAppointmentPage(driver)
    create_page.search_by_name(TEST_PARTIAL_NAME)

@then('I click the name search button')
def click_name_search(driver):
    """Click name search button"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_name_search()

@then('I should see search results and select the contact then save')
def select_and_save_contact_partial_name(driver):
    """Select search result and save contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()
    
    
    
    

# Scenario: Search contact by full name
@allure.feature('Create Appointment for full name')
@allure.story('Search contact by full name')
@pytest.mark.run(order=30)
@given('I click the create appointment option')
def click_create_appointment_for_full_name(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I click contact info section')
def click_contact_info_full_name(driver):
    """Click contact info section for full name search"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_contact_info()

@when('I enter a full name')
def enter_full_name(driver):
    """Enter full name"""
    create_page = CreateAppointmentPage(driver)
    create_page.search_by_name(TEST_CONTACT_NAME)

@then('I click the name search button')
def click_name_search_full(driver):
    """Click name search button for full name"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_name_search()

@then('I should see search results and select the contact then save')
def select_and_save_contact_full_name(driver):
    """Select search result and save contact"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_search_result_and_save()


@allure.feature('Create Appointment with partial information then cancel')
@allure.story('Create Appointment with partial information then cancel')
@pytest.mark.run(order=31)
@given('I click the create appointment option')
def click_create_appointment_for_partial_cancel(driver):
    """Click create appointment button"""
    create_page = CreateAppointmentPage(driver)
    create_page.create_appointment()

@when('I fill in the contact with anonymous nickname')
def fill_anonymous_contact(driver):
    """Fill contact info as anonymous"""
    create_page = CreateAppointmentPage(driver)
    create_page.fill_anonymous_contact()

@then('I select a service person')
def select_service_person(driver):
    """Select service person"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service_person()

@then('I select a service')
def select_service(driver):
    """Select service"""
    create_page = CreateAppointmentPage(driver)
    create_page.select_service()

@then('I click back button should see the unfinished window')
def click_back_button(driver):
    """Click back button and see unfinished window"""
    create_page = CreateAppointmentPage(driver)
    create_page.click_back_button()
