import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.inventory import InventoryPage

scenarios('../../../features/navigation/more/inventory.feature')

# TEST DATA



# [INVENTORY]
@allure.feature('Inventory More')
@allure.story('Inventory Management')
@pytest.mark.navigation
@pytest.mark.run(order=84)
@given('I tap on inventory management')
def tap_on_inventory_management(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.tap_inventory_management() 
    
@when('I tap on the products tab')
def tap_on_products_tab(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.tap_products_tab()
    
@then('I can add inventory')
def add_inventory(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.add_inventory()
    
@then('I can set a safety stock level')
def set_safety_stock_level(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.set_safety_stock_level()
    
@then('I can process a return-to-warehouse action')
def process_return_to_warehouse_action(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.process_return_to_warehouse_action()
    
    
@then('I can view the inventory records')
def view_inventory_records(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.view_inventory_records()
    
    
@then('I can return to the calendar page')
def return_to_calendar(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.return_to_calendar()
    
    
