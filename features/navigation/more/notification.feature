Feature: Notification

  # [NOTIFICATIONS AND MESSAGES] 
  @regression @notifications_and_messages_in_more
  Scenario: Managing Notifications and Viewing Updates
    Given I click on notifications and messages
    When I click on the view latest features button
    Then I should be redirected to the changelog page
    When I click on any notification
    Then I should be successfully redirected to the corresponding page
    When I click the mark all as read button
    Then all notifications should be marked as read
    Then I can return to the calendar page