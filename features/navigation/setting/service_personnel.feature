Feature: Service Personnel Management

  @regression @service_personnel_in_branch_settings_page @service_personnel_page
  Scenario: Verify Service Personnel Management Flow
    Given I am on the Branch Settings page
    When I tap on Service Personnel in the Branch Settings page
    Then I should be navigated to the Service Personnel page
    When I tap on Add Service Personnel in the Service Personnel page
    Then the Add Service Personnel Alert Dialog is displayed
    When I tap on the Cancel button in the Add Service Personnel Alert Dialog
    Then the Add Service Personnel Alert Dialog is dismissed
    When I tap on Add Service Personnel in the Service Personnel page
    Then the Add Service Personnel Alert Dialog is displayed
    When I tap on the Add button in the Add Service Personnel Alert Dialog
    Then I should be navigated to the Add Service Personnel Page
    When I add a new service personnel
    Then a new service personnel should be successfully added on the Service Personnel page
    When I edit service personnel
    Then the service personnel details should be updated successfully
    When I delete service personnel
    Then the service personnel should not be present in the service personnel list



