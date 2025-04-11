from appium.webdriver.common.appiumby import AppiumBy


class OnboardingLocators:
      START_UPDATE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("開始更新")')
      SELECT_LANGUAGE = (AppiumBy.ACCESSIBILITY_ID, '繁體中文, 繁體中文(台灣)')
      CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '確定')