Feature: Setting Button in Navigation Bar

    @regression @navigate_to_branch_settings @calendar_page
    Scenario: Navigate to Branch Settings Page from Calendar
        Given I am on the Calendar page
        When I tap on the Settings button in the navigation bar
        Then I should be navigated to the Branch Settings page

    @regression @navigate_to_branch_and_brand_info @branch_settings_page
    Scenario: Access Branch Information from Branch Settings Page
        Given I am on the Branch Settings page
        When I tap on the Branch Information option section's Branch Name
        Then I should be navigated to the Branch and Brand Information page
        Then I can view the list of branches and their details

    @regression @edit_branch_name @branch_brand_info_page
    Scenario: Edit Branch Name on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        When I tap on the Branch Name field
        Then I enter a new branch name
        Then I tap the confirm edit button
        Then the branch name should be updated successfully

    @regression @edit_branch_description @branch_brand_info_page
    Scenario: Edit Branch Description on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        When I tap on the Branch Description field
        Then I enter a new branch description
        Then I tap the confirm edit button
        Then the branch description should be updated successfully

    @regression @toggle_branch_phone_switch_on @branch_brand_info_page
    Scenario: Open Show Branch Phone Toggle in Branch Phone Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Phone Toggle is off
        When I tap on the Show Branch Phone Toggle
        Then the Show Branch Phone Toggle should turn on
        Then I tap the confirm edit button
        Then the branch description should be updated successfully

    @regression @toggle_branch_phone_switch_off @branch_brand_info_page
    Scenario: Close Show Branch Phone Toggle in Branch Phone Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Phone Toggle is on
        When I tap on the Show Branch Phone Toggle
        Then the Show Branch Phone Toggle should turn off
        Then I tap the confirm edit button
        Then the branch description should be updated successfully

    @regression @edit_taiwan_phone_number @branch_brand_info_page
    # Note: Currently only supporting Taiwan region, country code selection not implemented yet
    Scenario: Edit Taiwan Phone Number in Branch Phone Section
        Given I am on the Branch and Brand Information page
        When I tap on the Branch Phone field
        Then I enter a new phone number
        Then I tap the Confirm Edit Button
        Then the Branch Phone should be updated successfully

    @regression @toggle_branch_address_switch_on @branch_brand_info_page
    Scenario: Open Show Branch Address Toggle in Branch Address Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Address Toggle is off
        When I tap on the Show Branch Address Toggle
        Then the Show Branch Address Toggle should turn on
        Then I tap the confirm edit button
        Then the branch address should be updated successfully

    @regression @toggle_branch_address_switch_off @branch_brand_info_page
    Scenario: Close Show Branch Address Toggle in Branch Address Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Address Toggle is on
        When I tap on the Show Branch Address Toggle
        Then the Show Branch Address Toggle should turn off
        Then I tap the confirm edit button
        Then the branch address should be updated successfully


    @regression @expand_brand_setting_button @branch_brand_info_page
    Scenario: Expand Brand Setting Button on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        When I tap on the expand brand settings button
        Then the button text should change to collapse brand settings button
        Then the brand settings section should be expanded
        Then within the brand settings section, I should see the brand image
        Then within the brand settings section, I should see the brand name
        Then within the brand settings section, I should see the brand description

    @regression @edit_brand_name @branch_brand_info_page
    Scenario: Edit Brand Name on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        When I tap on the expand brand settings button
        Then the brand settings section should be expanded
        Then I can see the original brand name
        When I tap on the Brand Name field
        Then I enter a new brand name
        Then I tap the confirm edit button
        Then the brand name should be updated successfully

    @regression @edit_brand_description @branch_brand_info_page
    Scenario: Edit Brand Description on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        When I tap on the expand brand settings button
        Then the brand settings section should be expanded
        Then I can see the original brand description
        When I tap on the Brand Description field
        Then I enter a new brand description
        Then I tap the confirm edit button
        Then the brand description should be updated successfully

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