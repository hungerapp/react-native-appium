Feature: Calendar Page Interactions
  As a user
  I want to manage my calendar
  So that I can see my schedule and events
  
  @regression @open_month_selection
  Scenario: Open Month Selection
    Given I am on the calendar page
    When I click on the Date selector
    Then a month selection window opens allowing me to switch years or select a month

  @regression @change_display_mode
  Scenario: Change Display Mode
    When I click the month icon
    Then a display mode selection window opens allowing me to choose any of options
    Then I can click the month icon again to switch back to the previous mode

  @regression @filter_personnel
  Scenario: Filter Personnel
    When I click the filter icon
    Then a filter window opens allowing me to select personnel
    Then I can edit personnel colors and save the changes
    Then I change the personnel filter to all personnel


  @regression @navigate_to_today
  Scenario: Navigate to Today
    When I swipe to other pages and click the today icon
    Then the calendar page jumps to today's date


  @regression @add_appointment_in_calendar @calendar
  Scenario: Add Appointment
    When I long-press any date in calendar
    Then I click on the add appointment option
    Then I create a new appointment in the create appointment page
    Then I can successfully create an appointment


  @regression @add_and_change_appointment_time @calendar
  Scenario: Add and change the appointment time
    When I long-press any date 
    Then I click on the add appointment option
    Then I create an appointment in the create appointment page
    Then I change the time of the appointment
    Then I can successfully create an appointment

  @regression @long_press_and_add_event @calendar
  Scenario: Add Event
    When I long-press any date
    Then I click on the add event option
    Then I create event and input name in the create event page
    Then I can successfully create an event

  @regression @add_and_change_event_time @calendar
  Scenario: Add and change the event time
    When I long-press any date
    Then I click on the add event option
    Then I create an event in the create event page
    Then I change the time of the event
    Then I can successfully create an event
  
  @regression @refresh_calendar @calendar
  Scenario: Refresh Calendar
    When I click the refresh button
    Then the calendar page refreshes and shows the correct data
  