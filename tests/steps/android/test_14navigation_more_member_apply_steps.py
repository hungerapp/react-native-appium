import pytest
import allure

from pytest_bdd import scenarios, given, when, then

from pages.android.navigation.more.member_apply import MemberApplyPage

scenarios('../../../features/navigation/more/member_apply.feature')

# TEST DATA


    
# GENERAL VOUCHER MANAGEMENT
@allure.feature('General Voucher Management')
@allure.story('General Voucher Management')
@pytest.mark.navigation
@pytest.mark.run(order=75)
@given('I tap on membership application')
def tap_member_apply(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.tap_member_apply()

@when('I tap on voucher management')
def tap_voucher_management(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.tap_voucher_management()

@then('I can add a general voucher')
def add_general_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.add_general_voucher()

@then('I can edit and delete a general voucher')
def edit_and_delete_general_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.edit_and_delete_general_voucher()


    
# BONUS POINT VOUCHER MANAGEMENT
@allure.feature('Bonus Point Voucher Management')
@allure.story('Bonus Point Voucher Management')
@pytest.mark.navigation
@pytest.mark.run(order=76)
@given('I am in the voucher management section')
def in_voucher_management_section(driver):
    pass

@when('I switch to the bonus point redemption tab')
def switch_to_bonus_point_tab(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.switch_to_bonus_point_tab()

@then('I can add a bonus point voucher')
def add_bonus_point_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.add_bonus_point_voucher()

@then('I can edit and delete a bonus point voucher')
def edit_and_delete_bonus_point_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.edit_and_delete_bonus_point_voucher()    


  
    
# MEMBERSHIP GIFT VOUCHER MANAGEMENT
@allure.feature('Membership Gift Voucher Management')
@allure.story('Membership Gift Voucher Management')
@pytest.mark.navigation
@pytest.mark.run(order=77)
@given('I am in the voucher management section')
def in_voucher_management_section(driver):
    pass

@when('I switch to the membership gift tab')
def switch_to_membership_gift_tab(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.switch_to_membership_gift_tab()

@then('I can add a membership gift voucher')
def add_membership_gift_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.add_membership_gift_voucher()

@then('I can edit and delete a membership gift voucher')
def edit_and_delete_membership_gift_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.edit_and_delete_membership_gift_voucher()

    

# BIRTHDAY GIFT VOUCHER MANAGEMENT
@allure.feature('Birthday Gift Voucher Management')
@allure.story('Birthday Gift Voucher Management')
@pytest.mark.navigation
@pytest.mark.run(order=78)
@given('I am in the voucher management section')
def in_voucher_management_section(driver):
    pass
  
@when('I switch to the birthday gift tab')
def switch_to_birthday_gift_tab(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.switch_to_birthday_gift_tab()

@then('I can add a birthday gift voucher')
def add_birthday_gift_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.add_birthday_gift_voucher()

@then('I can edit and delete a birthday gift voucher')
def edit_and_delete_birthday_gift_voucher(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.edit_and_delete_birthday_gift_voucher()

@then('I can return to the membership application page')
def return_to_membership_application(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.back_to_membership_application()


# DOCUMENT MANAGEMENT
@allure.feature('Document Management')
@allure.story('Document Management in Membership Application')
@pytest.mark.navigation
@pytest.mark.run(order=79)
@given('I am on the membership application page')
def in_membership_application_page(driver):
    pass

@when('I tap on document management')
def tap_document_management(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.tap_document_management()
    
@then('I can add a document')
def add_document(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.add_document()

@then('I can edit, preview, and share a document')
def edit_preview_share_document(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.edit_preview_share_document()


# DISABLED DOCUMENT MANAGEMENT
@allure.feature('Disabled Document Management')
@allure.story('Disabled Document Management in Membership Application')
@pytest.mark.navigation
@pytest.mark.run(order=80)
@given('I am in the document management section')
def in_document_management_section(driver):
    pass

@when('I disable a document')
def disable_document(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.disable_document()
    
@then('I click on the disabled tab')
def click_disabled_tab(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.click_disabled_tab()
    
@then('I can reactivate a disabled document')
def reactivate_disabled_document(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.reactivate_disabled_document()

@then('I can edit and reactivate another disabled document')
def edit_disabled_document(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.edit_and_reactivate_disabled_document()

@then('I can successfully return to the membership application page')
def return_to_membership_application(driver):
    pass



# BONUS POINT RATIO MANAGEMENT
@allure.feature('Bonus Point Ratio Management')
@allure.story('Bonus Point Ratio Management in Membership Application')
@pytest.mark.navigation
@pytest.mark.run(order=81)
@given('I am on the membership application page')
def in_membership_application_page(driver):
    pass

@when('I tap on bonus points')
def tap_bonus_points(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.tap_bonus_points()

@then('I can freely set the bonus point ratio')
def set_bonus_point_ratio(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.set_bonus_point_ratio()

@then('I can return to the membership application page')
def return_to_membership_application(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.back_to_membership_application()
    
    
    
# CUSTOM MEMBERSHIP REGISTRATION
@allure.feature('Custom Membership Registration')
@allure.story('Custom Membership Registration in Membership Application')
@pytest.mark.navigation
@pytest.mark.run(order=82)
@given('I am on the membership application page')
def in_membership_application_page(driver):
    pass

@when('I tap on custom membership registration fields')
def tap_custom_membership_registration_fields(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.tap_custom_membership_registration_fields()

@then('I can add a new field')
def add_new_field(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.add_new_field()

@then('I can edit or delete a field')
def edit_or_delete_field(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.edit_and_delete_field()
    
@then('I can return to the membership application page')
def return_to_membership_application(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.back_to_membership_application()  
    
@then('I can tap the return to calendar button to go back to the calendar page')
def tap_return_to_calendar_button(driver):
    member_apply_page = MemberApplyPage(driver)
    member_apply_page.return_to_membership_application()
    
    
    


    