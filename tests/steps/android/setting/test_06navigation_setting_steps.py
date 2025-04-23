from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.brand import BrandPage


scenarios('../../../../features/navigation/setting/brand.feature')

@given("I am on the Branch Settings page")
def verify_on_branch_settings_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the Branch Name")
def tap_branch_name(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_branch_name(), "Branch Name not found in Branch Settings page"

@then("I should see the Branch and Brand Information page")
def verify_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_brand_info_page(), "Branch and Brand Information page not found"

@given("I am on the Branch and Brand Information page")
def verify_on_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_brand_info_page(), "Branch and Brand Information page not found"

@when("I clear the Branch Name field")
def clear_branch_name(driver):
    brand_page = BrandPage(driver)
    brand_page.clear_branch_name()

@then('I should see an error message "This field is required"')
def verify_error_message(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_error_message(), "Error message not found"

@when(parsers.parse('I enter "{branch_name}" in the Branch Name field'))
def enter_branch_name(driver, branch_name):
    brand_page = BrandPage(driver)
    brand_page.enter_branch_name(branch_name)

@then(parsers.parse('I should see "{branch_name}" in the branch name field'))
def verify_branch_name(driver, branch_name):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_name(branch_name), f"Branch Name field does not display {branch_name}"

@when("I clear the branch introduction text")
def clear_branch_introduction(driver):
    brand_page = BrandPage(driver)
    assert brand_page.clear_branch_introduction(), "Branch introduction text not found"

@then("the branch introduction field should be empty")
def verify_branch_introduction_empty(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_introduction_empty(), "Branch introduction field is not empty"

@when(parsers.parse('I enter "{branch_introduction}" in the branch introduction'))
def enter_branch_introduction(driver, branch_introduction):
    brand_page = BrandPage(driver)
    assert brand_page.enter_branch_introduction(branch_introduction), "Branch introduction field not found"

@then(parsers.parse('I should see "{branch_introduction}" in the branch introduction'))
def verify_branch_introduction(driver, branch_introduction):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_introduction(branch_introduction), f"Branch introduction field does not display {branch_introduction}"

@when(parsers.parse('I select "{country_code}" as the country code'))
def select_country_code(driver, country_code):
    brand_page = BrandPage(driver)
    assert brand_page.select_country_code(country_code), f"Country code {country_code} not found"

@when(parsers.parse('I enter "{phone_number}" in the branch phone number field'))
def enter_branch_phone_number(driver, phone_number):
    brand_page = BrandPage(driver)
    assert brand_page.enter_branch_phone_number(phone_number), "Branch phone number field not found"

@then(parsers.parse('I should see "{country_code}" "{phone_number}" in the branch phone field'))
def verify_branch_phone_number(driver, country_code, phone_number):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_phone_number(country_code, phone_number), f"Branch phone number field does not display {country_code} {phone_number}"

@when("I turn off the branch phone display switch")
def turn_off_branch_phone_display_switch(driver):
    brand_page = BrandPage(driver)
    assert brand_page.turn_off_branch_phone_display_switch(), "Branch phone display switch not found"

@when("I turn on the branch phone display switch")
def turn_on_branch_phone_display_switch(driver):
    brand_page = BrandPage(driver)
    assert brand_page.turn_on_branch_phone_display_switch(), "Branch phone display switch not found"

@when("I turn off the branch address display switch")
def turn_off_branch_address_display_switch(driver):
    brand_page = BrandPage(driver)
    assert brand_page.turn_off_branch_address_display_switch(), "Branch address display switch not found"

@when("I turn on the branch address display switch")
def turn_on_branch_address_display_switch(driver):
    brand_page = BrandPage(driver)
    assert brand_page.turn_on_branch_address_display_switch(), "Branch address display switch not found"

@when(parsers.parse('I select "{branch_city}" as the city'))
def select_branch_city(driver, branch_city):
    brand_page = BrandPage(driver)
    assert brand_page.select_branch_city(branch_city), f"Branch city {branch_city} not found"

@when(parsers.parse('I select "{branch_district}" as the district'))
def select_branch_district(driver, branch_district):
    brand_page = BrandPage(driver)
    assert brand_page.select_branch_district(branch_district), f"Branch district {branch_district} not found"

@when(parsers.parse('I enter "{branch_address}" in the branch address field'))
def enter_branch_address(driver, branch_address):
    brand_page = BrandPage(driver)
    assert brand_page.enter_branch_address(branch_address), "Branch address field not found"

@then(parsers.parse('I should see "{branch_city}" "{branch_district}" "{branch_address}" in the branch address field'))
def verify_branch_address(driver, branch_city, branch_district, branch_address):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_address(branch_city, branch_district, branch_address), f"Branch address field does not display {branch_city} {branch_district} {branch_address}"

@when("I tap on the Expand Brand Settings button")
def tap_expand_brand_settings(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_expand_brand_settings(), "Expand Brand Settings button not found"

@then("I should see the Brand Settings section")
def verify_brand_settings_section(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_brand_settings_section(), "Brand Settings section not found"

@when("I tap on the Close button")
def tap_close_button(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_close_button(), "Close button not found"

@then("I should see the Branch Settings page")
def verify_branch_settings_page_after_close(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the confirm button")
def tap_confirm_button(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_confirm_button(), "Confirm button not found"