Feature: Create Event
  As a user
  I want to create an event
  So that I can manage my schedule

  @regression @add_event_flow
  Scenario: Add event flow
  Given I click the create event option
  When I select Add Service Personnel for single choice
  Then I enter the event title
  Then I select the event time and choose All Day
  Then I disable the Repeat option
  Then I click the Save button and back to the calendar page

  @regression @service_personnel_selection_and_time_setting
  Scenario: Service Personnel Selection and Time Setting
  Given I click the create event option
  When I select Service Personnel for multi-select or select all
  Then I quickly select the event
  Then I select the event time and choose a period
  Then I enable the Repeat option
  Then I click the Save button and back to the calendar page

  @regression @error_handling_for_missing_time
  Scenario: Error Handling for Missing Time
  Given I click the create event option
  When I select Add Service Personnel for single choice
  Then I click the time section and do not enter an event time
  Then I click the Save button and verify the error message
  Then I revise the selected time and return to the Create Event page


  @regression @repeat_enabled_but_save_error
  Scenario: Repeat Enabled but Save Error
  Given I am on the Create Event page
  When I enable the Repeat option and save
  Then I verify the error message
  Then I return to Create Event page


