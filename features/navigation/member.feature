Feature: Member Page

  @regression @member_management
  Scenario: Manage member and page functionality
    Given I click on the member option in the bottom navigation bar
    When I click any member below the tab
    Then I should be navigated to the member passport page
    When I add a new member
    Then I should be able to create a new member
    When I apply member filters
    Then I can see the filtered results
    When I check the scheduling records
    Then I can see the scheduling records



  @regression @search_tags_billing
  Scenario: Search and passport tags and billing
    Given I am on the member page
    When I tap the search button
    Then I search for a valid phone number and see the search result
    Then I tap on the search result
    When I click more icon in bottom navigation bar and select member tags
    Then I can modify tag setting
    When I click on the member custom tags setting
    Then I can add, edit, or delete a custom tag
    Then I successfully change the custom tag and return to the member passport page
    When I tap on the billing tab
    Then I can view details and export details file
    When I tap view checkout
    Then I can delete the billing record
               

  # 儲值金
  @regression @top_up_balance
  Scenario: Edit member top-up balance
    Given I am on the member passport page
    When I click on the Top-up Balance section
    Then I can edit the top-up amount
    When I click the Top-up button
    Then I can finish the top-up process
    Then I return to the Member Passport page

  @regression @bonus_points
  Scenario: Edit Bonus Points
    Given I am on the member passport page
    When I click on the bonus points section
    Then I can edit the bonus points
    Then I return to the member passport page


  @regression @edit_tickets
  Scenario: Edit tickets
    Given I am on the member passport page
    When I click on the tickets section
    Then I click the Sell ticket button
    Then I can select a performance personnel
    Then I can choose a ticket type for sale
    Then I can finish the checkout process



  @regression @use_tickets
  Scenario: Use and gift a ticket from the ticket page
    Given I am on the ticket page
    When I tap on a ticket under owned tickets tab
    Then I can use the selected ticket
    Then I switches to history tab
    When I click the gift ticket button
    Then I can select the tickets for sending
    Then I return to member passport page

  @regression @edit_member_info
  Scenario: Edit member info in member passport page
    Given I am on the member passport page
    Then I can edit the basic information
    Then I can edit the custom fields
    Then I can edit the member description

  @regression @message_review
  Scenario: Bottom navigation functionality
    Given I am on the member passport page
    #先註解掉
    #When I click on the message icon
    #Then I can enter send message page
    #When I click on the sign document icon
    #Then I can sign the review document
    When I click on the review member icon
    Then I can view member review
    When I click on the more icon
    Then I can link account and send line message
    Then I cam successfully click back to member passport page


  @regression @modify_checkout
  Scenario: Modify checkout and re-checkout
    When I add member to blacklist
    Then I can remove member from blacklist
    When I tap on the billing tab
    Then I tap view checkout
    Then I can delete and reprocess the checkout
    Then I can choose the item I have bought before
    Then I can finish the checkout process
    Then I return to the calendar page
  
