import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.brand_setting import BrandSettingPage

scenarios('../../../features/navigation/more/brand_setting.feature')

# TEST DATA
BRAND_DESCRIPTION = "夯客提供預約管理、數據分析、會員系統、再行銷工具"


@allure.feature('Brand Setting')
@allure.story('Brand Setting')
@pytest.mark.navigation
@pytest.mark.run(order=74)
@given('I tap on more in the bottom navigation bar')
def tap_more_tab(driver):
    brand_setting_page = BrandSettingPage(driver)
    brand_setting_page.tap_more_option()

@when('I tap on brand settings')
def tap_brand_settings(driver):
    brand_setting_page = BrandSettingPage(driver)
    brand_setting_page.tap_brand_settings()

@then('I can edit the brand name')
def edit_brand_name(driver):
    brand_setting_page = BrandSettingPage(driver)
    brand_setting_page.edit_brand_name()

@then('I can edit the brand description')
def edit_brand_description(driver):
    brand_setting_page = BrandSettingPage(driver)
    brand_setting_page.edit_brand_description(BRAND_DESCRIPTION)
    brand_setting_page.save_changes()