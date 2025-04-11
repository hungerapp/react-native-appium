import allure
import pytest

from pytest_bdd import given, when, then, scenarios
from pages.android.navigation.search_page import SearchPage


scenarios('../../../features/navigation/search.feature')

FULL_NUMBER = "0972205690"
INVALID_NUMBER = "99999999999999999"
EXISTING_NAME = "王貝克"
INVALID_NAME = "王一二三四五六"

# Search with a valid complete number
@allure.feature('Search Functionality')
@allure.story('Search with a valid complete number')
@pytest.mark.run(order=66)
@pytest.mark.navigation
@given('I tap on the Search option in the navigation bar')
def tap_search_option(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_option()

@when('I enter a valid complete number')
def enter_valid_number(driver):
    search_page = SearchPage(driver)
    search_page.enter_search_number(FULL_NUMBER)

@then('I tap on the corresponding result')
def tap_search_result(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_result(is_member_tab=False)
    
@then('I scroll down to view the relevant search results')
def scroll_down_results(driver):
    search_page = SearchPage(driver)
    search_page.scroll_down()

@then('I tap on the Member tab')
def tap_member_tab(driver):
    search_page = SearchPage(driver)
    search_page.tap_member_tab()

@then('I tap on the corresponding result again')
def tap_search_result_again(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_result(is_member_tab=True)

@then('I click back button to return to the previous page')
def click_back_first_scenario(driver):
    search_page = SearchPage(driver)
    search_page.click_back()


# Search with an existing name
@allure.feature('Search Functionality')
@allure.story('Search with an existing name')
@pytest.mark.run(order=67)
@pytest.mark.navigation
@given('I tap on the Search option in the navigation bar')
def tap_search_option(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_option()
    
@when('I enter an existing name')
def enter_existing_name(driver):
    search_page = SearchPage(driver)
    search_page.enter_search_name(EXISTING_NAME)
    
@then('I tap on the corresponding result')
def tap_search_result(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_result(is_member_tab=False)

@then('I tap on the Member')
def tap_member(driver):
    search_page = SearchPage(driver)
    search_page.tap_member_tab()

@then('I tap on the corresponding result again')
def tap_search_result_again(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_result(is_member_tab=True)

@then('I click back button to return to the previous page')
def click_back_second_scenario(driver):
    search_page = SearchPage(driver)
    search_page.click_back()


# Search with an invalid name
@allure.feature('Search Functionality')
@allure.story('Search with an invalid name')
@pytest.mark.run(order=68)
@pytest.mark.navigation
@given('I tap on the Search option in the navigation bar')
def tap_search_option(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_option()
    
@when('I enter an invalid name')
def enter_invalid_name(driver):
    search_page = SearchPage(driver)
    search_page.enter_search_name(INVALID_NAME)

@then('I see no data indicating that the name is invalid')
def check_no_data(driver):
    search_page = SearchPage(driver)
    assert search_page.is_no_data_displayed()

@then('I switch to the Member tab')
def switch_to_member_tab(driver):
    search_page = SearchPage(driver)
    search_page.tap_member_tab()

@then('I see no data indicating that the name is invalid')
def check_no_data(driver):
    search_page = SearchPage(driver)
    assert search_page.is_no_data_displayed()

@then('I click back button to return to the previous page')
def click_back_third_scenario(driver):
    search_page = SearchPage(driver)
    search_page.click_back()
    
    

# Search with an invalid complete number
@allure.feature('Search Functionality')
@allure.story('Search with an invalid complete number')
@pytest.mark.run(order=69)
@pytest.mark.navigation
@given('I tap on the Search option in the navigation bar')
def tap_search_option(driver):
    search_page = SearchPage(driver)
    search_page.tap_search_option()

@when('I enter an invalid complete number')
def enter_invalid_number(driver):
    search_page = SearchPage(driver)
    search_page.enter_search_number(INVALID_NUMBER)

@then('I see no data indicating that the number is invalid')
def check_no_data(driver):
    search_page = SearchPage(driver)
    assert search_page.is_no_data_displayed()

@then('I switch to the Member tab')
def switch_to_member_tab(driver):
    search_page = SearchPage(driver)
    search_page.tap_member_tab()

@then('I click back button to return to the previous page')
def click_back_second_scenario(driver):
    search_page = SearchPage(driver)
    search_page.click_back()