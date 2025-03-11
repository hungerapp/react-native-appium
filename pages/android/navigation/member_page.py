import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains

from pages.android.create.create_checkout_page import CreateCheckoutPage
from pages.shared_components.common_use import CommonUseSection

class MemberPage(CommonUseSection):
    def __init__(self, driver):
        self.driver = driver
        self.create_checkout_page = CreateCheckoutPage(driver)
        
    # Member option in calendar nav bar
    MEMBER_OPTION = (AppiumBy.ACCESSIBILITY_ID, '會員')
    
    
    # Member tabs
    MEMBER_TABS = {
      'recent_join': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近加入")'),
      'black_list': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("黑名單")'),
      'birthday': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("本月壽星")'),
    }
    
    MEMBER_PHONE_NUMBERS = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "+886")]')
    
    
    # bottom navigation bar in member passport page
    NAVIGATION_ICONS = {
        'message': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("訊息")'),
        'review_doc': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("評鑑")'),
        'member_review': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("評鑑")'),
        'more': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更多")')
    }
    
    # Member page functions
    MEMBER_PAGE_FUNCTIONS = {
      'add_member': (AppiumBy.ACCESSIBILITY_ID, '新增會員'),
      'apply_filters': (AppiumBy.ACCESSIBILITY_ID, '會員篩選'),
      'check_scheduling_records': (AppiumBy.ACCESSIBILITY_ID, '排程記錄'),
      'search_member': (AppiumBy.ACCESSIBILITY_ID, '搜尋'),
      'sent_tag': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("已發送").instance(0)'),
      'member_filer_back': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'),
      'passport_return_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'),
      'scheduling_records_back': (AppiumBy.XPATH, '//com.horcrux.svg.PathView')
    }
    
    MEMBER_FILTER_SECTIONS = {
      "member_tag": (AppiumBy.ACCESSIBILITY_ID, '會員標籤, 無'),
      "birthday_month": (AppiumBy.ACCESSIBILITY_ID, '生日月份, 無'),
      "sign": (AppiumBy.ACCESSIBILITY_ID, '星座, 無'),
      "age": (AppiumBy.ACCESSIBILITY_ID, '年齡, 無'),
      "save_button": (AppiumBy.XPATH, '(//com.horcrux.svg.GroupView)[2]')
    }
    
    DELETE_CONDITION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("排除條件, 黑名單, 評分低於4.0")')
    DELETE_CONDITION_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(9)')
    
    MEMBER_FILTER_OPTIONS = {
      "member_tag": [
        (AppiumBy.ACCESSIBILITY_ID, '全部選取'),
        (AppiumBy.ACCESSIBILITY_ID, '社區熟客'),
        (AppiumBy.ACCESSIBILITY_ID, '老闆朋友'),
        (AppiumBy.ACCESSIBILITY_ID, '敏感型客人'),
        (AppiumBy.ACCESSIBILITY_ID, '口碑介紹客')
      ],
      "birthday_month" : [
        (AppiumBy.ACCESSIBILITY_ID, '全部選取'),
        (AppiumBy.ACCESSIBILITY_ID, '1月'),
        (AppiumBy.ACCESSIBILITY_ID, '2月'),
        (AppiumBy.ACCESSIBILITY_ID, '3月'),
        (AppiumBy.ACCESSIBILITY_ID, '4月'),
        (AppiumBy.ACCESSIBILITY_ID, '5月'),
        (AppiumBy.ACCESSIBILITY_ID, '6月'),
        (AppiumBy.ACCESSIBILITY_ID, '7月'),
        (AppiumBy.ACCESSIBILITY_ID, '8月'),
        (AppiumBy.ACCESSIBILITY_ID, '9月'),
        (AppiumBy.ACCESSIBILITY_ID, '10月'),
        (AppiumBy.ACCESSIBILITY_ID, '11月')
      ],
      "sign" : [
        (AppiumBy.ACCESSIBILITY_ID, '全部選取'),
        (AppiumBy.ACCESSIBILITY_ID, '牡羊座 (3/21 ~ 4/19)'),
        (AppiumBy.ACCESSIBILITY_ID, '金牛座 (4/20 ~ 5/20)'),
        (AppiumBy.ACCESSIBILITY_ID, '雙子座 (5/21 ~ 6/20)'),
        (AppiumBy.ACCESSIBILITY_ID, '巨蟹座 (6/21 ~ 7/22)'),
        (AppiumBy.ACCESSIBILITY_ID, '獅子座 (7/23 ~ 8/22)'),
        (AppiumBy.ACCESSIBILITY_ID, '處女座 (8/23 ~ 9/22)'),
        (AppiumBy.ACCESSIBILITY_ID, '天秤座 (9/23 ~ 10/22)'),
        (AppiumBy.ACCESSIBILITY_ID, '天蠍座 (10/23 ~ 11/21)'),
        (AppiumBy.ACCESSIBILITY_ID, '射手座 (11/22 ~ 12/21)'),
        (AppiumBy.ACCESSIBILITY_ID, '摩羯座 (12/22 ~ 1/19)'),
        (AppiumBy.ACCESSIBILITY_ID, '水瓶座 (1/20 ~ 2/18)')
      ],
      "age" : [
        #(AppiumBy.ACCESSIBILITY_ID, '全部選取'),
        (AppiumBy.ACCESSIBILITY_ID, '15歲以下'),
        (AppiumBy.ACCESSIBILITY_ID, '16~20歲'),
        (AppiumBy.ACCESSIBILITY_ID, '21~25歲'),
        (AppiumBy.ACCESSIBILITY_ID, '26~30歲'),
        (AppiumBy.ACCESSIBILITY_ID, '31~35歲'),
        (AppiumBy.ACCESSIBILITY_ID, '36~40歲'),
        (AppiumBy.ACCESSIBILITY_ID, '41~45歲'),
        (AppiumBy.ACCESSIBILITY_ID, '46~50歲'),
        (AppiumBy.ACCESSIBILITY_ID, '51~55歲'),
        (AppiumBy.ACCESSIBILITY_ID, '56~60歲'),
        (AppiumBy.ACCESSIBILITY_ID, '61~65歲')
      ],
      "amount" : [
        (AppiumBy.ACCESSIBILITY_ID, '累計至今'),
        (AppiumBy.ACCESSIBILITY_ID, '近60天'),
        (AppiumBy.ACCESSIBILITY_ID, '近90天'),
        (AppiumBy.ACCESSIBILITY_ID, '近180天'),
        (AppiumBy.ACCESSIBILITY_ID, '近360天'),
        (AppiumBy.ACCESSIBILITY_ID, '今年累計'),
        (AppiumBy.ACCESSIBILITY_ID, '去年累計'),
      ]
    }
    
    DELETE_CONDITION_OPTIONS = {  
     'delete_condition': [
        (AppiumBy.ACCESSIBILITY_ID, '全部選取'),
        (AppiumBy.ACCESSIBILITY_ID, '黑名單'),
        (AppiumBy.ACCESSIBILITY_ID, '來店次數為0'),
        (AppiumBy.ACCESSIBILITY_ID, '評分低於4.0'),
      ]
    }
    
    INPUT_AMOUNT = {
      "min_cost_amount": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[1]'),
      "max_cost_amount": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[1]'),
      "min_come_amount": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[2]'),
      "max_come_amount": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[2]'),
      "min_top_up_remaining": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[3]'),
      "max_top_up_remaining": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[3]'),
      "min_join_date": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[4]'),
      "max_join_date": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[4]'),
      "min_last_visit_date": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[5]'),
      "max_last_visit_date": (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[5]'),
    }
    
    # Cost amount menu
    COST_AMOUNT_MENU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(5)')
    
    # Come amount menu
    COME_AMOUNT_MENU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(6)')
    
    FILTER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '進行篩選')
    RESET_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '重置條件')
    
    
    # return to member page button
    RETURN_TO_MEMBER_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    
    # Search elements
    SEARCH_ELEMENTS = {
        'input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜尋")'),
        'result': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+886 972 205690")')
    }
    
    # System tag section
    SYSTEM_TAGS_SECTION = {
      'deposit': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="chevron-right"])[1]/com.horcrux.svg.SvgView'),
      'early_booking': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="chevron-right"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    }
    
    SYSTEM_TAGS_OPTIONS = {
      'deposit': [
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("依照系統判定")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("強制收取")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("強制不收取")')
      ],
      'early_booking': [
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("無")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("1 天")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("3 天")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("5 天")')
      ]
    }
    
    CUSTOMIZE_TAGS = [
      #(AppiumBy.ACCESSIBILITY_ID, "全部選取"),
      (AppiumBy.ACCESSIBILITY_ID, "社區熟客"),
      (AppiumBy.ACCESSIBILITY_ID, "老闆朋友"),
      (AppiumBy.ACCESSIBILITY_ID, "敏感型客人"),
      (AppiumBy.ACCESSIBILITY_ID, "口碑介紹客")
    ]
    
    MANAGE_CUSTOM_TAG = (AppiumBy.ACCESSIBILITY_ID, '管理自訂標籤')
    
    CUSTOM_TAGS_FUNCTIONS = {
      'add_tag': (AppiumBy.ACCESSIBILITY_ID, '新增標籤'),
      'edit_tag': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[5]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
      'delete_tag': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-minus"])[5]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
      'save_new_tag': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="check"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
      'error_msg': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 此欄位為必填。")'),
      'confirm_delete': (AppiumBy.ACCESSIBILITY_ID, '刪除'),
      'manage_custom_back_button': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[13]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    }
    
    SELECT_MEMBER_CONFIRM = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="check"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    
    
    PASSPORT_TABS = {
      'billing_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帳單")'),
      'info_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("資訊")'),
      'reserve_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("預約")'),
    }
    
    BILLING_FUNCTIONS = {
      'view_details': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="檢視明細"])[1]'),
      'view_checkout': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="檢視結帳"])[1]'),
      'expand_details': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="chevron-right"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
      'export_details': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[7]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
      'view_details_back': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'),
      'details_back': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'),
      'delete_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除結帳")'),
      'delete_checkout_option': (AppiumBy.ACCESSIBILITY_ID, '刪除結帳'),
      'delete_checkout_again_option': (AppiumBy.ACCESSIBILITY_ID, '刪除並重新結帳')
    }
    
    TOP_UP_SECTION = {
      'top_up_section': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("儲值金")'),
      'edit_top_up_icon': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
      'input_top_up_amount': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入數值")'),
      'increase_button': (AppiumBy.ACCESSIBILITY_ID, '增加'),
      'decrease_button': (AppiumBy.ACCESSIBILITY_ID, '扣除'),
      'confirm_button': (AppiumBy.ACCESSIBILITY_ID, '確定'),
      'top_up_button': (AppiumBy.ACCESSIBILITY_ID, '儲值')
    }
    
    BONUS_POINTS_SECTION = {
      'bonus_points_section': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紅利點數")')
    }
    
    TICKETS_SECTION = {
      'tickets_section': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("票券")'),
      'sell_ticket_button': (AppiumBy.ACCESSIBILITY_ID, '販售票券'),
      'ticket': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("自動化測試票券")'),
      'use_button': (AppiumBy.ACCESSIBILITY_ID, '使用'),
      'plus_button': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="plus"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
      'input_field': (AppiumBy.XPATH, '//android.widget.EditText'),
      'save_button': (AppiumBy.ACCESSIBILITY_ID, '確定'),
      'cancel_button': (AppiumBy.ACCESSIBILITY_ID, '取消'),
      'history_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歷史紀錄")'),
      'gift_ticket_button': (AppiumBy.ACCESSIBILITY_ID, '贈送票券')
    }
    
    
    EDIT_SECTION = {
      'edit_info_icon': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("基本資訊")'),
      'input': (AppiumBy.XPATH, '//android.widget.EditText'),
      'edit_save': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
      'edit_custom_info_icon': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自訂欄位")'),
      'edit_member_description_icon': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員描述")'),
      'confirm_button': (AppiumBy.ACCESSIBILITY_ID, '確定'),
      'cancel_button': (AppiumBy.ACCESSIBILITY_ID, '取消'),
      'option_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("^自動化測試.*")'),
      'fourth_question_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("^自動化測試.*")'),
      'friend_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("自動化測試")'),
      'member_description_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("自動化測試")'),
      'modal_save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
      
    }
    
    
    BOTTOM_NAVIGATION = {
        'send_message_icon': (AppiumBy.ACCESSIBILITY_ID, '發送訊息'),
        'sign_document_icon': (AppiumBy.ACCESSIBILITY_ID, '簽署文件'),
        'member_review_icon': (AppiumBy.ACCESSIBILITY_ID, '會員評論'),
        'more_icon': (AppiumBy.ACCESSIBILITY_ID, '更多')
    }
    
    SEND_MESSAGE_FUNCTIONS = {
        'send_message_button': (AppiumBy.ACCESSIBILITY_ID, '發送新訊息')
    }
    
    
    
    SIGN_DOCUMENT_FUNCTIONS = {
        'signed_document': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("自動化測試文件")'),
        'sign_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("請輸入")'),
        'sign_name': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("請點擊")'),
        'sign_field': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").instance(21)'),
        'sign_finish_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("完成")'),
        'finish_button': (AppiumBy.XPATH, "//android.widget.Button[contains(@text, '完成')]")
    }
    
    MEMBER_REVIEW_FUNCTIONS = {
        'review_element': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員評論")'),
        'review_content': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員評論是由所有使用夯客的夥伴，對此會員的預約評論。評論者皆為匿名，且僅有商家端可以查看。")')
    }
    
    
    MORE_OPTIONS_FUNCTIONS = {
        'add_new_appointment': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增預約")'),
        'quick_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("快速結帳")'),
        'member_tags': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員標籤")'),
        'link_account': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("綁定帳號")'),
        'line_section': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Beck")'),
        'send_line_message_btn': (AppiumBy.ACCESSIBILITY_ID, '發送 LINE 訊息'),
        'input_message_content': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入訊息內容")'),
        'input_modal': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")'),
        'modal_save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'use_message_template': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("使用訊息範本")'),
        'manage_message_template': (AppiumBy.ACCESSIBILITY_ID, '管理訊息範本'),
        'add_new_message_template_button': (AppiumBy.ACCESSIBILITY_ID, '新增訊息範本'),
        'title_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入範本名稱")'),
        'content_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入範本內容")'),
        'edit_tag': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(30)'),
        'error_msg': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("此欄位為必填。")'),
        'save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)'),
        'delete_tag': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(29)'),
        'confirm': (AppiumBy.ACCESSIBILITY_ID, '確定'),
        'confirm_delete': (AppiumBy.ACCESSIBILITY_ID, '刪除'),
        'message_save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'add_to_blacklist': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("加入黑名單")'),
    }
    
    MESSAGE_TEMPLATE_OPTIONS = [
        (AppiumBy.ACCESSIBILITY_ID, '美甲保固, 感謝你的到來，美甲項目我們提供7天的保固期，若有掉甲、缺色，請重新預約與我們聯繫\nhunger Salon團隊敬上'),
        (AppiumBy.ACCESSIBILITY_ID, '關懷, 你好，好久不見。上次做的服務，還滿意嗎？歡迎你再次來訪，我們會盡全力打造你的美麗！\n\n上次做的服務，還滿意嗎？'),
        (AppiumBy.ACCESSIBILITY_ID, '我是名字很長很長很長很長很長很長很長很長很長的範本, 一段內容一段內容一段內容一段內容一段內容一段內容一段內容一段內容\n\n一段內容一段內容一段內容一段內容\n\n一段內容一段內容一段內容一段內容一段內容一段內容一段內容一段內容'),
        (AppiumBy.ACCESSIBILITY_ID, 'ok, okletsgo')
    ]
    
    
    
    def click_member_option(self):
        try:
            member_option = self.driver.find_element(*self.MEMBER_OPTION)
            if member_option.is_displayed() and member_option.is_enabled():
                member_option.click()
                time.sleep(1)
                return self
            else:
                raise Exception("Member option not found or not enabled")
        except Exception as e:
            raise Exception(f"Error clicking member option: {e}")

    def click_member_item(self):
        tab = random.choice(list(self.MEMBER_TABS.values()))
        self.driver.find_element(*tab).click()
        time.sleep(1)
        
        phone_elements = self.driver.find_elements(*self.MEMBER_PHONE_NUMBERS)
        if phone_elements:
            random.choice(phone_elements).click()
            time.sleep(1)
            self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['passport_return_button']).click()
            
        else:
            raise Exception("No member phone numbers found")
        
        return self
      
    def add_member(self):
        self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['add_member']).click()
        time.sleep(0.5)
        self.new_member()
        
    def apply_member_filters(self):
        
        self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['apply_filters']).click()
        time.sleep(0.5)
        
        try:
          
          # get all filter sections except last one
          filter_sections = list(self.MEMBER_FILTER_SECTIONS.items())[:-1]
          
          # handle each section
          for section_name, section_locator in filter_sections:
              self.driver.find_element(*section_locator).click()
              time.sleep(0.5)
              
              # member tags, birthday month, sign, age
              if section_name in self.MEMBER_FILTER_OPTIONS:
                 options = self.MEMBER_FILTER_OPTIONS[section_name]
                 num_selections = random.randint(1, min(3, len(options)))
                 selected_options = random.sample(options, num_selections)
                 
                 for option in selected_options:
                     self.driver.find_element(*option).click()
                     time.sleep(0.5)
              
              # click save button
              self.driver.find_element(*self.MEMBER_FILTER_SECTIONS['save_button']).click()
              time.sleep(0.5)
              
          # handle cost amount menu
          self.driver.find_element(*self.COST_AMOUNT_MENU).click()
          time.sleep(0.5)
          
          amount_options = random.choice(self.MEMBER_FILTER_OPTIONS['amount'])
          self.driver.find_element(*amount_options).click()
          time.sleep(0.5)
          
          # handle come amount menu
          self.driver.find_element(*self.COME_AMOUNT_MENU).click()
          time.sleep(0.5)
          
          come_amount_options = random.choice(self.MEMBER_FILTER_OPTIONS['amount'])
          self.driver.find_element(*come_amount_options).click()
          time.sleep(2)

          # handle all input field       
          input_pairs = [
            ('min_cost_amount', 'max_cost_amount'),         
            ('min_come_amount', 'max_come_amount'),        
            ('min_top_up_remaining', 'max_top_up_remaining'), 
            ('min_join_date', 'max_join_date'),            
            ('min_last_visit_date', 'max_last_visit_date')  
          ]
    
          # randomly select one pair
          selected_pair = random.choice(input_pairs)

          # handle selected input pair
          min_field, max_field = selected_pair
          min_value = random.randint(1, 1000)
          max_value = random.randint(min_value + 10, min_value + 100)

          # input min value
          time.sleep(1)
          min_input = self.driver.find_element(*self.INPUT_AMOUNT[min_field])
          min_input.click()
          min_input.send_keys(str(min_value))
          time.sleep(0.5)

          # input max value
          time.sleep(1)
          max_input = self.driver.find_element(*self.INPUT_AMOUNT[max_field])
          max_input.click()
          max_input.send_keys(str(max_value))
          time.sleep(0.5)
          
          
                  
          # Scroll to find delete condition section   
          scroll_to_view = ('new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1)')
          self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_to_view)
          
          assert self.driver.find_element(*self.DELETE_CONDITION).is_displayed()
              
              
          # click filter button
          self.driver.find_element(*self.FILTER_BUTTON).click()
          time.sleep(0.5)
          
          # click back to button
          self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['member_filer_back']).click()
          
          self.driver.back()
          
          
        except Exception as e:
            print(f"Error in apply_member_filters: {str(e)}")
            raise
       
                      
    def check_scheduling_records(self):
        self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['check_scheduling_records']).click()
        time.sleep(1)
        sent_tag = self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['sent_tag'])
        assert sent_tag.is_displayed()
        self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['scheduling_records_back']).click()
    
    def verify_on_member_page(self):
        assert all ([
          self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['add_member']).is_displayed(),
          self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['apply_filters']).is_displayed(),
          self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['check_scheduling_records']).is_displayed(),
          self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['search_member']).is_displayed()
        ]), "Not all required member page functions are displayed"
        
        
        
    def tap_search_button(self):
        self.driver.find_element(*self.MEMBER_PAGE_FUNCTIONS['search_member']).click()
        time.sleep(0.5)
        
    def search_phone_number(self, phone_number):
        self.driver.find_element(*self.SEARCH_ELEMENTS['input']).send_keys(phone_number)
        time.sleep(0.5)
        self.driver.press_keycode(66)
        time.sleep(0.5)
        
    def tap_search_result(self):
        self.driver.find_element(*self.SEARCH_ELEMENTS['result']).click()
        time.sleep(0.5)
        
    def select_member_tags(self):
        self.click_more_icon()
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['member_tags']).click()
        time.sleep(0.5)
        
        return self

    def modify_tag_setting(self):
      
        # system tag section
        for section_name, section_locator in self.SYSTEM_TAGS_SECTION.items():
            self.driver.find_element(*section_locator).click()
            time.sleep(0.5)
            
            if section_name in self.SYSTEM_TAGS_OPTIONS:
               options = self.SYSTEM_TAGS_OPTIONS[section_name]
               selected_option = random.choice(options)
               self.driver.find_element(*selected_option).click()
               time.sleep(0.5)
         
        # customize tag section
        selected_tag = random.choice(self.CUSTOMIZE_TAGS)
        self.driver.find_element(*selected_tag).click()
        time.sleep(0.5)
            
        return self
    
    def click_custom_tag_settings(self):
        self.driver.find_element(*self.MANAGE_CUSTOM_TAG).click()
        time.sleep(0.5)
        
    def modify_custom_tag(self):
        self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['add_tag']).click()
        time.sleep(1)
        
        # add new tag
        tag_input = self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')
        random_tag = "自動化測試標籤" +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(5, 10)))
        time.sleep(0.5)
        tag_input.send_keys(random_tag)
        
        self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['save_new_tag']).click()
        time.sleep(0.5)
        
        # edit tag
        self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['edit_tag']).click()
        tag_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        tag_input.click()
        tag_input.clear()
        time.sleep(0.5)
        
        # verify error message
        error_msg = self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['error_msg'])
        assert error_msg.is_displayed(), "Error message not displayed"
        
        # reenter tag name
        tag_input.send_keys(random_tag)
        self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['save_new_tag']).click()
        time.sleep(0.5)
        
        # remove tag
        self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['delete_tag']).click()
        self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['confirm_delete']).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CUSTOM_TAGS_FUNCTIONS['manage_custom_back_button']).click()
        
        # confirm member tag
        self.driver.find_element(*self.SELECT_MEMBER_CONFIRM).click()
        
        # click outside the window to close the dialog
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員護照")').click()
        
        return self
      
    def tap_billing_tab(self):
        time.sleep(0.5)
        self.driver.find_element(*self.PASSPORT_TABS['billing_tab']).click()
    
        return self
    
    def tap_view_details(self):
        self.driver.find_element(*self.BILLING_FUNCTIONS['view_details']).click()
        time.sleep(0.5)
        
        self.driver.find_element(*self.BILLING_FUNCTIONS['expand_details']).click()
        
        self.driver.find_element(*self.BILLING_FUNCTIONS['export_details']).click()
        time.sleep(0.5)
        self.driver.back()
        
        self.driver.find_element(*self.BILLING_FUNCTIONS['view_details_back']).click()
        time.sleep(0.5)
        self.driver.find_element(*self.BILLING_FUNCTIONS['details_back']).click()
        
        return self
    
    def tap_view_checkout(self):
        self.driver.find_element(*self.BILLING_FUNCTIONS['view_checkout']).click()
        time.sleep(0.5)
        
        return self
    
    def delete_and_reprocess_checkout(self):
        self.driver.find_element(*self.BILLING_FUNCTIONS['delete_checkout']).click()
        time.sleep(0.5)
        
        self.driver.find_element(*self.BILLING_FUNCTIONS['delete_checkout_again_option']).click()
    
    def delete_checkout(self):
        self.driver.find_element(*self.BILLING_FUNCTIONS['delete_checkout']).click()
        time.sleep(0.5)
        
        self.driver.find_element(*self.BILLING_FUNCTIONS['delete_checkout_option']).click()
        return self
    
    def verify_on_member_passport_page(self):
        self.driver.find_element(*self.PASSPORT_TABS['info_tab']).click()
        
    def click_top_up_section(self):
        self.driver.find_element(*self.TOP_UP_SECTION['top_up_section']).click()
        time.sleep(0.5)
        
        return self
    
    def edit_top_up_amount(self):
        self.driver.find_element(*self.TOP_UP_SECTION['edit_top_up_icon']).click()
        time.sleep(0.5)
        
        self.driver.find_element(*self.TOP_UP_SECTION['input_top_up_amount']).click()
        amount = random.randint(1, 1000)
        self.driver.find_element(*self.TOP_UP_SECTION['input_top_up_amount']).send_keys(amount)
        
        if random.choice([True, False]):
            self.driver.find_element(*self.TOP_UP_SECTION['increase_button']).click()
        else:
            self.driver.find_element(*self.TOP_UP_SECTION['decrease_button']).click()
        time.sleep(0.5)
        
        self.driver.find_element(*self.TOP_UP_SECTION['confirm_button']).click()
        
        return self
    
    def click_top_up_button(self):
        self.driver.find_element(*self.TOP_UP_SECTION['top_up_button']).click()
        time.sleep(0.5)
        
        return self
    
    def finish_top_up_process(self):
        self.create_checkout_page.select_sales_owner()
        self.create_checkout_page.enter_deposit_amount()
        self.create_checkout_page.select_payment_method()
        self.create_checkout_page.proceed_to_checkout()
        self.create_checkout_page.confirm_checkout()
        time.sleep(1)
        
        return self
      
    def return_to_member_passport(self):
        self.driver.back()
        time.sleep(0.5)
        
        return self
      
    def click_bonus_points_section(self):
        self.driver.find_element(*self.BONUS_POINTS_SECTION['bonus_points_section']).click()
        time.sleep(0.5)
        
        return self
    
    def edit_bonus_points(self):
        # same id same logic 
        self.edit_top_up_amount()
        time.sleep(0.5) 
        
        return self
    
    def click_tickets_section(self):
        self.driver.find_element(*self.TICKETS_SECTION['tickets_section']).click()
        time.sleep(0.5)
        
        return self
    
    def click_sell_ticket_button(self):
        self.driver.find_element(*self.TICKETS_SECTION['sell_ticket_button']).click()
        time.sleep(0.5)
        
        return self
      
    def select_performance_personnel(self):
        self.create_checkout_page.select_sales_owner()
        
    def choose_ticket_type(self):
        self.create_checkout_page.select_ticket()
    
    def finish_checkout_process(self):
        self.create_checkout_page.select_payment_method()
        self.create_checkout_page.proceed_to_checkout()
        self.create_checkout_page.confirm_checkout()
        
        return self
    
    def tap_ticket(self):
        self.driver.find_element(*self.TICKETS_SECTION['ticket']).click()
        time.sleep(0.5)
        
        return self
    
    def use_ticket(self):
        self.driver.find_element(*self.TICKETS_SECTION['use_button']).click()
        time.sleep(0.5)
        
        if random.choice([True, False]):
           plus_button = self.driver.find_element(*self.TICKETS_SECTION['plus_button'])
           clicks = random.randint(3,6)
           for _ in range(clicks):
               plus_button.click()
        
        else:
          input_field = self.driver.find_element(*self.TICKETS_SECTION['input_field'])
          random_number = str(random.randint(10, 100))
          input_field.clear()
          input_field.send_keys(random_number)
        
        time.sleep(1)
        self.driver.find_element(*self.TICKETS_SECTION['save_button']).click()
        
        #todo: 目前點擊後確定後有bug, 確定使用window被蓋在修層, 需要解決
        time.sleep(1)
        self.driver.find_element(*self.TICKETS_SECTION['cancel_button']).click()
        
        # click confirm again
        time.sleep(0.5)
        self.driver.find_element(*self.TICKETS_SECTION['save_button']).click()
        return self
    
    def switch_to_history_tab(self):
        self.driver.find_element(*self.TICKETS_SECTION['history_tab']).click()
        time.sleep(0.5)
        
        return self
      
    def click_gift_ticket_button(self):
        self.driver.find_element(*self.TICKETS_SECTION['gift_ticket_button']).click()
        time.sleep(0.5)
        
        return self
    
    def select_tickets_for_sending(self):
        self.create_checkout_page.select_ticket()
        time.sleep(0.5)
        
        # click confirm btn
        self.driver.find_element(*self.TICKETS_SECTION['save_button']).click()
        time.sleep(1)
        return self
      
    def edit_basic_info(self):
        self.driver.find_element(*self.EDIT_SECTION['edit_info_icon']).click()
        time.sleep(0.5)
        
        # edit name
        name_input = self.driver.find_element(*self.EDIT_SECTION['input'])
        name_input.clear()
        random_nickname = "自動化測試" + ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(3, 10)))
        name_input.send_keys(random_nickname)
        
        self.select_random_gender()
        self.select_random_date()
        
        # click save
        self.driver.find_element(*self.EDIT_SECTION['edit_save']).click()
        self.driver.find_element(*self.EDIT_SECTION['confirm_button']).click()
        
        return self
    
    def edit_custom_fields(self):
        self.driver.find_element(*self.EDIT_SECTION['edit_custom_info_icon']).click()
        time.sleep(0.5)
        
        single_choice = ['官網', 'IG', 'FB']
        selected_choice = random.choice(single_choice)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_choice}').click()
        
        music_choice = ['民謠', '搖滾', '流行']
        num_selections = random.randint(1, 2)
        selected_music = random.sample(music_choice, num_selections)
        for music in selected_music:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, music).click()
            
        option_input = self.driver.find_element(*self.EDIT_SECTION['option_input'])
        option_input.click()
        
        
        random_option = "自動化測試" + ''.join(random.choice(
          string.ascii_letters + string.digits + "!@#$%^&*" + "測試回饋意見"
        ) for _ in range(random.randint(3, 10)))
        option_modal = self.driver.find_element(*self.EDIT_SECTION['input'])
        option_modal.clear()
        option_modal.click()
        option_modal.send_keys(random_option)
        
        # click save
        self.driver.find_element(*self.EDIT_SECTION['modal_save_button']).click()
        
        
        
        # scroll to bottom
        for _ in range(2):
            self.driver.execute_script('mobile: scrollGesture', {
                'left': 100,
                'top': 100,
                'width': 200,
                'height': 800,
                'direction': 'down',
                'percent': 0.9
            })
        time.sleep(1)
        
        # fourth question
        fourth_question = self.driver.find_element(*self.EDIT_SECTION['fourth_question_input'])
        fourth_question.click()
        
        
        random_answer = "自動化測試" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 8)))
        fourth_question_modal = self.driver.find_element(*self.EDIT_SECTION['input'])
        fourth_question_modal.clear()
        fourth_question_modal.click()
        fourth_question_modal.send_keys(random_answer)
        time.sleep(1)
        
        self.driver.find_element(*self.EDIT_SECTION['modal_save_button']).click()
        
        time.sleep(0.5)
        self.driver.find_element(*self.EDIT_SECTION['modal_save_button']).click()
        
        return self
    
    def edit_member_description(self):
        # scroll to bottom
        time.sleep(1)
        for _ in range(1):
            self.driver.execute_script('mobile: scrollGesture', {
                'left': 100,
                'top': 100,
                'width': 200,
                'height': 800,
                'direction': 'down',
                'percent': 0.9
            })
        time.sleep(1)
        
        self.driver.find_element(*self.EDIT_SECTION['edit_member_description_icon']).click()
        time.sleep(0.5)
        
        # edit member description
        member_description = self.driver.find_element(*self.EDIT_SECTION['member_description_input'])
        member_description.click()
        
        member_modal = self.driver.find_element(*self.EDIT_SECTION['input'])
        member_modal.clear()
        member_modal.click()
        
        random_description = "自動化測試" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 8)))
        member_modal.send_keys(random_description)
        self.driver.find_element(*self.EDIT_SECTION['modal_save_button']).click()
        
        # click save
        time.sleep(0.5)
        self.driver.find_element(*self.EDIT_SECTION['modal_save_button']).click()
        
        return self
    
    def click_message_icon(self):
        self.driver.find_element(*self.BOTTOM_NAVIGATION['send_message_icon']).click()
        time.sleep(0.5)
        
        return self
    
    def enter_send_message_page(self):
        self.driver.find_element(*self.SEND_MESSAGE_FUNCTIONS['send_message_button']).click()
        time.sleep(0.5)
        
        # back to member passport page
        self.driver.back()
        time.sleep(0.5)
        
        self.driver.back()
        
        return self
    
    
    def click_sign_document_icon(self):
        self.driver.find_element(*self.BOTTOM_NAVIGATION['sign_document_icon']).click()
        time.sleep(0.5)
        
        return self
    
    def sign_review_document(self):
        self.driver.find_element(*self.SIGN_DOCUMENT_FUNCTIONS['signed_document']).click()
        time.sleep(1)
        
        return self
    
    def click_review_member_icon(self):
        self.driver.find_element(*self.BOTTOM_NAVIGATION['member_review_icon']).click()
        time.sleep(0.5)
        
        return self
    
    def view_member_review(self):
        assert all([
            self.driver.find_element(*self.MEMBER_REVIEW_FUNCTIONS['review_element']).is_displayed(),
            self.driver.find_element(*self.MEMBER_REVIEW_FUNCTIONS['review_content']).is_displayed()
        ])
        
        # back to member passport page
        self.driver.back()
        time.sleep(0.5)

        return self
    
    def click_more_icon(self):
        self.driver.find_element(*self.BOTTOM_NAVIGATION['more_icon']).click()
        time.sleep(0.5)
        
        return self
    
    def link_account_and_send_line_message(self):
        time.sleep(0.5)
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['link_account']).click()
        
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['line_section']).click()
        
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['send_line_message_btn']).click()
        
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['input_message_content']).click()
        time.sleep(0.5)
        
        
        random_msg = "自動化測試" + ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(random.randint(5, 10)))
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['input_modal']).clear()
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['input_modal']).send_keys(random_msg)
        
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['modal_save_button']).click()
        
        #use message template after entering message content
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['use_message_template']).click()
        
        # randomly select a message template
        selected_option = random.choice(self.MESSAGE_TEMPLATE_OPTIONS)
        self.driver.find_element(*selected_option).click()
        time.sleep(0.5)
        
        # manage message template
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['manage_message_template']).click()
        time.sleep(0.5)
        
        
        # add new message template
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['add_new_message_template_button']).click()
        time.sleep(0.5)
        
        title_input = self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['title_input'])
        title_input.click()
        title_input.send_keys(random_msg)
        time.sleep(0.5)
        
        content_input = self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['content_input'])
        content_input.click()
        content_input_modal = self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['input_modal'])
        content_input_modal.clear()
        content_input_modal.click()
        content_input_modal.send_keys(random_msg)
        time.sleep(0.5)
        
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['modal_save_button']).click()
        
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['save_button']).click()
        time.sleep(0.5)

        # remove tag
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['delete_tag']).click()
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['confirm_delete']).click()
        time.sleep(0.5)
        
        # back to message template page
        self.driver.back()
        time.sleep(0.5)
        
        
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['message_save_button']).click()
        time.sleep(1)
        
        # click to save again
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['message_save_button']).click()
        self.driver.find_element(*self.MORE_OPTIONS_FUNCTIONS['confirm']).click()
        
        return self
        
        
    def click_back_to_member_passport_page(self):
        self.driver.back()
        time.sleep(0.5)
        
        self.return_to_member_passport()
        time.sleep(0.5)
        
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員護照")').click()
        
        
        