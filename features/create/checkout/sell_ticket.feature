Feature: Ticket Checkout Process  

  @regression @sell_ticket_without_payment_adjustment
  Scenario: Checkout a ticket without selecting a payment adjustment  
    I want to complete a ticket checkout without adjusting the payment  
    So that I can verify the default checkout flow  

    Given I click the create checkout option
    When I select sell ticket option  
    Then I search for an existing member  
    Then I select a sales performance owner  
    Then I select a ticket and view the ticket info for sell
    Then I select a payment method without making changes
    Then I calculate the change amount
    Then I proceed to checkout 
    Then I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout

   
  @regression @new_member_modify_payment_method
  Scenario: Checkout a ticket with a new member and modified payment method  
    I want to complete a ticket checkout with a new member and modify the payment  
    So that I can validate the checkout process with changes  

    Given I click the create checkout option
    When I select sell ticket option  
    Then I directly add a new member  
    Then I select a sales performance owner  
    Then I select a ticket and view the ticket info for sell  
    Then I attempt to adjust the item details
    Then I select a payment method and change it below the item price and validate errors
    Then I input checkout record content  
    Then I adjust the total sales performance  
    Then I adjust the bonus points using quick select
    Then I proceed to checkout  
    Then I attempt to sign the signature  
    Then I clear the signature  
    Then I confirm the checkout and successfully create a checkout

 
  @regression @multiple_modifications_and_re_selections
  Scenario: Checkout a ticket with multiple modifications and re-selections  
    I want to complete a ticket checkout with multiple modifications and re-selections  
    So that I can verify the system handles all changes correctly  

    Given I click the create checkout option
    When I select sell ticket option  
    Then I search for an non-existing member and re-search for an existing member
    Then I select a sales performance owner  
    Then I select a ticket and view the ticket info for sell
    Then I clear all selections and reselect them  
    Then I delete the member information and re-add it
    Then I add new discount for the item
    Then I select a payment method and change it above the item price and validate errors
    Then I input checkout record content and cancel it
    Then I adjust the total sales performance  
    Then I adjust the bonus points using quick select
    Then I proceed to checkout  
    Then I attempt to sign the signature  
    Then I clear the signature  
    Then I confirm the checkout and successfully create a checkout
