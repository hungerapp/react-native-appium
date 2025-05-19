import allure
import pytest
from pytest_bdd import scenarios, given, when, then

from pages.android.create.create_request_page import CreateRequestPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../features/create/create_request.feature')



# Scenario: Request items without signing
@allure.feature('Create Request')
@allure.story('Request items without signing')
@pytest.mark.run(order=44)
@pytest.mark.create_request
@given('I click the create request option')
def click_create_request_option(driver):
    create_page = CreateRequestPage(driver)
    create_page.click_create_request()

@when('I select a requester')
def select_requester(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_requester()

@when('I select an item')
def select_item(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_item()

@when('I request the item without signing')
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
@pytest.mark.run(order=45)
@pytest.mark.create_request
@given('I click the create request option')
def click_create_request_option(driver):
    create_page = CreateRequestPage(driver)
    create_page.click_create_request()

@when('I select a requester')
def select_requester(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_requester()

@when('I select an item')
def select_item(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_item()

@when('I change the requester')
def change_requester(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_requester(change=True)

@when('I clear all selected items')
def clear_items(driver):
    create_page = CreateRequestPage(driver)
    create_page.clear_all_items()

@when('I reselect items')
def reselect_items(driver):
    create_page = CreateRequestPage(driver)
    create_page.select_item()

@when('I update the items amount')
def update_amount(driver):
    common_use = CommonUseSection(driver)
    common_use.update_items_amount()

@when('I update the items quantity')
def update_quantity(driver):
    common_use = CommonUseSection(driver)
    common_use.update_items_quantity()

@when('I remove an item')
def remove_item(driver):
    create_page = CreateRequestPage(driver)
    create_page.remove_item()

@when('I sign for the request')
def sign_request(driver):
    create_page = CreateRequestPage(driver)
    common_use = CommonUseSection(driver)
    create_page.submit_signing()
    common_use.sign_request()

@when('I clear the signature and resign')
def clear_and_resign(driver):
    create_page = CreateRequestPage(driver)
    create_page.clear_signature()
    common_use = CommonUseSection(driver)
    common_use.sign_request()

@then('I confirm the request and successfully create a request')
def confirm_request(driver):
    create_page = CreateRequestPage(driver)
    create_page.confirm_request() 