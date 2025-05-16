from pytest_bdd import scenarios, given, when, then
from pages.android.navigation.setting.third_party_tools import ThirdPartToolsPage

scenarios('../../../features/navigation/setting/third_party_tools.feature')

# Scenario: Navigate to Third Part Tools
@given("I am on the branch settings page")
def on_branch_settings_page(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.verify_branch_settings_page(), "Branch settings page is not displayed"

@given('This branch is subscribed to "Free免費體驗方案"')
def subscribed_to_free_plan(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.verify_subscription_plan("Free免費體驗方案"), "Free plan is not displayed"

@when("I tap on the Third Party Tools")
def tap_third_party_tools(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.tap_third_party_tools(), "Failed to tap on Third Party Tools"

@then("I should see the Feature Unsupported Dialog")
def see_feature_unsupported_dialog(driver):
    third_part_tools_page = ThirdPartToolsPage(driver)
    assert third_part_tools_page.verify_feature_unsupported_dialog(), "Feature Unsupported Dialog is not displayed"