from appium.webdriver.common.appiumby import AppiumBy


class PersonalPageLocators:
      # View basic personal information 
      PROFILE_PICTURE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')
      USERNAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("ann")')
      GREETING_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*保持好心情.*|.*開始美好.*|.*好好休息.*")')
      EMAIL_ADDRESS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*@.*")')


      # View brand list
      BRAND_LIST_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("品牌列表")')
      BRAND_HUNGER_SALON_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("hunger Salon-staging")')
      BRAND_HUNGER_SALON_PROFILE_PICTURE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
      BRANCH_LIST = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      BRANCH_ITEM_TEMPLATE = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup//android.widget.TextView[contains(@text, '{}')]"
      POP_UP_CANCEL_ICON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      FREE_WINDOW_BACK_TO_PERSONAL_PAGE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("返回主頁")')
      TALK_TO_YOU_LATER_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("稍後再說")')
      WAY_TO_GIVE_UP_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("忍痛放棄")')
      BACK_TO_PERSONAL_PAGE_BTN = (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, '分店')]/descendant::com.horcrux.svg.PathView")
      UNEXPECTED_ERROR_BTN = (AppiumBy.ACCESSIBILITY_ID, '關閉')
    
      
      # Branch name list
      BRANCH_NAMES = [
        {"name": "Ultra分店", "locator": (AppiumBy.ACCESSIBILITY_ID, 'Ultra 分店')},
        {"name": "Star分店", "locator": (AppiumBy.ACCESSIBILITY_ID, 'Star分店, 品牌管理員')},
        {"name": "Free分店", "locator": (AppiumBy.ACCESSIBILITY_ID, 'Free分店, 品牌管理員')}
      ]
      
      PRO_BRANCH_NAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pro 分店")')
  
  
      # Quick functions
      ALL_RESERVATIONS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '所有預約')
      GOOGLE_CALENDAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Google 日曆')
      PUSH_NOTIFICATION_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '推播設定')
      INTEGRATE_GOOGLE_CALENDAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Google行事曆, 進行串接')
  
      # Push notification page
      PUSH_NOTTIFICATION_SAVE = (AppiumBy.ACCESSIBILITY_ID, 'check')
  
      # Manage account settings
      SETTINGS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'gear')
      SETTINGS_POPUP = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(7)')
      ACCOUNT_SETTINGS_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帳號設定")')
      LANGUAGE_SETTINGS_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("語言設定")')
      LANGUAGE_CHINESE_OPTION = (AppiumBy.ACCESSIBILITY_ID, '繁體中文, 繁體中文(台灣)')
      LANGUAGE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
  
      
      # For Toggle locators
      TOGGLE_LOCATORS = {
        "wen_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "sally_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "bella_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "dami_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "ella_toggle": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[2]/android.view.ViewGroup'),
        "test_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "918mmm_toggle": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[7]/android.view.ViewGroup[2]/android.view.ViewGroup'),
        "new1_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[8]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "new2_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[9]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "cindy_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[10]/android.view.ViewGroup[2]/android.view.ViewGroup")
      }
      
      
      # Locators for account settings page
      NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, '姓名-text-input')
  
      GENDER_OPTIONS = {
      "男": (AppiumBy.ACCESSIBILITY_ID, "男"),
      "女": (AppiumBy.ACCESSIBILITY_ID, "女"),
      "其他": (AppiumBy.ACCESSIBILITY_ID, "其他")
      }
      
      EMPTY_NAME_ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 此欄位為必填。")')
      BIRTHDAY_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生日")')
      CALENDAR_WINDOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/pickers")')
      CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')
      PHONE_INPUT_INITIAL = (AppiumBy.ACCESSIBILITY_ID, '電話-text-input')
      PHONE_INPUT_CLEAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入電話")')
      EMPTY_PHONE_ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 此欄位為必填。")')
      INVALID_PHONE_ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("格式錯誤")')
      SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      ACCOUNT_SETTINGS_CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
  
      COUNTRY_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down")')
      COUNTRY_CODE_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '+')]")
      CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
      COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      
      
      # Common country code search terms
      COMMON_SEARCH_TERMS = [
            {"keyword": "台", "expected": "+886"},
            {"keyword": "香", "expected": "+852"},
            {"keyword": "日", "expected": "+81"},
            {"keyword": "美", "expected": "+1"},
            {"keyword": "英", "expected": "+44"},
            {"keyword": "新", "expected": "+65"},
            {"keyword": "澳", "expected": "+61"},
            {"keyword": "中", "expected": "+86"}
        ]
  
      SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入國家或號碼進行搜尋")')
