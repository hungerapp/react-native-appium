Feature: iPad Device
    As a branch administrator
    I want to manage the iPad device of the branch
    To provide a better customer experience

    @regression @ipad_device_management @navigation_to_ipad_device @navigate_settings @navigate @navigate_settings_ipad_device
    Scenario: Navigate to iPad Device
        Given I am on the branch settings page
        When I tap on the iPad Device
        Then I should see the ipad device page

    @regression @ipad_device_management @add_ipad_device @navigate_settings @navigate @navigate_settings_ipad_device
    Scenario: Add iPad Device
        Given I am on the iPad device page
        When I add a new iPad device
        And I tap on the close button in the iPad device page
        Then I should see the branch settings page