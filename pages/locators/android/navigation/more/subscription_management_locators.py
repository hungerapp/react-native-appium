from appium.webdriver.common.appiumby import AppiumBy

class SubscriptionManagementLocators():
    SUBSCRIPTION_MANAGEMENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("方案管理")')
    RETURN_TO_CALENDAR_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("返回夯客APP")')
    
    