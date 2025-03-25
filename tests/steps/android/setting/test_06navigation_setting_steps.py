from pytest_bdd import given, when, then, scenarios
from pages.android.navigation.setting.brand import BrandPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../../features/navigation/setting/brand.feature')

BRANCH_NAME = f"Robot_Test_Name_{CommonUseSection.get_current_timestamp()}"
BRANCH_DESCRIPTION = f"Robot_Test_Description_{CommonUseSection.get_current_timestamp()}"
BRANCH_PHONE_NUMBER = f"09{str(CommonUseSection.get_current_timestamp())[-8:]}"
BRANCH_ADDRESS = f"地球路{str(CommonUseSection.get_current_timestamp())[-3:]}號"

# Scenario: Navigate to Branch Settings and Edit Branch Information
@given("I tap the Settings button in the navigation bar")
def tap_setting_option_in_navigation_bar(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_settings_option()

@then("I should see the Branch Settings Page")
def verify_branch_settings_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the Branch Name in the Branch Information section in the Branch Settings page")
def tap_branch_name_in_branch_setting_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_name_in_branch_setting_page()

@then("I should see the Branch and Brand Information page")
def verify_branch_name_in_branch_setting_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_branch_info_page(), "Branch Name not found in Branch Settings page"

@then("I modify the branch name")
def enter_new_branch_name_in_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    brand_page.enter_new_branch_name_in_branch_brand_info_page(BRANCH_NAME)
    brand_page.verify_branch_name_updated_in_branch_brand_info_page(BRANCH_NAME)

@then("I modify the branch description")
def enter_new_branch_description_in_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_description_in_branch_information_page()
    brand_page.enter_new_branch_description_in_description_dialog(BRANCH_DESCRIPTION)
    brand_page.tap_confirm_button_in_description_dialog()
    brand_page.verify_branch_description_updated(BRANCH_DESCRIPTION)

@then("I turn on the Show Branch Phone Toggle")
def tap_show_branch_phone_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_phone_toggle_off()
    brand_page.tap_branch_phone_toggle()
    assert brand_page.verify_branch_phone_turn_on(), "Branch phone information section is not displayed"

@then("I modify the branch phone number")
def enter_new_branch_phone_number(driver):
    brand_page = BrandPage(driver)
    brand_page.select_branch_phone_county_code()
    brand_page.select_branch_phone_county_code_tw()
    brand_page.enter_new_branch_phone_number(BRANCH_PHONE_NUMBER)

@then("I turn on the Show Branch Address Toggle")
def tap_show_branch_address_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_address_toggle_off()
    brand_page.tap_branch_address_toggle()
    assert brand_page.verify_branch_address_turn_on(), "Branch address information section is not displayed"

@then("I modify the branch address")
def enter_new_branch_address(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_address_city_in_branch_brand_info_page()
    brand_page.scroll_city_dialog()
    brand_page.select_random_city()
    brand_page.tap_branch_address_district_in_branch_brand_info_page()
    brand_page.scroll_district_dialog()
    brand_page.select_random_district()
    brand_page.enter_new_branch_address(BRANCH_ADDRESS)

@then("I tap on the expand brand settings button")
def tap_expand_brand_settings_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_expand_brand_settings_button()

@then("the brand settings section should be expanded")
def verify_brand_settings_section_expanded(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_brand_settings_section_expanded(), "Brand settings section not expanded"

@then("I tap the Confirm Edit button in the Branch and Brand Information page")
def tap_confirm_edit_button_in_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_confirm_edit_button_in_branch_brand_info_page()

@then("I should return to the Branch Settings page")
def verify_return_to_branch_settings_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_return_to_branch_settings_page(), "Failed to return to Branch Settings page"

# Scenario: Turn Off Branch Phone Display And Address Display
@given("I tap on the Branch Name in the Branch Information section in the Branch Settings page")
def tap_branch_name_in_branch_setting_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_name_in_branch_setting_page()

@when("I turn off the Show Branch Phone Toggle")
def tap_show_branch_phone_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_phone_toggle_on()
    brand_page.tap_branch_phone_toggle()
    assert brand_page.verify_branch_phone_turn_off(), "Branch phone information section is displayed"

@then("I turn off the Show Branch Address Toggle")
def tap_show_branch_address_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_address_toggle_on()
    brand_page.tap_branch_address_toggle()
    assert brand_page.verify_branch_address_turn_off(), "Branch address information section is displayed"
