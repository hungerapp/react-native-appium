import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.tutorial_guide import TutorialGuidePage

scenarios('../../../features/navigation/more/tutorial_guide.feature')

# TEST DATA



# [TUTORIAL GUIDE]
@allure.feature('Tutorial Guide')
@allure.story('Tutorial Guide - Opening the User Guide')
@pytest.mark.navigation
@pytest.mark.run(order=93)
@given('I click on the tutorial guide')
def click_tutorial_guide(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.click_tutorial_guide()
    
@then('I can click tutorial video')
def click_tutorial_video(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.click_tutorial_video()
   
@then('I can click on the service staff section')
def click_service_staff_section(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.click_service_staff_section()
    
@then('I can click on the service items section')
def click_service_items_section(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.click_service_items_section()
    
@then('I can click on online reservation management section')
def click_online_reservation_management_section(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.click_online_reservation_management_section()
    
@then('I can click on the connect Line official account section')
def click_connect_line_official_account_section(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.click_connect_line_official_account_section()
    
@then('I can click tutorial book button')
def click_tutorial_book_button(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.click_tutorial_book_button()
    
@then('I can return to the calendar page')
def return_to_calendar_page(driver):
    tutorial_guide_page = TutorialGuidePage(driver)
    tutorial_guide_page.return_to_calendar_page()
    
    
    
    
    
    
    
    
    
    