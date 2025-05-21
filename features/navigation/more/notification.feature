Feature: Notification

  # [NOTIFICATIONS AND MESSAGES] 
  @regression @notifications_and_messages_in_more @navigation @navigation_more @navigation_more_notification
  Scenario: Managing Notifications and Viewing Updates
    Given I click on notifications and messages
    When I click on the view latest features button
    Then I should be redirected to the changelog page
    When I on the notification page
    Then I can see the notification below
    When I click the mark all as read button
    Then all notifications should be marked as read
    Then I can return to the calendar page