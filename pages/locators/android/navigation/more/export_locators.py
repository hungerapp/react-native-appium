from appium.webdriver.common.appiumby import AppiumBy

class ExportLocators:
    EXPORT_AVAILABLE_TIME_SLOTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("匯出空檔")')
    AVAILABLE_TIME_SLOTS_AS_CALENDAR_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("可預約時段")')
    AVAILABLE_TIME_SLOTS_AS_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("可預約時段")')
    SERVICE_PERSONNEL_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    SERVICE_TESTING_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SERVICE_ITEM_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務項目")')
    MONTH_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("chevron-right").instance(2)')
    MONTH_OPTION = ['2025/03', '2025/04', '2025/05', '2025/06', '2025/07', '2025/08']
    EXPORT_CALENDAR = (AppiumBy.ACCESSIBILITY_ID, '匯出')
    SAVE_IMAGE = (AppiumBy.ACCESSIBILITY_ID, '儲存圖片')
    TEXT_TAB = (AppiumBy.ACCESSIBILITY_ID, '文字')
    DATE_RANGE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("日期區間")')
    END_DATE_BLOCK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("結束日期")')
    RIGHT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right")')
    START_SECTION = (AppiumBy.ACCESSIBILITY_ID, '從')
    COPY_TEXT = (AppiumBy.ACCESSIBILITY_ID, '複製文字')
    QUICK_SELECT_OPTION = ['未來7天', '未來14天', '未來30天']
    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')