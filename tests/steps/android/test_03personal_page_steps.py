import random
import time
import allure
import pytest

from pytest_bdd import scenarios, given, then, when

from pages.android.login_page import LoginPage
from pages.android.personal_page import PersonalPage

scenarios('../../../features/personal_page.feature')

TEST_EMAIL = 'ann@hunger.ai'
TEST_VER = '5556666'

# View basic personal information
@allure.feature('Personal Page')
@allure.story('View basic personal information')
@pytest.mark.run(order=6)
@given('I successfully logged in first time')
def login_to_personal_page(driver):
    login_page = LoginPage(driver)
    login_page.login(TEST_EMAIL, TEST_VER)
    login_page.is_logged_in()
    
    
@then('I should see my profile picture')
def see_profile_picture(driver):
    personal_page = PersonalPage(driver)
    personal_page.is_profile_picture_displayed()

@then('I should see my username')
def see_username(driver):
    personal_page = PersonalPage(driver)
    personal_page.is_username_displayed()

@then('I should see greeting message')
def see_greeting_message(driver):
    personal_page = PersonalPage(driver)
    greeting = personal_page.get_greeting_message_message()
    assert greeting is not None

@then('I should see my email address')
def see_email_address(driver):
    personal_page = PersonalPage(driver)
    personal_page.is_email_address_displayed()
  
  

# View brand list section
@allure.feature('Brand List')
@allure.story('View brand list section')
@pytest.mark.run(order=7)
@given('I am on the personal page')
def login_to_personal_page(driver):
    pass
  
  
@then('I should see the brand list title')
def see_brand_list_title(driver):
    personal_page = PersonalPage(driver)
    personal_page.is_brand_list_title_displayed()

@then('I should see hunger Salon-staging title with profile picture')
def see_hunger_salon_title_with_profile_picture(driver):
    personal_page = PersonalPage(driver)
    personal_page.is_brand_hunger_salon_title_displayed()
    personal_page.is_brand_hunger_salon_profile_picture_displayed()

@then('I should be able to visit all branches')
def visit_all_branches(driver):
    personal_page = PersonalPage(driver)
    results = personal_page.visit_all_branches_smart()
    # verify all branches visit results
    failed_branches = [r for r in results if r['status'] == 'failed']
    assert len(failed_branches) == 0, f"Failed to visit branches: {failed_branches}"
    # for some reason, the back button is not working, so we need to click the cancel button
    try :
      personal_page.click_back_to_personal_page()
    except:
      pass



# Manage Push Notification
@allure.feature('Push Notification')
@allure.story('Manage Push Notification')
@pytest.mark.run(order=8)
@given('I am on the personal page')
def login_to_personal_page(driver):
    pass
  
@when('I click push notification button')
def click_push_notification_button(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_push_notification_button()

@then('I should be able to toggle random notification settings')
def toggle_random_notification_settings(driver):
    personal_page = PersonalPage(driver)
    
    # random toggle 3-6 switches
    num_toggles = random.randint(5, 7)
    personal_page.random_toggle_switches(num_toggles)


@then('I should be able to save notification settings')
def save_notification_settings(driver):
    personal_page = PersonalPage(driver)
    personal_page.save_notification_settings()
 



# Manage account settings
@allure.feature('Account Settings')
@allure.story('Manage account settings')
@pytest.mark.run(order=9)
@given('I am on the personal page')
def login_to_personal_page(driver):
    pass
  
@when('I click settings icon')
def click_settings_icon(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_setting_icon()

@then('I click account settings option')
def click_account_settings_option(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_account_settings()

@then('I should be able to update account information and save settings')
def update_account_information(driver):
    personal_page = PersonalPage(driver)
    personal_page.update_account_information_and_save_settings()
    


# Account Settings for empty name
@allure.feature('Account Settings for empty name')
@allure.story('Account Settings for empty name')
@pytest.mark.run(order=10)
@when('I click settings icon')
def click_settings_icon(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_setting_icon()

@then('I click account settings option')
def click_account_settings_option(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_account_settings()

@then('I input empty name and get error message')
def input_empty_name(driver):
    personal_page = PersonalPage(driver)
    personal_page.get_empty_name_error_message()
    personal_page.cancel_account_settings()




# Account Settings for empty phone number
@allure.feature('Account Settings for empty phone number')
@allure.story('Account Settings for empty phone number')
@pytest.mark.run(order=11)
@given('I am on the personal page')
def login_to_personal_page(driver):
    pass
  
@when('I click settings icon')
def click_settings_icon(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_setting_icon()

@then('I click account settings option')
def click_account_settings_option(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_account_settings()

@then('I input empty phone number and get error message')
def input_empty_phone_number(driver):
    personal_page = PersonalPage(driver)
    personal_page.get_empty_phone_error_message()
    personal_page.cancel_account_settings()
    


# Account Settings for invalid phone number
@allure.feature('Account Settings for invalid phone number')
@allure.story('Account Settings for invalid phone number')
@pytest.mark.run(order=12)
@given('I am on the personal page')
def login_to_personal_page(driver):
    pass
  
@when('I click settings icon')
def click_settings_icon(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_setting_icon()

@then('I click account settings option')
def click_account_settings_option(driver):
    personal_page = PersonalPage(driver)
    personal_page.click_account_settings()

@then('I input invalid phone number')
def input_invalid_phone_number(driver):
    personal_page = PersonalPage(driver)
    personal_page.input_phone_number(valid=False)

@then('I should see error message for invalid phone')
def see_error_message_for_invalid_phone(driver):
    personal_page = PersonalPage(driver)
    personal_page.get_invalid_phone_error_message()
    personal_page.cancel_account_settings()
    


