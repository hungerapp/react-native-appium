Feature: Brand Management in Branch Settings

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
    Scenario: Verify PRO Business Plan Features and Navigation
        Given I am on the Branch Settings page
        Then my branch has a Pro Business plan subscription
        When I tap on the Branch Information option section's Branch Purchase Plan
        Then I should be navigated to the Plan Management page
        When I tap on the view next plan details button
        Then the Payment Details dialog should be displayed
        When I tap on the close button in the Payment Details dialog
        Then the Payment Details dialog should be dismissed
        When I tap on the plan change button
        Then I should be navigated to the Plan Change page
        When I tap the select Pro business plan button
        Then I should be navigated to the Pro Business plan page
        Then the select Pro Business plan button should be disabled
        When I tap the different plan button on the Pro Business plan page
        Then I should see the Pro Business plan content in the plan functionality dialog
        When I switch to the Start New tab
        Then I should see the Start New plan content in the plan functionality dialog
        When I switch to the Free Trial tab
        Then I should see the Free Trial plan content in the plan functionality dialog
        When I tap the close button plan functionality dialog button
        Then the plan functionality dialog should be dismissed
        When I tap the close button in the Pro Business plan page
        Then I should be navigated back to the Plan Change page
        When I tap the select Start New plan button
        Then I should be navigated to the Start New plan page
        Then the select Start New plan button should be enable
        When I tap the different plan button on the Pro Business plan page
        Then I should see the Start New plan content in the plan functionality dialog
        When I switch to the Free Trial tab
        Then I should see the Free Trial plan content in the plan functionality dialog
        When I switch to the Pro Business plan tab
        Then I should see the Pro Business plan content in the plan functionality dialog
        When I tap the close button plan functionality dialog button
        Then the plan functionality dialog should be dismissed
        When I tap the close button in the Start New Plan page
        Then I should be navigated back to the Plan Change page
        When I tap on Downgrade to Free Trial Plan in the Plan Change page
        Then the Cancel Payment Plan dialog should be displayed
        When I tap on Cancel button in the Cancel Payment Plan dialog
        Then the Cancel Payment Plan dialog should be dismissed
        When I tap close button in the Plan Change page
        Then I should be navigated to the Plan Management page
        When I tap on the Payment Records section
        Then I should be navigated to the Payment Records page
        When I tap close button in the Payment Records page
        Then I should be navigated to the Plan Management page
        When I tap back hotcake app button
        Then I should be navigated to the Branch Settings page