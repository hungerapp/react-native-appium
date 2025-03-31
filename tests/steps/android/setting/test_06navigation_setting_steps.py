from pytest_bdd import given, when, then, scenarios
from pages.android.navigation.setting.brand import BrandPage
from pages.android.navigation.setting.invitation_code import InvitationCodePage
from pages.android.navigation.setting.service_personnel import ServicePersonnelPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../../features/navigation/setting/brand.feature')
scenarios('../../../../features/navigation/setting/invitation_code.feature')
scenarios('../../../../features/navigation/setting/service_personnel.feature')

BRANCH_NAME = f"Robot_Test_Name_{CommonUseSection.get_current_timestamp()}"
BRANCH_DESCRIPTION = f"Robot_Test_Description_{CommonUseSection.get_current_timestamp()}"
BRANCH_PHONE_NUMBER = f"09{str(CommonUseSection.get_current_timestamp())[-8:]}"
BRANCH_ADDRESS = f"地球路{str(CommonUseSection.get_current_timestamp())[-3:]}號"
SERVICE_PERSONNEL_NAME = f"Robot_{CommonUseSection.get_current_timestamp()}"
# SERVICE_PERSONNEL_NAME = "Robot_edit_20250331151040253"
SERVICE_PERSONNEL_INTRODUCTION = f"Robot_Test_Introduction_{CommonUseSection.get_current_timestamp()}"
# EDIT_SERVICE_PERSONNEL_NAME = f"Robot_edit_{CommonUseSection.get_current_timestamp()}"
EDIT_SERVICE_PERSONNEL_NAME = "Robot_edit_20250331154203197"
EDIT_SERVICE_PERSONNEL_INTRODUCTION = f"Robot__edit_Test_Introduction_{CommonUseSection.get_current_timestamp()}"

# Scenario: Navigate to Branch Settings and Edit Branch Information
@given("I tap the Settings button in the navigation bar")
def tap_setting_option_in_navigation_bar(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_settings_option()

@then("I should see the Branch Settings Page")
def verify_branch_settings_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the Branch Name in the Branch Information section in the Branch Settings page")
def tap_branch_name_in_branch_setting_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_name_in_branch_setting_page()

@then("I should see the Branch and Brand Information page")
def verify_branch_name_in_branch_setting_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_branch_info_page(), "Branch Name not found in Branch Settings page"

@then("I modify the branch name")
def enter_new_branch_name_in_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    brand_page.enter_new_branch_name_in_branch_brand_info_page(BRANCH_NAME)
    brand_page.verify_branch_name_updated_in_branch_brand_info_page(BRANCH_NAME)

@then("I modify the branch description")
def enter_new_branch_description_in_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_description_in_branch_information_page()
    brand_page.enter_new_branch_description_in_description_dialog(BRANCH_DESCRIPTION)
    brand_page.tap_confirm_button_in_description_dialog()
    brand_page.verify_branch_description_updated(BRANCH_DESCRIPTION)

@then("I turn on the Show Branch Phone Toggle")
def tap_show_branch_phone_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_phone_toggle_off()
    brand_page.tap_branch_phone_toggle()
    assert brand_page.verify_branch_phone_turn_on(), "Branch phone information section is not displayed"

@then("I modify the branch phone number")
def enter_new_branch_phone_number(driver):
    brand_page = BrandPage(driver)
    brand_page.select_branch_phone_county_code()
    brand_page.select_branch_phone_county_code_tw()
    brand_page.enter_new_branch_phone_number(BRANCH_PHONE_NUMBER)

@then("I turn on the Show Branch Address Toggle")
def tap_show_branch_address_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_address_toggle_off()
    brand_page.tap_branch_address_toggle()
    assert brand_page.verify_branch_address_turn_on(), "Branch address information section is not displayed"

@then("I modify the branch address")
def enter_new_branch_address(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_address_city_in_branch_brand_info_page()
    brand_page.scroll_city_dialog()
    brand_page.select_random_city()
    brand_page.tap_branch_address_district_in_branch_brand_info_page()
    brand_page.scroll_district_dialog()
    brand_page.select_random_district()
    brand_page.enter_new_branch_address(BRANCH_ADDRESS)

@then("I tap on the expand brand settings button")
def tap_expand_brand_settings_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_expand_brand_settings_button()

@then("the brand settings section should be expanded")
def verify_brand_settings_section_expanded(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_brand_settings_section_expanded(), "Brand settings section not expanded"

@then("I tap the Confirm Edit button in the Branch and Brand Information page")
def tap_confirm_edit_button_in_branch_brand_info_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_confirm_edit_button_in_branch_brand_info_page()

@then("I should return to the Branch Settings page")
def verify_return_to_branch_settings_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_return_to_branch_settings_page(), "Failed to return to Branch Settings page"

# Scenario: Turn Off Branch Phone Display And Address Display
@given("I tap on the Branch Name in the Branch Information section in the Branch Settings page")
def tap_branch_name_in_branch_setting_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_name_in_branch_setting_page()

@when("I turn off the Show Branch Phone Toggle")
def tap_show_branch_phone_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_phone_toggle_on()
    brand_page.tap_branch_phone_toggle()
    assert brand_page.verify_branch_phone_turn_off(), "Branch phone information section is displayed"

@then("I turn off the Show Branch Address Toggle")
def tap_show_branch_address_toggle(driver):
    brand_page = BrandPage(driver)
    brand_page.is_branch_address_toggle_on()
    brand_page.tap_branch_address_toggle()
    assert brand_page.verify_branch_address_turn_off(), "Branch address information section is displayed"

# Scenario: Verify Pro Business Plan Features and Navigation
@given("I am on the Branch Settings page")
def verify_on_branch_settings_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"

@then("my branch has a Pro Business plan subscription")
def verify_pro_business_plan(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_pro_business_plan(), "Pro Business plan not found"

@when("I tap on the Branch Information option section's Branch Purchase Plan")
def tap_branch_purchase_plan(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_branch_purchase_plan()

@then("I should be navigated to the Plan Management page")
def verify_plan_management_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_plan_management_page(), "Plan Management page not found"

@when("I tap on the view next plan details button")
def tap_view_next_plan_details_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_view_next_plan_details_button()

@then("the Payment Details dialog should be displayed")
def verify_payment_details_dialog(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_payment_details_dialog(), "Payment Details dialog not found"

@when("I tap on the close button in the Payment Details dialog")
def tap_close_button_in_payment_details_dialog(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_close_button_in_payment_details_dialog()

@then("the Payment Details dialog should be dismissed")
def verify_payment_details_dialog_dismissed(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_payment_details_dialog_dismissed(), "Payment Details dialog not dismissed"

@when("I tap on the plan change button")
def tap_plan_change_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_plan_change_button()

@then("I should be navigated to the Plan Change page")
def verify_plan_change_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_plan_change_page(), "Plan Change page not found"

@when("I tap the select Pro business plan button")
def tap_pro_business_plan_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_pro_business_plan_button()

@then("I should be navigated to the Pro Business plan page")
def verify_pro_business_plan_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_pro_business_plan_page(), "Pro Business plan page not found"

@then("the select Pro Business plan button should be disabled")
def verify_pro_business_plan_button_disabled(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_pro_business_plan_button_disabled(), "Pro Business plan button is enabled"

@when("I tap the different plan button on the Pro Business plan page")
def tap_different_plan_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_different_plan_button()

@then("I should see the Pro Business plan content in the plan functionality dialog")
def verify_pro_business_plan_content_in_plan_functionality_dialog(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_pro_business_plan_content_in_plan_functionality_dialog(), "Pro Business plan content not found in Plan Functionality dialog"

@when("I switch to the Start New tab")
def switch_to_star_new_tab(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_star_new_tab()

@then("I should see the Start New plan content in the plan functionality dialog")
def verify_star_new_plan_content_in_plan_functionality_dialog(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_start_new_plan_content_in_plan_functionality_dialog(), "Star new plan content not found in Plan Functionality dialog"

@when("I switch to the Free Trial tab")
def switch_to_free_plan_tab(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_free_plan_tab()

@then("I should see the Free Trial plan content in the plan functionality dialog")
def verify_free_plan_content_in_plan_functionality_dialog(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_free_plan_content_in_plan_functionality_dialog(), "Free trial plan content not found in Plan Functionality dialog"

@when("I tap the close button plan functionality dialog button")
def tap_close_plan_functionality_dialog_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_close_plan_functionality_dialog_button()

@then("the plan functionality dialog should be dismissed")
def verify_plan_functionality_dialog_dismissed(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_plan_functionality_dialog_dismissed(), "Plan Functionality dialog not dismissed"

@when("I tap the close button in the Start New Plan page")
def tap_close_button_in_start_new_plan_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_close_button_in_start_new_plan_page()

@when("I tap the close button in the Pro Business plan page")
def tap_close_button_in_pro_business_plan_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_close_button_in_pro_business_plan_page()

@then("I should be navigated back to the Plan Change page")
def verify_plan_change_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_plan_change_page(), "Plan Change page not found"

@when("I tap the select Start New plan button")
def tap_start_new_plan_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_start_new_plan_button()

@then("I should be navigated to the Start New plan page")
def verify_start_new_plan_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_start_new_plan_page(), "Start new plan page not found"

@then("the select Start New plan button should be enable")
def verify_start_new_plan_button_enabled(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_start_new_plan_button_enabled(), "Start new plan button is disabled"

@when("I switch to the Pro Business plan tab")
def switch_to_pro_business_plan_tab(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_pro_business_plan_tab()

@when("I tap on Downgrade to Free Trial Plan in the Plan Change page")
def tap_downgrade_to_free_trial_plan(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_downgrade_to_free_trial_plan()

@then("the Cancel Payment Plan dialog should be displayed")
def verify_cancel_payment_plan_dialog(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_cancel_payment_plan_dialog(), "Cancel Payment Plan dialog not found"

@when("I tap on Cancel button in the Cancel Payment Plan dialog")
def tap_cancel_button_in_cancel_payment_plan_dialog(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_cancel_button_in_cancel_payment_plan_dialog()

@then("the Cancel Payment Plan dialog should be dismissed")
def verify_cancel_payment_plan_dialog_dismissed(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_cancel_payment_plan_dialog_dismissed(), "Cancel Payment Plan dialog not dismissed"

@when("I tap close button in the Plan Change page")
def tap_close_button_in_plan_change_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_close_button_in_plan_change_page()

@when("I tap on the Payment Records section")
def tap_payment_records_section(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_payment_records_section()

@then("I should be navigated to the Payment Records page")
def verify_payment_records_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_payment_records_page(), "Payment Records page not found"

@when("I tap close button in the Payment Records page")
def tap_close_button_in_payment_records_page(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_close_button_in_payment_records_page()

@when("I tap back hotcake app button")
def tap_back_hotcake_app_button(driver):
    brand_page = BrandPage(driver)
    brand_page.tap_back_hotcake_app_button()

@then("I should be navigated to the Branch Settings page")
def verify_branch_settings_page(driver):
    brand_page = BrandPage(driver)
    assert brand_page.verify_branch_settings_page(), "Branch Settings page not found"

# Invitation Code Page
# Scenario: Verify Invitation Code Management Flow
@when("I tap on Invitation Code in the Branch Settings page")
def tap_invitation_code_in_branch_settings_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invitation_code_in_branch_settings_page(), "Invitation Code not found in Branch Settings page"

@then("I should be navigated to the Invitation Code page")
def verify_invitation_code_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_invitation_code_page(), "Invitation Code page not found"

@when("I tap on Invitation Code Sharing")
def click_invitation_code_sharing(driver):
    invitation_code_page = InvitationCodePage(driver)
    invitation_code_page.tap_invitation_code_sharing()

@then("the Invitation Code Sharing dialog is displayed")
def verify_invitation_code_sharing_dialog(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_invitation_code_sharing_dialog(), "Invitation Code Sharing dialog not found"

@when("I tap on Copy in the Invitation Code Sharing dialog")
def tap_copy_in_invitation_code_sharing_dialog(driver):
    invitation_code_page = InvitationCodePage(driver)
    invitation_code_page.tap_copy_button_in_invitation_code_sharing_dialog()

@then("the Invitation Code Sharing dialog is dismissed")
def verify_invitation_code_sharing_dialog_dismissed(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_invitation_code_sharing_dialog_dismissed(), "Invitation Code Sharing dialog not dismissed"

@when("I tap on Invited List in the Invitation Code page")
def tap_invited_list_in_invitation_code_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    invitation_code_page.tap_invited_list_in_invitation_code_page()

@then("I should be navigated to the Invited List page")
def verify_invited_list_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_invited_list_page(), "Invited List page not found"

@when("I tap on Close Button in the Invited List page")
def tap_close_button_in_invited_list_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    invitation_code_page.tap_close_button_in_invited_list_page()

@then("I should be navigated back to the Invitation Code page")
def verify_invitation_code_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_invitation_code_page(), "Invitation Code page not found"

@when("I tap on Close Button in the Invitation Code page")
def tap_close_button_in_invitation_code_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    invitation_code_page.tap_close_button_in_invitation_code_page()

@then("I should be navigated back to the Branch Settings page")
def verify_branch_settings_page(driver):
    band_page = BrandPage(driver)
    assert band_page.verify_branch_settings_page(), "Branch Settings page not found"

# Scenario: Verify Service Personnel Management Flow
@when("I tap on Service Personnel in the Branch Settings page")
def tap_service_personnel_in_branch_settings_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.tap_service_personnel_in_branch_settings_page()

@then("I should be navigated to the Service Personnel page")
def verify_service_personnel_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_page(), "Service Personnel page not found"

@when("I tap on Add Service Personnel in the Service Personnel page")
def tap_add_service_personnel_in_service_personnel_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.tap_add_service_personnel_in_service_personnel_page()

@then("the Add Service Personnel Alert Dialog is displayed")
def verify_add_service_personnel_alert_dialog(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_add_service_personnel_alert_dialog(), "Add Service Personnel Alert Dialog not found"

@when("I tap on the Cancel button in the Add Service Personnel Alert Dialog")
def tap_cancel_button_in_add_service_personnel_alert_dialog(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.tap_cancel_button_in_add_service_personnel_alert_dialog()

@then("the Add Service Personnel Alert Dialog is dismissed")
def verify_add_service_personnel_alert_dialog_dismissed(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_add_service_personnel_alert_dialog_dismissed(), "Add Service Personnel Alert Dialog not dismissed"

@when("I tap on the Add button in the Add Service Personnel Alert Dialog")
def tap_add_button_in_add_service_personnel_alert_dialog(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.tap_add_button_in_add_service_personnel_alert_dialog()

@then("I should be navigated to the Add Service Personnel Page")
def verify_add_service_personnel_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_add_service_personnel_page(), "Add Service Personnel page not found"

@when("I add a new service personnel")
def add_new_service_personnel(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.enter_name_in_add_service_personnel_page(SERVICE_PERSONNEL_NAME)
    service_personnel_page.select_random_color_in_personnel_color()
    service_personnel_page.tap_introduction_in_add_service_personnel_page()
    service_personnel_page.verify_personnel_introduction_dialog()
    service_personnel_page.enter_introduction_in_introduction_dialog(SERVICE_PERSONNEL_INTRODUCTION)
    service_personnel_page.tap_confirm_button_in_introduction_dialog()
    service_personnel_page.tap_expand_advanced_settings_button_in_add_service_personnel_page()
    service_personnel_page.verify_advanced_settings_section_expanded()
    service_personnel_page.enter_random_service_count_in_add_service_personnel_page()
    service_personnel_page.tap_confirm_button_in_add_service_personnel_page()

@then("a new service personnel should be successfully added on the Service Personnel page")
def verify_new_service_personnel_added(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_new_service_personnel_added(SERVICE_PERSONNEL_NAME), "New Service Personnel not added successfully"

@when("I edit service personnel")
def edit_service_personnel(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.tap_service_personnel_in_service_personnel_page(SERVICE_PERSONNEL_NAME)
    service_personnel_page.verify_edit_service_personnel_page()
    service_personnel_page.enter_name_in_edit_service_personnel_page(EDIT_SERVICE_PERSONNEL_NAME)
    service_personnel_page.select_random_color_in_personnel_color()
    service_personnel_page.tap_introduction_in_edit_service_personnel_page()
    service_personnel_page.verify_personnel_introduction_dialog()
    service_personnel_page.enter_introduction_in_introduction_dialog(EDIT_SERVICE_PERSONNEL_INTRODUCTION)
    service_personnel_page.tap_confirm_button_in_introduction_dialog()
    service_personnel_page.tap_expand_advanced_settings_button_in_edit_service_personnel_page()
    service_personnel_page.verify_advanced_settings_section_expanded()
    service_personnel_page.enter_random_service_count_in_edit_service_personnel_page()
    service_personnel_page.tap_confirm_button_in_edit_service_personnel_page()

@then("the service personnel details should be updated successfully")
def verify_service_personnel_details_updated(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_updated(EDIT_SERVICE_PERSONNEL_NAME), "Service Personnel details not updated successfully"

@when("I delete service personnel")
def delete_service_personnel(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.tap_service_personnel_in_service_personnel_page(EDIT_SERVICE_PERSONNEL_NAME)
    service_personnel_page.verify_edit_service_personnel_page()
    service_personnel_page.tap_delete_button_in_edit_service_personnel_page()
    service_personnel_page.verify_delete_service_personnel_alert_dialog(EDIT_SERVICE_PERSONNEL_NAME)
    service_personnel_page.enter_delete_text_in_delete_service_personnel_alert_dialog()
    service_personnel_page.tap_delete_button_in_delete_service_personnel_alert_dialog()

@then("the service personnel should not be present in the service personnel list")
def verify_service_personnel_not_present(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    assert service_personnel_page.verify_service_personnel_not_present(EDIT_SERVICE_PERSONNEL_NAME), "Service Personnel still present in the list"
