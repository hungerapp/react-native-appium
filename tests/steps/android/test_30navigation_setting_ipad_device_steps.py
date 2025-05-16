from pytest_bdd import scenarios, given, when, then
from pages.android.navigation.setting.ipad_device import IpadDevicePage

scenarios('../../../features/navigation/setting/ipad_device.feature')

# Scenario: Navigate to iPad Device
@given("I am on the branch settings page")
def on_branch_settings_page(driver):
    ipad_device_page = IpadDevicePage(driver)
    assert ipad_device_page.verify_branch_settings_page(), "Branch settings page is not displayed"

@when("I tap on the iPad Device")
def tap_ipad_device(driver):
    ipad_device_page = IpadDevicePage(driver)
    assert ipad_device_page.tap_ipad_device(), "Failed to tap on iPad Device"

@then("I should see the ipad device page")
def see_ipad_device_page(driver):
    ipad_device_page = IpadDevicePage(driver)
    assert ipad_device_page.verify_ipad_device_page(), "iPad Device page is not displayed"




# Scenario: Add iPad Device
@given("I am on the iPad device page")
def on_ipad_device_page(driver):
    ipad_device_page = IpadDevicePage(driver)
    assert ipad_device_page.verify_ipad_device_page(), "iPad Device page is not displayed"

@when("I add a new iPad device")
def add_new_ipad_device(driver):
    ipad_device_page = IpadDevicePage(driver)
    assert ipad_device_page.add_new_ipad_device(), "Failed to add new iPad device"

@when("I tap on the close button in the iPad device page")
def tap_close_button_ipad_device_page(driver):
    ipad_device_page = IpadDevicePage(driver)
    assert ipad_device_page.tap_close_button_ipad_device_page(), "Failed to tap on close button in iPad device page"

@then("I should see the branch settings page")
def see_branch_settings_page(driver):
    ipad_device_page = IpadDevicePage(driver)
    assert ipad_device_page.verify_branch_settings_page(), "Branch settings page is not displayed"