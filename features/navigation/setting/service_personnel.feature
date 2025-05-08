Feature: Service Personnel Management
    As a Merchant User
    I want to manage service personnel
    So that I can maintain service staff information

    @regression @add_service_personnel
    Scenario: Add service personnel
        Given I am on the Branch Settings page
        When I tap on the Service Personnel
        And I add service personnel "要刪掉的人員<current_datetime>" and select color "1" and enter "robot_introduction<current_datetime>" and the Simultaneous Service Count "1"
        And I delete "要刪掉的人員<current_datetime>" from the Service Personnel list
        And I add service personnel "需要編輯的人員<current_datetime>" and select color "1" and enter "robot_introduction<current_datetime>" and the Simultaneous Service Count "1"
        When I edit service personnel "需要編輯的人員<current_datetime>" to "服務人員1_<current_datetime>" and select color "2" and enter "我是1號服務人員" and the Simultaneous Service Count "1"
        And I add service personnel "服務人員2_<current_datetime>" and select color "3" and enter "我是2號服務人員" and the Simultaneous Service Count "1"
        And I tap on the close button in service personnel Page
        Then I should see the branch settings page








