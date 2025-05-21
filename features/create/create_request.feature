Feature: Create Request

  As a user
  I want to request an item
  So I can successfully complete the request process

  @regression @request_items_without_signing @create_request @create @create_create_request
  Scenario: Request items without signing
    Given I click the create request option    
    When I select a requester  
    And I select an item  
    And I request the item without signing  
    Then I confirm the request and successfully create a request  

  @regression @modify_request_details_before_confirming @create_request @create @create_create_request
  Scenario: Modify request details before confirming
    Given I click the create request option   
    When I select a requester  
    And I select an item  
    And I change the requester  
    When I clear all selected items  
    And I reselect items  
    And I update the items amount  
    And I update the items quantity  
    And I remove an item  
    And I sign for the request  
    And I clear the signature and resign  
    Then I confirm the request and successfully create a request  


