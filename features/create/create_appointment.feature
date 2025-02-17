Feature: Create Appointment

  @regression @create_appointment_anonymous 
  Scenario: Successfully create an appointment with anonymous nickname
    Given I click the back button to go to calendar page
    When I click the create appointment option
    Then I fill in the contact with anonymous nickname
    Then I select a service person
    Then I select a service
    Then I change service time and service person
    Then I input the note in the note section
    Then I select a valid appointment time
    Then I click create appointment and should see the appointment created successfully
  
 
  @regression @create_one_more_service 
  Scenario: Successfully create an appointment with one more service
    Given I click the create appointment option
    When I select a service person
    Then I select a service
    Then I select a valid appointment time
    Then I click one more service button
    Then I change the reservation time and add one more service
    Then I choose which deposit should be selected
    Then I can successfully create an appointment with one more service

  @regression @create_one_more_then_delete 
  Scenario: Successfully create an appointment with one more service then delete
    Given I click the create appointment option
    When I select a service person
    Then I select a service
    Then I select a valid appointment time
    Then I click one more service button
    Then I delete one service
    Then I can go back to calendar page after delete

  @regression @create_appointment_existing_name_phone 
  Scenario: Successfully create an appointment with existing name and phone number
    Given I click the create appointment option
    When I fill in the contact with existing name and phone number
    Then I check the member passport and back 
    Then I select a service person
    Then I select a service
    Then I select a valid appointment time
    Then I click create appointment and should see the appointment created successfully


  @regression @contact_info_invalid_phone_number 
  Scenario: Show error for invalid phone number format
    Given I click the create appointment option
    When I click contact info section
    Then I enter an invalid phone number
    Then I should see an error message for invalid phone number

  @regression @create_appointment_for_selecting_and_searching_country_code
  Scenario: Create Appointment for selecting and searching country code
    Given I am on the contact page
    When I select random country code
    Then I should see different country code in the phone number input field
    When I search different country code
    Then I should see different country code in the phone number input field



  @regression @contact_info_search_by_partial_phone_number  
  Scenario: Search contact by partial phone number
    Given I am on the create appointment page
    When I click contact info section
    Then I enter a partial phone number
    Then I click the phone search button for partial phone number
    Then I should see search results and select the contact then save


  @regression @create_appointment_for_modify_contact 
  Scenario: Create Appointment for modify contact
    Given I have chosen a contact
    When I change the contact info section
    Then I should save then back to calendar


  @regression @contact_info_search_by_full_phone_number 
  Scenario: Search contact by full phone number
    Given I click the create appointment option
    When I click contact info section
    Then I enter a full phone number
    Then I click the phone search button for full phone number
    Then I should see search results and save then back to calendar


  @regression @contact_info_search_by_partial_name  
  Scenario: Search contact by partial name
    Given I click the create appointment option
    When I click contact info section
    Then I enter a partial name
    Then I click the name search button for partial name
    Then I should see search results and save then back to calendar


  @regression @contact_info_search_by_full_name 
  Scenario: Search contact by full name
    Given I click the create appointment option
    When I click contact info section
    When I enter a full name
    Then I click the name search button for full name
    Then I should see search results and save then back to calendar
