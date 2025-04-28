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
    When I select a service category named "New Category"
    And I click the add service item button
    And I enter the service item name "Service Name"
    And I enter the service code name "SC"
    And I enter the service introduction "Service Introduction"
    And I select the service category "New Category" in the add service item
    And I enter the service duration "60" minutes
    And I enter the service price "100"
    And I select the service display type "固定價"
    And I select the service display type "起標價"
    And I select the sub service type "單選"
    And I select the sub service type "複選"
    And I add sub service items name "Sub Service 1" and duration "30" minutes and price "50"
    And I click the save add service item button
    Then I should see the service item name "Service Name"

  Scenario: Navigate to Online Booking Page
    Given I am on the service appointment page
    When I tap on the online booking
    Then I should see the online booking page

  Scenario: Add Online Booking Without Appointment Combination
    Given I am on the online booking page
    When I tap on the add unspecified appointment combination
    And I enter the appointment combination name "New Combination"
    And I enter the appointment combination introduction "Combination Introduction"
    And I select the appointment combination service personnel "全部選取"
    And I tap on the confirm button on the add appointment combination
    Then I should see the appointment combination name "New Combination" on the online booking page

  Scenario: Edit Online Booking Appointment Combination
    Given I am on the online booking page
    When I tap on the edit appointment combination named "New Combination"
    And I tap on the open item tab
    And I select the main service item and clear all options "New Category" "Service Name"
    And I select the main service item "New Category" "Service Name 2"
    And I select the online booking type "單選"
    And I select the online booking type "複選"
    And I select the additional service item and clear all options "New Category" "Service Name 4"
    And I tap on the close button on the edit appointment combination
    Then I should see the appointment combination name "New Combination" on the online booking page