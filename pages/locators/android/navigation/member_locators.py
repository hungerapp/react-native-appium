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
      ADD_MEMBER = (AppiumBy.ACCESSIBILITY_ID, '新增會員')
      APPLY_FILTERS = (AppiumBy.ACCESSIBILITY_ID, '會員篩選')
      CHECK_SCHEDULING_RECORDS = (AppiumBy.ACCESSIBILITY_ID, '排程記錄')
      SEARCH_MEMBER = (AppiumBy.ACCESSIBILITY_ID, '搜尋')
      SENT_TAG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("已發送").instance(0)')
      MEMBER_FILER_BACK = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      PASSPORT_RETURN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      SCHEDULING_RECORDS_BACK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
      
      # Member filter section
      MEMBER_FILTER_SECTIONS = {
        'member_tag': (AppiumBy.ACCESSIBILITY_ID, '會員標籤-multi-select-field'),
        'birthday_month': (AppiumBy.ACCESSIBILITY_ID, '生日月份-multi-select-field'),
        'sign': (AppiumBy.ACCESSIBILITY_ID, '星座-multi-select-field'),
        'age': (AppiumBy.ACCESSIBILITY_ID, '年齡-multi-select-field'),
        'save_button': (AppiumBy.XPATH, '(//com.horcrux.svg.GroupView)[2]')
      }
    
      DELETE_CONDITION = (AppiumBy.ACCESSIBILITY_ID, '排除條件-multi-select-field')
    
      MEMBER_FILTER_OPTIONS = {
        'member_tag': [
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("全部選取")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("社區熟客")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("老闆朋友")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("敏感型客人")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("口碑介紹客")')
        ],
        'birthday_month': [
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("全部選取")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("1月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("2月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("3月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("4月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("5月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("6月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("7月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("8月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("9月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("10月")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("11月")')
        ],
        'sign' : [
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("全部選取")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("牡羊座 (3/21 ~ 4/19)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("金牛座 (4/20 ~ 5/20)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("雙子座 (5/21 ~ 6/20)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("巨蟹座 (6/21 ~ 7/22)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("獅子座 (7/23 ~ 8/22)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("處女座 (8/23 ~ 9/22)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("天秤座 (9/23 ~ 10/22)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("天蠍座 (10/23 ~ 11/21)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("射手座 (11/22 ~ 12/21)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("摩羯座 (12/22 ~ 1/19)")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("水瓶座 (1/20 ~ 2/18)")')
        ],
        'age' : [
          #(AppiumBy.ACCESSIBILITY_ID, '全部選取'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("15歲以下")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("16~20歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("21~25歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("26~30歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("31~35歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("36~40歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("41~45歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("46~50歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("51~55歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("56~60歲")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("61~65歲")')
        ],
        'amount' : [
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("累計至今")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("近60天")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("近90天")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("近180天")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("近360天")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("今年累計")'),
          (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("去年累計")'),
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
      COST_AMOUNT_MENU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down").instance(0)')
    
      # Come amount menu
      COME_AMOUNT_MENU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down").instance(1)')
    
      FILTER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '進行篩選')
      RESET_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '重置條件')
    
    
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
        (AppiumBy.ACCESSIBILITY_ID, "checkbox-multiple-option-0"),
        (AppiumBy.ACCESSIBILITY_ID, "checkbox-multiple-option-1"),
        (AppiumBy.ACCESSIBILITY_ID, "checkbox-multiple-option-2"),
        (AppiumBy.ACCESSIBILITY_ID, "checkbox-multiple-option-3")
      ]
    
      MANAGE_CUSTOM_TAG = (AppiumBy.ACCESSIBILITY_ID, '管理自訂標籤')
      
      # Custom tag FUNCTIONS
      CUSTOM_TAG_ADD_TAG = (AppiumBy.ACCESSIBILITY_ID, '新增標籤')
      CUSTOM_TAG_EDIT_TAG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(4)')
      CUSTOM_TAG_DELETE_TAG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("circle-minus").instance(4)')
      CUSTOM_TAG_SAVE_NEW_TAG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
      CUSTOM_TAG_ERROR_MSG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 此欄位為必填。")')
      CUSTOM_TAG_CONFIRM_DELETE = (AppiumBy.ACCESSIBILITY_ID, '刪除')
      

    
      SELECT_MEMBER_CONFIRM = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="check"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      MEMBER_PASSPORT_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員護照")')
      
      
      PASSPORT_TABS = {
        'billing_tab': (AppiumBy.ACCESSIBILITY_ID, '帳單'),
        'info_tab': (AppiumBy.ACCESSIBILITY_ID, '資訊'),
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
    
      # Top-up balance section
      TOP_UP_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("儲值金")')
      EDIT_TOP_UP_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square")')
      INPUT_TOP_UP_AMOUNT = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
      INCREASE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '增加')
      DECREASE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '扣除')
      BALANCE_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '確定')
      TOP_UP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '儲值')
     
      # Bonus points section
      BONUS_POINTS_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紅利點數")')
    
      # Tickets section
      TICKETS_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("票券")')
      SELL_TICKET_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '販售票券')
      TICKET = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("自動化測試票券")')
      USE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '使用')
      PLUS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("plus")')
      INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'undefined-number-field-input')
      SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(0)')
      TICKET_PAGE_RETURN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      HISTORY_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歷史紀錄")')
      GIFT_TICKET_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '贈送票券')
      

    
      # Edit section below member passport page
      EDIT_INFO_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("基本資訊")')
      EDIT_BASIC_INFO_CHOOSE_DATE_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("chevron-right")')
      OTHER_NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, '別名-text-input')
      INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
      EDIT_SAVE = (AppiumBy.ACCESSIBILITY_ID, 'check')
      EDIT_CUSTOM_INFO_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自訂欄位")')
      EDIT_MEMBER_DESCRIPTION_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員描述")')
      CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '確定')
      CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '取消')
      OPTION_INPUT = (AppiumBy.ACCESSIBILITY_ID, '簡答 / 選填 / 僅商家可見-textarea-field')
      SIMPLE_ANSWER_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'textMatches("簡答 / 選填 / 僅商家可見")')
      FOURTH_QUESTION_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("簡答 / 選填 / 僅商家可見-textarea-field").instance(1)')
      FRIEND_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("自動化測試")')
      MEMBER_DESCRIPTION_INPUT = (AppiumBy.ACCESSIBILITY_ID, '會員描述-textarea-field')
      MODAL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      CUSTOM_MODAL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(0)')
      MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      


      SINGLE_CHOICE = ['checkbox-single-option-0', 'checkbox-single-option-1', 'checkbox-single-option-2']
      
      MUSIC_CHOICE = ['checkbox-multiple-option-0', 'checkbox-multiple-option-1', 'checkbox-multiple-option-2']
    
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
    
    
      # Link account
      LINK_ACCOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("綁定帳號")')
      LINE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Beck")')
      ADD_NEW_APPOINTMENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增預約")')
      QUICK_CHECKOUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("快速結帳")')
      MEMBER_TAGS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員標籤")')
      SEND_LINE_MESSAGE_BTN = (AppiumBy.ACCESSIBILITY_ID, '發送 LINE 訊息')
      INPUT_MESSAGE_CONTENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入訊息內容")')
      INPUT_MODAL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
      MODAL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      USE_MESSAGE_TEMPLATE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("使用訊息範本")')
      MANAGE_MESSAGE_TEMPLATE = (AppiumBy.ACCESSIBILITY_ID, '管理訊息範本')
      ADD_NEW_MESSAGE_TEMPLATE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增訊息範本')
      TITLE_INPUT = (AppiumBy.ACCESSIBILITY_ID, '範本名稱-text-input')
      CONTENT_INPUT = (AppiumBy.ACCESSIBILITY_ID, '範本內容-textarea-field')
      EDIT_TAG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(30)')
      ERROR_MSG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("此欄位為必填。")')
      SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(2)')
      DELETE_TAG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("circle-minus").instance(8)')
      CONFIRM = (AppiumBy.ACCESSIBILITY_ID, '確定')
      CONFIRM_DELETE = (AppiumBy.ACCESSIBILITY_ID, '刪除')
      MESSAGE_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      ADD_TO_BLACKLIST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("加入黑名單")')
      REMOVE_FROM_BLACKLIST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("移出黑名單")')
      DEPOSIT_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("儲值金")')
      SELECT_ITEM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("選擇商品")')
      ADD_NEW_MESSAGE_TEMPLATE_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(2)')
      SELECT_TICKET_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("選擇票券")')
      
    
      MESSAGE_TEMPLATE_OPTIONS = [
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("美甲保固")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("關懷")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("我是名字很長")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("ok")')
      ]
    
      