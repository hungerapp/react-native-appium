Feature: Service Personnel Management
    As a Merchant User
    I want to manage service personnel
    So that I can maintain service staff information

    @regression @add_service_personnel
    Scenario: Add service personnel
        Given I am on the Branch Settings page
        When I tap on the Service Personnel
        And I add service personnel "需要編輯的人員<current_datetime>" and select color "1" and enter "robot_introduction<current_datetime>" and the Simultaneous Service Count "1"
        And I edit service personnel "需要編輯的人員<current_datetime>" to "要刪掉的人員_<current_datetime>" and select color "2" and enter "我將會被刪掉" and the Simultaneous Service Count "2"
        And I delete "要刪掉的人員_<current_datetime>" from the Service Personnel list
        And I tap on the close button in service personnel Page
        Then I should see the branch settings page








