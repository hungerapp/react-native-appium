from appium.webdriver.common.appiumby import AppiumBy


class RecordLocators:
      RECORD_ELEMENTS = {
        'records_nav_option': (AppiumBy.ACCESSIBILITY_ID, "紀錄"),
        'appointments_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("預約")'),
        'billing_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帳單")'),
        'recently_added_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近新增")'),
        'recently_canceled_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近取消")'),
        'claim_request_tab': (AppiumBy.ACCESSIBILITY_ID, '請領'),
        'filter_icon': (AppiumBy.ACCESSIBILITY_ID, '篩選'),
        'search_icon': (AppiumBy.ACCESSIBILITY_ID, '搜尋帳單編號'),
        'appointment_number': (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "20")]'),
        'canceled_orders': (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "20")]'),
        'input_save': (AppiumBy.XPATH, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'view_details': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視明細")'),
        'view_request_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視請領")'),
        'expand_details': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(2)'),
        'export_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'view_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視結帳")'),
        'delete_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除結帳")'),
        'delete_request': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除請領")'),
        'checkout_note_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入結帳備注")'),
        'edit_remark': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(7)'),
        'save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'search_field': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)'),
        'search_result': (AppiumBy.ACCESSIBILITY_ID, '搜尋結果'),
        'check_payment': (AppiumBy.ACCESSIBILITY_ID, '查看支付方式'),
        'delete_checkout_confirm': (AppiumBy.ACCESSIBILITY_ID, '刪除')
      }
    
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


