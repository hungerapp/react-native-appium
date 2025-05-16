Feature: Customer Deposit Checkout  
   
   @regression  @successful_deposit_checkout
   Scenario: Successful deposit checkout  
    I want to complete a deposit transaction successfully  
    So that I can verify the deposit process works correctly  

    Given I click the create checkout option
    When I select deposit option  
    And I search for an existing member "0972205690"
    And I click the search result
    And I select a sales performance owner  
    And I enter the deposit amount  
    And I select a payment method and do not make any changes
    And I calculate the change amount
    When I proceed to checkout  
    And I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout



   @regression  @modify_and_clear_deposit_details_before_checkout_with_existing_member
   Scenario: Modify and clear deposit details before checkout with existing member  
    I want to modify and clear deposit details before completing checkout with existing member  
    So that I can ensure the system handles data changes correctly  

    Given I click the create checkout option
    When I select deposit option  
    And I search for an existing member "0972205690"
    And I click the search result
    And I select a sales performance owner  
    And I enter the deposit amount  
    And I delete the member and re-search for an existing member "0972205690"
    And I modify and clear the deposit amount before re-entering it  
    And I modify the sales amount  
    And I select a different payment method and change it below the item price and validate errors  
    And I input checkout record content  
    And I adjust the bonus points using quick select
    When I proceed to checkout  
    And I attempt to sign the signature  
    And I clear the signature  
    Then I confirm the checkout and successfully create a checkout



   @regression  @error_validation_during_deposit_checkout_with_new_member
   Scenario: Error validation during deposit checkout with new member  
    I want to validate error messages when entering incorrect deposit details with new member  
    So that I can verify the system correctly handles invalid inputs  

    Given I click the create checkout option
    When I select deposit option  
    And I add a brand new member
    And I select a sales performance owner  
    And I enter the deposit amount  
    And I select a payment method and change it above the item price and validate errors  
    And I input checkout record content and cancel it 
    And I adjust the total sales performance  
    And I adjust the bonus points using quick select
    When I proceed to checkout  
    And I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout


