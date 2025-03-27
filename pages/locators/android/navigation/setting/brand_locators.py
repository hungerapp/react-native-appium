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
    BRANCH_SUBSCRIPTION_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@content-desc="Pro商務方案, 方案管理、帳務資訊設定"]')

    # Brand Info Page
    BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店和品牌資訊"]')
    CONFIRM_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'check')
    BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    BRANCH_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店介紹"]/../android.view.ViewGroup')
    BRANCH_DESCRIPTION_VALUE_IN_BRANCH_BRAND_INFO_PAGE = lambda self, text: (AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")

    # Phone Information Section
    BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="分店電話"]')
    BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="顯示分店電話-switch-button"]')
    BRANCH_PHONE_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店電話"]/../android.widget.EditText')
    BRANCH_PHONE_COUNTY_CODE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="caret-down"]')

    # Address Information Section
    BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="顯示分店地址-switch-button"]')
    BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="國家"]')
    BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="城市"]/../android.view.ViewGroup')
    BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="地區"]/../android.view.ViewGroup')
    BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="地址"]/../android.widget.EditText')
    BRANCH_ADDRESS_DISTRICT_WARM_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text=" 此欄位為必填。"]')

    # Brand Settings
    EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@content-desc="展開品牌設定"]')
    CLOSE_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@content-desc="收起品牌設定"]')
    BRAND_SETTINGS_SECTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="android:id/parentPanel"]')
    BRAND_IMAGE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="com.hunger.hotcakeapp.staging:id/action_bar_root"]//android.widget.ImageView')
    BRAND_NAME_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="品牌名稱"]')
    BRAND_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="品牌介紹"]')

    # Description Dialogs
    TEXT_IN_BRANCH_DESCRIPTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//android.widget.EditText')
    CONFIRM_BUTTON_IN_BRANCH_DESCRIPTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="circle-check"]//com.horcrux.svg.GroupView')

    # Phone County Code Dialogs
    SEARCH_COUNTRY_CODE_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="magnifying-glass"]/../android.view.ViewGroup//android.widget.EditText')
    CONFIRM_BUTTON_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="國碼-modal-right-button "]')

    # Address dialogs
    BRANCH_ADDRESS_CITY_IN_DIALOG = (AppiumBy.XPATH, '//*[@text="城市"]/../android.view.ViewGroup//android.widget.ScrollView')
    BRANCH_ADDRESS_CITY_OPTION_IN_DIALOG = lambda self, index: (AppiumBy.XPATH, f'//*[@text="本期方案"]/../android.widget.TextView[1]')
    BRANCH_ADDRESS_DISTRICT_IN_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="地區-close-button"]/../android.view.ViewGroup//android.widget.ScrollView')
    BRANCH_ADDRESS_DISTRICT_OPTION_IN_DIALOG = lambda self, index: (AppiumBy.XPATH, f'//*[@resource-id="地區-close-button"]/../android.view.ViewGroup//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup[{index}]//*[@resource-id="circle"]')

    #Plan Management Page
    PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="方案管理"]')
    HOTCOIN_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="夯幣"]')
    CREDIT_CARD_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="信用卡"]')
    INVOICE_INFO_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="發票資訊"]')
    CURRENT_PLAN_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="本期方案"]')
    NEXT_PLAN_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="下期方案"]')
    NEXT_DEDUCTION_DATE_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="下期扣款日期"]')
    VIEW_NEXT_PLAN_DETAILS_BUTTON_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="查看下期方案明細"]')
    PLAN_CHANGE_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="方案變更"]')
    DEDUCTION_RECORD_IN_PLAN_MANAGEMENT_PAGE = (AppiumBy.XPATH, '//*[@text="扣款紀錄"]')

    #payment details dialog
    PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="付款明細"]')
    SUBSCRIPTION_PLAN_IN_PAYMENT_DETAILS_DIALOG = lambda self, text: (AppiumBy.XPATH, f'//*[@text="HotcakeApp Merchant"]//*[@text="{text}"]')
    DISCOUNT_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="折扣"]')
    SMS_COST_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="簡訊費用"]')
    TOTAL_COST_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="總計"]')
    CLOSE_BUTTON_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="bullseye-arrow"]')







