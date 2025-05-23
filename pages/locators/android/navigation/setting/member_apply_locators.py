from appium.webdriver.common.appiumby import AppiumBy

class MemberApplyLocators:
    ################# BRANCH SETTING #################

    # BRANCH SETTING SECTION
    MEMBER_APPLY_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="會員應用"]')

    ##################################################


    ################# VOUCHER MANAGEMENT #################

    # VOUCHER SECTION
    MEMBER_APPLY = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("會員應用")')

    ##################################################