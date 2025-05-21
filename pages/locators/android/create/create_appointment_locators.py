from appium.webdriver.common.appiumby import AppiumBy

class CreateAppointmentLocators:
      # Basic element locators
      PERSONAL_PAGE_BACK_TO_CALENDAR_BTN = (AppiumBy.ACCESSIBILITY_ID, '返回')
      CREATE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'calendar-fab-trigger')
      CREATE_APPOINTMENT_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("預約")')
      CONTACT_INFO_SECTION = (AppiumBy.ACCESSIBILITY_ID, '匿名')
      SAVE_DEFAULT_CONTACT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      SERVICE_PERSON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
      SERVICE_TESTING_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
      SERVICE2_PERSON = (AppiumBy.ACCESSIBILITY_ID, '服務人員')
      SERVICE_OTHER_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'checkbox-single-option-2')
      SERVICE_PAGE_TOGGLE_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '該筆預約為指定預約-switch-button')
      SERVICE_PAGE_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'check')
      SERVICE = (AppiumBy.ACCESSIBILITY_ID, '服務')
      SERVICE2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務")')
      TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
      SERVICE_TAB_CONTAINER = (AppiumBy.XPATH, "//android.widget.HorizontalScrollView/android.view.ViewGroup")
      AUTO_TEST_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試服物分類")')
      SERVICE_ITEMS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("測試服務")')
      SAVE_SERVICE1_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(0)')
      SAVE_SERVICE2_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(1)')
      SERVICE_OPTION1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務1")')
      SERVICE_OPTION4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務4")')
      SUB_SERVICE_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, '選擇子服務-modal-right-button ')
      CHANGE_SERVICE_TIME_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      CHANGE_SERVICE_PERSON_COUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      BACK_TO_CALENDAR_BTN = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    
      MEMBER_PASSPORT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查看會員護照")')
      MEMBER_PASSPORT_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("會員護照")')
      MEMBER_PASSPORT_BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      
      
      # Sub-service options
      SUB_SERVICE_OPTIONS = {
        '附加服務1': (AppiumBy.ACCESSIBILITY_ID, 'checkbox-multiple-option-0'),
        '附加服務2': (AppiumBy.ACCESSIBILITY_ID, 'checkbox-multiple-option-1'),
        '附加服務3': (AppiumBy.ACCESSIBILITY_ID, 'checkbox-multiple-option-2'),
      }
    
    
      # Locators for service time and quantity
      SERVICE_TIME_MINUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("minus").instance(0)')
      SERVICE_TIME_PLUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("plus").instance(0)')
      QUANTITY_MINUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("minus").instance(1)')
      QUANTITY_PLUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("plus").instance(1)')

    
      # Note only for business
      NOTE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("筆記 (僅商家可見)")')
      NOTE_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入內容")')
      MODAL_NOTE_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
      
      QUICK_SELECT_NOTE_CONTENT = {
        '自動化測試1': (AppiumBy.ACCESSIBILITY_ID, '自動化測試1'),
        '自動化測試2': (AppiumBy.ACCESSIBILITY_ID, '自動化測試2'),
        '自動化測試3': (AppiumBy.ACCESSIBILITY_ID, '自動化測試3'),
      }
    
      MODAL_NOTE_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'circle-check')
      NOTE_CONTENT_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'check')
    
      ADD_ONE_MORE_SERVICE = (AppiumBy.ACCESSIBILITY_ID, '再新增一筆預約')
      DELETE_SERVICE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'trash-can')
    
      #  Unexpected Cancel  related elements
      CONTACT_CANCEL_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
      SERVICE_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '離開')
    
      # Time section related elements
      TIME = (AppiumBy.XPATH, '//android.widget.TextView[@text="預約時間"]')
      TIME_SLOTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(":")')
      DATE_BLOCK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down")')
      LEFT_DATE_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-left").instance(1)')
      RIGHT_DATE_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right").instance(1)')
      TODAY_TIME_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("今天")')
      LEFT_TIME_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-left")')
      RIGHT_TIME_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right")')
      SAVE_TIME_BTN = (AppiumBy.ACCESSIBILITY_ID, 'check')
      SELECT_BUSY_TIME = (AppiumBy.ACCESSIBILITY_ID, '確定')
      DEPOSIT_BTN = (AppiumBy.ACCESSIBILITY_ID, 'pen-to-square')
      DEPOSIT_TOGGLE_1 = (AppiumBy.ACCESSIBILITY_ID, '定金收取：第 1 筆預約-switch-button')
      DEPOSIT_TOGGLE_2 = (AppiumBy.ACCESSIBILITY_ID, '定金收取：第 2 筆預約-switch-button')
      DEPOSIT_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, '定金-modal-right-button ')
      CONFIRM_CREATE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增預約')

    
      # Contact related elements
      PHONE_INPUT = (AppiumBy.ACCESSIBILITY_ID, '電話-text-input')
      NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, '姓名-text-input')
      PHONE_SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '電話搜尋')
      NAME_SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '姓名搜尋')
      SPECIFIC_SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+886 972 205690")')
      CHANGE_SPECIFIC_SEARCH_RESULT = (AppiumBy.ACCESSIBILITY_ID, '+886 911 111116, Wei 先生, 上次預約姓名： Wei')
      SAVE_CONTACT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      INVALID_PHONE_MSG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 格式錯誤。")')
      CONTACT_BACK_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
      CONTACT_HAS_CHOSEN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("王貝克")')
      CONTACT_PHONE_CHANGE = (AppiumBy.ACCESSIBILITY_ID, '電話-text-input')
     