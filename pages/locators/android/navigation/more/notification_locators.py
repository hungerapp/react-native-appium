from appium.webdriver.common.appiumby import AppiumBy

class NotificationLocators:
    NOTIFICATION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("通知與消息")')
    VIEW_LATEST_FEATURES_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '查看最新功能')
    BACK_TO_HOTCAKE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("返回夯客APP")')
    ANY_NOTIFICATION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("20")')
    MARK_ALL_AS_READ_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '全部已讀')
    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    