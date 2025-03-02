Feature: Customer Deposit Checkout  
   
   @regression  @successful_deposit_checkout
   Scenario: Successful deposit checkout  
    I want to complete a deposit transaction successfully  
    So that I can verify the deposit process works correctly  

    Given I click the create checkout option
    When I select deposit option  
    Then I search for an existing member  
    Then I click the search result
    Then I select a sales performance owner  
    Then I enter the deposit amount  
    Then I select a payment method and do not make any changes
    Then I calculate the change amount
    Then I proceed to checkout  
    Then I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout



   @regression  @modify_and_clear_deposit_details_before_checkout
   Scenario: Modify and clear deposit details before checkout  
    I want to modify and clear deposit details before completing checkout  
    So that I can ensure the system handles data changes correctly  

    Given I click the create checkout option
    When I select deposit option  
    Then I add a new member  
    Then I select a sales performance owner  
    Then I enter the deposit amount  
    Then I delete the member and re-add a new one  
    Then I modify and clear the deposit amount before re-entering it  
    Then I modify the sales amount  
    Then I select a different payment method and change it below the item price and validate errors  
    Then I input checkout record content 
    Then I adjust the total sales performance  
    Then I adjust the bonus points using quick select
    Then I proceed to checkout  
    Then I attempt to sign the signature  
    Then I clear the signature  
    Then I confirm the checkout and successfully create a checkout



   @regression  @error_validation_during_deposit_checkout
   Scenario: Error validation during deposit checkout  
    I want to validate error messages when entering incorrect deposit details  
    So that I can verify the system correctly handles invalid inputs  

    Given I click the create checkout option
    When I select deposit option  
    Then I search for an non-existing member and re-search for an existing member
    Then I click the search result
    Then I select a sales performance owner  
    Then I enter the deposit amount  
    Then I select a payment method and change it above the item price and validate errors  
    Then I input checkout record content and cancel it 
    Then I adjust the total sales performance  
    Then I adjust the bonus points using quick select
    Then I proceed to checkout  
    Then I do not sign any signature  
    Then I confirm the checkout and successfully create a checkout


