from appium.webdriver.common.appiumby import AppiumBy

class BrandSettingLocators:
      MORE_OPTION = (AppiumBy.ACCESSIBILITY_ID, '更多')
      BRAND_SETTINGS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("品牌設定")')
      BRAND_NAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("hunger Salon-staging")')
      BRAND_DESCRIPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("夯客提供預約管理、數據分析、會員系統、再行銷工具")')
      BRAND_TITLE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("請輸入品牌名稱")')
      MODAL_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("輸入內容")')
      CLEAR_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")')
      MODAL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')