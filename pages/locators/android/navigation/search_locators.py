from appium.webdriver.common.appiumby import AppiumBy


class SearchLocators:
      SEARCH_OPTION = (AppiumBy.ACCESSIBILITY_ID, '搜尋')
      SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜尋")')
      SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+886 972 205690").instance(0)')
      MEMBER_TAB = (AppiumBy.ACCESSIBILITY_ID, '會員')
      MEMBER_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("+886 972 205690")')
      NO_DATA_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("目前沒有資料")')  