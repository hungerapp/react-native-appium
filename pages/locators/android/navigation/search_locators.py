from appium.webdriver.common.appiumby import AppiumBy


class SearchLocators:
      SEARCH_OPTION = (AppiumBy.ACCESSIBILITY_ID, '搜尋')
      SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜尋")')
      SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+886 972 205690").instance(0)')
      MEMBER_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="會員"]/android.view.ViewGroup')
      MEMBER_RESULT = (AppiumBy.ACCESSIBILITY_ID, '+886 972 205690, 王貝克')
      NO_DATA_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("目前沒有資料")')  