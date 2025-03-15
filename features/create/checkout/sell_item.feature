Feature: Sell Item Checkout Process  

  @regression @no_member_no_signature
  Scenario: Checkout without selecting a member and without signing  
    I want to complete a checkout without selecting a member and without signing  
    So that I can verify the checkout flow when no member is chosen  

    Given I click the create checkout option
    When I select sell item option  
    Then I select a sales performance owner  
    Then I select an item and view the item info
    Then I do not select a member  
    Then I choose a payment method without making adjustments  
    Then I proceed to checkout  
    Then I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout


  @regression @item_below_price_and_payment_adjustment
  Scenario: Checkout with existing member and  below item price payment adjustment validation  
    I want to complete a checkout with an existing member and validate payment adjustments  
    So that I can verify the behavior when modifying payment options  

    Given I click the create checkout option
    When I select sell item option  
    Then I select a sales performance owner  
    Then I select an item and view the item info
    Then I search non-existing member then re-search for an existing member
    Then I click search result
    When I clear all selected items
    Then I reselect items
    Then I adjust the item  
    Then I select a payment method below the item price and validate errors  
    Then I input checkout record content
    Then I adjust the total sales performance  
    Then I adjust the bonus points  
    Then I proceed to checkout  
    Then I attempt to sign the signature  
    Then I clear the signature  
    Then I confirm the checkout and successfully create a checkout



  @regression @item_above_price_payment_adjustment
  Scenario: Checkout with above item price payment adjustment validation  
    I want to complete a checkout validate payment adjustments  
    So that I can verify the behavior when adding a new member  

    Given I click the create checkout option
    When I select sell item option  
    Then I select a sales performance owner  
    Then I select an item and view the item info
    Then I select a member and search for an existing member
    Then I delete the selected member and re-add it
    Then I click the search result
    Then I add new discount for the item
    Then I select a payment method above the item price and validate errors
    Then I calculate the change amount
    Then I input checkout record content and cancel it  
    Then I adjust the total sales performance  
    Then I adjust the bonus points  
    Then I proceed to checkout  
    Then I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout



