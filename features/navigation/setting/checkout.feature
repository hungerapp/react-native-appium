Feature: Checkout in Branch Settings
    As a branch administrator
    I want to manage the checkout information of the branch
    To provide a better customer experience

    @regression @checkout_management @navigation_to_checkout @navigate_settings @navigate @navigate_settings_checkout
    Scenario: Navigate to Checkout
        Given I am on the branch settings page
        When I tap on the Checkout
        Then I should see the checkout page

    @regression @checkout_management @checkout_signature @navigate_settings @navigate @navigate_settings_checkout
    Scenario: Checkout Signature
        Given I am on the checkout page
        When I turn on the checkout signature switch
        And I tap on  the back button
        Then I should see the branch settings page