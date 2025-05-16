from appium.webdriver.common.appiumby import AppiumBy

class MemberApplyLocators:
      
      ################# VOUCHER MANAGEMENT #################
      
      # VOUCHER SECTION
      MEMBER_APPLY = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("會員應用")')
      VOUCHER_MANAGEMENT = (AppiumBy.ACCESSIBILITY_ID, '票券管理, 提供多種類型的票券設定，可應用於折價券、堂數券、點數券等票券形式')
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
      
      DISCOUNT_OPTIONS = ["現金-popup-option", "折數-popup-option"]
      
      DISCOUNT_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0")')
      DISCOUNT_AMOUNT_INPUT = (AppiumBy.ACCESSIBILITY_ID, '折扣金額-text-input')
      DISCOUNT_PERCENTAGE_LIST = ["95", "90", "85", "80", "75", "70", "65", "60", "50"]
      DISCOUNT_PERCENTAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, '折數-text-input')
      USAGE_PERIOD = (AppiumBy.ACCESSIBILITY_ID, '使用期限')
      USAGE_OPTIONS = ["不限期-popup-option", "天數-popup-option", "到期時間-popup-option"]
      USAGE_PERIOD_TIME_INPUT = (AppiumBy.ACCESSIBILITY_ID, '天數-text-input')
      USAGE_PERIOD_CHOOSE_TIME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇日期")')
      INCLUDE_PERFORMANCE_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '核銷時計入業績-switch-button')
      INPUT_PERFORMANCE_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入業績金額")')
      OTHER_TICKET_TRANSFER_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '票券轉贈-switch-button')
      ADD_NEW_VOUCHER_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
      EDIT_GENERAL_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(5)')
      DELETE_GENERAL_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
      
      
      
      # BONUS POINT VOUCHER LOCATORS
      BONUS_POINT_TAB = (AppiumBy.ACCESSIBILITY_ID, 'category-1')
      OPEN_TO_CHANGE_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '開放兌換-switch-button')
      ADD_BONUS_POINT_VOUCHER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增紅利點數兌換券')
      BONUS_POINT_TITLE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入票券名稱")')
      BONUS_POINT_CONTENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入票券內容")')
      BONUS_POINT_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
      BONUS_POINT_CONTENT_INPUT_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      REQUIRED_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0")')
      REQUIRED_AMOUNT_INPUT = (AppiumBy.ACCESSIBILITY_ID, '兌換所需紅利點數-text-input')
      EDIT_BONUS_POINT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(1)')
      DELETE_BONUS_POINT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
    
      
      
      # MEMBERSHIP GIFT TAB LOCATORS
      MEMBERSHIP_GIFT_TAB = (AppiumBy.ACCESSIBILITY_ID, 'category-2')
      ADD_MEMBERSHIP_GIFT_VOUCHER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增入會禮')
      EDIT_MEMBERSHIP_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(1)')
      DELETE_MEMBERSHIP_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
      RIGHT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right")') 
      
      
      
      # BIRTHDAY GIFT TAB LOCATORS
      BIRTHDAY_GIFT_TAB = (AppiumBy.ACCESSIBILITY_ID, 'category-3')
      ADD_BIRTHDAY_GIFT_VOUCHER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增生日禮')
      EDIT_BIRTHDAY_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(1)')
      DELETE_BIRTHDAY_GIFT_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除票券")')
      
      
      ##################################
      
      
      
      ####################### DOCUMENT MANAGEMENT #######################
      DOCUMENT_MANAGEMENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("文件管理")')
      ADD_DOCUMENT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("新增文件")')
      MEMBER_AUTO_SIGN_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '會員自行簽署與填寫-switch-button')
      CUSTOMER_NEED_TO_SIGN_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '顧客需簽名-switch-button')
      DOCUMENT_NAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入文件標題")')
      ADD_TEXT_PARAGRAPH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增文字段落、問題')
      ADD_TEXT_PROBLEM_OPTIONS = ["新增文字段落", "新增問題"]
      ADD_TEXT_PARAGRAPH_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
      ADD_TEXT_PARAGRAPH_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      NEW_PROBLEM_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入題目名稱")')
      OPTION_TYPE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選項類型")')
      OPTION_TYPE_OPTIONS = ["單選-popup-option", "複選-popup-option", "簡答-popup-option"]
      QUESTION_TYPE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("填答類型")')
      QUESTION_TYPE_OPTIONS = ["必填-popup-option", "選填-popup-option"]
      NEW_OPTION = (AppiumBy.ACCESSIBILITY_ID, '新增選項')
      NEW_OPTION_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("請輸入選項")')
      ADD_CUSTOM_COLUMN_NEW_QUESTION_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(1)')
      ADD_DOCUMENT_ADD_NEW_QUESTION_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(1)')
      ADD_NEW_DOCUMENT_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
      ADD_NEW_COLUMN_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      EDIT_DOCUMENT_TITLE_INPUT = (AppiumBy.ACCESSIBILITY_ID, '文件標題-text-input')
      DOCUMENT_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
      EDIT_DOCUMENT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("circle-ellipsis").instance(9)')
      EDIT_DOCUMENT_OPTIONS = ["編輯文件", "預覽文件", "分享文件連結", "簽署紀錄"]
      PREVIEW_DOCUMENT_BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
      SIGN_RECORD_BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
      SHARE_DOCUMENT_COPY_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '複製')
      
      DISABLE_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("已停用")')
      DISABLE_DOCUMENT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("circle-minus").instance(9)')
      DISABLE_DOCUMENT_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '停用')
      REACTIVATE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrows-repeat").instance(0)')
      REACTIVATE_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '啟用')
      RANDOMLY_EDIT_DISABLE_DOCUMENT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(2)')
      REACTIVATE_DOCUMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '重新啟用')
      
      ##################################
      
      
      
      ######## BONUS POINT RATIO MANAGEMENT ########
      BONUS_POINTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紅利點數")')
      BONUS_POINT_RATIO_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("贈點比例")')
      CHECKOUT_AUTO_SEND_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '結帳自動贈點-switch-button')
      BONUS_POINT_RATIO_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
      BONUS_POINT_RATIO_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
      ##################################
      
      
      
      ########## CUSTOM MEMBERSHIP REGISTRATION ##########
      CUSTOM_MEMBERSHIP_REGISTRATION_FIELDS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自訂會員註冊欄位")')
      ADD_NEW_FIELD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增欄位')
      MEMBER_INPUT_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '開放會員填寫-switch-button')
      FIELD_TITLE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入欄位標題")')
      ADD_NEW_COLUMN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增')
      EDIT_FIELD_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(5)')
      EDIT_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '編輯')
      EDIT_FIELD_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
      DELETE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("circle-minus").instance(5)')
      DELETE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
      RETURN_TO_CALENDAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '回到行事曆')
      
      