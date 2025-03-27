Feature: Subscription Management

  # [SUBSCRIPTION MANAGEMENT]
  @regression @subscription_management_in_more
  Scenario: Viewing and Returning from Subscription Management
    Given I click on subscription management
    Then I should be able to view the current plans
    Then I should be able to return to the calendar page
