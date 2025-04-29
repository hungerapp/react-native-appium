from appium.webdriver.common.appiumby import AppiumBy


class RecordLocators:
      # Record elements
      RECORD_NAV_OPTION = (AppiumBy.ACCESSIBILITY_ID, "紀錄")
      APPOINTMENTS_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("預約")')
      BILLING_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帳單")')
      RECENTLY_ADDED_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近新增")')
      RECENTLY_CANCELED_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近取消")')
      CLAIM_REQUEST_TAB = (AppiumBy.ACCESSIBILITY_ID, '請領')
      FILTER_ICON = (AppiumBy.ACCESSIBILITY_ID, '篩選')
      SEARCH_ICON = (AppiumBy.ACCESSIBILITY_ID, '搜尋帳單編號')
      APPOINTMENT_NUMBER = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "20")]')
      CANCELED_ORDERS = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "20")]')
      INPUT_SAVE = (AppiumBy.XPATH, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      VIEW_DETAILS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視明細")')
      VIEW_REQUEST_CHECKOUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視請領")')
      EXPAND_DETAILS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(2)')
      EXPORT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      VIEW_CHECKOUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視結帳")')
      DELETE_CHECKOUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除結帳")')
      DELETE_REQUEST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除請領")')
      CHECKOUT_NOTE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入結帳備注")')
      EDIT_REMARK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(7)')
      SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      SEARCH_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
      SEARCH_RESULT = (AppiumBy.ACCESSIBILITY_ID, '搜尋結果')
      CHECK_PAYMENT = (AppiumBy.ACCESSIBILITY_ID, '查看支付方式')
      DELETE_CHECKOUT_CONFIRM = (AppiumBy.ACCESSIBILITY_ID, '刪除')
      

    
      FILTER_STAFF_OPTIONS = [
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("QA")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Wen")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Sally")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Bella")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Ella")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Dami")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains ("918")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Test")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("新人1")')
      ]


