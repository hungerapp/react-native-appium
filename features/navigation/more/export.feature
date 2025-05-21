Feature: Export

  # [EXPORT] AVAILABLE_TIME_SLOTS_AS_CALENDAR_IMAGE
  @regression @available_time_slots_export_as_calendar_image @navigate_more @navigate @navigate_more_export
  Scenario: Exporting Available Time Slots as a Calendar Image
    Given I click on export available time slots
    When I select a staff member
    Then I select a service item
    Then I select a month
    Then I should be able to export the calendar
    Then I should be able to save the image
    Then I should be able to return to the calendar page


  # [EXPORT] AVAILABLE_TIME_SLOTS_AS_TEXT
  @regression @time_slots_export_as_text @navigate_more @navigate @navigate_more_export
  Scenario: Exporting Available Time Slots as Text
    Given I click on export available time slots
    When I click on the text tab
    Then I select a staff member
    Then I select a service item
    Then I select a date range
    Then I should be able to export the text
    Then I should be able to copy the text
    Then I should be able to return to the calendar page