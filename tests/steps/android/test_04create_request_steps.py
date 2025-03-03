import allure
import pytest
from pytest_bdd import scenarios, given, when, then

from pages.android.create.create_request_page import CreateRequestPage

scenarios('../../../features/create/create_request.feature')



# Scenario: Request items without signing
@allure.feature('Create Request')
@allure.story('Request items without signing')
@pytest.mark.run(order=43)
@pytest.mark.create
@given('I click the create request option')
def click_create_request_option(driver):
    create_page = CreateRequestPage(driver)
    create_page.click_create_request()

@when('I select a requester')
def select_requester(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_requester()

@then('I select an item')
def select_item(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_item()

@then('I request the item without signing')
def request_without_signing(driver):
    create_page = CreateRequestPage(driver)
    create_page.submit_signing()

@then('I confirm the request and successfully create a request')
def confirm_request(driver):
    create_page = CreateRequestPage(driver)
    create_page.confirm_request()





# Scenario: Modify request details before confirming
@allure.feature('Create Request')
@allure.story('Modify request details before confirming')
@pytest.mark.run(order=44)
@pytest.mark.create
@given('I click the create request option')
def click_create_request_option(driver):
    create_page = CreateRequestPage(driver)
    create_page.click_create_request()

@when('I select a requester')
def select_requester(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_requester()

@then('I select an item')
def select_item(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_item()

@then('I change the requester')
def change_requester(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_requester(change=True)

@when('I clear all selected items')
def clear_items(driver):
    create_page = CreateRequestPage(driver)
    create_page.clear_all_items()

@then('I reselect items')
def reselect_items(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_item()

@then('I update the items amount')
def update_amount(driver):
    create_page = CreateRequestPage(driver)
    create_page.update_items_amount()

@then('I update the items quantity')
def update_quantity(driver):
    create_page = CreateRequestPage(driver)
    create_page.update_items_quantity()

@then('I remove an item')
def remove_item(driver):
    create_page = CreateRequestPage(driver)
    create_page.remove_item()

@then('I sign for the request')
def sign_request(driver):
    create_page = CreateRequestPage(driver)
    create_page.submit_signing()
    create_page.sign_request()

@then('I clear the signature and resign')
def clear_and_resign(driver):
    create_page = CreateRequestPage(driver)
    create_page.clear_signature()
    create_page.sign_request()

@then('I confirm the request and successfully create a request')
def confirm_request(driver):
    create_page = CreateRequestPage(driver)
    create_page.confirm_request() 