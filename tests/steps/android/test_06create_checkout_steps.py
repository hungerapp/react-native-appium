import allure
import pytest

from pytest_bdd import scenarios, given, when, then
from pages.android.create.create_checkout_page import CreateCheckoutPage


scenarios('../../../features/create/checkout/sell_item.feature')
scenarios('../../../features/create/checkout/sell_ticket.feature')
scenarios('../../../features/create/checkout/deposit.feature')

# TEST DATA
TEST_INVALID_PHONE_NUMBER = "99999999999999999"
TEST_VALID_PHONE_NUMBER = "0972205690"

# general sell item 
@allure.feature('Create Checkout')
@allure.story('Sell Item')
@pytest.mark.run(order=35)
@pytest.mark.create_checkout
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
@pytest.mark.run(order=36)
@pytest.mark.create_checkout
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

@then('I search non-existing member then re-search for an existing member')
def search_members(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.non_selected_member_section()
    checkout_page.search_non_existing_member(TEST_INVALID_PHONE_NUMBER)
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)
    
@then('I click search result')
def click_search_result(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_search_result()
    
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
    checkout_page.adjust_item(existing_member=True)

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
@pytest.mark.run(order=37)
@pytest.mark.create_checkout
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

@then('I click the non-selected member section and add a brand new member')
def add_new_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_non_selected_member_section()
    checkout_page.add_new_member()
    
@then('I delete the member information and re-add it')
def delete_and_readd_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.delete_selected_member()
    checkout_page.add_new_member()
 
@then('I add new discount for the item')
def add_new_discount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.add_new_discount(existing_member=False)

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
    
    
########## Sell Ticket ##########

# General Sell Ticket without selecting a payment adjustment
@allure.feature('Create Checkout with sell ticket')
@allure.story('Sell Ticket without payment adjustment')
@pytest.mark.run(order=38)
@pytest.mark.create_checkout
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select sell ticket option')
def select_sell_ticket(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sell_ticket()

@then('I search for an existing member')
def search_existing_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)
    
@then('I click the search result')
def click_search_result(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_search_result()


@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner()

@then('I select a ticket and view the ticket info for sell')
def select_ticket(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_ticket()

@then('I select a payment method without making changes')
def select_payment_method(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_method()
    
@then('I calculate the change amount')
def calculate_change_amount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.calculate_change_amount()

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
    
    
    

# Checkout a ticket with existing member and below item price payment adjustment
@allure.feature('Create Checkout with sell ticket')
@allure.story('Checkout a ticket with existing member and below item price payment adjustment')
@pytest.mark.run(order=39)
@pytest.mark.create_checkout
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select sell ticket option')
def select_sell_ticket(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sell_ticket()

@then('I directly search for an existing member')
def search_existing_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)

@then('I click the search result')
def click_search_result(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_search_result()

@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner()
    
@then('I select a ticket and view the ticket info for sell')
def select_ticket(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_ticket()
    
@then('I attempt to adjust the item details')
def adjust_item_details(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.ticket_section()
    checkout_page.adjust_item(existing_member=True)

@then('I select a payment method and change it below the item price and validate errors')
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

@then('I adjust the bonus points using quick select')
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
    
@then('I confirm the checkout and successfully create a checkout')
def confirm_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.confirm_checkout()
    
    


# Checkout a ticket with new member and above item price payment adjustment
@allure.feature('Create Checkout with sell ticket')
@allure.story('Checkout a ticket with new member and above item price payment adjustment')
@pytest.mark.run(order=40)
@pytest.mark.create_checkout
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select sell ticket option')
def select_sell_ticket(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sell_ticket()
    
@then('I add a brand new member')
def add_new_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.add_new_member()
    
@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner()

@then('I select a ticket and view the ticket info for sell')
def select_two_tickets(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_ticket()
    
@then('I clear all selections and reselect them')
def clear_and_reselect_tickets(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.clear_all_tickets()
    checkout_page.select_ticket()
    checkout_page.adjust_item()

@then('I delete the member information and re-add new member')
def delete_and_add_new_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.delete_selected_member()
    checkout_page.click_non_selected_member_section()
    checkout_page.add_new_member()
    
    
@then('I add new discount for the item')
def add_new_discount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.add_new_discount(existing_member=False)

@then('I select a payment method and change it above the item price and validate errors')
def select_payment_above_price(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_with_price_adjustment(is_above_price=True)

@then('I input checkout record content and cancel it')
def input_and_cancel_record(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.cancel_record_content()

@then('I adjust the total sales performance')
def adjust_sales_performance(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.adjust_sales_performance()

@then('I adjust the bonus points using quick select')
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

@then('I confirm the checkout and successfully create a checkout')
def confirm_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.confirm_checkout()
    
    
    
########## Deposit ##########

# Deposit Checkout
@allure.feature('Create Checkout')
@allure.story('Successful Deposit Checkout')
@pytest.mark.run(order=41)
@pytest.mark.create_checkout
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select deposit option')
def select_deposit_option(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_deposit()

@then('I search for an existing member')
def search_existing_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)
    
@then('I click the search result')
def click_search_result(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_search_result()

@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner()

@then('I enter the deposit amount')
def enter_deposit_amount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.enter_deposit_amount()

@then('I select a payment method and do not make any changes')
def select_payment_no_changes(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_method()
    
@then('I calculate the change amount')
def calculate_change_amount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.calculate_change_amount()

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
    
    

# Modify and clear deposit details before checkout
@allure.feature('Create Checkout')
@allure.story('Modify and Clear Deposit Details')
@pytest.mark.run(order=42)
@pytest.mark.create_checkout
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select deposit option')
def select_deposit_option(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_deposit()

@then('I search for an existing member')
def search_existing_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)
    
@then('I click the search result')
def click_search_result(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_search_result()

@then('I delete the member and re-search for an existing member')
def delete_and_add_new_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.delete_selected_member()
    checkout_page.search_existing_member(TEST_VALID_PHONE_NUMBER)
    checkout_page.click_search_result()
    
@then('I modify and clear the deposit amount before re-entering it')
def modify_clear_reenter_deposit(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.edit_deposit_amount()
    
@then('I modify the sales amount')
def modify_sales_amount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.edit_sales_amount()

@then('I select a different payment method and change it below the item price and validate errors')
def select_different_payment_below_price(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_with_price_adjustment(is_above_price=False)

@then('I input checkout record content')
def input_record_content(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.input_record_content()


@then('I adjust the bonus points using quick select')
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
    
@then('I confirm the checkout and successfully create a checkout')
def confirm_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.confirm_checkout()
    
    

# Error validation during deposit checkout
@allure.feature('Create Checkout')
@allure.story('Error Validation During Deposit')
@pytest.mark.run(order=43)
@pytest.mark.create_checkout
@given('I click the create checkout option')
def click_create_checkout(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.click_create_checkout()

@when('I select deposit option')
def select_deposit_option(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_deposit()

@then('I add a brand new member')
def add_new_member(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.add_new_member()

@then('I select a sales performance owner')
def select_sales_owner(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_sales_owner()

@then('I enter the deposit amount') 
def enter_deposit_amount(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.enter_deposit_amount()

@then('I select a payment method and change it above the item price and validate errors')
def select_payment_above_price(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.select_payment_with_price_adjustment(is_above_price=True)

@then('I input checkout record content and cancel it')
def input_and_cancel_record(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.cancel_record_content()

@then('I adjust the total sales performance')
def adjust_sales_performance(driver):
    checkout_page = CreateCheckoutPage(driver)
    checkout_page.adjust_sales_performance()

@then('I adjust the bonus points using quick select')
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
