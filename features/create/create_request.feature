Feature: Create Request

  As a user
  I want to request an item
  So I can successfully complete the request process

  @regression @request_items_without_signing
  Scenario: Request items without signing
    Given I click the create request option    
    When I select a requester  
    Then I select an item  
    Then I request the item without signing  
    Then I confirm the request and successfully create a request  

  @regression @modify_request_details_before_confirming
  Scenario: Modify request details before confirming
    Given I click the create request option   
    When I select a requester  
    Then I select an item  
    Then I change the requester  
    When I clear all selected items  
    Then I reselect items  
    Then I update the items amount  
    Then I update the items quantity  
    Then I remove an item  
    Then I sign for the request  
    Then I clear the signature and resign  
    Then I confirm the request and successfully create a request  


