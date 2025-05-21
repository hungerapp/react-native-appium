from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.invitation_code import InvitationCodePage

scenarios('../../../features/navigation/setting/invitation_code.feature')


# Scenario: Invitation Code
@given("I am on the Branch Settings page")
def on_branch_setting_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_branch_settings_page(), "Branch Settings page not found"

@when("I tap on the invitation code")
def tap_invitation_code(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invitation_code(), "Invitation Code not found in Branch Settings page"

@when("I tap on the invitation code share button")
def tap_invitation_code_share_button(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invitation_code_share_button(), "Invitation Code Share button not found"

@when("I tap on the invited list")
def tap_invited_list_button(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invited_list(), "Invited List button not found"

@when("I tap on the invited list close button")
def tap_invited_list_close_button(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invited_list_close_button(), "Invited List Close button not found"

@when("I tap on the invitation code close button")
def tap_invitation_code_close_button(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invitation_code_close_button(), "Invitation Code Close button not found"

@then("I should see the Branch Settings page")
def verify_branch_settings_page_after_close(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_branch_settings_page(), "Branch Settings page not found"

