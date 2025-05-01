from appium.webdriver.common.appiumby import AppiumBy

class ServicePersonnelPageLocators:
    # Service Personnel Page
    TITLE_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="服務人員"]')
    CLOSE_BUTTON_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.ACCESSIBILITY_ID, "xmark")
    SERVICE_PERSONNEL_DESCRIPTION_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="「服務人員」是夯客計費的單位，新增後將會增加收費。"]')
    ADD_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE = (AppiumBy.XPATH, '//*[@text="新增服務人員"]')
    DELETE_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')
    EDIT_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    # Add Service Personnel Dialog
    TITLE_IN_ADD_SERVICE_PERSONNEL_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//*[@text="新增服務人員"]')
    DESCRIPTION_IN_ADD_SERVICE_PERSONNEL_DIALOG = (AppiumBy.XPATH, '//*[@text="夯客的收費方式是以「服務人員數量＊方案價格」計價，新增人員可能會導致費用增加。"]')
    CANCEL_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG = (AppiumBy.XPATH, '//*[@text="取消"]')
    ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG = (AppiumBy.XPATH, '//*[@text="新增"]')
    # Add Service Personnel Modal
    TITLE_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.XPATH, '//*[@resource-id="check"]/../*[@text="新增服務人員"]')
    CLOSE_BUTTON_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.XPATH, '//*[@resource-id="check"]/../*[@resource-id="xmark"]')
    CONFIRM_BUTTON_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    SERVICE_PERSONNEL_NAME_FIELD_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.ACCESSIBILITY_ID, "人員名稱-text-input")
    SERVICE_PERSONNEL_COLOR_SELECTION_IN_SERVICE_PERSONNEL_MODAL = lambda self, text: (AppiumBy.XPATH, f'//android.widget.HorizontalScrollView//android.view.ViewGroup//android.view.ViewGroup[{text}]')
    SERVICE_PERSONNEL_INTRODUCTION_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.ACCESSIBILITY_ID, "人員介紹-textarea-field")
    SERVICE_PERSONNEL_INTRODUCTION_FIELD = (AppiumBy.ACCESSIBILITY_ID, "人員介紹-textarea-input")
    CLEAR_SERVICE_PERSONNEL_INTRODUCTION_BUTTON = (AppiumBy.XPATH, '//*[@text="清除"]')
    CONFIRM_CLEAR_SERVICE_PERSONNEL_INTRODUCTION_BUTTON = (AppiumBy.XPATH, '//*[@content-desc="circle-check"]')
    CLOSE_SERVICE_PERSONNEL_INTRODUCTION_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "人員介紹-close-button")
    # TODO: 展開進階設定locator有變動要修改
    EXPAND_ADVANCED_SETTINGS_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.XPATH, '//android.widget.TextView[@text="展開進階設定"]')
    CLOSE_ADVANCED_SETTINGS_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.XPATH, '//android.widget.TextView[@text="收起進階設定"]')
    SIMULTANEOUS_SERVICE_COUNT_FIELD_IN_SERVICE_PERSONNEL_MODAL = (AppiumBy.ACCESSIBILITY_ID, "同時服務數量-text-input")
    # Delete Service Personnel Dialog
    TITLE_IN_DELETE_SERVICE_PERSONNEL_DIALOG = (AppiumBy.XPATH, '//*[@text="刪除服務人員"]')
    DESCRIPTION_IN_DELETE_SERVICE_PERSONNEL_DIALOG = lambda self, text: (AppiumBy.XPATH, f'//*[@text="確定要刪除 {text}？刪除後，預約、結帳紀錄不會消失，但在部份頁面 (如行事曆、業績統計) 將會隱藏該位人員的資料。"]')
    DELETE_FIELD_IN_DELETE_SERVICE_PERSONNEL_DIALOG = (AppiumBy.ACCESSIBILITY_ID, "undefined-text-input")
    CANCEL_BUTTON_IN_DELETE_SERVICE_PERSONNEL_DIALOG = (AppiumBy.XPATH, '//*[@content-desc="取消"]')
    DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_DIALOG = (AppiumBy.XPATH, '//*[@content-desc="刪除"]')



