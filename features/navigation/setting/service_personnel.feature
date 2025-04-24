Feature: Service Personnel Management
    As a Merchant User
    I want to manage service personnel
    So that I can maintain service staff information

    @regression @service_personnel_add
    Scenario: Successfully add new service personnel
        Given I am on the Service Personnel page
        When I tap on Add Service Personnel button
        Then I should see the service personnel Modal
        When I enter "Robot大軍" in the Name field
        And I select color "3" from the Color list
        And I enter "robot_introduction" in the Introduction field
        And I enter "3" in the Simultaneous Service Count field
        And I tap on the Confirm button in service personnel modal
        Then I should see the Service Personnel page
        And I should see "Robot大軍" in the Service Personnel list

    @regression @service_personnel_delete
    Scenario: Successfully delete service personnel
        Given I am on the Service Personnel page
        And I should see "Robot大軍" in the Service Personnel list
        When I delete "Robot大軍" from the Service Personnel list
        Then I should see the Service Personnel page







