from appium.webdriver.common.appiumby import AppiumBy

class MemberApplyLocators:
      
      ################# COUCHER MANAGEMENT #################
      
      # VOUCHER SECTION
      MEMBER_APPLY = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("會員應用")')
      VOUCHER_MANAGEMENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("票券管理")')
      DELETE_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '刪除')
      
      
      
      # GENERAL VOUCHER LOCATORS
      ADD_GENERAL_VOUCHER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增一般券')
      VOUCHER_TITLE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入票券名稱")')
      VOUCHER_CONTENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入票券內容")')
      VOUCHER_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
      VOUCHER_CONTENT_INPUT_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      SALES_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '提供店內販售-switch-button')
      SALES_AMOUNT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0")')
      SALES_INPUT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入販售金額")')
      AUTO_DISCOUNT_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '結帳時自動折扣-switch-button')
      DISCOUNT_TYPE_BLOCK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("折扣類型")')
      
      DISCOUNT_OPTIONS = ["現金", "折數"]
      
      DISCOUNT_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0")')
      DISCOUNT_AMOUNT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入折扣金額")')
      DISCOUNT_PERCENTAGE_LIST = ["95", "90", "85", "80", "75", "70", "65", "60", "50"]
      DISCOUNT_PERCENTAGE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入折數")')
      USAGE_PERIOD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)')
      USAGE_OPTIONS = ["不限期", "天數", "到期時間"]
      USAGE_PERIOD_TIME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入天數")')
      USAGE_PERIOD_CHOOSE_TIME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇日期")')
      INCLUDE_PERFORMANCE_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '核銷時計入業績-switch-button')
      INPUT_PERFORMANCE_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入業績金額")')
      OTHER_TICKET_TRANSFER_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '票券轉贈-switch-button')
      ADD_NEW_VOUCHER_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
      EDIT_GENERAL_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(9)')
      DELETE_GENERAL_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
      
      
      
      # BONUS POINT VOUCHER LOCATORS
      BONUS_POINT_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紅利點數兌換券")')
      OPEN_TO_CHANGE_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '開放兌換-switch-button')
      ADD_BONUS_POINT_VOUCHER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增紅利點數兌換券')
      BONUS_POINT_TITLE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入票券名稱")')
      BONUS_POINT_CONTENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入票券內容")')
      BONUS_POINT_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
      BONUS_POINT_CONTENT_INPUT_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      REQUIRED_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0")')
      REQUIRED_AMOUNT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入兌換所需紅利點數")')
      EDIT_BONUS_POINT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(1)')
      DELETE_BONUS_POINT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
    
      
      
      # MEMBERSHIP GIFT TAB LOCATORS
      MEMBERSHIP_GIFT_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("入會禮")')
      ADD_MEMBERSHIP_GIFT_VOUCHER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增入會禮')
      EDIT_MEMBERSHIP_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(1)')
      DELETE_MEMBERSHIP_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
      
      
      
      # BIRTHDAY GIFT TAB LOCATORS
      BIRTHDAY_GIFT_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生日禮")')
      ADD_BIRTHDAY_GIFT_VOUCHER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增生日禮')
      EDIT_BIRTHDAY_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(1)')
      DELETE_BIRTHDAY_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
      
      
      ##################################
      
      
      
      ####################### DOCUMENT MANAGEMENT #######################