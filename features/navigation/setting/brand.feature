Feature: Setting Button in Navigation Bar

    @regression @branch_settings_management @branch_settings_page @branch_brand_info_page
    Scenario: Navigate to Branch Settings and Edit Branch Information
        Given I tap the Settings button in the navigation bar
        Then I should see the Branch Settings Page
        When I tap on the Branch Name in the Branch Information section in the Branch Settings page
        Then I should see the Branch and Brand Information page
        Then I modify the branch name
        Then I modify the branch description
        Then I turn on the Show Branch Phone Toggle
        Then I modify the branch phone number
        Then I turn on the Show Branch Address Toggle
        Then I modify the branch address
        Then I tap on the expand brand settings button
        Then the brand settings section should be expanded
        Then I tap the Confirm Edit button in the Branch and Brand Information page
        Then I should return to the Branch Settings page

    @regression @branch_settings @toggle_off_display_features @branch_brand_info_page
    Scenario: Turn Off Branch Phone Display And Address Display
        Given I tap on the Branch Name in the Branch Information section in the Branch Settings page
        When I turn off the Show Branch Phone Toggle
        Then I turn off the Show Branch Address Toggle
        Then I tap the Confirm Edit button in the Branch and Brand Information page
        Then I should return to the Branch Settings page

    @regression @pro_business_plan_verification @plan_management_page
    Scenario: Verify Pro Business Plan Features and Navigation
#        Given I am on the Branch Settings page
#        Then my branch has a Pro Business plan subscription
#        When I tap on the Branch Information option section's Branch Purchase Plan
#        Then I should be navigated to the Plan Management page
#        When I tap on the view next plan details button
        Then the Payment Details dialog should be displayed
        When I tap on the close button in the Payment Details dialog
        Then the Payment Details dialog should be dismissed
#        When I tap on the plan change button
#        Then I should be navigated to the Plan Change page
#        When I navigate back to the Plan Management page
#        Then I tap on the Payment Records section
#        Then I should be navigated to the Payment Records page