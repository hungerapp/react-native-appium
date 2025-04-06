import pytest
from pytest_bdd import given, when, then, scenarios
from pages.android.navigation.setting.brand import BrandPage
from pages.android.navigation.setting.invitation_code import InvitationCodePage
from pages.android.navigation.setting.service_appointment import ServiceAppointmentPage
from pages.android.navigation.setting.service_personnel import ServicePersonnelPage
from pages.shared_components.common_use import CommonUseSection

scenarios('../../../../features/navigation/setting/brand.feature')
scenarios('../../../../features/navigation/setting/invitation_code.feature')
scenarios('../../../../features/navigation/setting/service_personnel.feature')
scenarios('../../../../features/navigation/setting/service_appointment.feature')

BRANCH_NAME = f"Robot_Test_Name_{CommonUseSection.get_current_timestamp()}"
BRANCH_DESCRIPTION = f"Robot_Test_Description_{CommonUseSection.get_current_timestamp()}"
BRANCH_PHONE_NUMBER = f"09{str(CommonUseSection.get_current_timestamp())[-8:]}"
BRANCH_ADDRESS = f"地球路{str(CommonUseSection.get_current_timestamp())[-3:]}號"
# SERVICE_PERSONNEL_NAME = f"Robot_{CommonUseSection.get_current_timestamp()}"
SERVICE_PERSONNEL_NAME = "Robot_20250406215123090"
SERVICE_PERSONNEL_INTRODUCTION = f"Robot_Test_Introduction_{CommonUseSection.get_current_timestamp()}"
EDIT_SERVICE_PERSONNEL_NAME = "Robot_edit_20250331154203197"
EDIT_SERVICE_PERSONNEL_INTRODUCTION = f"Robot__edit_Test_Introduction_{CommonUseSection.get_current_timestamp()}"
# SERVICE_CATEGORY_NAME = f"Robot_Category_{CommonUseSection.get_current_timestamp()}"
SERVICE_CATEGORY_NAME = "Robot_Category_20250401022219748"
# SERVICE_ITEM_NAME = f"Robot_{CommonUseSection.get_current_timestamp()}"
SERVICE_ITEM_NAME = "Robot_20250402144516846"
SERVICE_ITEM_INTRODUCTION = f"Robot_Test_Service_Item_Introduction_{CommonUseSection.get_current_timestamp()}"
SERVICE_ITEM_CODE = f"{str(CommonUseSection.get_current_timestamp())[-2:]}"
SUB_SERVICE_ITEM_NAME = f"Robot_Sub_Service_Item_{CommonUseSection.get_current_timestamp()}"
EDIT_SUB_SERVICE_ITEM_NAME = f"Robot_Sub_Service_Item_{CommonUseSection.get_current_timestamp()}"
EDIT_SERVICE_ITEM_NAME = f"Robot_Edit_Service_Item_{CommonUseSection.get_current_timestamp()}"
EDIT_SERVICE_ITEM_CODE = f"{str(CommonUseSection.get_current_timestamp())[-2:]}"
EDIT_SERVICE_ITEM_INTRODUCTION = f"Robot_Edit_Service_Item_Introduction_{CommonUseSection.get_current_timestamp()}"
SERVICE_COMBINATION_NAME = f"Robot_Combination_{CommonUseSection.get_current_timestamp()}"
SERVICE_COMBINATION_INTRODUCTION = f"Robot_Test_Combination_Introduction_{CommonUseSection.get_current_timestamp()}"


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

@when("I tap on Invitation Code in the Branch Settings page")
def tap_invitation_code_in_branch_settings_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invitation_code_in_branch_settings_page(), "Invitation Code not found in Branch Settings page"


# Scenario: Verify Invitation Code Management Flow
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

@when("I tap on the close button in the Service Personnel page")
def tap_close_button_in_service_personnel_page(driver):
    service_personnel_page = ServicePersonnelPage(driver)
    service_personnel_page.tap_close_button_in_service_personnel_page()

# Scenario: Verify Service Appointment Management Flow
@when("I tap on Service Appointment in the Branch Settings page")
def tap_service_appointment_in_branch_settings_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.tap_service_appointment_in_branch_settings_page(), "Service Appointment not found in Branch Settings page"
    except Exception as e:
        pytest.fail("Step [I tap on Service Appointment in the Branch Settings page] failed: " + str(e))

@then("I should be navigated to the Service Appointment page")
def verify_service_appointment_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_service_appointment_page(), "Service Appointment page not found"
    except Exception as e:
        pytest.fail("Step [I should be navigated to the Service Appointment page] failed: " + str(e))

@given("I am on the Service Appointment page")
def verify_on_service_appointment_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_service_appointment_page(), "Service Appointment page not found"
    except Exception as e:
        pytest.fail("Step [I am on the Service Appointment page] failed: " + str(e))

@when("I tap the member exclusive booking link copy button")
def tap_member_exclusive_booking_link_copy_button(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.tap_member_exclusive_booking_link_copy_button(), \
            "Member exclusive booking link copy button not found"
    except Exception as e:
        pytest.fail("Step [I tap the member exclusive booking link copy button] failed: " + str(e))

@then("A copy link dialog should be displayed")
def verify_copy_link_dialog(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_copy_link_dialog(), \
            "Copy Link dialog not found"
    except Exception as e:
        pytest.fail("Step [A copy link dialog should be displayed] failed: " + str(e))

@when("I tap copy link in the copy link dialog")
def tap_copy_link_in_copy_link_dialog(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_copy_link_in_copy_link_dialog()
    except Exception as e:
        pytest.fail("Step [I tap copy link in the copy link dialog] failed: " + str(e))

@then("A copy link dialog should be dismissed")
def verify_copy_link_dialog_dismissed(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_copy_link_dialog_dismissed(), "Copy Link dialog not dismissed"
    except Exception as e:
        pytest.fail("Step [A copy link dialog should be dismissed] failed: " + str(e))

@when("I tap the service item in the Service Appointment page")
def tap_service_item_in_service_appointment_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_item_in_service_appointment_page()
    except Exception as e:
        pytest.fail("Step [I tap the service item in the Service Appointment page] failed: " + str(e))

@then("I should be navigated to the Service item page")
def verify_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_service_item_page(), "Service Item page not found"
    except Exception as e:
        pytest.fail("Step [I should be navigated to the Service item page] failed: " + str(e))

@when("I tap the category edit button in the Service item page")
def tap_category_edit_button_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_category_edit_button_in_service_item_page()
    except Exception as e:
        pytest.fail("Step [I tap the category edit button in the Service item page] failed: " + str(e))

@then("I should be navigated to the Category page")
def verify_category_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_category_page(), "Category page not found"
    except Exception as e:
        pytest.fail("Step [I should be navigated to the Category page] failed: " + str(e))

@when("I tap the add category in the Category page")
def tap_add_category_in_category_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_add_category_in_category_page()
    except Exception as e:
        pytest.fail("Step [I tap the add category in the Category page] failed: " + str(e))

@then("I should be navigated to the Add Category page")
def verify_add_category_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_add_category_page(), "Add Category page not found"
    except Exception as e:
        pytest.fail("Step [I should be navigated to the Add Category page] failed: " + str(e))

@when("I add a new category in the Add Category page")
def add_new_category_in_add_category_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.enter_new_category_in_add_category_page(SERVICE_CATEGORY_NAME)
        service_appointment_page.tap_confirm_button_in_add_category_page()
    except Exception as e:
        pytest.fail("Step [I add a new category in the Add Category page] failed: " + str(e))

@then("the category is added successfully")
def verify_category_added(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_category_added(SERVICE_CATEGORY_NAME), \
            "Category not added successfully"
    except Exception as e:
        pytest.fail("Step [the category is added successfully] failed: " + str(e))

@when("I tap the close button in the Category page")
def tap_close_button_in_category_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_close_button_in_category_page()
    except Exception as e:
        pytest.fail("Step [I tap the close button in the Category page] failed: " + str(e))

@then("the category is displayed in the Service item page")
def verify_category_displayed_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_category_displayed_in_service_item_page(SERVICE_CATEGORY_NAME), \
            "Category not displayed in Service Item page"
    except Exception as e:
        pytest.fail("Step [the category is displayed in the Service item page] failed: " + str(e))

@when("I tap the add service item button in the Service item page")
def tap_add_service_item_in_new_category_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_category_item_in_service_item_page(SERVICE_CATEGORY_NAME)
        service_appointment_page.tap_add_service_item_in_service_item_page()
        service_appointment_page.verify_add_service_item_page()
        service_appointment_page.tap_close_button_in_add_service_item_page()
    except Exception as e:
        pytest.fail("Step [I tap the add service item button in the Service item page] failed: " + str(e))

@then("I fill in the service item details")
def fill_in_service_item_details(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_add_service_item_in_service_item_page()
        service_appointment_page.enter_service_item_name_in_add_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.enter_service_code_in_add_service_item_page(SERVICE_ITEM_CODE)
        service_appointment_page.is_introduction_toggle_on_in_add_service_item_page()
        service_appointment_page.tap_introduction_in_add_service_item_page()
        service_appointment_page.verify_service_item_introduction_dialog()
        service_appointment_page.enter_introduction_in_introduction_dialog(SERVICE_ITEM_INTRODUCTION)
        service_appointment_page.tap_confirm_button_in_introduction_dialog()
        service_appointment_page.tap_service_category_in_add_service_item_page()
        service_appointment_page.verify_service_category_dialog()
        service_appointment_page.select_service_category(SERVICE_CATEGORY_NAME)
        service_appointment_page.service_category_dialog_dismissed()
        service_appointment_page.enter_service_duration_in_add_service_item_page("60")
        service_appointment_page.enter_service_price_in_add_service_item_page("1000")
        service_appointment_page.tap_service_display_price_toggle()
        service_appointment_page.tap_service_display_price_toggle()
        service_appointment_page.tap_service_display_method_in_add_service_item_page()
        service_appointment_page.verify_service_display_method_dialog()
        service_appointment_page.select_starting_price_in_service_display_method_dialog()
        service_appointment_page.tap_service_display_method_in_add_service_item_page()
        service_appointment_page.select_fixed_price_in_service_display_method_dialog()
        service_appointment_page.tap_sub_service_type_in_add_service_item_page()
        service_appointment_page.verify_sub_service_type_dialog()
        service_appointment_page.select_multiple_choice_in_sub_service_type_dialog()
        service_appointment_page.tap_sub_service_type_in_add_service_item_page()
        service_appointment_page.select_single_choice_in_sub_service_type_dialog()
        service_appointment_page.tap_add_sub_service_in_add_service_item_page()
        service_appointment_page.verify_add_sub_service_dialog()
        service_appointment_page.enter_sub_service_name_in_add_sub_service_dialog(SUB_SERVICE_ITEM_NAME)
        service_appointment_page.enter_duration_in_add_sub_service_dialog("10")
        service_appointment_page.enter_price_in_add_sub_service_dialog("100")
        service_appointment_page.tap_confirm_button_in_add_sub_service_dialog()
        service_appointment_page.tap_edit_sub_service_in_add_service_item_page(SUB_SERVICE_ITEM_NAME)
        service_appointment_page.verify_edit_sub_service_dialog()
        service_appointment_page.enter_sub_service_name_in_edit_sub_service_dialog(EDIT_SUB_SERVICE_ITEM_NAME)
        service_appointment_page.enter_duration_in_edit_sub_service_dialog("20")
        service_appointment_page.enter_price_in_edit_sub_service_dialog("200")
        service_appointment_page.tap_confirm_button_in_edit_sub_service_dialog()
        service_appointment_page.tap_delete_sub_service_in_add_service_item_page(EDIT_SUB_SERVICE_ITEM_NAME)
        service_appointment_page.tap_confirm_button_in_add_service_item_page()
    except Exception as e:
        pytest.fail("Step [I fill in the service item details] failed: " + str(e))

@then("the service item is added successfully")
def verify_service_item_added(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_category_item_in_service_item_page(SERVICE_CATEGORY_NAME)
        assert service_appointment_page.verify_service_item_added(SERVICE_ITEM_NAME), \
            "Service Item not added successfully"
    except Exception as e:
        pytest.fail("Step [the service item is added successfully] failed: " + str(e))

@when("I edit the service item in the Service item page")
def edit_service_item_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_item_in_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.verify_edit_service_item_dialog()
        service_appointment_page.tap_edit_service_item_in_edit_service_item_dialog()
        service_appointment_page.verify_edit_service_item_page()
        service_appointment_page.tap_close_button_in_edit_service_item_page()
        service_appointment_page.tap_service_item_in_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.tap_edit_service_item_in_edit_service_item_dialog()
        service_appointment_page.edit_service_item_name_in_edit_service_item_page(EDIT_SERVICE_ITEM_NAME)
        service_appointment_page.edit_service_code_in_edit_service_item_page(EDIT_SERVICE_ITEM_CODE)
        service_appointment_page.is_introduction_toggle_on_in_edit_service_item_page()
        service_appointment_page.tap_introduction_in_edit_service_item_page()
        service_appointment_page.verify_service_item_introduction_dialog()
        service_appointment_page.enter_introduction_in_introduction_dialog(EDIT_SERVICE_ITEM_INTRODUCTION)
        service_appointment_page.tap_confirm_button_in_introduction_dialog()
        service_appointment_page.tap_service_category_in_edit_service_item_page()
        service_appointment_page.verify_service_category_dialog()
        service_appointment_page.select_service_category(SERVICE_CATEGORY_NAME)
        service_appointment_page.service_category_dialog_dismissed()
        service_appointment_page.enter_service_duration_in_edit_service_item_page("60")
        service_appointment_page.enter_service_price_in_edit_service_item_page("1000")
        service_appointment_page.tap_service_display_price_toggle()
        service_appointment_page.tap_service_display_method_in_edit_service_item_page()
        service_appointment_page.verify_service_display_method_dialog()
        service_appointment_page.select_starting_price_in_service_display_method_dialog()
        service_appointment_page.tap_service_display_method_in_edit_service_item_page()
        service_appointment_page.select_fixed_price_in_service_display_method_dialog()
        service_appointment_page.tap_sub_service_type_in_edit_service_item_page()
        service_appointment_page.verify_sub_service_type_dialog()
        service_appointment_page.select_multiple_choice_in_sub_service_type_dialog()
        service_appointment_page.tap_confirm_button_in_edit_service_item_page()
    except Exception as e:
        pytest.fail("Step [I edit the service item in the Service item page] failed: " + str(e))

@then("the service item is edited successfully")
def verify_service_item_edited(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_service_item_edited(EDIT_SERVICE_ITEM_NAME), \
            "Service Item not edited successfully"
    except Exception as e:
        pytest.fail("Step [the service item is edited successfully] failed: " + str(e))

@when("I copy the service item in service item page")
def copy_service_item_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_item_in_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.verify_edit_service_item_dialog()
        service_appointment_page.tap_copy_service_item_in_edit_service_item_dialog()
    except Exception as e:
        pytest.fail("Step [I copy the service item in service item page] failed: " + str(e))

@then("the service item is copied successfully")
def verify_service_item_copied(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_service_item_copied(SERVICE_ITEM_NAME), \
            "Service Item not copied successfully"
    except Exception as e:
        pytest.fail("Step [the service item is copied successfully] failed: " + str(e))

@when("I delete the service item in service item page")
def delete_service_item_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_item_in_service_item_page(EDIT_SERVICE_ITEM_NAME)
        service_appointment_page.verify_edit_service_item_dialog()
        service_appointment_page.tap_edit_service_item_in_edit_service_item_dialog()
        service_appointment_page.tap_delete_service_item_in_edit_service_item_page()
        service_appointment_page.verify_delete_service_item_alert_dialog(EDIT_SERVICE_ITEM_NAME)
        service_appointment_page.tap_delete_button_in_delete_service_item_alert_dialog()
    except Exception as e:
        pytest.fail("Step [I delete the service item in service item page] failed: " + str(e))

@then("the service item is deleted successfully")
def verify_service_item_deleted(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_service_item_deleted_in_service_item_page(SERVICE_ITEM_NAME), \
            "Service Item not deleted successfully"
    except Exception as e:
        pytest.fail("Step [the service item is deleted successfully] failed: " + str(e))

@when("I tap delete service item in service item page")
def tap_delete_service_item_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_delete_all_service_item_in_service_item_page(SERVICE_ITEM_NAME)
    except Exception as e:
        pytest.fail("Step [I tap delete service item in service item page] failed: " + str(e))

@when("I add a new service item")
def fill_in_service_item(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_add_service_item_in_service_item_page()
        service_appointment_page.enter_service_item_name_in_add_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.tap_service_category_in_edit_service_item_page()
        service_appointment_page.select_service_category(SERVICE_CATEGORY_NAME)
        service_appointment_page.tap_confirm_button_in_edit_service_item_page()
    except Exception as e:
        pytest.fail("Step [I add a new service item] failed: " + str(e))

@when("I Delete the service category in the Service item page")
def delete_service_category_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_category_edit_button_in_service_item_page()
        service_appointment_page.tap_delete_category_item_in_category_page(SERVICE_CATEGORY_NAME)
        service_appointment_page.tap_delete_button_in_delete_category_item_alert_dialog()
    except Exception as e:
        pytest.fail("Step [I Delete the service category in the Service item page] failed: " + str(e))

@then("the service category is deleted successfully")
def verify_service_category_deleted(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        assert service_appointment_page.verify_service_category_deleted_in_category_page(SERVICE_CATEGORY_NAME), "Service Category not deleted successfully"
        service_appointment_page.tap_close_button_in_category_page()
        service_appointment_page.verify_service_item_page()
        assert service_appointment_page.verify_service_category_deleted_in_service_item_page(SERVICE_CATEGORY_NAME), "Service Category not deleted successfully"
    except Exception as e:
        pytest.fail("Step [the service category is deleted successfully] failed: " + str(e))

@when("I tap the close button in the Service item page")
def tap_close_button_in_service_item_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_close_button_in_service_item_page()
    except Exception as e:
        pytest.fail("Step [I tap the close button in the Service item page] failed: " + str(e))

# Scenario: Verify Online Booking Management
@then("I have added a new service personnel")
def add_new_service_personnel(driver):
    try:
        service_personnel_page = ServicePersonnelPage(driver)
        service_personnel_page.tap_service_personnel_in_branch_settings_page()
        service_personnel_page.tap_add_service_personnel_in_service_personnel_page()
        service_personnel_page.verify_add_service_personnel_alert_dialog()
        service_personnel_page.tap_add_button_in_add_service_personnel_alert_dialog()
        service_personnel_page.enter_name_in_add_service_personnel_page(SERVICE_PERSONNEL_NAME)
        service_personnel_page.tap_confirm_button_in_add_service_personnel_page()
        service_personnel_page.tap_close_button_in_service_personnel_page()
    except Exception as e:
        pytest.fail("Step [I have added a new service personnel] failed: " + str(e))

@then("I have added a new service item")
def add_new_service_item(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_appointment_in_branch_settings_page()
        service_appointment_page.tap_service_item_in_service_appointment_page()
        service_appointment_page.tap_add_service_item_in_service_item_page()
        service_appointment_page.enter_service_item_name_in_add_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.enter_service_duration_in_add_service_item_page("60")
        service_appointment_page.enter_service_price_in_add_service_item_page("1000")
        service_appointment_page.tap_confirm_button_in_add_service_item_page()
        service_appointment_page.tap_close_button_in_service_item_page()
    except Exception as e:
        pytest.fail("Step [I have added a new service item] failed: " + str(e))

@when("I tap the online booking management button in the Service Appointment page")
def tap_online_booking_management_button_in_service_appointment_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_online_booking_management_button_in_service_appointment_page()
    except Exception as e:
        pytest.fail("Step [I tap the online booking management button in the Service Appointment page] failed: " + str(e))

@then("I should be navigated to the Online Booking Management page")
def verify_online_booking_management_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.verify_online_booking_management_page()
    except Exception as e:
        pytest.fail("Step [I should be navigated to the Online Booking Management page] failed: " + str(e))

@when("I tap the personal online booking management in the Online Booking Management page")
def tap_personal_online_booking_management_in_online_booking_management_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_personal_online_booking_management_in_online_booking_management_page(SERVICE_PERSONNEL_NAME)
    except Exception as e:
        pytest.fail("Step [I tap the personal online booking management in the Online Booking Management page] failed: " + str(e))

@then("I should be navigated to the Personal Online Booking page")
def verify_personal_online_booking_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.verify_personal_online_booking_page(SERVICE_PERSONNEL_NAME)
    except Exception as e:
        pytest.fail("Step [I should be navigated to the Personal Online Booking page] failed: " + str(e))

@then("I configure open days in the Open Setting tab in the Personal Online Booking page")
def configure_open_days_in_open_setting_tab(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_open_setting_tab_in_personal_online_booking_page()
        service_appointment_page.tap_open_days_in_open_setting_tab()
        service_appointment_page.tap_random_specific_day_in_open_days()
        service_appointment_page.tap_specific_time_in_open_days()
        service_appointment_page.tap_random_open_months_available_in_open_days()
        service_appointment_page.tap_confirm_button_in_open_days()
    except Exception as e:
        pytest.fail("Step [I configure open days in the Open Setting tab in the Personal Online Booking page] failed: " + str(e))

@then("I configure latest appointment time in the Personal Online Booking page")
def configure_latest_appointment_time_in_personal_online_booking_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_latest_appointment_time_in_personal_online_booking_page()
        service_appointment_page.tap_random_latest_appointment_time_in_latest_appointment_time()
    except Exception as e:
        pytest.fail("Step [I configure latest appointment time in the Personal Online Booking page] failed: " + str(e))

@then("I configure advance setting in the Personal Online Booking page")
def configure_advance_setting_in_personal_online_booking_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_advance_setting_in_personal_online_booking_page()
        service_appointment_page.tap_random_advance_setting_in_advance_setting()
    except Exception as e:
        pytest.fail("Step [I configure advance setting in the Personal Online Booking page] failed: " + str(e))

@then("I configure open time in the Personal Online Booking page")
def configure_open_time_in_personal_online_booking_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_open_time_tab_in_personal_online_booking_page()
        service_appointment_page.tap_open_time_today_in_open_time_tab()
        service_appointment_page.tap_display_early_morning_in_edit_open_time_page()
        service_appointment_page.tap_random_time_in_edit_open_time_page()
        service_appointment_page.tap_close_button_in_edit_open_time_page()
        service_appointment_page.tap_edit_open_time_today_in_open_time_tab()
        service_appointment_page.copy_open_time_in_edit_open_time_page()
        service_appointment_page.tap_specific_time_in_copy_dialog_in_edit_open_time_page()
        service_appointment_page.select_next_day_open_time_in_copy_specific_time_page()
        service_appointment_page.tap_confirm_button_in_copy_specific_time_page()
        service_appointment_page.copy_open_time_in_edit_open_time_page()
        service_appointment_page.tap_date_range_in_copy_dialog_in_edit_open_time_page()
        service_appointment_page.select_repeat_open_time_range_in_copy_range_page()
        service_appointment_page.tap_confirm_button_in_copy_range_page()
        service_appointment_page.tap_quick_close_button_in_edit_open_time_page()
        service_appointment_page.tap_today_close_in_quick_close_dialog()
        service_appointment_page.verify_today_close_dialog()
        service_appointment_page.tap_confirm_button_in_today_close_dialog()
        service_appointment_page.tap_quick_close_button_in_edit_open_time_page()
        service_appointment_page.tap_range_close_in_quick_close_dialog()
        service_appointment_page.select_range_close_in_range_close_page()
        service_appointment_page.tap_confirm_button_in_range_close_page()
        service_appointment_page.tap_quick_close_button_in_edit_open_time_page()
        service_appointment_page.tap_all_close_in_quick_close_dialog()
        service_appointment_page.verify_all_close_dialog()
        service_appointment_page.tap_confirm_button_in_all_close_dialog()
        service_appointment_page.tap_close_button_in_edit_open_time_page()
    except Exception as e:
        pytest.fail("Step [I configure open time in the Personal Online Booking page] failed: " + str(e))

@then("I configure open items in the Personal Online Booking page")
def configure_open_items_in_personal_online_booking_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_open_items_tab_in_personal_online_booking_page()
        service_appointment_page.tap_main_service_item_in_open_items_tab()
        service_appointment_page.tap_service_item_in_select_main_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.tap_confirm_button_in_select_main_service_item_page()
        service_appointment_page.tap_online_booking_item_in_open_items_tab()
        service_appointment_page.tap_single_choice_in_select_online_booking_item_dialog()
        service_appointment_page.tap_additional_service_item_in_open_items_tab()
        service_appointment_page.tap_confirm_button_in_select_additional_service_item_page()
    except Exception as e:
        pytest.fail("Step [I configure open items in the Personal Online Booking page] failed: " + str(e))

@when("I tap the close button in the Personal Online Booking page")
def tap_close_button_in_personal_online_booking_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_close_button_in_personal_online_booking_page()
    except Exception as e:
        pytest.fail("Step [I tap the close button in the Personal Online Booking page] failed: " + str(e))

@when("I close the Personal Online Booking")
def close_personal_online_booking_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_personal_online_booking_management_in_online_booking_management_page(SERVICE_PERSONNEL_NAME)
        service_appointment_page.open_personal_online_booking_toggle()
        service_appointment_page.tap_close_button_in_personal_online_booking_page()
    except Exception as e:
        pytest.fail("Step [I close the Personal Online Booking] failed: " + str(e))

@then("the service personnel should be displayed in the closed online booking section in the Online Booking Management page")
def verify_closed_online_booking_section(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_personal_online_booking_closed_section_expand_in_online_booking_management_page()
        service_appointment_page.verify_personal_online_booking_closed_section_in_online_booking_management_page(SERVICE_PERSONNEL_NAME)
    except Exception as e:
        pytest.fail("Step [the service personnel should be displayed in the closed online booking section in the Online Booking Management page] failed: " + str(e))

@when("I add service unspecified appointment combination")
def add_service_unspecified_appointment_combination(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_add_unspecified_appointment_combination_in_service_appointment_page()
        service_appointment_page.verify_add_unspecified_appointment_combination_page()
        service_appointment_page.enter_unspecified_appointment_combination_name_in_add_unspecified_appointment_combination_page(SERVICE_COMBINATION_NAME)
        service_appointment_page.enter_unspecified_appointment_combination_introduction_in_add_unspecified_appointment_combination_page(SERVICE_COMBINATION_INTRODUCTION)
        service_appointment_page.tap_service_personnel_in_add_unspecified_appointment_combination_page(SERVICE_PERSONNEL_NAME)
        service_appointment_page.tap_confirm_button_in_add_unspecified_appointment_combination_page()
    except Exception as e:
        pytest.fail("Step [I add service unspecified appointment combination] failed: " + str(e))

@then("the service unspecified appointment combination should be added successfully")
def verify_service_unspecified_appointment_combination_added(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.verify_service_unspecified_appointment_combination_added_in_service_appointment_page(SERVICE_COMBINATION_NAME)
    except Exception as e:
        pytest.fail("Step [the service unspecified appointment combination should be added successfully] failed: " + str(e))

@then("I edit service unspecified appointment combination")
def edit_service_unspecified_appointment_combination(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_unspecified_appointment_combination_in_service_appointment_page(SERVICE_COMBINATION_NAME)
        service_appointment_page.tap_open_item_setting_tab_in_edit_unspecified_appointment_combination_page()
        service_appointment_page.tap_main_service_item_in_open_item_setting_tab_in_edit_unspecified_appointment_combination_page()
        service_appointment_page.tap_service_item_in_select_main_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.tap_confirm_button_in_select_main_service_item_page()
        service_appointment_page.tap_close_button_in_edit_unspecified_appointment_combination_page()
    except Exception as e:
        pytest.fail("Step [I edit service unspecified appointment combination] failed: " + str(e))

@when("I Delete service unspecified appointment combination")
def delete_service_unspecified_appointment_combination(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_unspecified_appointment_combination_in_service_appointment_page(SERVICE_COMBINATION_NAME)
        service_appointment_page.tap_delete_button_in_edit_unspecified_appointment_combination_page(SERVICE_COMBINATION_NAME)
    except Exception as e:
        pytest.fail("Step [I Delete service unspecified appointment combination] failed: " + str(e))

@then("the service unspecified appointment combination should be deleted successfully")
def verify_service_unspecified_appointment_combination_deleted(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.verify_service_unspecified_appointment_combination_deleted_in_service_appointment_page(SERVICE_COMBINATION_NAME)
    except Exception as e:
        pytest.fail("Step [the service unspecified appointment combination should be deleted successfully] failed: " + str(e))

@when("I tap the close button in the Online Booking Management page")
def tap_close_button_in_online_booking_management_page(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_close_button_in_online_booking_management_page()
    except Exception as e:
        pytest.fail("Step [I tap the close button in the Online Booking Management page] failed: " + str(e))

@then("I Delete the service item")
def delete_service_item(driver):
    try:
        service_appointment_page = ServiceAppointmentPage(driver)
        service_appointment_page.tap_service_item_in_service_appointment_page()
        service_appointment_page.tap_delete_service_item_in_service_item_page(SERVICE_ITEM_NAME)
        service_appointment_page.tap_delete_button_in_delete_service_item_alert_dialog()
        service_appointment_page.tap_close_button_in_service_item_page()
        service_appointment_page.tap_back_button_in_service_appointment_page()
    except Exception as e:
        pytest.fail("Step [I Delete the service item] failed: " + str(e))

@then("I Delete the service personnel")
def delete_service_personnel(driver):
    try:
        service_personnel_page = ServicePersonnelPage(driver)
        service_personnel_page.tap_service_personnel_in_branch_settings_page()
        service_personnel_page.tap_delete_service_personnel_in_service_personnel_page(SERVICE_PERSONNEL_NAME)
        service_personnel_page.enter_delete_text_in_delete_service_personnel_alert_dialog()
        service_personnel_page.tap_delete_button_in_delete_service_personnel_alert_dialog()
        service_personnel_page.tap_close_button_in_service_personnel_page()
    except Exception as e:
        pytest.fail("Step [I Delete the service personnel] failed: " + str(e))
