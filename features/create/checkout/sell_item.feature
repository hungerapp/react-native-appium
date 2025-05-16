Feature: Sell Item Checkout Process  

  @regression @no_member_no_signature
  Scenario: Checkout without selecting a member and without signing  
    I want to complete a checkout without selecting a member and without signing  
    So that I can verify the checkout flow when no member is chosen  

    Given I click the create checkout option
    When I select sell item option  
    And I select a sales performance owner  
    And I select an item and view the item info
    And I do not select a member  
    And I choose a payment method without making adjustments  
    And I proceed to checkout  
    And I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout


  @regression @existing_member_item_below_price_and_payment_adjustment
  Scenario: Checkout with existing member and  below item price payment adjustment validation  
    I want to complete a checkout with an existing member and validate payment adjustments  
    So that I can verify the behavior when modifying payment options  

    Given I click the create checkout option
    When I select sell item option  
    And I select a sales performance owner  
    And I select an item and view the item info
    And I search non-existing member "99999999999999999" then re-search for an existing member "0972205690"
    And I click search result
    When I clear all selected items
    And I reselect items
    And I adjust the item  
    And I select a payment method below the item price and validate errors  
    And I input checkout record content
    And I adjust the total sales performance  
    And I adjust the bonus points  
    When I proceed to checkout  
    And I attempt to sign the signature  
    And I clear the signature
    And I attempt to sign the signature again
    Then I confirm the checkout and successfully create a checkout



  @regression @new_member_item_above_price_payment_adjustment
  Scenario: Checkout with new member and above item price payment adjustment validation  
    I want to complete a checkout validate payment adjustments  
    So that I can verify the behavior when adding a new member  

    Given I click the create checkout option
    When I select sell item option  
    And I select a sales performance owner  
    And I select an item and view the item info
    And I click the non-selected member section and add a brand new member
    And I delete the member information and re-add it
    And I add new discount for the item
    And I select a payment method above the item price and validate errors
    And I calculate the change amount
    And I input checkout record content and cancel it  
    And I adjust the total sales performance  
    And I adjust the bonus points  
    When I proceed to checkout  
    And I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout



