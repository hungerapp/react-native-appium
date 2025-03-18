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
        And I should see a close button
        And I should see the Branch ID
        And I should see the Branch Information option section
        And within the Branch Information option section, I should see the Branch Name and Branch Purchase Plan
        And I should see the Invitation Code
        And I should see the Operations Management section
        And within the Operations Management section, I should see service personnel, service appointment, item, and third-party tools
        And I should see the Web Layout Management section
        And I should see the Member Apply section
        And the layout should be responsive

    @regression @navigate_to_branch_and_brand_info
    Scenario: Access Branch Information from Branch Settings Page
        Given I am on the Branch Settings page
        When I tap on the Branch Information option section's Branch Name
        Then I should be navigated to the Branch and Brand Information page
        And I can view the list of branches and their details

    @regression @check_branch_and_brand_info_layout
    Scenario: Check Layout of Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        Then I should see the header with text "Branch and Brand Information"
        And I should see a close button
        And I should see a confirm edit button
        And I should see the branch image
        And within the branch image, I should see a camera icon
        And I should see the branch image ratio hint text
        And I should see the branch information section
        And within the branch information section, I should see the branch name
        And within the branch information section, I should see the branch description
        And I should see the branch phone section
        And within the branch phone section, I should see the show branch phone toggle
        And I should see the branch phone
        And I should see the branch address section
        And within the branch address section, I should see the country
        And within the branch address section, I should see the city
        And within the branch address section, I should see the district
        And within the branch address section, I should see the address
        And I should see the expand brand settings button

    @regression @edit_branch_name
    Scenario: Edit Branch Name on Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        And I can see the original branch name
        And I can see branch name title
        When I tap on the Branch Name field
        And I enter a new branch name
        And I tap the confirm edit button
        Then the branch name should be updated successfully