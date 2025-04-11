import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.export import ExportPage

scenarios('../../../features/navigation/more/export.feature')

# TEST DATA



# [EXPORT] AVAILABLE_TIME_SLOTS_AS_CALENDAR_IMAGE
@allure.feature('Export')
@allure.story('Available Time Slots as Calendar Image')
@pytest.mark.navigation
@pytest.mark.run(order=86)
@given('I click on export available time slots')
def click_export_available_time_slots(driver):
    export_page = ExportPage(driver)
    export_page.click_export_available_time_slots()
    
@when('I select a staff member')
def select_a_staff_member(driver):
    export_page = ExportPage(driver)
    export_page.select_a_staff_member()
    
@then('I select a service item')
def select_a_service_item(driver):
    export_page = ExportPage(driver)
    export_page.select_a_service_item()
    
@then('I select a month')
def select_a_month(driver):
    export_page = ExportPage(driver)
    export_page.select_a_month()
    
@then('I should be able to export the calendar')
def export_the_calendar(driver):
    export_page = ExportPage(driver)
    export_page.export()
    
@then('I should be able to save the image')
def save_the_image(driver):
    export_page = ExportPage(driver)
    export_page.save_the_image()
    
@then('I should be able to return to the calendar page')
def return_to_calendar_page(driver):
    export_page = ExportPage(driver)
    export_page.return_to_calendar_page()
    
    



# [EXPORT] AVAILABLE_TIME_SLOTS_AS_TEXT
@allure.feature('Export')
@allure.story('Available Time Slots as Text')
@pytest.mark.navigation
@pytest.mark.run(order=87)
@given('I click on export available time slots')
def click_export_available_time_slots(driver):
    export_page = ExportPage(driver)
    export_page.click_export_available_time_slots()
    
@when('I click on the text tab')
def click_on_the_text_tab(driver):
    export_page = ExportPage(driver)
    export_page.click_on_the_text_tab()
    
@then('I select a staff member')
def select_a_staff_member(driver):
    export_page = ExportPage(driver)
    export_page.select_a_staff_member()
    
@then('I select a service item')    
def select_a_service_item(driver):
    export_page = ExportPage(driver)
    export_page.select_a_service_item()
    
@then('I select a date range')
def select_a_date_range(driver):
    export_page = ExportPage(driver)
    export_page.select_a_date_range()
    
@then('I should be able to export the text')
def export_the_text(driver):
    export_page = ExportPage(driver)
    export_page.export()
    
@then('I should be able to copy the text')
def copy_the_text(driver):
    export_page = ExportPage(driver)
    export_page.copy_the_text()
    
@then('I should be able to return to the calendar page')
def return_to_calendar_page(driver):
    export_page = ExportPage(driver)
    export_page.return_to_calendar_page()           
    
    
    
    
    
    
    