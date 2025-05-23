Feature: Personal Page
  As a user
  I want to manage my profile and branch settings
  So that I can customize my account preferences and branch notifications

  

  
  @regression @basic_personal_information @personal_page
  Scenario: View basic personal information
    Given I successfully logged in first time
    Then I should see my profile picture
    Then I should see my username
    Then I should see greeting message
    Then I should see my email address
  
  @regression @view_brand_list @personal_page
  Scenario: View brand list section
    Given I am on the personal page
    Then I should see the brand list title
    Then I should see hunger Salon-staging title with profile picture
    Then I should be able to visit all branches
  

  @regression @integrate_calendar @skip @personal_page
  Scenario: Access all reservations
    Given I am on the personal page
    When I tap on all reservations button
    Then I should be redirected to the reservation list page

  @regression @integrate_google_calendar @personal_page
  Scenario: Access Google Calendar
    Given I am on the personal page
    When I click on google calendar button  
    Then I should be redirected to google login page

  @regression @push_notification @personal_page
  Scenario: Manage Push Notification
    Given I am on the personal page
    When I click push notification button
    Then I should be able to toggle random notification settings
    Then I should be able to save notification settings
  


  @regression @manage_account_settings @personal_page
  Scenario: Update account settings
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I should be able to update account information and save settings

  
  
  @regression @empty_name @personal_page
  Scenario: Verify empty name error
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I input empty name and get error message
  
  @regression @empty_phone_number @personal_page
  Scenario: Verify empty phone number error
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I input empty phone number and get error message

  @regression @personal_page_invalid_phone_number @personal_page
  Scenario: Verify invalid phone number error
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I input invalid phone number
    Then I should see error message for invalid phone

 @regression @select_different_country_code @personal_page
 Scenario: Select different country code
    Given I am on the personal page
    When I click settings icon
    Then I click account settings option
    Then I select different country code and save 
    Then I should see different country code in the phone number input field

 @regression @search_country_code @personal_page
 Scenario: Search different country code
    Given I am on the acc setting page
    When I search different country code and save 
    Then I should see different country code I've searched in the phone number input field

@regression @select_language_on_personal_page @personal_page
 Scenario: Select language on personal page
    Given I am on the personal page
    When I click settings icon
    Then I click language settings
    Then I select language and save


