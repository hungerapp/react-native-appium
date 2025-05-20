import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.tutorial_book import TutorialBookPage

scenarios('../../../features/navigation/more/tutorial_book.feature')

# TEST DATA



# [TUTORIAL BOOK]
@allure.feature('Tutorial Book')
@allure.story('Tutorial Book - Opening the User Book')
@pytest.mark.navigation_more_tutorial_book
@pytest.mark.run(order=92)
@given('I click on the user book')
def click_user_book(driver):
    tutorial_book_page = TutorialBookPage(driver)
    tutorial_book_page.click_tutorial_book()
    
@then('I can successfully redirect to the user book')
def successfully_redirect_to_the_user_book(driver):
    pass
    
@then('I can return to the calendar page')
def return_to_calendar_page(driver):
    tutorial_book_page = TutorialBookPage(driver)
    tutorial_book_page.return_to_calendar_page()
    
    
    