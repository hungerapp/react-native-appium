import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.deposit import DepositPage

scenarios('../../../features/navigation/more/deposit.feature')

# TEST DATA



@allure.feature('Deposit More')
@allure.story('Deposit Management')
@pytest.mark.navigation
@pytest.mark.run(order=83)
@given('I tap on deposit')
def tap_on_deposit(driver):
    deposit_page = DepositPage(driver)
    deposit_page.tap_deposit()
    
@when('I tap on the unpaid tab')
def tap_on_unpaid_tab(driver):
    deposit_page = DepositPage(driver)
    deposit_page.tap_unpaid_tab()
    
@then('I can edit the deposit amount')
def edit_deposit_amount(driver):
    deposit_page = DepositPage(driver)
    deposit_page.edit_deposit_amount()
    
@then('I can tap on confirm payment, do not collect, or cancel appointment')
def tap_on_confirm_payment_do_not_collect_or_cancel_appointment(driver):
    deposit_page = DepositPage(driver)
    deposit_page.handle_payment()
    
@when('I tap on the paid tab')
def tap_on_paid_tab(driver):
    deposit_page = DepositPage(driver)
    deposit_page.tap_paid_tab()
    
@then('I can tap on any paid invoice')
def tap_on_any_paid_invoice(driver):
    deposit_page = DepositPage(driver)
    deposit_page.tap_paid_invoice()
    
@then('I can return to the calendar page')
def return_to_calendar(driver):
    deposit_page = DepositPage(driver)
    deposit_page.return_to_calendar()
    
    
