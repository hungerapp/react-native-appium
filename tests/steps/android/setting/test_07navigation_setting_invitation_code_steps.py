from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.navigation.setting.invitation_code import InvitationCodePage

scenarios('../../../../features/navigation/setting/invitation_code.feature')

#TODO: 這邊預設你會是在發店設定頁, 所以given的話會是點擊邀請碼管理進入邀請碼頁面
@given("I am on the invitation code page")
def verify_invitation_code_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_invitation_code_page(), "Invitation Code page not found"

@when("I tap on the invitation code share button")
def tap_invitation_code_share_button(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invitation_code_share_button(), "Invitation Code Share button not found"

@then("I should see the invitation code page")
def verify_invitation_code_page(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.verify_invitation_code_page(), "Invitation Code page not found"


# TODO:  這邊這兩條func要修改元素驗證, 目前看locator是沒有的
'''
@when("I tap on the invited list button")
def tap_invited_list_button(driver): 
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invited_list_button(), "Invited List button not found"

@then("I tap on the invited list close button")
def tap_invited_list_close_button(driver):
    invitation_code_page = InvitationCodePage(driver)
    assert invitation_code_page.tap_invited_list_close_button(), "Invited List Close button not found"
'''

