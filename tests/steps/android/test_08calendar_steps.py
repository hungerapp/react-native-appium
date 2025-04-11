import allure
import pytest

from pytest_bdd import scenarios, given, when, then


from pages.android.calendar.calendar_page import CalendarPage
from pages.android.create.create_appointment_page import CreateAppointmentPage
from pages.android.create.create_event_page import CreateEventPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../features/calendar.feature')

# Scenario: Open Month Selection
@allure.feature('Calendar for open month selection')
@allure.story('Open Month Selection')
@pytest.mark.run(order=46)
@pytest.mark.calendar
@given('I am on the calendar page')
def on_calendar_page(driver):
    pass

@when('I click on the Date selector')
def click_date_selector(driver):
    """Click on the Date selector"""
    calendar_page = CalendarPage(driver)
    calendar_page.open_month_selection()

@then('a month selection window opens allowing me to switch years or select a month')
def verify_month_selection_window(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.change_month_display_mode()




# Scenario: Change Display Mode
@allure.feature('Calendar for change display mode')
@allure.story('Change Display Mode')
@pytest.mark.run(order=47)
@pytest.mark.calendar
@when('I click the month icon')
def click_month_icon(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.change_calendar_display()

@then('a display mode selection window opens allowing me to choose any of options')
def verify_display_mode_selection(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.select_target_display_mode()

@then('I can click the month icon again to switch back to the previous mode')
def switch_back_to_previous_mode(driver):
    """Switch back to the previous mode"""
    calendar_page = CalendarPage(driver)
    calendar_page.switch_back_to_month_mode()




# Scenario: Filter Personnel
@allure.feature('Calendar for filter personnel')
@allure.story('Filter Personnel')
@pytest.mark.run(order=48)
@pytest.mark.calendar
@when('I click the filter icon')
def click_filter_icon(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.filter_personnel()

@then('a filter window opens allowing me to select personnel')
def select_personnel(driver):
    """Select personnel"""
    calendar_page = CalendarPage(driver)
    calendar_page.select_personnel()

@then('I can edit personnel colors and save the changes')
def edit_personnel_colors(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.edit_personnel_colors()

@then('I change the personnel filter to all personnel')
def change_personnel_filter(driver):
    """Change personnel filter to all personnel"""
    calendar_page = CalendarPage(driver)
    calendar_page.change_personnel_filter()



# Scenario: Navigate to Today
@allure.feature('Calendar for navigate to today')
@allure.story('Navigate to Today')
@pytest.mark.run(order=49)
@pytest.mark.calendar
@when('I swipe to other pages and click the today icon')
def navigate_to_today(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.perform_swipe_left_or_right()

@then('the calendar page jumps to today\'s date')
def verify_navigate_to_today(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.navigate_to_today()




# Scenario: Add Appointment
@allure.feature('Calendar for add appointment')
@allure.story('Add Appointment')
@pytest.mark.run(order=50)
@pytest.mark.calendar
@when('I long-press any date in calendar')
def long_press_any_date(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.long_press_date()

@then('I click on the add appointment option')
def click_add_appointment_option(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.add_appointment()

@then('I create a new appointment in the create appointment page')
def create_appointment(driver):
    """Create an appointment"""
    create_appointment = CreateAppointmentPage(driver)
    common_use = CommonUseSection(driver)
    common_use.select_service_person()
    create_appointment.select_service()


@then('I can successfully create an appointment')
def appointment_created(driver):
    """Verify appointment is created"""
    create_appointment = CreateAppointmentPage(driver)
    create_appointment.click_create_button()





# Scenario: Add Appointment and change the time
@allure.feature('Calendar for add appointment and change the time')
@allure.story('Add Appointment and change the time')
@pytest.mark.run(order=51)
@pytest.mark.calendar
@when('I long-press any date')
def long_press_date(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.long_press_date()

@then('I click on the add appointment option')
def click_add_appointment_option(driver):
    """Click on the add appointment option"""
    calendar_page = CalendarPage(driver)
    calendar_page.add_appointment()

@then('I create an appointment in the create appointment page')
def create_appointment(driver):
    create_appointment = CreateAppointmentPage(driver)
    common_use = CommonUseSection(driver)
    common_use.select_service_person()
    create_appointment.select_service()

@then('I change the time of the appointment')
def change_appointment_time(driver):
    create_appointment = CreateAppointmentPage(driver)
    create_appointment.select_appointment_time()

@then('I can successfully create an appointment')
def verify_appointment_created(driver): 
    create_appointment = CreateAppointmentPage(driver)
    create_appointment.click_create_button()





# Scenario: Add Event
@allure.feature('Calendar for add event')
@allure.story('Add Event')
@pytest.mark.run(order=52)
@pytest.mark.calendar
@when('I long-press any date')
def long_press_date(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.long_press_date()

@then('I click on the add event option')
def click_add_event_option(driver):
    """Click on the add event option"""
    calendar_page = CalendarPage(driver)
    calendar_page.add_event()

@then('I create event and input name in the create event page')
def create_event(driver):
    create_event = CreateEventPage(driver)
    common_use = CommonUseSection(driver)
    common_use.select_service_multiple_personnel(single_choice=True)
    create_event.click_event_section()
    create_event.enter_event_title("Event Testing 事件測試 #@!123")


@then('I can successfully create an event')
def verify_event_created(driver):
    """Verify event is created"""
    create_event = CreateEventPage(driver)
    create_event.new_event_page_save_button()





# Scenario: Add Event and change the time
@allure.feature('Calendar for add event and change the time')
@allure.story('Add Event and change the time')
@pytest.mark.run(order=53)
@pytest.mark.calendar
@when('I long-press any date')
def long_press_date(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.long_press_date()


@then('I click on the add event option')
def click_add_event_option(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.add_event()

@then('I create an event in the create event page')
def create_event(driver):
    create_event = CreateEventPage(driver)
    common_use = CommonUseSection(driver)
    common_use.select_service_multiple_personnel(single_choice=False)
    create_event.click_event_section()
    create_event.quickly_select_event()

@then('I change the time of the event')
def change_event_time(driver):
    create_event = CreateEventPage(driver)
    create_event.change_selected_time()
    create_event.click_repeat_section()

@then('I can successfully create an event')
def verify_event_created(driver):
    # Implement verification logic
    create_event = CreateEventPage(driver)
    create_event.new_event_page_save_button()




# Scenario: Refresh Calendar
@allure.feature('Calendar for refresh calendar')
@allure.story('Refresh Calendar')
@pytest.mark.run(order=54)
@pytest.mark.calendar
@when('I click the refresh button')
def click_refresh_button(driver):
    """Click the refresh button"""
    calendar_page = CalendarPage(driver)
    calendar_page.refresh_calendar()

@then('the calendar page refreshes and shows the correct data')
def verify_calendar_refresh(driver):
    pass
