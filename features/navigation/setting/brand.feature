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