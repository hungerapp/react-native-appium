from appium.webdriver.common.appiumby import AppiumBy

class WebLayoutManagementLocators:
    ############ Branch Settings Page ############
    WEB_LAYOUT_MANAGEMENT_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="網站佈局管理"]')
    CLOSE_BUTTON_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    ##############################################

    ############# Web Layout Management Page ############
    CLOSE_BUTTON_IN_WEB_LAYOUT_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_WEB_LAYOUT_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="check"]')
    ONLINE_SERVICE_APPOINTMENT_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '線上服務預約-switch-button')
    STORED_VALUE_FEATURE_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '儲值金功能-switch-button')
    TICKET_FEATURE_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '票券功能-switch-button')
    BONUS_POINTS_FEATURE_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '紅利點數功能-switch-button')
    WEB_COLOR_SELECTION_IN_WEB_LAYOUT_MANAGEMENT_PAGE = lambda self, num: (AppiumBy.XPATH, f'//android.widget.HorizontalScrollView//android.view.ViewGroup/android.view.ViewGroup[{num}]/android.view.ViewGroup')
    WEEK_START_DAY = (AppiumBy.ACCESSIBILITY_ID, '會員端：預約行事曆起始日-fake-field')
    WEEK_START_DAY_SELECTION = lambda self, day: (AppiumBy.ACCESSIBILITY_ID, f'{day}-popup-option')
    GOOGLE_TACKING_CODE = (AppiumBy.ACCESSIBILITY_ID, 'Google 追蹤代碼-fake-field')
    ############# Web Layout Management Page / Google Tracking CODE Modal ############
    CONFIRM_BUTTON_IN_GOOGLE_TRACKING_CODE_MODAL = (AppiumBy.XPATH, '(//*[@content-desc="check"])[2]')
    GOOGLE_TRACKING_CODE_FIELD_IN_GOOGLE_TRACKING_CODE_MODAL = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
    #####################################################



