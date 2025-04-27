Feature: Service Appointment Settings
  As a merchant user
  I want to manage service appointment settings
  So that I can provide better booking experience for customers

  Scenario: Share Appointment Link
    Given I am on the service appointment page
    When I share the appointment link
    Then I should see the service appointment page

  Scenario: Navigate to Service Items Page
    Given I am on the service appointment page
    When I tap on the service items
    Then I should see the service items page

  Scenario: Add Service Category
    Given I am on the service items page
    When I Add a new service category named "New Category"
    Then I should see the service category named "New Category"

  Scenario: Edit Service Category
    Given I am on the service items page
    When I edit the service category named "New Category" to "Updated Category"
    Then I should see the service category named "Updated Category"

  Scenario: Delete Service Category
    Given I am on the service items page
    When I delete the service category named "Updated Category"
    Then I should not see the service category named "Updated Category"

  Scenario: Add Service Item
    Given I am on the service items page
    When I select a service category named "推薦項目"
    And I click the add service item button
    And I enter the service item name "Service Name"
    And I enter the service code name "SC"
    And I enter the service introduction "Service Introduction"
    And I select the service category "推薦項目" in the add service item
    And I enter the service duration "60" minutes
    And I enter the service price "100"
    And I select the service display type fixed price
    And I select the service display type starting price
    And I select the sub service type single choice
    And I select the sub service type multiple choice
    And I add sub service items name "Sub Service 1" and duration "30" minutes and price "50"
    And I click the save add service item button
    Then I should see the service item name "Service Name"

  @haha
  Scenario: Navigate to Online Booking Page
    Given I am on the service appointment page
    When I tap on the online booking
    Then I should see the online booking page