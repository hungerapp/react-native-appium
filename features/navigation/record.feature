Feature: Record function in bottom navigation

    @regression @view_recent_and_canceled_appointments
    Scenario: View and Switch Between Recent and Canceled Appointments
        Given I tap on records in the navigation bar
        Then I can tap on any recently added order under the appointments tab
        When I switch to the recently canceled tab
        Then I can tap on any recently canceled order
    
    @regression @filter_by_personnel_and_search
    Scenario: Filter by Personnel and Search
        Given I am on the Records page
        When I click on the billing tab
        Then I click the filter icon
        Then I can filter by service staff
        Then I can tap on the search field and enter a billing number
        Then I can successfully search for the specified billing number

    @regression @view_checkout_details_and_check_payment_method
    Scenario: View Checkout Details and Check Payment Method
        Given I am on the Records page
        When I click on the billing tab
        Then I tap view details
        Then I can view the details and export them
        When I tap the view checkout button
        Then I can check the payment method
        
    
    @regression @process_and_delete_claim_request
    Scenario: Process and Delete a claim request
        Given I am on the Records page
        When I click on the billing tab
        Then I click on the claim request option
        Then I click the filter icon
        Then I can filter by service staff
        When I tap view details
        Then I can successfully view the details and export them
        When I tap the view request checkout button
        Then I can delete the checkout request
        Then I can successfully return to the Calendar page

    @regression @appointment_function_validation
    Scenario: Appointment Function Validation
        Given I successfully create an specific appointment data
        When I tap on records in the navigation bar
        Then I can switch any state option
        When I tap the deposit section
        Then I can see the deposit details
        When I tap the deposit section
        Then I can change the deposit state
        When I tap the deposit section
        Then I can see the deposit details
        Then I can change the service personnel
        Then I can change the service
        When I click note section
        Then I can input the note details
        When I click rate section
        Then I can rate for the user

    @regression @appointment_bottom_navigation_validation
    Scenario: Appointment Bottom Navigation Validation
        Given I am on the record appointment page
        When  I click send message option and attempt to send message
        Then I can successfully send message
        When I click edit option and attempt to edit the appointment
        Then I can successfully edit the appointment
        When I click cancel option and attempt to cancel the appointment
        Then I can successfully cancel the appointment
        When I click copy option and attempt to copy the appointment
        Then I can successfully copy the appointment
    
    @regression @successfully_checkout_more_function_validation
    Scenario: Successfully Checkout More Function Validation
        Given I successfully finish checkout
        When I click checkout more option
        Then I can view checkout details
        Then I can view billing details
        Then I can view member passport
        Then I can send tickets to the member
        Then I can view the appointment history
        
        
        
        






