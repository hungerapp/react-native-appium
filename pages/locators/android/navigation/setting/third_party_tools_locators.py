from appium.webdriver.common.appiumby import AppiumBy

class ThirdPartToolsPageLocators:
    # Branch Settings Page
    THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="第三方工具整合"]')
    SUBSCRIPTION_PLAN_IN_BRANCH_SETTINGS_PAGE = lambda self, subscription_name: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{subscription_name}"]')
    # Third Party Tools Settings Page
    BACK_BUTTON_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="arrow-left"]')
    SMS_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="簡訊"]')
    LINE_OA_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="LINE官方帳號"]')
    PAYMENT_INTEGRATION_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="金流整合"]')
    # Feature Unsupported Dialog
    SUBSCRIPTION_PLAN_NOW_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="立即訂閱付費方案"]')

