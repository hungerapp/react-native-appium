import allure
import pytest

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.cs_page import CSPage

scenarios('../../../features/navigation/cs.feature')


# Send and Check message via customer service
@allure.feature('Customer Service')
@allure.story('Message Interaction')
@pytest.mark.run(order=55)  
@pytest.mark.navigation_cs
@given('I click on the Customer Service option in the navigation bar')
def click_cs_option(driver):
    cs_page = CSPage(driver)
    cs_page.click_cs_option()

@when('I click on the message section')
def click_message_section(driver):
    cs_page = CSPage(driver)
    cs_page.click_message_section()

@then('I click on a past message to confirm it')
def click_past_message(driver):
    cs_page = CSPage(driver)
    cs_page.past_message()

@when('I click on the recent message section')
def click_recent_message(driver):
    cs_page = CSPage(driver)
    cs_page.click_recent_message_section()

@then('I enter a message in the recent message input field')
def enter_message(driver):
    cs_page = CSPage(driver)
    cs_page.enter_message()
    
    



# Navigate Customer Service Links
@allure.feature('Customer Service')
@allure.story('Hyperlink Navigation')
@pytest.mark.run(order=56)
@pytest.mark.navigation_cs
@then('I tap on the follow Hotcake Instagram hyperlink')
def tap_instagram_link(driver):
    cs_page = CSPage(driver)
    cs_page.tap_instagram_link()

@then('I tap on the Pricing & Plans hyperlink')
def tap_pricing_link(driver):
    cs_page = CSPage(driver)
    cs_page.tap_pricing_link()

@then('I tap on the Help Center hyperlink')
def tap_help_center_link(driver):
    cs_page = CSPage(driver)
    cs_page.tap_help_center_link()

@then('I click back button to go back to calendar page')
def click_back_button(driver):
    cs_page = CSPage(driver)
    cs_page.click_back_button()
