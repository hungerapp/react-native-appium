# pages/locators/android/navigation/setting/service_appointment_locators.py
from appium.webdriver.common.appiumby import AppiumBy

class ServiceAppointmentPageLocators:
    # Branch Setting Page
    SERVICE_APPOINTMENT_IN_BRANCH_SETTING_PAGE = (AppiumBy.XPATH, '//*[@content-desc="服務預約, 設定服務項目、定金、網路預約相關功能，並管理你的網路預約畫面"]')

    # Service Appointment Page
    TITLE_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@text="服務預約"]')
    BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@resource-id="arrow-left"]')
    MEMBER_EXCLUSIVE_LINK_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="服務項目(價目表), 價目表是預約、結帳的計算基礎"]')
    LINK_IN_MEMBER_EXCLUSIVE_LINK_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@text="會員專屬預約連結"]/../android.view.ViewGroup//android.widget.TextView')
    COPY_BUTTON_IN_MEMBER_EXCLUSIVE_LINK_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@resource-id="copy"]')
    SERVICE_ITEM_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="服務項目(價目表), 價目表是預約、結帳的計算基礎"]')
    ONLINE_BOOKING_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="網路預約管理, 設定服務人員和不指定預約組合的開放時間與開放項目，讓會員透過網路就能完成預約"]')
    BOOKING_ISSUE_AND_NOTES_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="預約問題與備註, 讓會員預約時可以填寫問題與備註"]')
    BOOKING_PRECAUTIONS_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="預約注意事項, 讓會員了解你的預約規範"]')
    DEPOSIT_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="定金管理, 依據會員狀態、預約期間，設定每一筆預約的定金"]')
    ADVANCED_SETTINGS_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="進階功能, 預約限制、預約後緩衝時間、營業結束時間、設備管理等進階設定"]')
    BACK_TO_CALENDER_BUTTON_IN_SERVICE_APPOINTMENT_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="回到行事曆"]')

    # Copy Link Dialog
    DESCRIPTION_IN_COPY_LINK_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="此連結可以完成會員註冊跟線上預約，但不支援綁定作業，如LINE綁定。"]')
    COPY_LINK_IN_COPY_LINK_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="複製連結"]')
    APPLY_LINE_LINK_IN_COPY_LINK_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="申請LINE官方帳號串接"]')

    # Service Item Page
    TITLE_IN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務項目(價目表)"]')
    CLOSE_BUTTON_IN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CATEGORY_EDIT_BUTTON_IN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    ADD_SERVICE_ITEM_IN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="新增服務項目"]')
    CATEGORY_ITEM_IN_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')
    SERVICE_ITEM_IN_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    DELETE_SERVICE_ITEM_IN_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')

    # Category Page
    TITLE_IN_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@text="分類管理"]')
    CLOSE_BUTTON_IN_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    ADD_CATEGORY_IN_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@text="新增分類"]')
    CATEGORY_ITEM_IN_CATEGORY_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    DELETE_CATEGORY_ITEM_IN_CATEGORY_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')

    # Add Category Page
    TITLE_IN_ADD_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@text="新增分類"]')
    CLOSE_BUTTON_IN_ADD_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_ADD_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    CATEGORY_NAME_IN_ADD_CATEGORY_PAGE = (AppiumBy.XPATH, '//android.widget.EditText')

    # Add Service Item Page
    TITLE_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="新增服務項目"]')
    CLOSE_BUTTON_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    UPLOAD_IMAGE_BUTTON_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="camera"]')
    SERVICE_ITEM_NAME_FIELD_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務名稱"]/../android.widget.EditText')
    SERVICE_CODE_FIELD_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務代號"]/../android.widget.EditText')
    SERVICE_INTRODUCTION_FIELD_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@content-desc="請輸入服務介紹"]')
    SERVICE_CATEGORY_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務分類"]/../android.view.ViewGroup')
    SERVICE_DURATION_FIELD_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="時長"]/../android.widget.EditText')
    SERVICE_PRICE_FIELD_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="價格"]/../android.widget.EditText')
    SERVICE_DISPLAY_PRICE_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="顯示價格-switch-button"]')
    SERVICE_DISPLAY_METHOD_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="顯示方式"]')
    SUB_SERVICE_TYPE_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="子服務類型"]')
    ADD_SUB_SERVICE_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="新增子服務"]')
    EDIT_SUB_SERVICE_ITEM_IN_ADD_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../*[@resource-id="pen-to-square"]')
    DELETE_SUB_SERVICE_ITEM_IN_ADD_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')
    SERVICE_INTRODUCTION_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="服務介紹-switch-button"]')

    # Introduction Dialog in Add Service Item Page
    CLOSE_BUTTON_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="服務介紹-close-button"]')
    TITLE_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="服務介紹-close-button"]/../*[@text="服務介紹"]')
    CLEAR_BUTTON_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="清除"]')
    CONFIRM_BUTTON_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="circle-check"]')
    INTRODUCTION_FIELD_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="服務介紹-close-button"]/../android.widget.EditText')

    # Service Category Dialog in Add Service Item Page
    CLOSE_BUTTON_IN_SERVICE_CATEGORY_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="服務分類-close-button"]')
    TITLE_IN_SERVICE_CATEGORY_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="服務分類-close-button"]/../*[@text="服務分類"]')
    SERVICE_CATEGORY_ITEM_IN_SERVICE_CATEGORY_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')

    # Service Display Method Dialog in Add Service Item Page
    TITLE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="顯示方式"]')
    STARTING_PRICE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="起標價"]')
    FIXED_PRICE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="固定價"]')

    # Sub Service Type Dialog in Add Service Item Page
    TITLE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="子服務類型"]')
    SINGLE_CHOICE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="單選"]')
    MULTIPLE_CHOICE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="複選"]')

    # Add Sub Service Dialog in Add Service Item Page
    TITLE_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="新增子服務"]')
    CLOSE_BUTTON_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="新增子服務-close-button"]')
    CONFIRM_BUTTON_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="新增子服務-modal-right-button "]')
    SUB_SERVICE_NAME_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="子服務名稱"]/../android.widget.EditText')
    DURATION_INCREASE_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="時長增加"]/../android.widget.EditText')
    PRICE_INCREASE_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="價格增加"]/../android.widget.EditText')

    # Edit Sub Service Item Dialog in Add Service Item Page
    TITLE_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="編輯子服務"]')
    CLOSE_BUTTON_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="編輯子服務-close-button"]')
    CONFIRM_BUTTON_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="編輯子服務-modal-right-button "]')
    SUB_SERVICE_NAME_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="子服務名稱"]/../android.widget.EditText')
    DURATION_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="時長增加"]/../android.widget.EditText')
    PRICE_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="價格增加"]/../android.widget.EditText')

    # Edit Service Item Dialog in Service Item Page
    EDIT_SERVICE_ITEM_IN_SERVICE_ITEM_DIALOG = (AppiumBy.XPATH, '//*[@text="編輯服務項目"]')
    COPY_SERVICE_ITEM_IN_SERVICE_ITEM_DIALOG = (AppiumBy.XPATH, '//*[@text="複製服務項目"]')

    # Edit Service Item Page
    TITLE_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="編輯服務項目"]')
    CLOSE_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    UPLOAD_IMAGE_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="camera"]')
    SERVICE_ITEM_NAME_FIELD_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務名稱"]/../android.widget.EditText')
    SERVICE_CODE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務代號"]/../android.widget.EditText')
    SERVICE_INTRODUCTION_FIELD_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務介紹"]/../../../android.view.ViewGroup//android.view.ViewGroup//android.view.ViewGroup//android.widget.TextView')
    SERVICE_CATEGORY_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="服務分類"]/../android.view.ViewGroup')
    SERVICE_DURATION_FIELD_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="時長"]/../android.widget.EditText')
    SERVICE_PRICE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="價格"]/../android.widget.EditText')
    SERVICE_DISPLAY_PRICE_TOGGLE_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="顯示價格-switch-button"]')
    SERVICE_DISPLAY_METHOD_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="顯示方式"]')
    SUB_SERVICE_TYPE_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="子服務類型"]')
    ADD_SUB_SERVICE_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="新增子服務"]')
    EDIT_SUB_SERVICE_ITEM_IN_EDIT_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../*[@resource-id="pen-to-square"]')
    DELETE_SUB_SERVICE_ITEM_IN_EDIT_SERVICE_ITEM_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')
    DELETE_SERVICE_ITEM_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="刪除服務項目"]')

    # Delete Service Item Alert Dialog in Edit Service Item Page
    TITLE_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="刪除服務"]')
    DESCRIPTION_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="確定要刪除 {text}？"]')
    CANCEL_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="取消"]')
    DELETE_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="刪除"]')

    # Delete Service Item Alert Dialog in Service Item Page
    TITLE_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="刪除服務"]')
    DESCRIPTION_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_SERVICE_ITEM_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="確定要刪除 {text}？"]')
    CANCEL_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="取消"]')
    DELETE_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="刪除"]')

    # Delete Category Item Alert Dialog in Category Page
    TITLE_IN_DELETE_CATEGORY_ITEM_ALERT_DIALOG_IN_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@text="刪除分類"]')
    DESCRIPTION_IN_DELETE_CATEGORY_ITEM_ALERT_DIALOG_IN_CATEGORY_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="確定要刪除 {text}？此分類中的所有服務項目也會一併刪除。"]')
    CANCEL_BUTTON_IN_DELETE_CATEGORY_ITEM_ALERT_DIALOG_IN_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@content-desc="取消"]')
    DELETE_BUTTON_IN_DELETE_CATEGORY_ITEM_ALERT_DIALOG_IN_CATEGORY_PAGE = (AppiumBy.XPATH, '//*[@content-desc="刪除"]')

    # Online Booking Management Page
    TITLE_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="網路預約管理"]')
    DESCRIPTION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="你可以透過排序管理你的網路預約頁面，並進行網路預約的細節設定，包含開放時間、開放項目等；另外，你也可以將多個服務人員組合在一起，自訂不指定預約組合。 "]')
    CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="新增不指定預約組合"]')
    PERSONAL_ONLINE_BOOKING_MANAGEMENT_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')
    PERSONAL_ONLINE_BOOKING_CLOSE_EXPAND_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@content-desc="個人網路預約關閉"]')
    SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="不指定"]/../../*[@text="{text}"]')
    # Add Service Unspecified Appointment Combination Page
    TITLE_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="新增不指定預約組合"]')
    CLOSE_BUTTON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    UPLOAD_IMAGE_BUTTON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@resource-id="camera"]')
    COMBINATION_NAME_FIELD_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="組合名稱"]/../android.widget.EditText')
    COMBINATION_INTRODUCTION_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="組合介紹"]/../android.view.ViewGroup')
    ALL_SELECTED_SERVICE_PERSON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="全部選取"]')
    SELECT_SERVICE_PERSON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    # Combination Introduction Dialog in Add Service Unspecified Appointment Combination Page
    CLOSE_BUTTON_IN_COMBINATION_INTRODUCTION_DIALOG_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@resource-id="組合介紹-close-button"]')
    CLEAR_BUTTON_IN_COMBINATION_INTRODUCTION_DIALOG_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="清除"]')
    CONFIRM_BUTTON_IN_COMBINATION_INTRODUCTION_DIALOG_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@resource-id="circle-check"]')
    COMBINATION_INTRODUCTION_FIELD_IN_COMBINATION_INTRODUCTION_DIALOG_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@resource-id="組合介紹-close-button"]/../android.widget.EditText')
    # Personal Online Booking Page
    TITLE_IN_PERSONAL_ONLINE_BOOKING_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    CLOSE_BUTTON_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="開放設定"]')
    OPEN_TIME_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="開放時間"]')
    OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="開放項目"]')
    #Open Setting Tab
    DESCRIPTION_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="服務人員不論是否開放個人網路預約，皆可以加入不指定預約組合，並且被指派預約。"]')
    OPEN_PERSONAL_ONLINE_BOOKING_TOGGLE_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@resource-id="開放個人網路預約-switch-button"]')
    OPEN_DAY_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="開放日"]')
    LATEST_APPOINTMENT_TIME_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@content-desc="最晚預約時間"]')
    ADVANCE_SETTING_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@content-desc="展開進階設定"]')
    # Advance Setting Dialog in Open Setting Tab
    ONLINE_BOOKING_LIMIT_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="網路預約可選擇數量"]')
    ONLINE_BOOKING_LIMIT_DESCRIPTION_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="服務人員在同一時段提供網路預約的數量。\n數量範圍 1 ~ 99"]')
    ONLINE_BOOKING_LIMIT_MINIMUM_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="網路預約可選擇數量"]/../android.view.ViewGroup[1]//android.widget.EditText')
    ONLINE_BOOKING_LIMIT_MAXIMUM_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="網路預約可選擇數量"]/../android.view.ViewGroup[2]//android.widget.EditText')
    # Open Time Setting Tab
    DESCRIPTION_IN_OPEN_TIME_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="開放顧客預約的時間。"]')
    # Open Item Setting Tab
    MAIN_SERVICE_ITEM_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@content-desc="主要服務項目"]')
    ONLINE_BOOKING_SELECTION_TYPE_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@content-desc="線上預約選取類型"]')
    ONLINE_BOOKING_SELECTION_TYPE_DESCRIPTION_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="網路預約時，主要項目是客人必選的服務。你可以設定顧客只能預約一項或多項服務。"]')
    ADDITIONAL_SERVICE_ITEM_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@content-desc="加購服務項目"]')
    ADDITIONAL_SERVICE_ITEM_DESCRIPTION_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE = (AppiumBy.XPATH, '//*[@text="網路預約時，加購項目是給客人額外加選的，非必選但可以重複選擇。"]')
    # Online Booking Selection Type Dialog in Open Item Setting Tab
    SINGLE_CHOICE_IN_ONLINE_BOOKING_SELECTION_TYPE_DIALOG = (AppiumBy.XPATH, '//*[@text="單選"]')
    MULTIPLE_CHOICE_IN_ONLINE_BOOKING_SELECTION_TYPE_DIALOG = (AppiumBy.XPATH, '//*[@text="複選"]')
    # Select Additional Service Item Page
    TITLE_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="選擇加購服務項目"]')
    CLOSE_BUTTON_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    SERVICE_ITEM_CATEGORY_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    ALL_CHOICE_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="全部選取"]/../*[@resource-id="square-check"]')
    SERVICE_ITEM_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    ALL_CLEAR_BUTTON_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@content-desc="全部清除"]')
    # Open Days page
    SPECIFIC_OPEN_DAYS_IN_OPEN_DAYS_PAGE = (AppiumBy.XPATH, '//*[@text="指定日期"]')
    SPECIFIC_OPEN_TIMES_IN_OPEN_DAYS_PAGE = (AppiumBy.XPATH, '//*[@text="指定時間"]')
    OPEN_MONTHS_AVAILABLE_IN_OPEN_DAYS_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="開放下{text}個月"]')
    ALL_OPEN_AVAILABLE_IN_OPEN_DAYS_PAGE = (AppiumBy.XPATH, '//*[@text="全部開放"]')
    CLOSE_BUTTON_IN_OPEN_DAYS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_OPEN_DAYS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    # Specific Days Page
    TITLE_IN_SPECIFIC_DAYS_PAGE = (AppiumBy.XPATH, '//*[@text="指定日期"]')
    BACK_BUTTON_IN_SPECIFIC_DAYS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="arrow-left"]')
    DAYS_IN_SPECIFIC_DAYS_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="每月{text}日"]')
    # Feature Not Available Dialog in Specific Days Page
    TITLE_IN_FEATURE_NOT_AVAILABLE_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="功能尚未開放"]')
    DESCRIPTION_IN_FEATURE_NOT_AVAILABLE_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="此功能尚未開放，敬請期待"]')
    GOT_IT_BUTTON_IN_FEATURE_NOT_AVAILABLE_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="我知道了"]')
    # Latest Appointment Time Page
    TITLE_IN_LATEST_APPOINTMENT_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="最晚預約時間"]')
    CLOSE_BUTTON_IN_LATEST_APPOINTMENT_TIME_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    LAST_APPOINTMENT_TIME_IN_LATEST_APPOINTMENT_TIME_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup//android.view.ViewGroup[{text}]')
    # Open Time Tab
    OPEN_TIME_ADD_TIME_BUTTON_IN_OPEN_TIME_TAB = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../../android.view.ViewGroup//*[@text="新增時間"]')
    OPEN_TIME_EDIT_TIME_BUTTON_IN_OPEN_TIME_TAB = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    # Edit Open Time Page
    DISPLAY_EARLY_MORNING_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="顯示凌晨"]')
    COPY_TODAY_SCHEDULE_BUTTON_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="複製本日"]')
    QUICK_CLOSE_BUTTON_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="快速關閉"]')
    TIME_IN_EDIT_OPEN_TIME_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    CLOSE_BUTTON_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    # Quick Close Dialog in Edit Open Time Page
    TODAY_CLOSE_IN_QUICK_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="本日關閉"]')
    RANGE_CLOSE_IN_QUICK_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="區間關閉"]')
    ALL_CLOSE_IN_QUICK_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="全部關閉"]')
    # Today Close Dialog in Edit Open Time Page
    TITLE_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="本日關閉"]')
    DESCRIPTION_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="確定要關閉本日所有時段？"]')
    CONFIRM_BUTTON_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@content-desc="確定"]')
    CANCEL_BUTTON_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@content-desc="取消"]')
    # RANGE CLOSE PAGE
    TITLE_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="區間關閉"]')
    CLOSE_BUTTON_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    START_DATE_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@content-desc="從"]')
    END_DATE_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@content-desc="到"]')
    # All Close Dialog in Edit Open Time Page
    TITLE_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="全部關閉"]')
    DESCRIPTION_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="確定要關閉全部時段？ 關閉後，此操作將無法復原"]')
    CONFIRM_BUTTON_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@content-desc="確定"]')
    CANCEL_BUTTON_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@content-desc="取消"]')
    # Copy Dialog in Edit Open Time Page
    COPY_TO_DATE_RANGE_BUTTON_IN_COPY_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="複製到區間日期"]')
    COPY_TO_SPECIFIC_DATE_BUTTON_IN_COPY_DIALOG_IN_EDIT_OPEN_TIME_PAGE = (AppiumBy.XPATH, '//*[@text="複製到指定日期"]')
    # Copy Specific Date Page
    TITLE_IN_COPY_SPECIFIC_DATE_PAGE = (AppiumBy.XPATH, '//*[@text="複製到指定日期"]')
    CLOSE_BUTTON_IN_COPY_SPECIFIC_DATE_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_COPY_SPECIFIC_DATE_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    DATE_IN_COPY_SPECIFIC_DATE_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"][1]')
    DATE_VALUE_IN_COPY_SPECIFIC_DATE_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    # Copy Date Range Page
    TITLE_IN_COPY_DATE_RANGE_PAGE = (AppiumBy.XPATH, '//*[@text="複製到區間範圍"]')
    CLOSE_BUTTON_IN_COPY_DATE_RANGE_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_COPY_DATE_RANGE_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    START_DATE_IN_COPY_DATE_RANGE_PAGE = (AppiumBy.XPATH, '//*[@content-desc="從"]')
    END_DATE_IN_COPY_DATE_RANGE_PAGE = (AppiumBy.XPATH, '//*[@content-desc="到"]')
    REPEAT_WEEKDAY_IN_COPY_DATE_RANGE_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="重複"]/../android.view.ViewGroup[{text}]')
    # Range Date Dialog
    START_DATE_IN_RANGE_DATE_DIALOG = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    START_DATE_VALUE_IN_RANGE_DATE_DIALOG = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="開始日期"]/../*[@text="{text}"]')
    END_DATE_IN_RANGE_DATE_DIALOG = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    END_DATE_VALUE_IN_RANGE_DATE_DIALOG = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="結束日期"]/../*[@text="{text}"]')
    # Select Main Service Item Page
    TITLE_IN_SELECT_MAIN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="選擇主要服務項目"]')
    CLOSE_BUTTON_IN_SELECT_MAIN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_SELECT_MAIN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    SERVICE_ITEM_CATEGORY_IN_SELECT_MAIN_SERVICE_ITEM_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    ALL_CHOICE_IN_SELECT_MAIN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@text="全部選取"]/../*[@resource-id="square-check"]')
    SERVICE_ITEM_IN_SELECT_MAIN_SERVICE_ITEM_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    ALL_CLEAR_BUTTON_IN_SELECT_MAIN_SERVICE_ITEM_PAGE = (AppiumBy.XPATH, '//*[@content-desc="全部清除"]')
    # Edit Service Unspecified Appointment Combination Page
    SERVICE_PERSONNEL_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    OPEN_ITEM_SETTING_TAB_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="開放項目"]')
    MAIN_SERVICE_ITEM_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@content-desc="主要服務項目"]')
    ONLINE_BOOKING_SELECTION_TYPE_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@content-desc="線上預約選取類型"]')
    ADDITIONAL_SERVICE_ITEM_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@content-desc="加購服務項目"]')
    CLOSE_BUTTON_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    DELETE_BUTTON_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="刪除不指定組合"]')
    # Delete Service Unspecified Appointment Combination Alert Dialog in Edit Service Unspecified Appointment Combination Page
    TITLE_IN_DELETE_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_ALERT_DIALOG_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@text="刪除組合"]')
    DESCRIPTION_IN_DELETE_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_ALERT_DIALOG_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = lambda  self, text: (AppiumBy.XPATH, f'//*[@text="確定要刪除 {text}？"]')
    CANCEL_BUTTON_IN_DELETE_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_ALERT_DIALOG_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@content-desc="取消"]')
    DELETE_BUTTON_IN_DELETE_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_ALERT_DIALOG_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE = (AppiumBy.XPATH, '//*[@content-desc="刪除"]')






























