Feature: web layout management
    As a branch administrator
    I want to manage the web layout of the branch
    To provide a better customer experience

    @regression @web_layout_management @navigation_to_web_layout @navigate_settings @navigate @navigate_settings_web_layout
    Scenario: Navigate to Web Layout
        Given I am on the branch settings page
        When I tap on the Web Layout
        Then I should see the web layout page

    @regression @web_layout_management @setting_the_web_layout @navigate_settings @navigate @navigate_settings_web_layout
    Scenario: Setting the web layout
        Given I am on the web layout page
        When I select the web layout color "1"
        And I set week start day to "週一"
        And I set week start day to "週日"
        And I set the google tracking code to "google tracking code <current_datetime>"
        And I tap on the confirm button
        And I tap on the close button in the web layout page
        Then I should see the branch settings page
