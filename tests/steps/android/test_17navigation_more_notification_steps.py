import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.notification import NotificationPage

scenarios('../../../features/navigation/more/notification.feature')

# TEST DATA



# [NOTIFICATION AND MESSAGES]
@allure.feature('Notification and Messages')
@allure.story('Notification and Messages Management')
@pytest.mark.navigation_more_notification
@pytest.mark.run(order=85)
@given('I click on notifications and messages')
def tap_on_notification(driver):
    notification_page = NotificationPage(driver)
    notification_page.tap_on_notification()
    
@when('I click on the view latest features button')
def click_view_latest_features_button(driver):
    notification_page = NotificationPage(driver)
    notification_page.click_view_latest_features_button()
    
@then('I should be redirected to the changelog page')
def redirect_to_changelog_page_and_back(driver):
    notification_page = NotificationPage(driver)
    notification_page.redirect_and_back()
    
@when('I on the notification page')
def click_any_notification(driver):
    notification_page = NotificationPage(driver)
    notification_page.on_notification_page()
    
@then('I can see the notification below')
def see_notification(driver):
    notification_page = NotificationPage(driver)
    notification_page.see_notification()
    
@when('I click the mark all as read button')
def click_mark_all_as_read_button(driver):
    notification_page = NotificationPage(driver)
    notification_page.click_mark_all_as_read_button()
    
@then('all notifications should be marked as read')
def all_notifications_marked_as_read(driver):
    pass
    
@then('I can return to the calendar page')
def return_to_calendar_page(driver):
    notification_page = NotificationPage(driver)
    notification_page.return_to_calendar_page()
