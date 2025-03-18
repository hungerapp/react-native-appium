Feature: Setting Button in Navigation Bar

    @regression @navigate_to_settings
    Scenario: Navigate to Setting Page from Calendar
        Given I am on the Calendar page
        When I tap on the Settings button in the navigation bar
        Then I should be navigated to the Settings page

    @regression @navigate_to_brand_shop
    Scenario: Access Brand Shop from Settings Page
        Given I am on the Settings page
        When I tap on the Brand Shop option
        Then I should be navigated to the Brand Shop page
        And I can view the list of branches and brand information
