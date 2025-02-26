import allure
import pytest

from pytest_bdd import scenarios, given, when, then
from pages.android.create.create_checkout_page import CreateCheckoutPage


scenarios('../../../features/create/checkout/sell_item.feature')


# TEST DATA
TEST_INVALID_PHONE_NUMBER = "99999999999999999"
TEST_VALID_PHONE_NUMBER = "0972205690"

# general sell item 
@allure.feature('Create Checkout')
@allure.story('Sell Item')
@pytest.mark.run(order=34)
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()
    
@when('I select sell item option')
def select_sell_item(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sell_item()

@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner(is_performance_change=False)

@then('I select an item and view the item info')
def select_item(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_item()


@then('I do not select a member')
def skip_member_selection(driver):
    pass

@then('I choose a payment method without making adjustments')
def select_payment_method(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_method()

@then('I proceed to checkout')
def proceed_to_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.proceed_to_checkout()

@then('I do not sign any signature')
def skip_signature(driver):
    pass

@then('I confirm the checkout and successfully create a checkout')
def confirm_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.confirm_checkout()



# sell item with existing member and payment adjustment validation
@allure.feature('Create Checkout')
@allure.story('Sell Item with existing member and payment adjustment validation')
@pytest.mark.run(order=35)
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select sell item option')
def select_sell_item(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sell_item()

@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner()

@then('I select an item and view the item info')
def select_and_view_item(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_item()

@then('I search for an non-existing member and re-search for an existing member')
def search_members(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.search_non_existing_member(TEST_INVALID_PHONE_NUMBER)
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)
    
@when('I clear all selected items')
def clear_items(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.clear_all_items()

@then('I reselect items')
def reselect_items(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_item()

@then('I adjust the item')
def adjust_item(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.adjust_item()

@then('I select a payment method below the item price and validate errors')
def select_payment_below_price(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_with_price_adjustment(is_above_price=False)

@then('I input checkout record content')
def input_record_content(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.input_record_content()

@then('I adjust the total sales performance')
def adjust_sales_performance(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.adjust_sales_performance()

@then('I adjust the bonus points')
def adjust_bonus_points(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.adjust_bonus_points()

@then('I proceed to checkout')
def proceed_to_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.proceed_to_checkout()

@then('I attempt to sign the signature')
def sign_signature(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.sign_request()

@then('I clear the signature')
def clear_signature(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.clear_signature()
    
@then('I attempt to sign the signature again')
def sign_signature_again(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.sign_request()

@then('I confirm the checkout and successfully create a checkout')
def confirm_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.confirm_checkout()
    
    
    

# sell item with new member and payment adjustment validation
@allure.feature('Create Checkout')
@allure.story('Checkout with new member and payment adjustment validation')
@pytest.mark.run(order=36)
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select sell item option')
def select_sell_item(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sell_item()

@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner()

@then('I select an item and view the item info')
def select_and_view_item(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_item()

@then('I add a new member')
def add_new_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.add_new_member()
    checkout_page.select_sales_owner()

@then('I delete the selected member and re-add it')
def delete_and_readd_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.delete_selected_member()
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)
 
@then('I add new discount for the item')
def add_new_discount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.add_new_discount()

@then('I select a payment method above the item price and validate errors')
def select_payment_above_price(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_with_price_adjustment(is_above_price=True)

@then('I calculate the change amount')
def calculate_change_amount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.calculate_change_amount()

@then('I input checkout record content and cancel it')
def input_and_cancel_record(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.cancel_record_content()

@then('I adjust the total sales performance')
def adjust_sales_performance(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.adjust_sales_performance()

@then('I adjust the bonus points')
def adjust_bonus_points(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.adjust_bonus_points()

@then('I proceed to checkout')
def proceed_to_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.proceed_to_checkout()

@then('I do not sign any signature')
def skip_signature(driver):
    pass

@then('I confirm the checkout and successfully create a checkout')
def confirm_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.confirm_checkout()


# Sell Ticket
