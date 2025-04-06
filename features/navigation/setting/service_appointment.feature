Feature: Service Appointment Management

  @regression @branch_settings_management_navigation_to_service_appointment @branch_settings_page @service_appointment_page
  Scenario: Navigate to Service Appointment Management
      Given I am on the Branch Settings page
      When I tap on Service Appointment in the Branch Settings page
      Then I should be navigated to the Service Appointment page

  @regression @member_exclusive_booking_link @service_appointment_page
  Scenario: Verify Member Exclusive Booking Link
    Given I am on the Service Appointment page
    When I tap the member exclusive booking link copy button
    Then A copy link dialog should be displayed
    When I tap copy link in the copy link dialog
    Then A copy link dialog should be dismissed

  @regression @service_item_management @service_appointment_page
  Scenario: Verify Service Item Management
    Given I am on the Service Appointment page
    When I tap the service item in the Service Appointment page
    Then I should be navigated to the Service item page
    When I tap the category edit button in the Service item page
    Then I should be navigated to the Category page
    When I tap the add category in the Category page
    Then I should be navigated to the Add Category page
    When I add a new category in the Add Category page
    Then I should be navigated to the Category page
    Then the category is added successfully
    When I tap the close button in the Category page
    Then I should be navigated to the Service item page
    Then the category is displayed in the Service item page
    When I tap the add service item button in the Service item page
    Then I fill in the service item details
    Then I should be navigated to the Service item page
    Then the service item is added successfully
    When I edit the service item in the Service item page
    Then I should be navigated to the Service item page
    Then the service item is edited successfully
    When I delete the service item in service item page
    Then the service item is deleted successfully
    When I add a new service item
    Then I should be navigated to the Service item page
    Then the service item is added successfully
    When I copy the service item in service item page
    Then the service item is copied successfully
    When I tap delete service item in service item page
    Then the service item is deleted successfully
    When I Delete the service category in the Service item page
    Then the service category is deleted successfully
    When I tap the close button in the Service item page
    Then I should be navigated to the Service Appointment page

  @regression @online_booking_management @service_appointment_page
  Scenario: Verify Online Booking Management
    Given I am on the Branch Settings page
    Then I have added a new service personnel
    Then I have added a new service item
    When I tap the online booking management button in the Service Appointment page
    Then I should be navigated to the Online Booking Management page
    When I tap the personal online booking management in the Online Booking Management page
    Then I should be navigated to the Personal Online Booking page
    Then I configure open days in the Open Setting tab in the Personal Online Booking page
    Then I configure latest appointment time in the Personal Online Booking page
    Then I configure advance setting in the Personal Online Booking page
    Then I configure open time in the Personal Online Booking page
    When I tap the close button in the Personal Online Booking page
    Then I should be navigated to the Online Booking Management page
    When I close the Personal Online Booking
    Then the service personnel should be displayed in the closed online booking section in the Online Booking Management page
    When I add service unspecified appointment combination
    Then the service unspecified appointment combination should be added successfully
    Then I edit service unspecified appointment combination
    When I Delete service unspecified appointment combination
    Then the service unspecified appointment combination should be deleted successfully
    When I tap the close button in the Online Booking Management page
    Then I should be navigated to the Service Appointment page
    Then I Delete the service item
    Then I Delete the service personnel

  @regression @booking_issue_and_note @service_appointment_page
  Scenario: Verify Booking Issue and Note
      Given I am on the Branch Settings page
      When I tap on Service Appointment in the Branch Settings page
      Then I should be navigated to the Service Appointment page











