from appium.webdriver.common.appiumby import AppiumBy

class CS_Locators:
      CS_OPTION = (AppiumBy.ACCESSIBILITY_ID, "客服")
      MESSAGE_SECTION = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[1]/android.view.View')
      PAST_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'),
      SEND_MESSAGE_TO_US_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("傳訊息給我們")')
      CS_SEND_OPTIONS = [
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("方案與價格")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新手教學")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("通知與提醒")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LINE官方帳號")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("😃 呼叫夯客教練")')
      ]
      MESSAGE_BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button")')
      RECENT_MESSAGE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Profile image for Fin")')
      RECENT_MESSAGE_BACK_BUTTON = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button')
      RECENT_MESSAGE_INPUT_FIELD = (AppiumBy.XPATH, '//android.widget.EditText')
      SEND_MESSAGE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')
      GIF_BUTTON = (AppiumBy.XPATH, '//android.widget.EditText/android.widget.Button[1]')
      GIF_LIST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("(附圖)").instance(0)')
      SEND_GIF_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Send')
  
      # hyper link
      INSTAGRAM_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("追蹤夯客Instagram")')
      PRICING_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("價格與方案")')
      HELP_CENTER_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("幫助中心")')
      MEETING_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("30分鐘")')
  