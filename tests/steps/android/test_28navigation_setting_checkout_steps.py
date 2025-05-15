from pytest_bdd import scenarios, given, when, then, parsers
from pages.shared_components.common_use import CommonUseSection
from pages.android.navigation.setting.checkout import CheckoutPage

scenarios('../../../features/navigation/setting/checkout.feature')

# Scenario: Navigate to Checkout
@given("I am on the branch settings page")
def on_branch_settings_page(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.verify_branch_settings_page(), "Branch settings page is not displayed"

@when("I tap on the Checkout")
def tap_checkout(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.tap_checkout(), "Failed to tap on Checkout"

@then("I should see the checkout page")
def see_checkout_page(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.verify_checkout_page(), "Checkout page is not displayed"




# Scenario: Checkout Signature
@given("I am on the checkout page")
def on_checkout_page(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.verify_checkout_page(), "Checkout page is not displayed"

@when("I turn on the checkout signature switch")
def turn_on_checkout_signature(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.turn_on_checkout_signature(), "Failed to turn on checkout signature"
    # TODO: The switch component currently does not have an implemented on/off state

@when("I tap on  the back button")
def tap_back_button(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.tap_back_button(), "Failed to tap on back button"

@then("I should see the branch settings page")
def see_branch_settings_page(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.verify_branch_settings_page(), "Branch settings page is not displayed"