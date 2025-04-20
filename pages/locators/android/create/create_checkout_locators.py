from appium.webdriver.common.appiumby import AppiumBy

class CreateCheckoutLocators:
      CREATE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'calendar-fab-trigger')
      CREATE_CHECKOUT_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("結帳")')
      WINDOW_SECTION = {
        'sell_item_option': (AppiumBy.ACCESSIBILITY_ID, '販售商品'),
        'sell_ticket_option': (AppiumBy.ACCESSIBILITY_ID, '販售票券, (會員限定)'),
        'deposit_option': (AppiumBy.ACCESSIBILITY_ID, '客人儲值（入金）, (會員限定)')
      }
      DESIGNATED_APPOINTMENT_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, "該筆為指定業績-switch-button")
      SALES_OWNER_SELECT_QA_TESTER = (AppiumBy.ACCESSIBILITY_ID, "checkbox-single-option-0")
      SALES_OWNER_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
      AUTO_TEST_TAB = (AppiumBy.ACCESSIBILITY_ID, 'category-8')
      TEST_PRODUCT_OPTIONS = [
              'product-item-0',
              'product-item-1',
              'product-item-2',
              'product-item-3',
            ]
      TESTING1_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試1")')
      TESTING_ITEM_INFO = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-info"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      ITEM_INFO_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試1")')
      ITEM_INFO_PRICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NT$")')
      ITEM_INFO_REQUEST_PRICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NT$")')
      ITEM_INFO_BACK_BUTTON = (AppiumBy.XPATH, '//com.horcrux.svg.GroupView')
      SAVE_PRODUCT_BTN = (AppiumBy.XPATH, '//com.horcrux.svg.GroupView')
      SAVE_ITEM_BTN = (AppiumBy.ACCESSIBILITY_ID, 'check')
      NON_SELECTED_MEMBER_SECTION = (AppiumBy.ACCESSIBILITY_ID, '尚未選擇會員')
      CLEAR_INPUT_SEARCH = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
      MEMBER_SEARCH = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
      MEMBER_SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("972 205690")')
      MEMBER_SEARCH_NOT_FOUND = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查無資料")')
      ADD_MEMBER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'user-plus')
      DELETE_MEMBER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'trash-can')
      PAYMENT_METHOD = (AppiumBy.ACCESSIBILITY_ID, '選擇支付方式')
      CASH_SECTION = {
        'edit_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(0)'),
        'input_field': (AppiumBy.XPATH, '//android.widget.EditText')
      }
      CREDIT_CARD_SECTION = {
        'edit_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(1)'),
        'input_field': (AppiumBy.XPATH, '//android.widget.EditText')
      }
      COMMON_BUTTONS = {
        'clear': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")'),
        'confirm': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      }
      PAYMENT_ERROR_MESSAGE = lambda self, is_above: (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().textMatches(".*{("多" if is_above else "少")}收\\sNT\\$.*")'
      )
      ITEM_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商品")')
      SELECT_ITEM_BTN = (AppiumBy.ACCESSIBILITY_ID, '選擇商品')
      SELECT_TICKETS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇票券")')
      CLEAR_ITEMS_BTN = (AppiumBy.ACCESSIBILITY_ID, '全部清除')
      TICKET_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("票券")')
      CLEAR_TICKETS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部清除")')
      CHECKOUT_SECTION = {
       'record_content': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入內容")'),
       'content_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")'),
       'save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
       'clear_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")'),
       'cancel_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'),
       'window_leave_button': (AppiumBy.ACCESSIBILITY_ID, '離開')
      }
      CANCEL_RECORD = (AppiumBy.XPATH, "//android.view.View[@content-desc='取消']")
      SALES_PERFORMANCE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("總業績")')
      POSTING_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("業績記入日期")')
      RIGHT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right")')
      PERFORMANCE_PERSONNEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("業績歸屬")')
      PERFORMANCE_CHANGE_PERSONNEL_SALLY = (AppiumBy.ACCESSIBILITY_ID, 'checkbox-single-option-2')
      SALES_PERFORMANCE_EDIT1_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(7)')
      SALES_PERFORMANCE_EDIT2_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(6)')
      TOTAL_PERFORMANCE_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      CALCULATE_ICON = (AppiumBy.ACCESSIBILITY_ID, '找零')
      CALCULATE_CHANGE_BACK_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView")')
    
      BONUS_POINTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紅利點數")')
      BONUS_POINTS_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, '點數-text-input')
      BONUS_POINTS_QUICK_SELECT_OPTIONS = [
            (AppiumBy.ACCESSIBILITY_ID, 'NT$1 : 1'),
            (AppiumBy.ACCESSIBILITY_ID, 'NT$10 : 1'),
            (AppiumBy.ACCESSIBILITY_ID, 'NT$50 : 1'),
            (AppiumBy.ACCESSIBILITY_ID, 'NT$100 : 1'),
            (AppiumBy.ACCESSIBILITY_ID, 'NT$200 : 1'),
            (AppiumBy.ACCESSIBILITY_ID, 'NT$250 : 1'),
            (AppiumBy.ACCESSIBILITY_ID, 'NT$500 : 1'),
            (AppiumBy.ACCESSIBILITY_ID, 'NT$1,000 : 1')
            ]
      BONUS_POINTS_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      CHECKOUT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("結帳 NT$")')
      MOVE_TO_SIGNATURE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '進行簽名')
      SIGNATURE_PAD = (AppiumBy.CLASS_NAME, "android.widget.Image")
      CLEAR_SIGNATURE = (AppiumBy.ACCESSIBILITY_ID, "清除簽名")
      CONFIRM_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, '確認結帳')
    
      # Sell ticket use ID
      TICKET_ELEMENTS = {
        'ticket1': {
            'select': (AppiumBy.ACCESSIBILITY_ID, '自動化測試票券'),
            'input': (AppiumBy.ACCESSIBILITY_ID, 'undefined-number-field-input')
        },
        'ticket2': {
            'select': (AppiumBy.ACCESSIBILITY_ID, '自動化測試票卷2'),
            'plus': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("plus").instance(1)')
        }
      }
      TICKET_INFO = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-info"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      TICKET_INFO_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票券")')
      TICKET_INFO_BACK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView")')
      SELECT_TICKETS_SAVE_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(0)')
    
      DEPOSIT_AMOUNT_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
      EDIT_DEPOSIT_AMOUNT_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      EDIT_SALES_AMOUNT_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')