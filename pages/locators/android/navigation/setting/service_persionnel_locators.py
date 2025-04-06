# pages/locators/android/navigation/setting/service_personnel_locators.py
from appium.webdriver.common.appiumby import AppiumBy

class ServicePersonnelPageLocators:
    # Service Personnel Page
    SERVICE_PERSONNEL_IN_BRANCH_SETTING_PAGE = (AppiumBy.XPATH, '//*[@content-desc="服務人員, 新增、編輯你的服務人員，修改照片、名稱、介紹等資訊"]')

    # Service Personnel Page
    TITLE_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="服務人員"]')
    DESCRIPTION_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="「服務人員」是夯客計費的單位，新增後將會增加收費。"]')
    CLOSE_BUTTON_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    ADD_SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="新增服務人員"]')
    SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@content-desc="{text}"]')
    DELETE_SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')

    # Add Service Personnel Alert Dialog
    DESCRIPTION_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@text="夯客的收費方式是以「服務人員數量＊方案價格」計價，新增人員可能會導致費用增加。"]')
    CANCEL_BUTTON_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@content-desc="取消"]')
    ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@content-desc="新增"]')

    # Add Service Personnel Page
    TITLE_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="新增服務人員"]')
    CLOSE_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    UPLOAD_IMAGE_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="上傳圖片"]')
    NAME_FIELD_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="人員名稱"]/../android.widget.EditText')
    CUSTOM_PERSONNEL_COLOR_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="自訂人員顏色"]')
    SELECT_PERSONNEL_COLOR_IN_ADD_SERVICE_PERSONNEL_PAGE = lambda self, index: (AppiumBy.XPATH, f'//*[@text="自訂人員顏色"]/../android.widget.HorizontalScrollView//android.view.ViewGroup//android.view.ViewGroup[{index}]')
    PERSONNEL_INTRODUCTION_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="人員介紹"]/../android.view.ViewGroup')
    EXPAND_ADVANCED_SETTINGS_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="展開進階設定"]')
    SERVICE_COUNT_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="同時服務數量"]')
    SERVICE_COUNT_FIELD_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="同時服務數量"]/../android.widget.EditText')
    SERVICE_QUANTITY_RANGE_IN_ADD_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="數量範圍 1 ~ 99"]')

    # Personnel introduction dialog
    TITLE_IN_PERSONNEL_INTRODUCTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="人員介紹-close-button"]/../*[@text="人員介紹"]')
    CLOSE_BUTTON_IN_PERSONNEL_INTRODUCTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="人員介紹-close-button"]')
    INTRODUCTION_TEXT_IN_PERSONNEL_INTRODUCTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="人員介紹-close-button"]/../android.widget.EditText')
    CLEAR_BUTTON_IN_PERSONNEL_INTRODUCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="清除"]')
    CONFIRM_BUTTON_IN_PERSONNEL_INTRODUCTION_DIALOG = (AppiumBy.XPATH, '//*[@content-desc="circle-check"]')

    # Edit Service Personnel Page
    TITLE_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="編輯服務人員"]')
    CLOSE_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    UPLOAD_IMAGE_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="上傳圖片"]')
    NAME_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="人員名稱"]/../android.widget.EditText')
    CUSTOM_PERSONNEL_COLOR_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="自訂人員顏色"]')
    SELECT_PERSONNEL_COLOR_IN_EDIT_SERVICE_PERSONNEL_PAGE = lambda self, index: (AppiumBy.XPATH, f'//*[@text="自訂人員顏色"]/../android.widget.HorizontalScrollView//android.view.ViewGroup//android.view.ViewGroup[{index}]')
    PERSONNEL_INTRODUCTION_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="人員介紹"]/../android.view.ViewGroup')
    EXPAND_ADVANCED_SETTINGS_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="展開進階設定"]')
    SERVICE_COUNT_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="同時服務數量"]')
    SERVICE_COUNT_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="同時服務數量"]/../android.widget.EditText')
    SERVICE_QUANTITY_RANGE_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="數量範圍 1 ~ 99"]')
    DELETE_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="刪除服務人員"]')

    # Delete Service Personnel Alert Dialog
    TITLE_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@text="※請在下方輸入："]/../*[@text="刪除服務人員"]')
    DESCRIPTION_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG = lambda self, text: (AppiumBy.XPATH, f'//*[@text="確定要刪除 {text}？刪除後，預約、結帳紀錄不會消失，但在部份頁面 (如行事曆、業績統計) 將會隱藏該位人員的資料。※請在下方輸入：Delete"]')
    DELETE_ITEM_1_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@text="※請在下方輸入："]')
    DELETE_ITEM_2_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@text="Delete"]')
    DELETE_INPUT_FIELD_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//android.widget.EditText[@text="Delete"]')
    CANCEL_BUTTON_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@content-desc="取消"]')
    DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG = (AppiumBy.XPATH, '//*[@content-desc="刪除"]')






