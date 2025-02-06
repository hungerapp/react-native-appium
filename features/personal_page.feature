Feature: Personal Page
  As a user
  I want to manage my profile and branch settings
  So that I can customize my account preferences and branch notifications

  

  
  @regression @basic_personal_information
  Scenario: View basic personal information
    Given I successfully logged in first time
    Then I should see my profile picture
    Then I should see my username
    Then I should see greeting message
    Then I should see my email address

  @regression @brand_list
  Scenario: View brand list section
    Given I am on the personal page
    Then I should see the brand list title
    Then I should see hunger Salon-staging title with profile picture
    Then I should be able to visit all branches
  
  @regression @In_development @skip
  Scenario: Access all reservations
    Given I am on the personal page
    When I tap on "所有預約" button
    Then I should be redirected to the reservation list page

  @regression @In_development @skip
  Scenario: Access Google Calendar
    Given I am on the personal page
    When I tap on "Google 日曆" button  
    Then I should be redirected to the Google Calendar page

  @regression @push_notification
  Scenario: Manage Push Notification
    Given I am on the personal page
    When I click push notification button
    Then I should be able to toggle random notification settings
    Then I should be able to save notification settings
  
  @regression @manage_account_settings
  Scenario Outline: Update account settings multiple times
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I should be able to update account information 3 times and save settings
      | field    | action                    |
      | name     | input random name         |
      #| gender   | select random gender      |
      | birthday | select random date        |
      | phone    | input valid phone number  |

    Examples:
      | times |
      | 3     |
  
  @regression @empty_name @skip
  Scenario: Verify empty name error
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I input empty name and get error message
  
  @regression @empty_phone_number @skip
  Scenario: Verify empty phone number error
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I input empty phone number and get error message

  @regression @invalid_phone_number @skip
  Scenario: Verify invalid phone number error
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I input invalid phone number
    Then I should see error message for invalid phone

 