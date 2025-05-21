import allure
import pytest
from pytest_bdd import scenarios, given, when, then

from pages.android.create.create_event_page import CreateEventPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../features/create/create_event.feature')



# Scenario: Add event flow
@allure.feature('Create Event')
@allure.story('Add event flow')
@pytest.mark.run(order=31)
@pytest.mark.create_event
@given('I click the create event option')
def click_create_event_option(driver):
    create_page = CreateEventPage(driver)
    create_page.create_event_option()

@when('I select Add Service Personnel for single choice')
def select_service_personnel_single(driver):
    common_use = CommonUseSection(driver)
    common_use.select_service_multiple_personnel(single_choice=True)

@when('I enter the event title')
def enter_event_title(driver):
    create_page = CreateEventPage(driver)
    create_page.click_event_section()
    create_page.enter_event_title("Meeting")

@when('I select the event time and choose All Day')
def select_event_time_all_day(driver):
    create_page = CreateEventPage(driver)
    create_page.click_time_section()
    create_page.select_event_time(all_day=True)

@when('I disable the Repeat option')
def disable_repeat_option(driver):
    create_page = CreateEventPage(driver)
    create_page.click_repeat_section()

@then('I click the Save button and back to the calendar page')
def click_save_button(driver):
    create_page = CreateEventPage(driver)
    create_page.click_save_button()





# Scenario: Service Personnel Selection and Time Setting
@allure.feature('Create Event')
@allure.story('Service Personnel Selection and Time Setting')
@pytest.mark.run(order=32)
@pytest.mark.create_event
@given('I click the create event option')
def click_create_event_option(driver):
    create_page = CreateEventPage(driver)
    create_page.create_event_option()

@when('I select Service Personnel for multi-select or select all')
def select_service_personnel_multi(driver):
    common_use = CommonUseSection(driver)
    common_use.select_service_multiple_personnel(single_choice=False)
 
@when('I quickly select the event')
def quick_select_event(driver):
    create_page = CreateEventPage(driver)
    create_page.click_event_section()
    create_page.quickly_select_event()

@when('I select the event time and choose a period')
def select_event_time_period(driver):
    create_page = CreateEventPage(driver)
    create_page.click_time_section()
    create_page.select_event_time(all_day=False)

@when('I enable the Repeat option')
def enable_repeat_option(driver):
    create_page = CreateEventPage(driver)
    create_page.toggle_repeat_option(enable=True, multi_select=True)

@then('I click the Save button and back to the calendar page')
def click_save_button(driver):
    create_page = CreateEventPage(driver)
    create_page.click_save_button()






# Scenario: Error Handling for Missing Time
@allure.feature('Create Event')
@allure.story('Error Handling for Missing Time')
@pytest.mark.run(order=33)
@pytest.mark.create_event
@given('I click the create event option')
def click_create_event_option(driver):
    create_page = CreateEventPage(driver)
    create_page.create_event_option()
    
@when('I select Add Service Personnel for single choice')
def select_service_personnel_single(driver):
    common_use = CommonUseSection(driver)
    common_use.select_service_multiple_personnel(single_choice=True)

@when('I click the time section and do not enter an event time')
def click_time_section_no_time(driver):
    create_page = CreateEventPage(driver)
    create_page.click_time_section()


@when('I click the Save button and verify the error message')
def verify_error_message(driver):
    create_page = CreateEventPage(driver)
    create_page.verify_time_error_display()

@then('I revise the selected time and return to the Create Event page')
def return_to_create_event_page(driver):
    create_page = CreateEventPage(driver)
    create_page.select_event_time(all_day=True)






# Scenario: Repeat Enabled but Save Error
@allure.feature('Create Event')
@allure.story('Repeat Enabled but Save Error')
@pytest.mark.run(order=34)
@pytest.mark.create_event
@given('I am on the Create Event page')
def on_create_event_page(driver):
    pass


@when('I enable the Repeat option and save')
def enable_repeat_option(driver):
    create_page = CreateEventPage(driver)
    create_page.click_repeat_toggle()


@when('I verify the error message')
def verify_error_message(driver):
    create_page = CreateEventPage(driver)
    create_page.verify_error_message()

@then('I return to Create Event page')
def return_to_create_event_page(driver):
    create_page = CreateEventPage(driver)
    create_page.click_repeat_back_button()








