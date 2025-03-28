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
    BACK_HOTCAKE_APP_BUTTON = (AppiumBy.XPATH, '//*[@text="返回夯客APP"]')

    #payment details dialog in plan management page
    PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="付款明細"]')
    SUBSCRIPTION_PLAN_IN_PAYMENT_DETAILS_DIALOG = lambda self, text: (AppiumBy.XPATH, f'//*[@text="HotcakeApp Merchant"]//*[@text="{text}"]')
    DISCOUNT_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="折扣"]')
    SMS_COST_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="簡訊費用"]')
    TOTAL_COST_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="總計"]')
    CLOSE_BUTTON_IN_PAYMENT_DETAILS_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="bullseye-arrow"]')

    #plan change page
    PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="方案變更"]')
    PLAN_CHANGE_DESCRIPTION_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text=concat("依據你的需求", "\n", "選擇適合你的方案")]')
    #pro business plan in plan change page
    PRO_BUSINESS_PLAN_TITLE_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="我 需要 結帳相關功能"]')
    PRO_BUSINESS_PLAN_DESCRIPTION_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text=concat("此方案擁有所有功能", "\n", "包含結帳、業績統計、商品管理與進銷存")]')
    PRO_BUSINESS_PLAN_BUTTON_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="選擇 Pro商務方案"]')
    #star new plan in plan change page
    STAR_NEW_PLAN_TITLE_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="我 不需要 結帳相關功能"]')
    STAR_NEW_PLAN_DESCRIPTION_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text=concat("給沒有結帳需求的美業夥伴更彈性的選擇", "\n", "專業度不變，價格更親民")]')
    STAR_NEW_PLAN_BUTTON_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="選擇 Star新星方案"]')
    SMS_COST_DESCRIPTION_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="簡訊發送採額外計費，1 封/元"]')
    #free trial plan in plan change page
    DOWN_GRADE_TO_FREE_TRIAL_PLAN_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//android.widget.Button[@text="降級為Free免費體驗方案"]')
    CLOSE_BUTTON_IN_PLAN_CHANGE_PAGE = (AppiumBy.XPATH, '//*[@text="方案變更"]/../android.widget.Button')

    # cancel payment plan dialog
    TITLE_IN_CANCEL_PAYMENT_PLAN_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="modal"]//*[@text="取消付費方案"]')
    CONFIRM_BUTTON_IN_CANCEL_PAYMENT_PLAN_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="modal"]//*[@text="確定"]')
    CANCEL_BUTTON_IN_CANCEL_PAYMENT_PLAN_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="modal"]//*[@text="取消"]')

    #pro business plan page
    DESCRIPTION_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="適合穩健發展的夥伴"]')
    PRICE_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="480元/每位服務人員"]')
    CONTENT_1_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="預約模組"]')
    CONTENT_2_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="會員與再行銷模組"]')
    CONTENT_3_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="文件管理 (同意書、問卷)"]')
    CONTENT_4_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="定金預付款模組 (完整)"]')
    CONTENT_5_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="結帳與分潤計算模組"]')
    CONTENT_6_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="商品與進銷存模組"]')
    CONTENT_7_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="TWODAY晚鳥預約模組"]')
    CONTENT_8_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="LINE官方帳號整合"]')
    TOLL_REMINDER_TEXT_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="無限會員數，收費上限 2880元/月"]')
    DIFFERENT_PLAN_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//android.widget.Button[@text="不同方案比較"]')
    SELECT_THIS_PLAN_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//android.widget.Button[@text="選擇此方案"]')
    CLOSE_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="Pro商務方案"]/../android.widget.Button')

    #star new plan page
    DESCRIPTION_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="適合成長中的夥伴"]')
    PRICE_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="360元/每位服務人員"]')
    CONTENT_1_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="預約模組"]')
    CONTENT_2_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="會員與再行銷模組"]')
    CONTENT_3_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="文件管理 (同意書、問卷)"]')
    CONTENT_4_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="定金預付款模組 (完整)"]')
    CONTENT_5_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="結帳與分潤計算模組"]')
    CONTENT_6_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="商品與進銷存模組"]')
    CONTENT_7_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="TWODAY晚鳥預約模組"]')
    CONTENT_8_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="LINE官方帳號整合"]')
    TOLL_REMINDER_TEXT_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="無限會員數，收費上限 2160元/月"]')
    DIFFERENT_PLAN_BUTTON_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//android.widget.Button[@text="不同方案比較"]')
    SELECT_THIS_PLAN_BUTTON_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//android.widget.Button[@text="選擇此方案"]')
    CLOSE_BUTTON_IN_START_NEW_PLAN_PAGE = (AppiumBy.XPATH, '//*[@text="Star新星方案"]/../android.widget.Button')


    # plan function dialog in pro business plan page
    # plan function dialog in star new plan page
    PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="方案功能"]')
    PRO_BUSINESS_PLAN_TAB_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="14"]')
    STAR_NEW_PLAN_TAB_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="16"]')
    FREE_TRIAL_TAB_PLAN_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="15"]')
    CLOSE_BUTTON_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="方案功能"]/../android.widget.Button')
    FEATURE_TEXT_1_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="預約模組"]')
    FEATURE_TEXT_2_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="會員與再行銷模組"]')
    FEATURE_TEXT_3_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="文件管理 (同意書、問卷)"]')
    FEATURE_TEXT_4_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="定金預付款模組 (完整)"]')
    FEATURE_TEXT_5_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="結帳與分潤計算模組"]')
    FEATURE_TEXT_6_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="商品與進銷存模組"]')
    FEATURE_TEXT_7_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="TWODAY晚鳥預約模組"]')
    FEATURE_TEXT_8_IN_PLAN_FUNCTION_DIALOG = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="LINE官方帳號整合"]')

    #pro business plan tab in plan function dialog in pro business plan page
    #pro business plan tab in plan function dialog in star new plan page
    DESCRIPTION_IN_PRO_BUSINESS_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="適合穩健發展的夥伴"]')
    PRICE_DETAILS_TEXT_1_IN_PRO_BUSINESS_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text=concat("480元/每位服務人員", "\n", "(收費上限 2,880元/月)")]')
    PRICE_DETAILS_TEXT_2_IN_PRO_BUSINESS_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="預約數、會員數無上限"]')
    #star new plan tab in plan function dialog in pro business plan page
    #star new plan tab in plan function dialog in star new plan page
    DESCRIPTION_IN_START_NEW_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="適合成長中的夥伴"]')
    PRICE_DETAILS_TEXT_1_IN_START_NEW_PLAN_TAB = (AppiumBy.XPATH,'//*[@text="HotcakeApp Merchant"]//*[@text=concat("360元/每位服務人員", "\n", "(收費上限 2,160元/月)")]')
    PRICE_DETAILS_TEXT_2_IN_START_NEW_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="預約數、會員數無上限"]')
    #free trial plan tab in plan function dialog in pro business plan page
    #free trial plan tab in plan function dialog in star new plan page
    DESCRIPTION_IN_FREE_TRIAL_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="適合剛創業的夥伴"]')
    PRICE_DETAILS_TEXT_1_IN_FREE_TRIAL_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="免費"]')
    PRICE_DETAILS_TEXT_2_IN_FREE_TRIAL_PLAN_TAB = (AppiumBy.XPATH, '//*[@text="HotcakeApp Merchant"]//*[@text="會員數限制 80 筆"]')

    #Payment Record Page
    TITLE_IN_PAYMENT_RECORD_PAGE = (AppiumBy.XPATH, '//*[@text="扣款紀錄"]')
    ClOSE_BUTTON_IN_PAYMENT_RECORD_PAGE = (AppiumBy.XPATH, '//*[@text="扣款紀錄"]/../android.widget.Button')


















