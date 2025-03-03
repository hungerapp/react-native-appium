import allure
import pytest

from pytest_bdd import given, when, then, scenarios
from pages.android.navigation.search_page import SearchPage


scenarios('../../../features/navigation/search.feature')

FULL_NUMBER = "0972205690"
INVALID_NUMBER = "99999999999999999"

# Search with a valid complete number
@allure.feature('Search Functionality')
@allure.story('Search with a valid complete number')
@pytest.mark.run(order=57)
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





# Search with an invalid complete number
@allure.feature('Search Functionality')
@allure.story('Search with an invalid complete number')
@pytest.mark.run(order=58)
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