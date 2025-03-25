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

    @regression @branch_settings_management @branch_settings_page @branch_brand_info_page
    Scenario: Turn Off Branch Address Display
        Given I tap the Settings button in the navigation bar
        Then I should see the Branch Settings Page
        When I tap on the Branch Name in the Branch Information section in the Branch Settings page
        Then I should see the Branch and Brand Information page
        When I turn off the Show Branch Address Toggle
        Then the branch address fields should be hidden
        Then I tap the Confirm Edit button in the Branch and Brand Information page
        Then I should return to the Branch Settings page
        Then I should see the branch address is not displayed


    @regression @navigate_to_plan_management @branch_settings_page
    Scenario: Navigate to Plan Management Page from Branch Settings
        Given I am on the Branch Settings page
        When I tap on the Branch Information option section's Branch Purchase Plan
        Then I should be navigated to the Plan Management page

    @regression @navigate_to_hotcake_coins_page @plan_management_page
    Scenario: Navigate to Hotcake Coins Page from Plan Management
        Given I am on the Plan Management page
        When I tap on the Hotcake Coins section
        Then I should be navigated to the Hotcake Coins page

    @regression @close_hotcake_coins_page @hotcake_coins_page
    Scenario: Close Hotcake Coins Page and Return to Plan Management
        Given I am on the Hotcake Coins page
        When I tap on the close button
        Then I should be navigated back to the Plan Management page

    @regression @navigate_to_credit_card_page @plan_management_page
    Scenario: Navigate to Credit Card Page when Card is Not Bound
        Given I am on the Plan Management page
        And the Credit Card is not bound
        When I tap on the Credit Card section
        Then I should be navigated to the Credit Card page
        # Note: Currently only testing unbound credit card state, bound state testing is not needed at this time

    @regression @validate_credit_card_required_fields @credit_card_page
    Scenario: Validate Required Fields in Credit Card Page
        Given I am on the Credit Card page
        Then I should see a confirm button that is disabled
        When I tap on the Cardholder Name field and leave it empty
        Then I should see "This field is required" message
        When I tap on the Mobile Number field and leave it empty
        Then I should see "This field is required" message
        When I tap on the Email Address field and leave it empty
        Then I should see "This field is required" message
        When I tap on the Credit Card Number field and leave it empty
        Then I should see "This field is required" message
        When I tap on the Expiration Date field and leave it empty
        Then I should see "This field is required" message
        When I tap on the CVV field and leave it empty
        Then I should see "This field is required" message
        Then I should see a confirm button that is still disabled

    @regression @close_credit_card_page @credit_card_page
    Scenario: Close Credit Card Page and Return to Plan Management
        Given I am on the Credit Card page
        When I tap on the close button
        Then I should be navigated back to the Plan Management page

    @regression @navigate_to_invoice_information @plan_management_page
    Scenario: Navigate to Invoice Information Page from Plan Management
        Given I am on the Plan Management page
        When I tap on the Invoice Information section
        Then I should be navigated to the Invoice Information page

    @regression @personal_invoice_no_billing_email @invoice_info_page
    Scenario: Verify Confirm Button is Disabled When No Billing Email for Personal Invoice
        Given I am on the Invoice Information page
        When I tap on the Invoice Type section
        And I tap on "Personal" option in the popup
        Then I should see the Invoice Type set to "Personal"
        Then I should see the Billing Email Address field is empty
        Then I should see a confirm button that is disabled
        When I enter some text and then clear the Billing Email Address field
        Then I should see a confirm button that is disabled

    @regression @modify_personal_billing_email @invoice_info_page
    Scenario: Modify Billing Email Address for Personal Invoice Type
        Given I am on the Invoice Information page
        When I tap on the Invoice Type section
        Then I tap on "Personal" option in the popup
        Then I should see the Invoice Type set to "Personal"
        Then I should see the Billing Email Address field
        Then I should see a confirm button that is disabled
        When I enter a valid email in the Billing Email Address field
        Then I should see a confirm button that is enabled
        When I tap the confirm button
        Then the changes should be saved successfully
        Then I should be navigated back to the Plan Management page

    @regression @company_invoice_no_fields @invoice_info_page
    Scenario: Verify Confirm Button is Disabled When Company Invoice Fields are Empty
        Given I am on the Invoice Information page
        When I tap on the Invoice Type section
        Then I tap on "Company" option in the popup
        Then I should see the Invoice Type set to "Company"
        Then I should see the Unified Business Number field is empty
        Then I should see the Company Name (Invoice Title) field is empty
        Then I should see the Billing Contact Email Address field is empty
        Then I should see a confirm button that is disabled
        When I enter some text and then clear all required fields
        Then I should see a confirm button that is disabled

    @regression @company_invoice_all_fields_filled @invoice_info_page
    Scenario: Verify Confirm Button is Enabled When All Company Invoice Fields are Filled
        Given I am on the Invoice Information page
        When I tap on the Invoice Type section
        Then I tap on "Company" option in the popup
        Then I should see the Invoice Type set to "Company"
        When I enter a valid Unified Business Number
        Then I enter a valid Company Name
        Then I enter a valid Billing Contact Email Address
        Then I should see a confirm button that is enabled
        When I tap the confirm button
        Then the changes should be saved successfully
        Then I should be navigated back to the Plan Management page

    @regression @free_plan_subscription_navigation @plan_management_page
    Scenario: Navigate to Plan Change Page from Free Plan
        Given I am on the Plan Management page
        Then my branch has a free trial plan subscription
        When I tap on the subscription payment button
        Then I should be navigated to the Plan Change page
        Then I should see the available paid plan options

    @regression @select_pro_business_plan @plan_change_page
    Scenario: Navigate to Pro Business Plan Details from Plan Change Page
        Given I am on the Plan Change page
        When I tap on the "Choose Pro Business Plan" button
        Then I should be navigated to the Pro Business Plan page
        Then I should see the Pro Business Plan information displayed correctly

    @regression @compare_plan_features @pro_business_plan_page @plan_comparison_popup
    Scenario: View Plan Comparison and Switch Between Plans in Comparison Popup
        Given I am on the Pro Business Plan page
        When I tap on the plan comparison button
        Then a plan feature comparison popup should appear
        Then the Pro Business tab should be selected
        Then I should see the Pro Business plan features displayed
        When I tap on another plan tab
        Then that plan tab should be selected
        Then I should see that plan's features displayed correctly

    @regression @close_plan_comparison @pro_business_plan_page @plan_comparison_popup
    Scenario: Close Plan Feature Comparison Popup
        Given I am on the Pro Business Plan page
        When I tap on the plan comparison button
        Then a plan feature comparison popup should appear
        When I tap on the close button in the comparison popup
        Then the plan feature comparison popup should close
        Then I should remain on the Pro Business Plan page

    @regression @select_star_new_star_plan @plan_change_page
    Scenario: Navigate to Star New Star Plan Details from Plan Change Page
        Given I am on the Plan Change page
        When I tap on the "Choose Star New Star Plan" button
        Then I should be navigated to the Star New Star Plan page
        Then I should see the Star New Star Plan information displayed correctly

    @regression @compare_plan_features @star_new_star_plan_page @plan_comparison_popup
    Scenario: View Plan Comparison and Switch Between Plans from Star New Star Plan Page
        Given I am on the Star New Star Plan page
        When I tap on the plan comparison button
        Then a plan feature comparison popup should appear
        Then the Star New Star tab should be selected
        Then I should see the Star New Star plan features displayed
        When I tap on another plan tab
        Then that plan tab should be selected
        Then I should see that plan's features displayed correctly

    @regression @close_plan_comparison @star_new_star_plan_page @plan_comparison_popup
    Scenario: Close Plan Feature Comparison Popup from Star New Star Plan Page
        Given I am on the Star New Star Plan page
        When I tap on the plan comparison button
        Then a plan feature comparison popup should appear
        When I tap on the close button in the comparison popup
        Then the plan feature comparison popup should close
        Then I should remain on the Star New Star Plan page

    @regression @navigate_to_payment_records @plan_management_page
    Scenario: Navigate to Payment Records Page from Plan Management
        Given I am on the Plan Management page
        When I tap on the Payment Records section
        Then I should be navigated to the Payment Records page
        Then I should see the Payment Records information displayed correctly

    @regression @close_payment_records @payment_records_page
    Scenario: Close Payment Records Page and Return to Plan Management
        Given I am on the Payment Records page
        When I tap on the close button
        Then I should be navigated back to the Plan Management page