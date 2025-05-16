Feature: Third Party Tools in Branch Settings
    As a branch administrator
    I want to manage the third party tools of the branch
    To provide a better customer experience

    @regression @third_party_tools_management @navigation_to_third_party_tools
    Scenario: Navigate to Third Party Tools with Subscription plan free
        Given I am on the branch settings page
        And This branch is subscribed to "Free免費體驗方案"
        When I tap on the Third Party Tools
        Then I should see the Feature Unsupported Dialog

    # TODO: Only testing the "Free" plan for now to prevent conflicts with other scenarios.


