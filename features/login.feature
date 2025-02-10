Feature: Login Feature (existing)
  As a registered user
  I want to log in using my existing account
  So that I can access the main features of the app
  

  @regression @select_language
  Scenario: Select language
    Given the app is launched
    When I select my language and click sure button
    Then I can save the language setting and continue to the login page

  @regression @click_terms_and_conditions
  Scenario: Click terms and conditions
    When I click terms and conditions button
    Then I can see the terms page and click the back button to go back to the start page
    When I click privacy button
    Then I can see the privacy page and click the back button to go back to the start page
  
  @regression  @login_invalid_email 
  Scenario: Unsuccessful login with invalid email
    When the user enters an invalid email
    Then the user should see an invalid email error message

  @regression @login_unregistered_email
  Scenario: Unsuccessful login with unregistered email
    When the user enters an unregistered email
    Then the user should see an popup window with email not registered
  
  @regression @login_invalid_verification_code 
  Scenario: Unsuccessful login with invalid verification code
    When the user enters an invalid verification code
    Then the user should see an invalid verification code error message

  @regression @login_modify_email
  Scenario: Modify email from verification code page
    When the user clicks modify email button
    Then the user can enter valid email again
    Then the user should be on verification code page again

  @regression @login_existing 
  Scenario: Successful login
    When the user enters valid credentials
    Then the user should be logged in successfully

  