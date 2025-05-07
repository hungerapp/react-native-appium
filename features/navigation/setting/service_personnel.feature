Feature: Service Personnel Management
    As a Merchant User
    I want to manage service personnel
    So that I can maintain service staff information

    @regression @service_personnel_add
    Scenario: Successfully add new service personnel
        Given I am on the Branch Settings page
        When I tap on the Service Personnel
        And I tap on Add Service Personnel button
        And I enter "Robot大軍<current_datetime>" in the Name field
        And I select color "3" from the Color list
        And I enter "robot_introduction<current_datetime>" in the Introduction field
        And I enter "3" in the Simultaneous Service Count field
        And I tap on the Confirm button in service personnel modal
        When I delete "Robot大軍<current_datetime>" from the Service Personnel list
        And I tap on the close button in service personnel Page
        Then I should see the branch settings page








