import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.member_page import MemberPage


scenarios('../../../features/navigation/member.feature')

# TEST DATA
VALID_NUMBER = "0972205690"



# Scenario: Manage member and page functionality
@allure.feature('Member Management')
@allure.story('Manage member and page functionality')
@pytest.mark.run(order=57)
@pytest.mark.navigation_member
@given('I click on the member option in the bottom navigation bar')
def click_member_option(driver):
    member_page = MemberPage(driver)
    member_page.click_member_option()

@when('I click any member below the tab')
def click_member_item(driver):
    member_page = MemberPage(driver)
    member_page.click_member_item()

@then('I should be navigated to the member passport page')
def verify_member_passport_page(driver):
    pass

@when('I add a new member')
def add_new_member(driver):
    member_page = MemberPage(driver)
    member_page.add_member()

@then('I should be able to create a new member')
def verify_new_member_created(driver):
    pass

@when('I apply member filters')
def apply_member_filters(driver):
    member_page = MemberPage(driver)
    member_page.apply_member_filters()

@then('I can see the filtered results')
def verify_filtered_results(driver):
    pass

@when('I check the scheduling records')
def check_scheduling_records(driver):
    member_page = MemberPage(driver)
    member_page.check_scheduling_records()

@then('I can see the scheduling records')
def verify_scheduling_records(driver):
    pass

    

# Scenario: Search and passport tags functionality
@allure.feature('Search and passport tags functionality')
@allure.story('Search and passport tags functionality')
@pytest.mark.run(order=58)
@pytest.mark.navigation_member
@given('I am on the member page')
def verify_on_member_page(driver):
    member_page = MemberPage(driver)
    member_page.verify_on_member_page()

@when('I tap the search button')
def tap_search_button(driver):
    member_page = MemberPage(driver)
    member_page.tap_search_button()

@then('I search for a valid phone number and see the search result')
def search_phone_number(driver):
    member_page = MemberPage(driver)
    member_page.search_phone_number(VALID_NUMBER)

@then('I tap on the search result')
def tap_search_result(driver):
    member_page = MemberPage(driver)
    member_page.tap_search_result()
    
@when('I click more icon in bottom navigation bar and select member tags')
def click_more_icon(driver):
    member_page = MemberPage(driver)
    member_page.select_member_tags()
    
@then('I can modify tag setting')
def modify_tag_setting(driver):
    member_page = MemberPage(driver)
    member_page.modify_tag_setting()
    

@when('I click on the member custom tags setting')
def click_custom_tag_settings(driver):
    member_page = MemberPage(driver)
    member_page.click_custom_tag_settings()

@then('I can add, edit, or delete a custom tag')
def modify_custom_tag(driver):
    member_page = MemberPage(driver)
    member_page.modify_custom_tag()

@then('I successfully change the custom tag and return to the member passport page')
def verify_custom_tag_changed(driver):
    pass

@when('I tap on the billing tab')
def tap_billing_tab(driver):
    member_page = MemberPage(driver)
    member_page.tap_billing_tab()
    

@then('I can view details and export details file')
def tap_view_details(driver):
    member_page = MemberPage(driver)
    member_page.tap_view_details()

@when('I tap view checkout')
def tap_view_checkout(driver):
    member_page = MemberPage(driver)
    member_page.tap_view_checkout()

@then('I can delete the billing record')
def delete_checkout(driver):
    member_page = MemberPage(driver)
    member_page.delete_checkout()
    
    
    
    
# Scenario: Edit member top-up balance
@allure.feature('Edit member top-up balance')
@allure.story('Edit member top-up balance')
@pytest.mark.run(order=59)
@pytest.mark.navigation_member
@given('I am on the member passport page')
def verify_on_member_passport_page(driver):
    member_page = MemberPage(driver)
    member_page.verify_on_member_passport_page()

@when('I click on the Top-up Balance section')
def click_top_up_section(driver):
    member_page = MemberPage(driver)
    member_page.click_top_up_section()

@then('I can edit the top-up amount')
def edit_top_up_amount(driver):
    member_page = MemberPage(driver)
    member_page.edit_top_up_amount()

@when('I click the Top-up button')
def click_top_up_button(driver):
    member_page = MemberPage(driver)
    member_page.click_top_up_button()

@then('I can finish the top-up process')
def finish_top_up_process(driver):
    member_page = MemberPage(driver)
    member_page.finish_top_up_process()

@then('I return to the Member Passport page')
def return_to_member_passport(driver):
    member_page = MemberPage(driver)
    member_page.return_to_member_passport()




# Scenario: Edit Bonus Points
@allure.feature('Edit Bonus Points')
@allure.story('Edit Bonus Points')
@pytest.mark.run(order=60)
@pytest.mark.navigation_member
@given('I am on the member passport page')
def verify_on_member_passport_page(driver):
    member_page = MemberPage(driver)
    member_page.verify_on_member_passport_page()

@when('I click on the bonus points section')
def click_bonus_points_section(driver):
    member_page = MemberPage(driver)
    member_page.click_bonus_points_section()

@then('I can edit the bonus points')
def edit_bonus_points(driver):
    member_page = MemberPage(driver)
    member_page.edit_bonus_points()
    
@then('I return to the member passport page')
def return_to_member_passport(driver):
    member_page = MemberPage(driver)
    member_page.return_to_member_passport()
    
    
    
    

# Scenario: Edit tickets
@allure.feature('Edit tickets')
@allure.story('Edit tickets')
@pytest.mark.run(order=61)
@pytest.mark.navigation_member
@given('I am on the member passport page')
def verify_on_member_passport_page(driver):
    member_page = MemberPage(driver)
    member_page.verify_on_member_passport_page()

@when('I click on the tickets section')
def click_tickets_section(driver):
    member_page = MemberPage(driver)
    member_page.click_tickets_section()

@then('I click the Sell ticket button')
def click_sell_ticket(driver):
    member_page = MemberPage(driver)
    member_page.click_sell_ticket_button()

@then('I can select a performance personnel')
def select_performance_personnel(driver):
    member_page = MemberPage(driver)
    member_page.select_performance_personnel()

@then('I can choose a ticket type for sale')
def choose_ticket_type(driver):
    member_page = MemberPage(driver)
    member_page.choose_ticket_type()

@then('I can finish the checkout process')
def select_payment_method(driver):
    member_page = MemberPage(driver)
    member_page.finish_checkout_process()   



# Scenario: Use and gift a ticket from the ticket page
@allure.feature('Use and gift a ticket from the ticket page')
@allure.story('Use and gift a ticket from the ticket page')
@pytest.mark.run(order=62)
@pytest.mark.navigation_member
@given('I am on the ticket page')
def verify_on_ticket_page(driver):
    pass

@when('I tap on a ticket under owned tickets tab')
def tap_ticket(driver):
    member_page = MemberPage(driver)  
    member_page.tap_ticket()

@then('I can use the selected ticket')
def use_ticket(driver):
    member_page = MemberPage(driver)
    member_page.use_ticket()  

@then('I switches to history tab')
def switch_to_history_tab(driver):
    member_page = MemberPage(driver)
    member_page.switch_to_history_tab()

@when('I click the gift ticket button')
def click_gift_ticket(driver):
    member_page = MemberPage(driver)
    member_page.click_gift_ticket_button()

@then('I can select the tickets for sending')
def select_tickets_for_sending(driver):
    member_page = MemberPage(driver)
    member_page.select_tickets_for_sending()

@then('I return to member passport page')
def return_to_member_passport(driver):
    member_page = MemberPage(driver)
    member_page.return_to_member_passport()




# Scenario: Edit member info in member passport page
@allure.feature('Edit member info in member passport page')
@allure.story('Edit member info in member passport page')
@pytest.mark.run(order=63)
@pytest.mark.navigation_member
@given('I am on the member passport page')
def verify_on_member_passport_page(driver):
    member_page = MemberPage(driver)
    member_page.verify_on_member_passport_page()

@then('I can edit the basic information')
def edit_basic_info(driver):
    member_page = MemberPage(driver)  
    member_page.edit_basic_info()

@then('I can edit the custom fields')
def edit_custom_fields(driver):
    member_page = MemberPage(driver)
    member_page.edit_custom_fields()    

@then('I can edit the member description')
def edit_member_description(driver):
    member_page = MemberPage(driver)
    member_page.edit_member_description()



# Scenario: Bottom navigation functionality
@allure.feature('Bottom navigation functionality')
@allure.story('Bottom navigation functionality')
@pytest.mark.run(order=64)
@pytest.mark.navigation_member
@given('I am on the member passport page')
def verify_on_member_passport_page(driver):
    member_page = MemberPage(driver)
    member_page.verify_on_member_passport_page()
    
'''
目前無法定位, 先註解
@when('I click on the message icon')
def click_message_icon(driver):
    member_page = MemberPage(driver)
    member_page.click_message_icon()  

@then('I can enter send message page')
def send_message(driver):
    member_page = MemberPage(driver)
    member_page.enter_send_message_page()


@when('I click on the sign document icon')
def click_sign_document_icon(driver):
    member_page = MemberPage(driver)
    member_page.click_sign_document_icon()

@then('I can sign the review document')
def sign_review_document(driver):
    member_page = MemberPage(driver)
    member_page.sign_review_document()

'''

@when('I click on the review member icon')
def click_review_member_icon(driver):
    member_page = MemberPage(driver)  
    member_page.click_review_member_icon()

@then('I can view member review')
def view_member_review(driver):
    member_page = MemberPage(driver)
    member_page.view_member_review()   

@when('I click on the more icon')
def click_more_icon(driver):
    member_page = MemberPage(driver)
    member_page.click_more_icon()

@then('I can link account and send line message')
def link_account_and_send_line_message(driver):
    member_page = MemberPage(driver)
    member_page.link_account_and_send_line_message()

@then('I cam successfully click back to member passport page')
def click_back_to_member_passport_page(driver):
    member_page = MemberPage(driver)
    member_page.click_back_to_member_passport_page()



# Scenario: Modify checkout and re-checkout
@allure.feature('Modify checkout and re-checkout')
@allure.story('Modify checkout and re-checkout')
@pytest.mark.run(order=65)
@pytest.mark.navigation_member
@when('I add member to blacklist')
def add_member_to_blacklist(driver):
    member_page = MemberPage(driver)
    member_page.add_member_to_blacklist()
    
@then('I can remove member from blacklist')
def remove_member_from_blacklist(driver):
    member_page = MemberPage(driver)
    member_page.remove_member_from_blacklist()


@when('I tap on the billing tab')
def tap_billing_tab(driver):
    member_page = MemberPage(driver)
    member_page.tap_billing_tab()

@then('I tap view checkout')
def tap_view_checkout(driver):
    member_page = MemberPage(driver)
    member_page.tap_view_checkout()

@then('I can delete and reprocess the checkout')
def delete_and_reprocess_checkout(driver):
    member_page = MemberPage(driver)
    member_page.delete_and_reprocess_checkout()

@then('I can choose the item I have bought before')
def can_choose_the_item_i_have_bought_before(driver):
    member_page = MemberPage(driver)
    member_page.can_choose_the_item_i_have_bought_before()  

@then('I can finish the checkout process')
def proceed_to_checkout(driver):
    member_page = MemberPage(driver)
    member_page.finish_checkout_process()
    

@then('I return to the calendar page')
def return_to_calendar_page(driver):
    member_page = MemberPage(driver)
    member_page.return_to_calendar_page()