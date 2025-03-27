from appium.webdriver.common.appiumby import AppiumBy

class TutorialBookLocators:
    TUTORIAL_BOOK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("教學手冊")')