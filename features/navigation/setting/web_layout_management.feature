Feature: web layout management
    As a branch administrator
    I want to manage the web layout of the branch
    To provide a better customer experience

    Background:
      Given I have selected the target branch "測試用分店"
      And I Navigate to the branch settings page

    @regression @web_layout_management @navigation_to_web_layout @navigate_settings @navigate @navigate_settings_web_layout
    Scenario: Navigate to Web Layout
        Given I am on the branch settings page
        When I tap on the Web Layout


    @regression @setting_the_web_layout @web_layout_management @setting_the_web_layout @navigate_settings @navigate @navigate_settings_web_layout
    Scenario: Setting the web layout
        Given I am on the branch settings page
        When I tap on the Web Layout
        And I turn on the online service appointment
        And I turn off the online service appointment
        And I turn on the stored value feature
        And I turn off the stored value feature
        And I turn on the ticket feature
        And I turn off the ticket feature
        And I turn on the bonus points feature
        And I turn off the bonus points feature
        And I select the web layout color "3"
        And I set week start day to "週一"
        And I set week start day to "週日"
        And I set the google tracking code to "google tracking code <current_datetime>"
        And I tap on the confirm button
        And I tap on the close button in the web layout page
        And I tap on the close button in the branch settings page
        Then I should see the calendar page
