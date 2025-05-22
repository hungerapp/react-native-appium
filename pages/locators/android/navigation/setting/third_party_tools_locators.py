from appium.webdriver.common.appiumby import AppiumBy

class ThirdPartToolsPageLocators:
    ############# Branch Settings Page Locators ##############
    THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="第三方工具整合"]')
    SUBSCRIPTION_PLAN_IN_BRANCH_SETTINGS_PAGE = lambda self, subscription_name: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{subscription_name}"]')
    #########################################################

    ############ Third Party Tools Settings Page Locators ############
    BACK_BUTTON_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="arrow-left"]')
    SMS_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="簡訊"]')
    LINE_OA_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="LINE官方帳號"]')
    PAYMENT_INTEGRATION_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="金流整合"]')
    BACK_TO_CALENDAR_BUTTON_IN_THIRD_PART_TOOLS_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="calendar"]')
    #################################################################

    ############## Feature Unsupported Dialog Locators ##############
    SUBSCRIPTION_PLAN_NOW_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="立即訂閱付費方案"]')
    #############################################################

    ############## SMS Settings Page Locators ##############
    CLOSE_BUTTON_IN_SMS_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    SENT_SMS_COUNT_IN_SMS_SETTINGS_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0")')
    APPOINTMENT_SUCCESS_SMS_SWITCH_IN_SMS_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, '預約成功簡訊-switch-button')
    APPOINTMENT_REMINDER_SMS_SWITCH_IN_SMS_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, '預約提醒簡訊-switch-button')
    ###########################################

    ############## LINE OA Settings Page Locators ##############
    CLOSE_BUTTON_IN_LINE_OA_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    LINE_LIFF_INTEGRATION_IN_LINE_OA_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'LINE官方帳號LIFF串接 (網址式), 由夯客團隊協助串接，你將獲得一個專屬預約網址，須在LINE APP中才能運作')
    LINE_WIDGETS_IN_LINE_OA_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'LINE外掛市集模組 (選單式), 外掛市集模組是使用選單式卡片，透過關鍵字呼叫，並提供預設夯客3格圖文選單')
    NOTIFICATION_SETTINGS_IN_LINE_OA_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, '通知設定, 管理透過LINE發送的通知，你也可以自訂當發出訊息時要一併發送的提醒訊息')
    ############## LINE LIFF Integration Module Locators ##############
    LINE_LIFF_INTEGRATION_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
    LINE_LIFF_INTEGRATION_DISCONNECT_LINE_LIFF_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '解除串接')
    ############ LINE Widgets Integration Module Locators ##############
    LINE_WIDGETS_INTEGRATION_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
    LINE_WIDGETS_INTEGRATION_DISCONNECT_LINE_WIDGETS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '解除串接')
    LINE_WIDGETS_INTEGRATION_HOTCAKE_RICH_MENU_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '使用夯客圖文選單-switch-button')
    ############ LINE OA Notification Settings Module Locators ##############
    LINE_OA_NOTIFICATION_SETTINGS_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
    ############## Appointment Reminder Notification Section Locators ##############
    APPOINTMENT_REMINDER_NOTIFICATION_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '預約提醒通知-switch-button')
    NOTIFICATION_TIME = (AppiumBy.ACCESSIBILITY_ID, '通知時間-fake-field')
    NOTIFICATION_TIME_SELECT = lambda self, time: (AppiumBy.ACCESSIBILITY_ID, f'{time}-popup-option')
    APPOINTMENT_REMINDER_NOTIFICATION_CUSTOM_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("自訂提醒事項-fake-field").instance(0)')
    ############## Appointment Success Notification Section Locators ##############
    APPOINTMENT_SUCCESS_NOTIFICATION_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '預約成功與等待付款通知-switch-button')
    APPOINTMENT_SUCCESS_NOTIFICATION_CUSTOM_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("自訂提醒事項-fake-field").instance(1)')
    ############## Appointment Cancellation Notification Section Locators ##############
    APPOINTMENT_CANCELLATION_NOTIFICATION_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '預約取消通知-switch-button')
    ############## Ticket Notification Section Locators ##############
    TICKET_NOTIFICATION_ON_MANUAL_SEND_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '票券發送通知 (人工發送票券)-switch-button')
    TICKET_NOTIFICATION_ON_AUTO_SEND_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '票券發送通知 (系統自動發送票券)-switch-button')
    ############## Custom Message Dialog Locators ##############
    CUSTOM_MESSAGE_DIALOG_CONFIRM_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="自訂提醒事項-modal-right-button "]')
    CUSTOM_MESSAGE_DIALOG_SWITCH = (AppiumBy.XPATH, '//*[@resource-id="自訂提醒事項-switch-button"]')
    CUSTOM_MESSAGE_DIALOG_MESSAGE = (AppiumBy.XPATH, '//*[@resource-id="自訂提醒事項-textarea-field"]')
    CUSTOM_MESSAGE_DIALOG_MESSAGE_CONFIRM_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="circle-check"]')
    CUSTOM_MESSAGE_DIALOG_MESSAGE_FIELD = (AppiumBy.XPATH, '//*[@resource-id="自訂提醒事項-textarea-input"]')
    ################################################################


    ############## Payment Integration Settings Page Locators ##############
    BACK_BUTTON_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'arrow-left')
    INSTO_INTEGRATION_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@text="INSTO"]/../android.view.ViewGroup//*[@text="進行串接"]')
    LINE_PAY_INTEGRATION_IN_PAYMENT_INTEGRATION_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@text="LINE Pay"]/../android.view.ViewGroup//*[@text="進行串接"]')
    ############## INSTOR Integration Module Locators ##############
    INSTO_INTEGRATION_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    INSTO_INTEGRATION_CONNECT_INSTO_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("進行串接").instance(2)')
    INSTO_INTEGRATION_ACCOUNT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("INSTO帳號(電子郵件)")')
    INSTO_INTEGRATION_PASSWORD_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("INSTO密碼")')
    ############## LINE Pay Integration Module Locators ##############
    LINE_PAY_INTEGRATION_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    LINE_PAY_INTEGRATION_CONNECT_LINE_PAY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("進行串接").instance(2)')
    LINE_PAY_INTEGRATION_ACCOUNT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Channel ID")')
    LINE_PAY_INTEGRATION_PASSWORD_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Channel Secret Key")')
    ############################################################################





