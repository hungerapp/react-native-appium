import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.record_page import RecordPage

scenarios('../../../features/navigation/record.feature')

# Test data
BILLING_NUMBER = '#86SXS'


# View and Switch Between Recent and Canceled Appointments
@allure.feature('Record')
@allure.story('View and Switch Between Recent and Canceled Appointments')
@pytest.mark.navigation
@pytest.mark.run(order=70)
@given('I tap on records in the navigation bar')
def navigate_to_records(driver):
    record_page = RecordPage(driver)
    record_page.tap_records_option()


@then('I can tap on any recently added order under the appointments tab')
def tap_recent_appointment(driver):
    record_page = RecordPage(driver)
    record_page.tap_recent_appointment()


@when('I switch to the recently canceled tab')
def switch_to_canceled_tab(driver):
    record_page = RecordPage(driver)
    record_page.switch_to_canceled_tab()


@then('I can tap on any recently canceled order')
def tap_canceled_order(driver):
    record_page = RecordPage(driver)
    record_page.tap_canceled_order()





# Filter by Personnel and Search 
@allure.feature('Record')
@allure.story('Filter by Personnel and Search')
@pytest.mark.navigation
@pytest.mark.run(order=71)
@given('I am on the Records page')
def navigate_to_records(driver):
    pass

@when('I click on the billing tab')
def click_billing_tab(driver):
    record_page = RecordPage(driver)
    record_page.click_billing_tab()


@then('I click the filter icon')
def click_filter(driver):
    record_page = RecordPage(driver)
    record_page.click_filter_icon()


@then('I can filter by service staff')
def filter_by_staff(driver):
    record_page = RecordPage(driver)
    record_page.click_filter_and_select_staff()
    
    
@then('I can tap on the search field and enter a billing number')
def search_billing(driver):
    record_page = RecordPage(driver)
    record_page.search_billing_number(BILLING_NUMBER)


@then('I can successfully search for the specified billing number')
def verify_search_result(driver):
    pass

    
    
    

# View Checkout Details and Check Payment Method
@allure.feature('Record')
@allure.story('View Checkout Details and Check Payment Method')
@pytest.mark.navigation
@pytest.mark.run(order=72)
@given('I am on the Records page')
def navigate_to_records(driver):
    pass
    
@when('I click on the billing tab')
def click_billing_tab(driver):
    record_page = RecordPage(driver)
    record_page.click_billing_tab()

@then('I tap view details')
def view_details(driver):
    record_page = RecordPage(driver)
    record_page.view_billing_details()


@then('I can view the details and export them')
def view_and_export_details(driver):
    record_page = RecordPage(driver)
    record_page.export_details(is_expand=True)


@when('I tap the view checkout button')
def view_checkout(driver):
    record_page = RecordPage(driver)
    record_page.view_checkout_details()


@then('I can check the payment method')
def check_payment_method(driver):
    record_page = RecordPage(driver)
    record_page.check_payment_method()
    
    



# Process and Delete a claim request
@allure.feature('Record')
@allure.story('Process and Delete a claim request')
@pytest.mark.navigation
@pytest.mark.run(order=73)
@given('I am on the Records page')
def navigate_to_records(driver):
    pass
    
@when('I click on the billing tab')
def click_billing_tab(driver):
    record_page = RecordPage(driver)
    record_page.click_billing_tab()

@then('I click on the claim request option')
def click_claim_request(driver):
    record_page = RecordPage(driver)
    record_page.claim_request_tab()
    
    
@then('I click the filter icon')
def click_filter(driver):
    record_page = RecordPage(driver)
    record_page.click_filter_icon()

    
@then('I can filter by service staff')
def filter_by_staff(driver):
    record_page = RecordPage(driver)
    record_page.click_filter_and_select_staff()

@when('I tap view details')
def view_details(driver):
    record_page = RecordPage(driver)
    record_page.view_billing_details()
    
@then('I can successfully view the details and export them')
def view_and_export_details(driver):
    record_page = RecordPage(driver)
    record_page.export_details()


@when('I tap the view request checkout button')
def view_checkout(driver):
    record_page = RecordPage(driver)
    record_page.view_request_checkout()


@then('I can delete the checkout request')
def delete_checkout(driver):
    record_page = RecordPage(driver)
    record_page.delete_checkout_request()


@then('I can successfully return to the Calendar page')
def return_to_calendar(driver):
    record_page = RecordPage(driver)
    record_page.return_to_calendar()