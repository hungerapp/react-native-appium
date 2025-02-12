Feature: Create Appointment

  @regression @create_appointment_anonymous
  Scenario: Successfully create an appointment with anonymous nickname
    Given I click the back button to go to calendar page
    When I click the create appointment option
    Then I fill in the contact with anonymous nickname
    Then I select a service person
    Then I select a service
    Then I select a valid appointment time
    Then I click create appointment and should see the appointment created successfully

  @regression @create_appointment_with_change_time_and_service_person
  Scenario: Successfully create an appointment with change time and service person
    Given I click the create appointment option
    When I fill in the contact with anonymous nickname
    Then I select a service person
    Then I select a service
    Then I change service time and service person
    Then I input the note in the note section
    Then I click create appointment and should see the appointment created successfully

  @regression @create_appointment_with_one_more_service
  Scenario: Successfully create an appointment with one more service
    Given I click the create appointment option
    When I fill in the contact with anonymous nickname
    Then I select a service person
    Then I select a service
    Then I add one more service
    Then I click create appointment and should see the appointment created successfully

  @regression @create_appointment_with_one_more_service_then_delete
  Scenario: Successfully create an appointment with one more service then delete
    Given I click the create appointment option
    When I fill in the contact with anonymous nickname
    Then I select a service person
    Then I select a service
    Then I add one more service
    Then I delete one service
    Then I can go back to calendar page after delete

  @regression @create_appointment_existing
  Scenario: Successfully create an appointment with existing nickname
    Given I click the create appointment option
    When I fill in the contact with existing nickname
    Then I select a service person
    Then I select a service
    Then I select a valid appointment time
    Then I click create appointment button
    Then I should see the appointment created successfully


  @regression @contact_info_valid_phone_number
  Scenario: Add a new contact with valid phone number
    Given I click the create appointment option
    When I click contact info section
    Then I enter a valid phone number
    Then I click the save button
    Then the contact should be saved successfully

  @regression @contact_info_invalid_phone_number
  Scenario: Show error for invalid phone number format
    Given I click the create appointment option
    When I click contact info section
    Then I enter an invalid phone number
    Then I should see an error message for invalid phone number

  @regression @contact_info_no_information
  Scenario: Save contact as anonymous when no information is entered
    Given I click the create appointment option
    When I click contact info section
    Then I click the save button without entering any information
    Then the contact should be saved as anonymous

  @regression @contact_info_search_by_partial_phone_number  
  Scenario: Search contact by partial phone number
    Given I click the create appointment option
    When I click contact info section
    Then I enter a partial phone number
    Then I click the phone search button
    Then I should see search results and select the contact then save

  @regression @contact_info_search_by_full_phone_number 
  Scenario: Search contact by full phone number
    Given I click the create appointment option
    When I click contact info section
    Then I enter a full phone number
    Then I click the phone search button
    Then I should see search results and select the contact then save

  @regression @contact_info_search_by_partial_name  
  Scenario: Search contact by partial name
    Given I click the create appointment option
    When I click contact info section
    Then I enter a partial name
    Then I click the name search button
    Then I should see search results and select the contact then save

  @regression @contact_info_search_by_full_name 
  Scenario: Search contact by full name
    Given I click the create appointment option
    When I click contact info section
    When I enter a full name
    Then I click the name search button
    Then I should see search results and select the contact then save

  @regression @create_partial_appointment_and_cancel
  Scenario: Create an appointment with partial information then cancel
    Given I click the create appointment option
    Then I fill in the contact with anonymous nickname
    Then I select a service person
    Then I select a service
    Then I click back button should see the unfinished window
