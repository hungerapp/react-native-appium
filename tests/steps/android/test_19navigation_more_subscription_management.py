import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.subscription_management import SubscriptionManagementPage

scenarios('../../../features/navigation/more/subscription_management.feature')

# TEST DATA



# [SUBSCRIPTION MANAGEMENT]
@allure.feature('Subscription Management')
@allure.story('Subscription Management - View Current Plans')
@pytest.mark.navigation_more_subscription_management    
@pytest.mark.run(order=88)
@given('I click on subscription management')
def click_subscription_management(driver):
    subscription_management_page = SubscriptionManagementPage(driver)
    subscription_management_page.click_subscription_management()
    
@then('I should be able to view the current plans')
def view_current_plans(driver):
    pass
    
@then('I should be able to return to the calendar page')
def return_to_calendar_page(driver):
    subscription_management_page = SubscriptionManagementPage(driver)
    subscription_management_page.return_to_calendar_page()
    
    
    