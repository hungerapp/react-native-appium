Feature: Login Feature (existing)
  As a registered user
  I want to log in using my existing account
  So that I can access the main features of the app
  

  @regression @select_language_and_contact_cs
  Scenario: Select language and click contact cs
    Given the app is launched
    Then I can see the login page displayed
    Then I can select my language and click sure button
    Then I can click contact cs button and go back to the login page

  @regression @click_terms_and_conditions
  Scenario: Click terms and conditions
    When I click terms and conditions button
    Then I can see the terms page and click the back button to go back to the start page
    When I click privacy button
    Then I can see the privacy page and click the back button to go back to the start page
  
  @regression  @login_invalid_email 
  Scenario: Unsuccessful login with invalid email
    When the user enters an invalid email "test@hotcake"
    Then the user should see an invalid email error message "請填寫正確的電子郵件。"

  @regression @login_unregistered_email
  Scenario: Unsuccessful login with unregistered email
    When the user enters an unregistered email "test@hotcake.com"
    Then the user should see an popup window with email not registered "請檢查信箱是否輸入正確"
  
  @regression @login_invalid_verification_code 
  Scenario: Unsuccessful login with invalid verification code
    When the user enters an invalid verification code "julian@hotcake.app" "123456"
    Then the user should see an invalid verification code error message "請檢查驗證通行碼是否輸入正確"

  @regression @login_modify_email
  Scenario: Modify email from verification code page
    When the user clicks modify email button "julian@hotcake.app"
    Then the user can enter valid email again "ann@hunger.ai"
    Then the user should be on verification code page again

  @regression @login_existing 
  Scenario: Successful login
    When the user enters valid credentials "julian@hotcake.app" "5556666"
    Then the user should be logged in successfully

  