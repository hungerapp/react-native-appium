Feature: Ticket Checkout Process  

  @regression @sell_ticket_without_payment_adjustment
  Scenario: Checkout a ticket without selecting a payment adjustment  
    I want to complete a ticket checkout without adjusting the payment  
    So that I can verify the default checkout flow  

    Given I click the create checkout option
    When I select sell ticket option  
    And I search for an existing member "0972205690"
    And I click the search result
    And I select a sales performance owner  
    And I select a ticket and view the ticket info for sell
    And I select a payment method without making changes
    And I calculate the change amount
    When I proceed to checkout 
    And I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout

   
  @regression @existing_member_ticket_below_price_payment_adjustment
  Scenario: Checkout a ticket with existing member and below item price payment adjustment  
    I want to complete a ticket checkout with existing member and below item price payment adjustment  
    So that I can validate the checkout process with changes  

    Given I click the create checkout option
    When I select sell ticket option  
    And I directly search for an existing member "0972205690"
    And I click the search result
    And I select a sales performance owner
    And I select a ticket and view the ticket info for sell  
    And I attempt to adjust the item details
    And I select a payment method and change it below the item price and validate errors
    And I input checkout record content  
    And I adjust the total sales performance  
    And I adjust the bonus points using quick select
    When I proceed to checkout  
    And I attempt to sign the signature  
    And I clear the signature
    And I attempt to sign the signature again
    Then I confirm the checkout and successfully create a checkout

 
  @regression @new_member_above_ticket_price_payment_adjustment_and_multiple_modifications
  Scenario: Checkout a ticket with new member and above item price payment adjustment and multiple modifications  
    I want to complete a ticket checkout with new member and above item price payment adjustment and multiple modifications  
    So that I can verify the system handles all changes correctly  

    Given I click the create checkout option
    When I select sell ticket option  
    And I add a brand new member
    And I select a sales performance owner  
    And I select a ticket and view the ticket info for sell
    And I clear all selections and reselect them  
    And I delete the member information and re-add new member
    And I add new discount for the item
    And I select a payment method and change it above the item price and validate errors
    And I input checkout record content and cancel it
    And I adjust the total sales performance  
    And I adjust the bonus points using quick select
    When I proceed to checkout  
    And I attempt to sign the signature  
    And I clear the signature  
    Then I confirm the checkout and successfully create a checkout
