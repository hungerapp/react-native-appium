from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.brand import BrandPage
from pages.shared_components.common_use import CommonUseSection


scenarios('../../../features/navigation/setting/brand.feature')


# Scenario: Navigate to the Branch Settings Page
@given('I am on the Calendar page')
def on_calendar_page(driver):
    pass

@when("I tap on the Settings icon in the navigation bar")
def tap_settings_icon(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_settings_icon(), "Settings icon not found in navigation bar"


@then("I should see the Branch Settings page")
def verify_branch_settings_page_after_close(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"





# Scenario: Save Branch and Brand Information
@given("I am on the Branch Setting page")
def on_branch_setting_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the Branch Name")
def tap_branch_name(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_branch_name(), "Branch Name not found in Branch Settings page"

@when(parsers.parse('I enter "{branch_name}" in the Branch Name field'))
def enter_branch_name(driver, branch_name):
    branch_name = CommonUseSection.replace_current_datetime(branch_name)
    brand_page = BrandPage(driver)
    assert brand_page.enter_branch_name(branch_name), "Branch Name field not found"

@when(parsers.parse('I enter "{branch_introduction}" in the branch introduction'))
def enter_branch_introduction(driver, branch_introduction):
    branch_introduction = CommonUseSection.replace_current_datetime(branch_introduction)
    brand_page = BrandPage(driver)
    assert brand_page.enter_branch_introduction(branch_introduction), "Branch introduction field not found"

@when("I turn off the branch phone display switch")
def turn_off_branch_phone_display_switch(driver):
    brand_page = BrandPage(driver)
    assert brand_page.turn_off_branch_phone_display_switch(), "Branch phone display switch not found"

@when("I turn on the branch phone display switch")
def turn_on_branch_phone_display_switch(driver):
    brand_page = BrandPage(driver)
    assert brand_page.turn_on_branch_phone_display_switch(), "Branch phone display switch not found"

@when(parsers.parse('I select "{country_code}" as the country code'))
def select_country_code(driver, country_code):
    brand_page = BrandPage(driver)
    assert brand_page.select_country_code(country_code), f"Country code {country_code} not found"

@when(parsers.parse('I enter "{phone_number}" in the branch phone number field'))
def enter_branch_phone_number(driver, phone_number):
    phone_number = CommonUseSection.replace_current_datetime(phone_number)
    brand_page = BrandPage(driver)
    assert brand_page.enter_branch_phone_number(phone_number), "Branch phone number field not found"

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
    branch_address = CommonUseSection.replace_current_datetime(branch_address)
    brand_page = BrandPage(driver)
    assert brand_page.enter_branch_address(branch_address), "Branch address field not found"

@when("I tap on the Expand Brand Settings button")
def tap_expand_brand_settings(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_expand_brand_settings(), "Expand Brand Settings button not found"

@when("I tap on the confirm button")
def tap_confirm_button(driver):
    brand_page = BrandPage(driver)
    assert brand_page.tap_confirm_button(), "Confirm button not found"

@then("I should see the Branch Settings page")
def verify_branch_settings_page_after_close(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"
    