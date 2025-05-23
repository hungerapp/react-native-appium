Feature: Inventory
  
  # [INVENTORY]
  @regression @inventory_management_in_more @navigate_more @navigate @navigate_more_inventory
  Scenario: Manage Inventory for Automated Test Products
    Given I tap on inventory management
    When I tap on the products tab
    Then I can add inventory
    Then I can set a safety stock level
    Then I can process a return-to-warehouse action
    Then I can view the inventory records
    Then I can return to the calendar page

  