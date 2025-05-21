from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.item import ItemPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../features/navigation/setting/item.feature')

# Scenario: Navigate to Item Management
@given("I am on the branch settings page")
def on_branch_settings_page(driver):
    item_page = ItemPage(driver)
    assert item_page.verify_branch_settings_page(), "Branch settings page is not displayed"

@when("I tap on the Item")
def tap_on_item(driver):
    item_page = ItemPage(driver)
    assert item_page.tap_on_item(), "Failed to tap on Item"

@then("I should see the item page")
def see_item_page(driver):
    item_page = ItemPage(driver)
    assert item_page.verify_item_page(), "Item page is not displayed"

# Scenario: Item List Setting
@given("I am on the item page")
def on_item_page(driver):
    item_page = ItemPage(driver)
    assert item_page.verify_item_page(), "Item page is not displayed"

@when("I tap on the Item in the item page")
def tap_on_item_in_item_page(driver):
    item_page = ItemPage(driver)
    assert item_page.tap_on_item_in_item_page(), "Failed to tap on Item in item page"

@when("I delete all item category")
def delete_all_item_category(driver):
    item_page = ItemPage(driver)
    assert item_page.delete_item_category(delete_all = True), "Failed to delete all item category"

@when(parsers.parse('I add a new item category to "{category_name}"'))
def add_item_category(driver, category_name):
    item_page = ItemPage(driver)
    category_name = CommonUseSection.replace_current_datetime(category_name)
    assert item_page.add_item_category(category_name), f"Failed to add item category {category_name}"

@when(parsers.parse('I edit the item category to "{old_category_name}" to "{new_category_name}"'))
def edit_item_category(driver, old_category_name, new_category_name):
    old_category_name = CommonUseSection.replace_current_datetime(old_category_name)
    new_category_name = CommonUseSection.replace_current_datetime(new_category_name)
    item_page = ItemPage(driver)
    assert item_page.edit_item_category(old_category_name, new_category_name), f"Failed to edit item category {old_category_name} to {new_category_name}"

@when(parsers.parse('I delete the item category "{category_name}"'))
def delete_item_category(driver, category_name):
    category_name = CommonUseSection.replace_current_datetime(category_name)
    item_page = ItemPage(driver)
    assert item_page.delete_item_category(category_name), f"Failed to delete item category {category_name}"

@when(parsers.parse('I add a new item to "{item_category_name}" "{item_name}" "{item_introduction}" "{item_sale_price}" "{item_cost_price}"'))
def add_item(driver, item_category_name, item_name, item_introduction, item_sale_price, item_cost_price):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    item_introduction = CommonUseSection.replace_current_datetime(item_introduction)
    item_sale_price = CommonUseSection.replace_current_datetime(item_sale_price)
    item_cost_price = CommonUseSection.replace_current_datetime(item_cost_price)
    item_page = ItemPage(driver)
    assert item_page.add_item(item_category_name, item_name, item_introduction, item_sale_price, item_cost_price), f"Failed to add new item {item_name}"

@when("I delete all item")
def delete_all_item(driver):
    item_page = ItemPage(driver)
    assert item_page.delete_item(delete_all = True), "Failed to delete all item"

@when(parsers.parse('I copy the item to "{item_category_name}" "{item_name}"'))
def copy_item(driver, item_category_name, item_name):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    item_page = ItemPage(driver)
    assert item_page.copy_item(item_category_name, item_name), f"Failed to copy item {item_name}"

@when(parsers.parse('I delete the item to "{item_category_name}" "{item_name}"'))
def delete_item(driver, item_category_name, item_name):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    item_page = ItemPage(driver)
    assert item_page.delete_item(item_category_name, item_name), f"Failed to delete item {item_name}"

@when(parsers.parse('I edit the item to "{item_category_name}" "{old_item_name}" to "{new_item_name}" "{item_introduction}" "{item_sale_price}" "{item_internal_price}"'))
def edit_item(driver, item_category_name, old_item_name, new_item_name, item_introduction, item_sale_price, item_internal_price):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    old_item_name = CommonUseSection.replace_current_datetime(old_item_name)
    new_item_name = CommonUseSection.replace_current_datetime(new_item_name)
    item_introduction = CommonUseSection.replace_current_datetime(item_introduction)
    item_page = ItemPage(driver)
    assert item_page.edit_item(item_category_name, old_item_name, new_item_name, item_introduction, item_sale_price, item_internal_price), f"Failed to edit item {old_item_name} to {new_item_name}"

@when("I tap on the close button in the item list page")
def tap_on_close_button_in_item_list_page(driver):
    item_page = ItemPage(driver)
    assert item_page.tap_on_close_button_in_item_list_page(), "Failed to tap on close button in item list page"

@then("I should see the item page")
def see_item_page(driver):
    item_page = ItemPage(driver)
    assert item_page.verify_item_page(), "Item page is not displayed"




# Scenario: Inventory Setting
@given("I am on the item page")
def on_item_page(driver):
    item_page = ItemPage(driver)
    assert item_page.verify_item_page(), "Item page is not displayed"

@given(parsers.parse('I have an item "{item_category_name}" "{item_name}" "{item_introduction}" "{item_sale_price}" "{item_cost_price}"'))
def have_item(driver, item_category_name, item_name, item_introduction, item_sale_price, item_cost_price):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    item_introduction = CommonUseSection.replace_current_datetime(item_introduction)
    item_sale_price = CommonUseSection.replace_current_datetime(item_sale_price)
    item_cost_price = CommonUseSection.replace_current_datetime(item_cost_price)
    item_page = ItemPage(driver)
    assert item_page.verify_item(item_category_name, item_name, item_introduction, item_sale_price, item_cost_price), f"Failed to add new item {item_name}"

@when("I tap on the Inventory in the item page")
def tap_on_inventory_in_item_page(driver):
    item_page = ItemPage(driver)
    assert item_page.tap_on_inventory_in_item_page(), "Failed to tap on Inventory in item page"

@when("I reset all inventory")
def reset_all_inventory(driver):
    item_page = ItemPage(driver)
    assert item_page.reset_all_inventory(), "Failed to reset all inventory"

@when(parsers.parse('I add a new inventory to "{item_category_name}" "{item_name}" "{date}" "{quantity}" "{cost_price}"'))
def add_inventory(driver, item_category_name, item_name, date, quantity, cost_price):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    date = CommonUseSection.replace_current_datetime(date)
    quantity = CommonUseSection.replace_current_datetime(quantity)
    cost_price = CommonUseSection.replace_current_datetime(cost_price)
    item_page = ItemPage(driver)
    assert item_page.add_inventory(item_category_name, item_name, date, quantity, cost_price), f"Failed to add inventory {add_inventory} to {item_name}"

@when(parsers.parse('I set safety stock to "{item_category_name}" "{item_name}" "{safety_stock_num}"'))
def set_safety_stock(driver, item_category_name, item_name, safety_stock_num):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    safety_stock_num = CommonUseSection.replace_current_datetime(safety_stock_num)
    item_page = ItemPage(driver)
    assert item_page.set_safety_stock(item_category_name, item_name, safety_stock_num), f"Failed to set safety stock {safety_stock_num} to {item_name}"

@when(parsers.parse('I return the inventory to "{item_category_name}" "{item_name}" "{date}" "{quantity}"'))
def return_inventory(driver, item_category_name, item_name, date, quantity):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    date = CommonUseSection.replace_current_datetime(date)
    item_page = ItemPage(driver)
    assert item_page.return_inventory(item_category_name, item_name, date, quantity), f"Failed to return inventory {item_name} to {date}"

@when(parsers.parse('I see the inventory record to "{inventory_operation}" "{item_category_name}" "{item_name}" "{quantity}" "{cost_price}"'))
def inventory_record(driver, inventory_operation, item_category_name, item_name, quantity, cost_price):
    item_category_name = CommonUseSection.replace_current_datetime(item_category_name)
    item_name = CommonUseSection.replace_current_datetime(item_name)
    quantity = CommonUseSection.replace_current_datetime(quantity)
    cost_price = CommonUseSection.replace_current_datetime(cost_price)
    item_page = ItemPage(driver)
    assert item_page.inventory_record(inventory_operation, item_category_name, item_name, quantity, cost_price), f"Failed to see inventory record {inventory_operation} {item_name}"

@when("I tap on the close button in the inventory page")
def tap_on_close_button_in_inventory_page(driver):
    item_page = ItemPage(driver)
    assert item_page.tap_on_close_button_in_inventory_page(), "Failed to tap on close button in inventory page"

@when("I tap on the back button in the item page")
def tap_on_back_button_in_item_page(driver):
    item_page = ItemPage(driver)
    assert item_page.tap_on_back_button_in_item_page(), "Failed to tap on back button in item page"

@then("I should see the Branch Settings page")
def verify_branch_settings_page_after_close(driver):
    item_page = ItemPage(driver)
    assert item_page.verify_branch_settings_page(), "Branch Settings page not found"