from appium.webdriver.common.appiumby import AppiumBy

class DepositLocators:
    DEPOSIT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("定金")')
    UNPAID_TAB = (AppiumBy.ACCESSIBILITY_ID, '未付款')
    EDIT_AMOUNT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(0)')
    OPTIONS = ["確定入帳", "不收取", "取消預約"]
    CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '確定')
    PAYMENT_OPTIONS = ["現金", "銀行匯款", "信用卡", "LINE PAY"]
    TRANSFER_NUMBER_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("輸入帳號後五碼")')
    PAID_TAB = (AppiumBy.ACCESSIBILITY_ID, '已付款')
    PAID_INVOICE_ITEM = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NT")')
    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')