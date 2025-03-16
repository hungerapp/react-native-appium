from appium.webdriver.common.appiumby import AppiumBy

class Member_Locators:
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
        'member_tag': (AppiumBy.ACCESSIBILITY_ID, '會員標籤, 無'),
        'birthday_month': (AppiumBy.ACCESSIBILITY_ID, '生日月份, 無'),
        'sign': (AppiumBy.ACCESSIBILITY_ID, '星座, 無'),
        'age': (AppiumBy.ACCESSIBILITY_ID, '年齡, 無'),
        'save_button': (AppiumBy.XPATH, '(//com.horcrux.svg.GroupView)[2]')
      }
    
      DELETE_CONDITION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("排除條件, 黑名單, 評分低於4.0")')
      DELETE_CONDITION_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(9)')
    
      MEMBER_FILTER_OPTIONS = {
        'member_tag': [
          (AppiumBy.ACCESSIBILITY_ID, '全部選取'),
          (AppiumBy.ACCESSIBILITY_ID, '社區熟客'),
          (AppiumBy.ACCESSIBILITY_ID, '老闆朋友'),
          (AppiumBy.ACCESSIBILITY_ID, '敏感型客人'),
          (AppiumBy.ACCESSIBILITY_ID, '口碑介紹客')
        ],
        'birthday_month': [
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
        'sign' : [
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
        'age' : [
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
        'amount' : [
          (AppiumBy.ACCESSIBILITY_ID, '累計至今'),
          (AppiumBy.ACCESSIBILITY_ID, '近60天'),
          (AppiumBy.ACCESSIBILITY_ID, '近90天'),
          (AppiumBy.ACCESSIBILITY_ID, '近180天'),
          (AppiumBy.ACCESSIBILITY_ID, '近360天'),
          (AppiumBy.ACCESSIBILITY_ID, '今年累計'),
          (AppiumBy.ACCESSIBILITY_ID, '去年累計'),
        ]
      }
      
      # handle all input field       
      INPUT_PAIRS = [
        ('min_cost_amount', 'max_cost_amount'),         
        ('min_come_amount', 'max_come_amount'),        
        ('min_top_up_remaining', 'max_top_up_remaining'), 
        ('min_join_date', 'max_join_date'),            
        ('min_last_visit_date', 'max_last_visit_date')  
      ]
          
          
    
      DELETE_CONDITION_OPTIONS = {  
        'delete_condition': [
          (AppiumBy.ACCESSIBILITY_ID, '全部選取'),
          (AppiumBy.ACCESSIBILITY_ID, '黑名單'),
          (AppiumBy.ACCESSIBILITY_ID, '來店次數為0'),
          (AppiumBy.ACCESSIBILITY_ID, '評分低於4.0'),
        ]
      }
    
      INPUT_AMOUNT = {
        'min_cost_amount': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[1]'),
        'max_cost_amount': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[1]'),
        'min_come_amount': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[2]'),
        'max_come_amount': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[2]'),
        'min_top_up_remaining': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[3]'),
        'max_top_up_remaining': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[3]'),
        'min_join_date': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[4]'),
        'max_join_date': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[4]'),
        'min_last_visit_date': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最小值"])[5]'),
        'max_last_visit_date': (AppiumBy.XPATH, '(//android.widget.EditText[@text="最大值"])[5]'),
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
      }
    
      SELECT_MEMBER_CONFIRM = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="check"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      MEMBER_PASSPORT_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員護照")')
      
      
      PASSPORT_TABS = {
        'billing_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帳單")'),
        'info_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("資訊")'),
        'reserve_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("預約")'),
      }
    
      BILLING_FUNCTIONS = {
        'view_details': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="檢視明細"])[1]'),
        'view_checkout': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="檢視結帳"])[1]'),
        'expand_details': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="chevron-right"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
        'export_details': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'delete_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除結帳")'),
        'delete_checkout_option': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("刪除結帳").instance(1)'),
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
        'modal_save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      }
      
      SINGLE_CHOICE = ['官網', 'IG', 'FB']
      
      MUSIC_CHOICE = ['民謠', '搖滾', '流行']
    
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
        'add_to_blacklist': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("加入黑名單")'),
        'remove_from_blacklist': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("移出黑名單")'),
        'deposit_title': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("儲值金")'),
        'selct_item_button': (AppiumBy.ACCESSIBILITY_ID, '選擇商品'),
        'select_ticket_button': (AppiumBy.ACCESSIBILITY_ID, '選擇票券'),
      }
    
      MESSAGE_TEMPLATE_OPTIONS = [
        (AppiumBy.ACCESSIBILITY_ID, '美甲保固, 感謝你的到來，美甲項目我們提供7天的保固期，若有掉甲、缺色，請重新預約與我們聯繫\nhunger Salon團隊敬上'),
        (AppiumBy.ACCESSIBILITY_ID, '關懷, 你好，好久不見。上次做的服務，還滿意嗎？歡迎你再次來訪，我們會盡全力打造你的美麗！\n\n上次做的服務，還滿意嗎？'),
        (AppiumBy.ACCESSIBILITY_ID, '我是名字很長很長很長很長很長很長很長很長很長的範本, 一段內容一段內容一段內容一段內容一段內容一段內容一段內容一段內容\n\n一段內容一段內容一段內容一段內容\n\n一段內容一段內容一段內容一段內容一段內容一段內容一段內容一段內容'),
        (AppiumBy.ACCESSIBILITY_ID, 'ok, okletsgo')
      ]
    
      