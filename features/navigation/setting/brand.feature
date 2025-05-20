@onboarding
Feature: Brand Management in Branch Settings
    As a branch administrator
    I hope to manage the brand information of the branch
    To provide a better customer experience

    @regression @navigation_to_branch_settings_page @setting_brand_and_branch
    Scenario: Navigate to the Branch Settings Page
        Given I am on the Calendar page
        When I tap on the Settings icon in the navigation bar
        Then I should see the Branch Settings page

    @regression @save_branch_brand_info
    Scenario: Save Branch and Brand Information
        Given I am on the Branch Setting page
        When I tap on the Branch Name
        And I enter "Robot_Branch_Name<current_datetime>" in the Branch Name field
        And I enter "🤖 Welcome to our AI-powered store! We provide <current_datetime> automated service." in the branch introduction
        And I turn off the branch phone display switch
        And I turn on the branch phone display switch
        And I select "+886" as the country code
        And I enter "0920250101" in the branch phone number field
        And I turn off the branch address display switch
        And I turn on the branch address display switch
        And I select "臺北市" as the city
        And I select "中正區" as the district
        And I enter "地球路<current_datetime>號" in the branch address field
        And I tap on the Expand Brand Settings button
        And I tap on the confirm button
        Then I should see the Branch Settings page

    # TODO: Add Subscription Plan Management



