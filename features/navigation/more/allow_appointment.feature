Feature: Allow Appointment

  # [ALLOW APPOINTMENT SETTINGS] ACCESS_RESERVATION_SETTINGS
  @regression @access_reservation_settings @navigate_more @navigate @navigate_more_allow_appointment
  Scenario: Accessing Reservation Settings
    Given I click on the allow appointment settings
    Then I can click the toggle and select open times
    Then I can select the latest reservation time
    When I click on the expand advanced settings
    Then I can enter the quantity selection


  # [ALLOW APPOINTMENT SETTINGS] OPEN_TIME_MANAGEMENT
  @regression @open_time_management_in_more @navigate_more @navigate @navigate_more_allow_appointment
  Scenario: Managing Open Time
    When I click on the open time tab
    Then I can select the display date
    Then I can add a new open time
    When I click on edit then copy today
    Then I can edit the open time and quick close


  # [ALLOW APPOINTMENT SETTINGS] OPEN_ITEMS_MANAGEMENT
  @regression @open_items_management_in_more @navigate_more @navigate @navigate_more_allow_appointment
  Scenario: Managing Open Items
    When I click on the open items tab
    Then I can select the main item
    Then I can select the online reservation type
    Then I can select the add-on service items
    Then I can return to the calendar page
