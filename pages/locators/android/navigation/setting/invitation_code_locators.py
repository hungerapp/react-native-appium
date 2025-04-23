from appium.webdriver.common.appiumby import AppiumBy

class InvitationCodePageLocators:
    # Branch Setting Page
    INVITATION_CODE_IN_BRANCH_SETTING_PAGE = (AppiumBy.XPATH, '//*[@text="邀請碼管理"]')

    # Invitation Code Page
    TITLE_IN_INVITATION_CODE_PAGE = (AppiumBy.XPATH, '//*[@text="已邀請名單"]')
    INVITATION_CODE_IN_INVITATION_CODE_PAGE = (AppiumBy.XPATH, '//*[@text="邀請碼"]/../android.widget.TextView')
    DESCRIPTION_IN_INVITATION_CODE_PAGE = (AppiumBy.XPATH, '//*[@text="邀請好友開始使用夯客吧！在建立新分店時輸入邀請碼，被邀請人可立即獲得 100 點夯幣。"]')
    SHARE_INVITATION_CODE_BUTTON_IN_INVITATION_CODE_PAGE = (AppiumBy.XPATH, '//*[@text="邀請碼"]/../android.view.ViewGroup//*[@resource-id="arrow-up-from-bracket"]')
    INVITED_LIST_IN_INVITATION_CODE_PAGE = (AppiumBy.XPATH, '//*[@text="已邀請名單"]')
    CLOSE_BUTTON_IN_INVITATION_CODE_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    # Share Invitation Code Modal
    COPY_INVITATION_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="com.android.intentresolver:id/copy"]')
    # Invited List Modal
    #Repeat the elements and cannot be caught very much
    # TITLE_IN_INVITED_LIST = (AppiumBy.XPATH, '//*[@text="已邀請名單"]')
    # CLOSE_BUTTON_IN_INVITED_LIST = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')



