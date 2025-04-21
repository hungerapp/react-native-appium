from appium.webdriver.common.appiumby import AppiumBy

class AllowAppointmentLocators:
    MORE_OPTION = (AppiumBy.ACCESSIBILITY_ID, '更多')
    ALLOW_APPOINTMENT_SETTINGS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("預約開放設定")')
    
    # edit personal icon
    EDIT_PERSONAL_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(0)')
    
    #personal page locators
    OPEN_APPOINTMENT_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '開放個人網路預約-switch-button')
    OPEN_DAY_SECTION = (AppiumBy.ACCESSIBILITY_ID, '開放日')
    OPEN_DAY_OPTION = [
      (AppiumBy.ACCESSIBILITY_ID, '每月6日'),
      (AppiumBy.ACCESSIBILITY_ID, '每月7日'),
      (AppiumBy.ACCESSIBILITY_ID, '每月8日'),
      (AppiumBy.ACCESSIBILITY_ID, '每月9日'),
      (AppiumBy.ACCESSIBILITY_ID, '每月10日'),
    ]
    TARGET_SECTION_DATE = (AppiumBy.ACCESSIBILITY_ID, '指定日期')
    TARGET_SECTION_TIME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("指定時間")')
    OPEN_MONTH_OPTION = [
      (AppiumBy.ACCESSIBILITY_ID, '開放下1個月'),
      (AppiumBy.ACCESSIBILITY_ID, '開放下2個月'),
      (AppiumBy.ACCESSIBILITY_ID, '開放下3個月'),
      (AppiumBy.ACCESSIBILITY_ID, '開放下4個月'),
      (AppiumBy.ACCESSIBILITY_ID, '開放下5個月'),
      (AppiumBy.ACCESSIBILITY_ID, '開放下6個月'),
      (AppiumBy.ACCESSIBILITY_ID, '全部開放')]
    TARGET_SECTION_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("每月")')
    TARGET_SECTION_CONFIRM = (AppiumBy.ACCESSIBILITY_ID, '我知道了')
    LATEST_RESERVATION_TIME = (AppiumBy.ACCESSIBILITY_ID, '最晚預約時間')
    
    LATEST_RESERVATION_TIME_OPTION = [
      (AppiumBy.ACCESSIBILITY_ID, "不限制 (0分鐘前)"),
      (AppiumBy.ACCESSIBILITY_ID, "30分鐘前"),
      (AppiumBy.ACCESSIBILITY_ID, "1天前 (當天不開放預約)"),
      (AppiumBy.ACCESSIBILITY_ID, "2天前"),
      (AppiumBy.ACCESSIBILITY_ID, "1週前"),
    ]
    
    # expand advanced settings
    EXPAND_ADVANCED_SETTINGS = (AppiumBy.ACCESSIBILITY_ID, '展開進階設定')
    MIN_QUANTITY_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
    MAX_QUANTITY_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
    
    
    
    
    # open time management
    OPEN_TIME_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("開放時間")')
    OPEN_CALENDAR_WINDOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down")')
    ARROW_RIGHT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right").instance(1)')
    ADD_NEW_OPEN_TIME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增時間").instance(1)')
    TIME_SLOTS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, ':')]")
    EDIT_OPEN_TIME1_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(0)')
    EDIT_OPEN_TIME2_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square")')
    COPY_TODAY_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '複製本日')
    QUICK_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '快速關閉')
    CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '確定')
    
    
    QUICK_CLOSE_BUTTON_OPTIONS = [
      '本日關閉',
      '區間關閉',
      '全部關閉'
    ]
    
    COPY_TODAY_BUTTON_OPTIONS = [
      '複製到區間日期',
      '複製到指定日期'
    ]
    
    WEEKDAYS = [
        '週一',
        '週二', 
        '週三', 
        '週四', 
        '週五', 
        '週六',
        '週日'
    ]
    
    START_SECTION = (AppiumBy.ACCESSIBILITY_ID, '從')
    END_DATE_BLOCK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("結束日期")')
    RIGHT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right")')
    
    # save button
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
    
    # close button
    OPEN_TIME_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
    EDIT_OPEN_TIME_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
    CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    
    
    
    # open items management
    OPEN_ITEMS_TAB = (AppiumBy.ACCESSIBILITY_ID, '開放項目')
    
    MAIN_ITEM_SECTION = (AppiumBy.ACCESSIBILITY_ID, '主要服務項目')
    ONLINE_RESERVATION_TYPE_SECTION = (AppiumBy.ACCESSIBILITY_ID, '線上預約選取類型')
    ONLINE_RESERVATION_TYPE_OPTION = [
        '單選-popup-option',
        '複選-popup-option'
    ]
    ADD_ON_SERVICE_ITEMS_SECTION = (AppiumBy.ACCESSIBILITY_ID, '加購服務項目')
    CLEAR_ALL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '全部清除')
    
    TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
    AUTO_TEST_TAB = (AppiumBy.ACCESSIBILITY_ID, '自動化測試服物分類')
    TESTING1_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務1")')
    TESTING2_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務2")')
    TESTING3_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務3")')
    TESTING4_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務4")')
    TESTING5_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務5")')
    SERVICE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')