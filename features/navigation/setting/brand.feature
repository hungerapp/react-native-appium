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