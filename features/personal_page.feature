Feature: Personal Page
  As a user
  I want to view and manage my personal information
  So that I can access my account details and quick functions

  
  Background:
    Given the user is logged in successfully
  
  @regression @basic_personal_information
  Scenario: View basic personal information
    Then the user should see the profile picture and username
    Then the user should see the greeting message based on the current time
    Then the user should see the email address

  @regression @brand_list
  Scenario: View brand list
    When the user views the brand list section
    Then the user should see all associated brands
    Then the user should see correct brand names in the list
    Then the user should see branch stores in correct order
    When the user tap on a brand item
    Then the user should be redirected to the corresponding brand page
  
  @regression @In_development 
  Scenario: Access all reservations
    When the user tap on "所有預約" button
    Then the user should be redirected to the reservation list page

  @regression @In_development 
  Scenario: Access Google Calendar
    When the user tap on "Google 日曆" button  
    Then the user should be redirected to the Google Calendar page

  @regression @push_notification
  Scenario: Access Push Notification
    When the user tap on "推播通知" button
    Then the user should be redirected to the Push Notification page

  @regression @manage_account_settings
  Scenario: Access Manage Account Settings
    When the user tap on the settings button
    Then the user should see the pop-up window and "帳號設定"、"語言設定"、"登出" options
    When the user tap on "帳號設定" option and revise account information
    Then the user should see the account information is updated
    When the user tap on "語言設定" option and select any of languages
    Then app should be restarted and the user should see the language is updated
  

