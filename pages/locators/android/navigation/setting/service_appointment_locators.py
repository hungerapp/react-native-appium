# pages/locators/android/navigation/setting/service_appointment_locators.py
from appium.webdriver.common.appiumby import AppiumBy

class ServiceAppointmentPageLocators:
    # Service Appointment Page
    TITLE_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="服務預約"]')
    BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.ACCESSIBILITY_ID,'arrow-left')
    MEMBER_BOOKING_LINK_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="會員專屬預約連結"]')
    COPY_MEMBER_BOOKING_LINK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.ACCESSIBILITY_ID,'copy')
    SERVICE_PRICE_LIST_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="服務項目(價目表)"]')
    ONLINE_BOOKING_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="網路預約管理"]')
    BOOKING_FAQ_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="預約問題與備註"]")')
    BOOKING_GUIDELINES_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="預約注意事項"]')
    DEPOSIT_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="定金管理"]')
    ADVANCED_FEATURES_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="進階功能"]')
    BACK_TO_CALENDAR_BUTTON_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH,'//*[@text="回到行事曆"]')

    # Service Appointment Page/Member Booking Link Dialog
    MEMBER_BOOKING_LINK_DIALOG_COPY_BUTTON = (AppiumBy.XPATH,'//*[@text="複製連結"]')
    MEMBER_BOOKING_LINK_DIALOG_LINE_OA_LINK_BUTTON = (AppiumBy.XPATH,'//*[@text="申請LINE官方帳號串接"]')

    # Service Appointment Page/Service Item List Page
    TITLE_IN_SERVICE_ITEM_LIST_PAGE = (AppiumBy.XPATH,'//*[@text="服務項目(價目表)"]')
    CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE = (AppiumBy.ACCESSIBILITY_ID,'xmark')
    ADD_FIRST_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE = (AppiumBy.XPATH,'//*[@text="新增第一個分類"]')
    EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE = (AppiumBy.XPATH,'//android.widget.HorizontalScrollView/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE = lambda self, category_name: (AppiumBy.XPATH,f'//android.widget.HorizontalScrollView//*[@text="{category_name}"]')
    ADD_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE = (AppiumBy.XPATH,'//*[@text="新增服務項目"]')
    SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE = lambda self, service_name: (AppiumBy.XPATH,f'//*[@text="{service_name}"]')
    EDIT_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE = lambda self, service_name: (AppiumBy.XPATH,f'//*[@text="{service_name}"]/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    DELETE_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE = lambda self, service_name: (AppiumBy.XPATH,f'//*[@text="{service_name}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')
    # Service Appointment Page/Service Item List Page/Category Management Modal
    CATEGORY_MANAGEMENT_MODAL_TITLE = (AppiumBy.XPATH,'//*[@text="分類管理"]')
    CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH,'//*[@text="分類管理"]/../*[@resource-id="xmark"]')
    CATEGORY_MANAGEMENT_MODAL_ADD_BUTTON = (AppiumBy.XPATH,'//*[@text="新增分類"]')
    CATEGORY_MANAGEMENT_MODAL_NAME = lambda self, category_name: (AppiumBy.XPATH,f'//*[@text="{category_name}"][1]')
    CATEGORY_MANAGEMENT_MODAL_EDIT_BUTTON = lambda self, category_name: (AppiumBy.XPATH,f'//*[@text="{category_name}"][1]/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    CATEGORY_MANAGEMENT_MODAL_DELETE_BUTTON = lambda self, category_name: (AppiumBy.XPATH,f'//*[@text="{category_name}"][1]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')
    # Service Appointment Page/Service Item List Page/Category Management Modal/Delete Category Dialog
    DELETE_CATEGORY_DIALOG_TITLE = (AppiumBy.XPATH,'//*[@text="刪除分類"]')
    DELETE_CATEGORY_DIALOG_DESCRIPTION = lambda self, category_name: (AppiumBy.XPATH,f'//*[@text="確定要刪除 {category_name}？此分類中的所有服務項目也會一併刪除。"]')
    DELETE_CATEGORY_DIALOG_CANCEL_BUTTON = (AppiumBy.XPATH,'//*[@text="取消"]')
    DELETE_CATEGORY_DIALOG_DELETE_BUTTON = (AppiumBy.XPATH,'//*[@text="刪除"]')
    # Service Appointment Page/Service Item List Page/Category Management Modal/Add Category Dialog
    ADD_CATEGORY_DIALOG_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID,'undefined-text-input')
    ADD_CATEGORY_DIALOG_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'check')
    ADD_CATEGORY_DIALOG_CLOSE_BUTTON = (AppiumBy.XPATH,'//*[@content-desc="xmark"][3]')
    # Service Appointment Page/Service Item List Page/Service Item Modal
    SERVICE_ITEM_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH,'//*[@resource-id="xmark"][2]')
    SERVICE_ITEM_MODAL_CONFIRM_BUTTON = (AppiumBy.XPATH,'//*[@resource-id="check"]')
    SERVICE_ITEM_MODAL_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID,'服務名稱-text-input')
    SERVICE_ITEM_MODAL_CODENAME_FIELD = (AppiumBy.ACCESSIBILITY_ID,'服務代號-text-input')
    SERVICE_ITEM_MODAL_INTRODUCTION_SWITCH = (AppiumBy.ACCESSIBILITY_ID,'服務介紹-switch-button')
    SERVICE_ITEM_MODAL_INTRODUCTION = (AppiumBy.ACCESSIBILITY_ID,'undefined-textarea-field')
    SERVICE_ITEM_MODAL_CATEGORY_SELECTION = (AppiumBy.ACCESSIBILITY_ID,'服務分類-select-field')
    SERVICE_ITEM_MODAL_DURATION_FIELD = (AppiumBy.ACCESSIBILITY_ID,'時長-text-input')
    SERVICE_ITEM_MODAL_PRICE_FIELD = (AppiumBy.ACCESSIBILITY_ID,'價格-text-input')
    SERVICE_ITEM_MODAL_DISPLAY_PRICE_SWITCH = (AppiumBy.ACCESSIBILITY_ID,'顯示價格-switch-button')
    SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD = (AppiumBy.ACCESSIBILITY_ID,'顯示方式-fake-field')
    DISPLAY_PRICE_METHOD_SELECTION = lambda self, text: (AppiumBy.ACCESSIBILITY_ID, f'{text}-popup-option') #固定價, 起標價
    SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE = (AppiumBy.ACCESSIBILITY_ID,'子服務類型-fake-field')
    SUB_SERVICE_TYPE_SELECTION = lambda self, text: (AppiumBy.ACCESSIBILITY_ID,f'{text}-popup-option') #單選, 複選
    SERVICE_ITEM_MODAL_ADD_SUB_SERVICE_BUTTON = (AppiumBy.XPATH,'//*[@text="新增子服務"]')
    SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM = lambda self, sub_service_name: (AppiumBy.XPATH,f'//*[@text="子服務"]/../android.view.ViewGroup//*[@text="{sub_service_name}"]')
    # Service Appointment Page/Service Item List Page/Service Item Modal/Category Selection Dialog
    CATEGORY_SELECTION_DIALOG_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'服務分類-close-button')
    CATEGORY_SELECTION_DIALOG_NAME_SELECTION = lambda self, category_name: (AppiumBy.XPATH,f'//*[@text="{category_name}"][1]')
    # Service Appointment Page/Service Item List Page/Service Item Modal/Sub Service Dialog
    SUB_SERVICE_DIALOG_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID,'子服務名稱-text-input')
    SUB_SERVICE_DIALOG_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'新增子服務-modal-right-button ')
    SUB_SERVICE_DIALOG_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'新增子服務-close-button')
    SUB_SERVICE_DIALOG_DURATION_FIELD = (AppiumBy.XPATH,'//*[@text="時長增加"]/../*[@resource-id="undefined-text-input"]')
    SUB_SERVICE_DIALOG_PRICE_FIELD = (AppiumBy.XPATH,'//*[@text="價格增加"]/../*[@resource-id="undefined-text-input"]')
    # Service Appointment Page/Service Item List Page/Service Item Modal/Introduction Modal
    INTRODUCTION_FIELD = (AppiumBy.ACCESSIBILITY_ID, '服務介紹-textarea-input')
    INTRODUCTION_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '服務介紹-close-button')
    INTRODUCTION_CLEAR_BUTTON = (AppiumBy.XPATH, '//*[@text="清除"]')
    INTRODUCTION_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'circle-check')

    # Service Appointment Page/Online Booking Management Page
    TITLE_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH,'//*[@text="網路預約管理"]')
    CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.ACCESSIBILITY_ID,'xmark')
    DESCRIPTION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH,'//*[@text="你可以透過排序管理你的網路預約頁面，並進行網路預約的細節設定，包含開放時間、開放項目等；另外，你也可以將多個服務人員組合在一起，自訂不指定預約組合。 "]')
    ADD_ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH,'//*[@text="新增不指定預約組合"]')
    SERVICE_PERSONNEL_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = lambda self, service_personnel: (AppiumBy.XPATH,f'//*[@text="{service_personnel}"]')
    UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = lambda self, unspecified_service: (AppiumBy.XPATH,f'//*[@content-desc="不指定"]/../*[@text="{unspecified_service}"]')
    EDIT_SERVICE_PERSONNEL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = lambda self, service_personnel: (AppiumBy.XPATH,f'//*[@text="{service_personnel}"]/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    EDIT_ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = lambda self, unspecified_service: (AppiumBy.XPATH,f'//*[@content-desc="不指定"]/../*[@text="{unspecified_service}"]/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    # Add Unspecified Appointment Combination Modal
    ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH,'//*[@resource-id="xmark"][2]')
    ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'check')
    ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID,'組合名稱-text-input')
    ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION = (AppiumBy.ACCESSIBILITY_ID,'組合介紹-textarea-field')
    ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_SERVICE_PERSONNEL_SELECTION = lambda self, service_personnel: (AppiumBy.XPATH,f'//*[@text="{service_personnel}"]')
    # Add Unspecified Appointment Combination Modal/Introduction Dialog
    UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_FIELD = (AppiumBy.ACCESSIBILITY_ID,'組合介紹-textarea-input')
    UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'組合介紹-close-button')
    UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_CLEAR_BUTTON = (AppiumBy.XPATH,'//*[@text="清除"]')
    UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'circle-check')
    # Edit Unspecified Appointment Combination Page
    COMBINATION_TAB_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH,'//*[@content-desc="組合設定"]')
    OPEN_ITEM_TAB_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH,'//*[@content-desc="開放項目"]')
    CLOSE_BUTTON_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.ACCESSIBILITY_ID,'xmark')
    BASIC_INFO_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.ACCESSIBILITY_ID,'基本資訊-fake-field')
    SERVICE_PERSONNEL_SELECTION_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = lambda self, service_personnel: (AppiumBy.XPATH,f'//*[@text="{service_personnel}"]')
    SERVICE_PERSONNEL_SELECTION_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE_ALL = (AppiumBy.XPATH,'//*[@text="全部選取"]')
    DELETE_BUTTON_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH,'//*[@text="刪除不指定組合"]')
    # Basic Info Modal
    BASIC_INFO_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH,'//*[@resource-id="xmark"][2]')
    BASIC_INFO_MODAL_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'check')
    BASIC_INFO_MODAL_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID,'組合名稱-text-input')
    BASIC_INFO_MODAL_INTRODUCTION = (AppiumBy.ACCESSIBILITY_ID,'組合介紹-textarea-field')
    # Edit Service Personnel Page
    OPEN_SITTING_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH,'//*[@text="開放設定"]')
    OPEN_TIME_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH,'//*[@text="開放時間"]')
    OPEN_ITEM_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH,'//*[@text="開放項目"]')
    ONLINE_BOOKING_ENABLE_TOGGLE_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.ACCESSIBILITY_ID,'開放個人網路預約-switch-button')
    AVAILABLE_DAYS_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.ACCESSIBILITY_ID,'開放日-fake-field')
    LATEST_BOOKING_TIME_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.ACCESSIBILITY_ID,'最晚預約時間-fake-field')
    EXPAND_ADVANCED_SETTINGS_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH,'//*[@content-desc="展開進階設定"]')
    CLOSE_ADVANCED_SETTINGS_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.ACCESSIBILITY_ID,'xmark')
    MIN_BOOKING_QUANTITY_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH,'//*[@resource-id="undefined-text-input"][1]')
    MAX_BOOKING_QUANTITY_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH,'//*[@resource-id="undefined-text-input"][2]')
    # Available Days Modal
    AVAILABLE_DAYS_MODAL_SPECIFIC_DATE = (AppiumBy.ACCESSIBILITY_ID,'指定日期-fake-field')
    AVAILABLE_DAYS_MODAL_SPECIFIC_DATE_SELECTION = lambda self, date: (AppiumBy.XPATH,f'//*[@text="每月{date}日"]') if 6 <= date <= 28 else None
    AVAILABLE_DAYS_MODAL_SPECIFIC_TIME = (AppiumBy.XPATH,'//*[@text="指定時間"]')
    AVAILABLE_DAYS_MODAL_MONTH_SELECTION = lambda self, num: (AppiumBy.XPATH,f'//*[@text="開放下{num}個月"]') if 1 <= num <= 6 else None
    AVAILABLE_DAYS_MODAL_MONTH_SELECTION_ALL = (AppiumBy.XPATH,'//*[@text="全部開放"]')
    AVAILABLE_DAYS_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH,'//*[@resource-id="xmark"][2]')
    AVAILABLE_DAYS_MODAL_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'check')
    # Latest Booking Time Modal
    LATEST_BOOKING_TIME_MODAL_TIME_SELECTION = lambda self, text: (AppiumBy.XPATH,f'//*[@text="最晚預約時間"][2]/../android.view.ViewGroup//*[@text="{text}"]')
    LATEST_BOOKING_TIME_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH,'//*[@resource-id="xmark"][2]')
    # Open Item Tab
    MAIN_SERVICE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE = (AppiumBy.ACCESSIBILITY_ID,'主要服務項目-fake-field')
    ONLINE_BOOKING_TYPE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE = (AppiumBy.ACCESSIBILITY_ID,'線上預約選取類型-fake-field')
    ADDITIONAL_SERVICE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE = (AppiumBy.ACCESSIBILITY_ID, '加購服務項目-fake-field')
    ONLINE_BOOKING_TYPE_SELECTION = lambda self, text: (AppiumBy.ACCESSIBILITY_ID,f'{text}-popup-option') #單選, 複選
    # Service Appointment Page/Service Item List Page/Service Item Modal/Service Item Selection Dialog
    SERVICE_ITEM_SELECTION_DIALOG_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'xmark')
    SERVICE_ITEM_SELECTION_DIALOG_CONFIRM_BUTTON = (AppiumBy.XPATH,'//*[@resource-id="check"]')
    SERVICE_ITEM_SELECTION_DIALOG_CLEAR_BUTTON = (AppiumBy.XPATH,'//*[@content-desc="全部清除"]')
    SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_CATEGORY_SELECTION = lambda self, category_name: (AppiumBy.XPATH,f'//*[@text="{category_name}"]')
    SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_SELECTION = lambda self, service_item: (AppiumBy.XPATH,f'//*[@text="{service_item}"]')






    DATE_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/date_selector")')
    TODAY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/today_button")')
    SHOW_EARLY_MORNING_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/show_early_morning_button")')
    TIME_PICKER = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/time_picker")')

    COPY_TODAY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/copy_today_button")')
    COPY_TO_SPECIFIC_DATE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/copy_to_specific_date_button")')
    COPY_TO_SPECIFIC_TIME_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/copy_to_specific_time_button")')
    QUICK_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/quick_close_button")')
    TODAY_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/today_close_button")')
    DATE_RANGE_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/date_range_close_button")')
    CLOSE_ALL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/close_all_button")')

    # Service Item Tab
    SERVICE_ITEM_TAB_CLOSE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/close_button")')
    SERVICE_ITEM_TAB_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.kkbox.app:id/confirm_button")')
    SERVICE_ITEM_TAB_CATEGORY_SELECTION = lambda self, category_name: (AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{category_name}")')
    SERVICE_ITEM_TAB_SERVICE_ITEM_SELECTION = lambda self, service_item: (AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{service_item}")')
    SERVICE_ITEM_TAB_SERVICE_ITEM_SELECTION_ALL = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("所有服務項目")')
    # Online Booking Type Dialog
    ONLINE_BOOKING_TYPE_DIALOG_SINGLE_SELECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("單選")')
    ONLINE_BOOKING_TYPE_DIALOG_MULTIPLE_SELECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("多選")')






