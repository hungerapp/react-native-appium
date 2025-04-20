from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:
      LANGUAGE_SETTING_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '語言設定')
      CHINESE_LANGUAGE = (AppiumBy.ACCESSIBILITY_ID, '繁體中文, 繁體中文(台灣)')
      # language save button may disappear frequently, thus we use uiautomator to find it
      LANGUAGE_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      CONTACT_CS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("聯繫客服")')
      CONTACT_CS_BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '關閉')
      TERMS_AND_CONDITIONS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務條款")')
      TC_BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '返回夯客APP')
      PRIVACY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("隱私權政策")')
      PRIVACY_BACK_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="返回夯客APP"]')
      LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '開始使用')
      EMAIL_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
      LOGIN_CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      EMAIL_NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '下一步')
      ERROR_UNREGISTERED_WINDOW_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("沒有此帳號")')
      ERROR_UNREGISTERED_WINDOW_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請檢查信箱是否輸入正確")')
      ERROR_UNREGISTERED_WINDOW_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '重新輸入')
      MODIFY_EMAIL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '修改信箱')
      IS_VERIFICATION_CODE_PAGE_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("驗證通行碼")')
      VER_CODE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
      VER_SUBMIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '送出')
      FINISH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '完成')
      LOGIN_SUCCESS_POPUP = (AppiumBy.ACCESSIBILITY_ID, '登入成功')
      ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 請填寫正確的電子郵件。")')
      ERROR_WINDOW_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請檢查驗證通行碼是否輸入正確")')
      ERROR_RETRY_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '好')
 


      ### Logout ###
      SETTING_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
      CLICK_WINDOW_LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '登出')
      SURE_TO_LOGOUT = (AppiumBy.ACCESSIBILITY_ID, '確定')
  