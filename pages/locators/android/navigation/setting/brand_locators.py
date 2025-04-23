# pages/locators/android/navigation/setting/brand_locators.py
from appium.webdriver.common.appiumby import AppiumBy

class BrandPageLocators:
    # Navigation
    SETTINGS_OPTION_IN_NAVIGATION = (AppiumBy.ACCESSIBILITY_ID, '設定')

    # Branch Settings Page
    BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@text="分店設定"]')
    BRANCH_NAME_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='chevron-right'])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView")
    BRANCH_NAME_VALUE_IN_BRANCH_SETTINGS_PAGE = lambda self, text: (AppiumBy.XPATH, f'//*[@text="{text}"]')
    BRANCH_SUBSCRIPTION_PLAN_IS_PRO_BUSINESS_PLAN_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@text="Pro商務方案"]')
    BRANCH_SUBSCRIPTION_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="bullseye-arrow"]')

    # Branch and Brand Info Page
    TITLE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店和品牌資訊"]')
    CONFIRM_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'check')
    CLOSE_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
    UPLOAD_IMAGE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'photo-field')
    BRANCH_PHOTO_DISPLAY_TEXT_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店照片的顯示比例為 2:1。"]')
    BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '分店名稱-text-input')
    BRANCH_INTRODUCTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '分店介紹-textarea-field')
    CLOSE_BRANCH_INTRODUCTION_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '分店介紹-close-button')
    CONFIRM_BRANCH_INTRODUCTION_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'circle-check')
    BRANCH_INTRODUCTION_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '分店介紹-textarea-input')
    CLEAR_BRANCH_INTRODUCTION_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@content-desc="清除"]')
    DISPLAY_BRANCH_PHONE_NUMBER_SWITCH_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '顯示分店電話-switch-button')
    BRANCH_PHONE_COUNTRY_CODE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店電話"]/../android.view.ViewGroup')
    BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '分店電話-text-input')
    DISPLAY_BRANCH_ADDRESS_SWITCH_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '顯示分店地址-switch-button')
    BRANCH_ADDRESS_COUNTRY_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="國家"]')
    BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '城市-select-field')
    BRANCH_ADDRESS_CITY_SELECTED = lambda self, city: (AppiumBy.XPATH, f'//android.widget.TextView[contains(@text,"{city}")]')
    BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '地區-select-field')
    BRANCH_ADDRESS_DISTRICT_SELECTED = lambda self, district: (AppiumBy.XPATH, f'//android.widget.TextView[contains(@text,"{district}")]')
    BRANCH_ADDRESS_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '地址-text-input')
    EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@content-desc="展開品牌設定"]')
    CLOSE_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@content-desc="收起品牌設定"]')
    BRAND_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '品牌名稱-text-input')
    BRAND_INTRODUCTION_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '品牌介紹-textarea-field')
    BRANCH_PHONE_COUNTRY_CODE_SELECTED = lambda self, country_code: (AppiumBy.XPATH,f'//android.widget.TextView[contains(@text,"{country_code}")]')
    CONFIRM_BRANCH_PHONE_COUNTRY_CODE_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, '國碼-modal-right-button ')
    BRANCH_PHONE_COUNTRY_CODE_SEARCH_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
    ERROR_MESSAGE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text=" 此欄位為必填。"]')
