from appium.webdriver.common.appiumby import AppiumBy

class TutorialGuideLocators:
    TUTORIAL_GUIDE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("教學導覽")')
    TUTORIAL_VIDEO_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '教學影片')
    SERVICE_STAFF_SECTION = (AppiumBy.ACCESSIBILITY_ID, '1, 服務人員, 預約的基礎，建立你的設計師或老師')
    SERVICE_ITEMS_SECTION = (AppiumBy.ACCESSIBILITY_ID, '2, 服務項目(價目表), 設定你的服務項目，包含時間長度與價格')
    ONLINE_RESERVATION_MANAGEMENT_SECTION = (AppiumBy.ACCESSIBILITY_ID, '3, 網路預約管理, 設定你想要開放的網路預約時間與項目')
    CONNECT_LINE_OFFICIAL_ACCOUNT_SECTION = (AppiumBy.ACCESSIBILITY_ID, '串接LINE官方帳號, 讓你的LINE官方帳號變成預約和會員系統')
    TUTORIAL_BOOK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '教學手冊')
    CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')