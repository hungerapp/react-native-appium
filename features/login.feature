Feature: Login Feature (existing)
  As a registered user
  I want to log in using my existing account
  So that I can access the main features of the app
  

  
  @regression  @login_invalid_email 
  Scenario: Unsuccessful login with invalid email
    Given the app is launched
    When the user enters an invalid email
    Then the user should see an invalid email error message
  
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

    