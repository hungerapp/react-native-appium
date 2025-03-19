Feature: Setting Button in Navigation Bar

    @regression @navigate_to_branch_settings
    Scenario: Navigate to Branch Settings Page from Calendar
        Given I am on the Calendar page
        When I tap on the Settings button in the navigation bar
        Then I should be navigated to the Branch Settings page

    @regression @check_branch_settings_layout
    Scenario: Check Layout of Branch Settings Page
        Given I am on the Branch Settings page
        Then I should see the header with text "Branch Settings"
        Then I should see a close button
        Then I should see the Branch ID
        Then I should see the Branch Information option section
        Then within the Branch Information option section, I should see the Branch Name Then Branch Purchase Plan
        Then I should see the Invitation Code
        Then I should see the Operations Management section
        Then within the Operations Management section, I should see service personnel, service appointment, item, and third-party tools
        Then I should see the Web Layout Management section
        Then I should see the Member Apply section
        Then the layout should be responsive

    @regression @navigate_to_branch_and_brand_info
    Scenario: Access Branch Information from Branch Settings Page
        Given I am on the Branch Settings page
        When I tap on the Branch Information option section's Branch Name
        Then I should be navigated to the Branch and Brand Information page
        Then I can view the list of branches and their details

    @regression @check_branch_and_brand_info_layout
    Scenario: Check Layout of Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I should see the header with text "Branch and Brand Information"
        Then I should see a close button
        Then I should see a confirm edit button
        Then I should see the branch image
        Then within the branch image, I should see a camera icon
        Then I should see the branch image ratio hint text
        Then I should see the branch information section
        Then within the branch information section, I should see the branch name
        Then within the branch information section, I should see the branch description
        Then I should see the branch phone section
        Then within the branch phone section, I should see the show branch phone toggle
        Then I should see the branch phone
        Then I should see the branch address section
        Then within the branch address section, I should see the country
        Then within the branch address section, I should see the city
        Then within the branch address section, I should see the district
        Then within the branch address section, I should see the address
        Then I should see the expand brand settings button

    @regression @edit_branch_name
    Scenario: Edit Branch Name on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I can see the original branch name
        Then I can see branch name title
        When I tap on the Branch Name field
        Then I enter a new branch name
        Then I tap the confirm edit button
        Then the branch name should be updated successfully

    @regression @edit_branch_description
    Scenario: Edit Branch Description on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I can see the branch description title
        Then I can see the original branch description
        When I tap on the Branch Description field
        Then I enter a new branch description
        Then I tap the confirm edit button
        Then the branch description should be updated successfully

    @regression @toggle_branch_phone_switch_on
    Scenario: Open Show Branch Phone Toggle in Branch Phone Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Phone Toggle title in the Branch Phone Section
        Then I can see the Show Branch Phone Toggle is off
        When I tap on the Show Branch Phone Toggle
        Then the Show Branch Phone Toggle should turn on
        Then I tap the confirm edit button
        Then the branch description should be updated successfully

    @regression @toggle_branch_phone_switch_off
    Scenario: Close Show Branch Phone Toggle in Branch Phone Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Phone Toggle title in the Branch Phone Section
        Then I can see the Show Branch Phone Toggle is on
        When I tap on the Show Branch Phone Toggle
        Then the Show Branch Phone Toggle should turn off
        Then I tap the confirm edit button
        Then the branch description should be updated successfully

    @regression @edit_taiwan_phone_number
    # Note: Currently only supporting Taiwan region, country code selection not implemented yet
    Scenario: Edit Taiwan Phone Number in Branch Phone Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Phone Toggle title in the Branch Phone Section
        Then I can see the country code and Branch Phone in the Branch Phone Section
        Then I can see the original country code and phone number
        When I tap on the Branch Phone field
        Then I enter a new phone number
        Then I tap the Confirm Edit Button
        Then the Branch Phone should be updated successfully

    @regression @toggle_branch_address_switch_on
    Scenario: Open Show Branch Address Toggle in Branch Address Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Address Toggle title in the Branch Address Section
        Then I can see the Show Branch Address Toggle is off
        When I tap on the Show Branch Address Toggle
        Then the Show Branch Address Toggle should turn on
        Then I tap the confirm edit button
        Then the branch address should be updated successfully

    @regression @toggle_branch_address_switch_off
    Scenario: Close Show Branch Address Toggle in Branch Address Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Address Toggle title in the Branch Address Section
        Then I can see the Show Branch Address Toggle is on
        When I tap on the Show Branch Address Toggle
        Then the Show Branch Address Toggle should turn off
        Then I tap the confirm edit button
        Then the branch address should be updated successfully

    @regression @toggle_branch_address_switch_on
    Scenario: Open Show Branch Address Toggle in Branch Address Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Address Toggle title in the Branch Address Section
        Then I can see the Show Branch Address Toggle is off
        When I tap on the Show Branch Address Toggle
        Then the Show Branch Address Toggle should turn on
        Then I tap the confirm edit button
        Then the branch address should be updated successfully

    @regression @toggle_branch_address_switch_off
    Scenario: Close Show Branch Address Toggle in Branch Address Section
        Given I am on the Branch and Brand Information page
        Then I can see the Show Branch Address Toggle title in the Branch Address Section
        Then I can see the Show Branch Address Toggle is on
        When I tap on the Show Branch Address Toggle
        Then the Show Branch Address Toggle should turn off
        Then I tap the confirm edit button
        Then the branch address should be updated successfully

    @regression @modify_branch_address
    Scenario: Modify Branch Address on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I can see the branch address section
        Then I can see Taiwan displayed in the Country field
        Then I can see the city, district, and address fields in branch address section
        Then I can see the original address
        When I tap on the City dropdown
        Then I select a new city from the dropdown menu
        When I tap on the District dropdown
        Then I select a new district from the dropdown menu
        When I tap on the Address field
        Then I enter a new address
        Then I tap the confirm edit button
        Then the branch address should be updated successfully

    @regression @expand_brand_setting_button
    Scenario: Expand Brand Setting Button on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I can see the expand brand settings button
        When I tap on the expand brand settings button
        Then the button text should change to collapse brand settings button
        Then the brand settings section should be expanded
        Then within the brand settings section, I should see the brand image
        Then within the brand settings section, I should see the brand name
        Then within the brand settings section, I should see the brand description

    @regression @edit_brand_name
    Scenario: Edit Brand Name on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I can see the expand brand settings button
        When I tap on the expand brand settings button
        Then the brand settings section should be expanded
        Then I can see the original brand name
        When I tap on the Brand Name field
        Then I enter a new brand name
        Then I tap the confirm edit button
        Then the brand name should be updated successfully
        
    @regression @edit_brand_description
    Scenario: Edit Brand Description on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I can see the expand brand settings button
        When I tap on the expand brand settings button
        Then the brand settings section should be expanded
        Then I can see the original brand description
        When I tap on the Brand Description field
        Then I enter a new brand description
        Then I tap the confirm edit button
        Then the brand description should be updated successfully

    @regression @navigate_to_plan_management
    Scenario: Navigate to Plan Management Page from Branch Settings
        Given I am on the Branch Settings page
        When I tap on the Branch Information option section's Branch Purchase Plan
        Then I should be navigated to the Plan Management page

    @regression @check_plan_management_layout
    Scenario: Check Layout of Plan Management Page
        Given I am on the Plan Management page
        Then I should see the header with text "Plan Management"
        Then I should see a Back to Hotcake APP button
        Then I should see the Branch Information section
        Then within the Branch Information section, I should see the Branch Image
        Then within the Branch Information section, I should see the Branch Name
        Then within the Branch Information section, I should see the Brand Name
        Then within the Branch Information section, I should see the Hotcake Coins
        Then within the Branch Information section, I should see the Credit Card
        Then within the Branch Information section, I should see the Invoice Information
        Then I should see the Current Plan section
        Then within the Current Plan section, I should see the current plan details
        Then within the Current Plan section, I should see the Payment Records

    @regression @check_hotcake_coins_display
    Scenario: Check Hotcake Coins Display on Plan Management Page
        Given I am on the Plan Management page
        Then I should see the Branch Information section
        Then within the Branch Information section, I should see the Hotcake Coins title
        Then within the Branch Information section, I should see the current amount of Hotcake Coins

    @regression @navigate_to_hotcake_coins_page
    Scenario: Navigate to Hotcake Coins Page from Plan Management
        Given I am on the Plan Management page
        When I tap on the Hotcake Coins section
        Then I should be navigated to the Hotcake Coins page

    @regression @check_hotcake_coins_layout
    Scenario: Check Layout of Hotcake Coins Page
        Given I am on the Hotcake Coins page
        Then I should see a close button
        Then I should see the header with text "Hotcake Coins"
        Then I should see the Current Hotcake Coins Balance
        Then I should see the Hotcake Coins Usage Tip
        Then I should see the History Records section

    @regression @close_hotcake_coins_page
    Scenario: Close Hotcake Coins Page and Return to Plan Management
        Given I am on the Hotcake Coins page
        When I tap on the close button
        Then I should be navigated back to the Plan Management page

    @regression @check_credit_card_display
    Scenario: Check Credit Card Display on Plan Management Page
        Given I am on the Plan Management page
        Then I should see the Branch Information section
        Then within the Branch Information section, I should see the Credit Card title
        Then within the Branch Information section, I should see the Credit Card binding status

    @regression @navigate_to_credit_card_page
    Scenario: Navigate to Credit Card Page when Card is Not Bound
        Given I am on the Plan Management page
        And the Credit Card is not bound
        When I tap on the Credit Card section
        Then I should be navigated to the Credit Card page
        # Note: Currently only testing unbound credit card state, bound state testing is not needed at this time

    @regression @check_credit_card_layout
    Scenario: Check Layout of Credit Card Page
        Given I am on the Credit Card page
        Then I should see a close button
        Then I should see the header with text "Credit Card"
        Then I should see a confirm button that is disabled
        Then I should see the Cardholder Name field
        Then I should see the Mobile Number field
        Then I should see the Email Address field
        Then I should see the Credit Card Number field
        Then I should see the Expiration Date field
        Then I should see the CVV field
        Then I should see the TapPay logo
        Then I should see the hint text

    @regression @validate_credit_card_required_fields
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

    @regression @close_credit_card_page
    Scenario: Close Credit Card Page and Return to Plan Management
        Given I am on the Credit Card page
        When I tap on the close button
        Then I should be navigated back to the Plan Management page

    @regression @navigate_to_invoice_information
    Scenario: Navigate to Invoice Information Page from Plan Management
        Given I am on the Plan Management page
        When I tap on the Invoice Information section
        Then I should be navigated to the Invoice Information page

    @regression @detailed_personal_invoice_layout
    Scenario: Verify Personal Invoice Information Layout Details
        Given I am on the Invoice Information page
        Then I should see a close button
        Then I should see the header with text "Invoice Information"
        Then I should see a confirm button
        Then I should see the Invoice Type section
        When I tap on the Invoice Type section
        Then I should see the Invoice Type Popup
        Then I should see the header with text "Invoice Type" in the popup
        Then I should see "Personal" option in the popup
        Then I should see "Company" option in the popup
        When I tap on "Personal" option in the popup
        Then I should see the Invoice Type set to "Personal"
        Then I should see the Billing Email Address field
        Then I should see a confirm button that is enabled

    @regression @detailed_company_invoice_layout
    Scenario: Verify Company Invoice Information Layout Details
        Given I am on the Invoice Information page
        Then I should see a close button
        Then I should see the header with text "Invoice Information"
        Then I should see a confirm button
        Then I should see the Invoice Type section
        When I tap on the Invoice Type section
        Then I should see the Invoice Type Popup
        Then I should see the header with text "Invoice Type" in the popup
        Then I should see "Personal" option in the popup
        Then I should see "Company" option in the popup
        When I tap on "Company" option in the popup
        Then I should see the Invoice Type set to "Company"
        Then I should see the Unified Business Number field
        Then I should see the Company Name (Invoice Title) field
        Then I should see the Billing Contact Email Address field
        Then I should see a confirm button that is enabled





