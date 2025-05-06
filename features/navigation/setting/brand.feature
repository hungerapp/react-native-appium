Feature: Brand Management in Branch Settings
    As a branch administrator
    I hope to manage the brand information of the branch
    To provide a better customer experience

    @regression @save_branch_brand_info
    Scenario: Navigate to Branch and Brand Information Page
        Given I am on the Calendar page
        When I tap on the Settings icon in the navigation bar
        And I tap on the Branch Name
        Then I should see the Branch and Brand Information page


    @regression @save_branch_brand_info
    Scenario: Save Branch and Brand Information
        Given I am on the Branch and Brand Information page
        When I enter "Robot_Branch_Name" in the Branch Name field
        And I enter "🤖 Welcome to our AI-powered store! We provide 24/7 automated service." in the branch introduction
        And I turn on the branch phone display switch
        And I select "+886" as the country code
        And I enter "0912345678" in the branch phone number field
        And I turn on the branch address display switch
        And I select "臺北市" as the city
        And I select "中正區" as the district
        And I enter "地球路1號" in the branch address field
        And I tap on the Expand Brand Settings button
        And I tap on the confirm button
        Then I should see the Branch Settings page

    # TODO: Add Subscription Plan Management



