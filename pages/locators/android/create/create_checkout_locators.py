from appium.webdriver.common.appiumby import AppiumBy

class CreateCheckoutLocators:
      CREATE_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[42]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView[6]/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      CREATE_CHECKOUT_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("結帳")')
      WINDOW_SECTION = {
        'sell_item_option': (AppiumBy.ACCESSIBILITY_ID, '販售商品'),
        'sell_ticket_option': (AppiumBy.ACCESSIBILITY_ID, '販售票券, (會員限定)'),
        'deposit_option': (AppiumBy.ACCESSIBILITY_ID, '客人儲值（入金）, (會員限定)')
      }
      DESIGNATED_APPOINTMENT_TOGGLE = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
      SALES_OWNER_SELECT = (AppiumBy.ACCESSIBILITY_ID, "QA測試人員")
      SALES_OWNER_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
      AUTO_TEST_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試商品")')
      TEST_PRODUCT_OPTIONS = [
              'new UiSelector().text("測試1")',
              'new UiSelector().text("測試2")',
              'new UiSelector().text("測試3")',
              'new UiSelector().text("測試4")',
            ]
      TESTING1_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試1")')
      TESTING_ITEM_INFO = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-info"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      ITEM_INFO_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試1")')
      ITEM_INFO_PRICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NT$")')
      ITEM_INFO_REQUEST_PRICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NT$")')
      ITEM_INFO_BACK_BUTTON = (AppiumBy.XPATH, '//com.horcrux.svg.GroupView')
      SAVE_PRODUCT_BTN = (AppiumBy.XPATH, '//com.horcrux.svg.GroupView')
      SAVE_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      NON_SELECTED_MEMBER_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("尚未選擇會員")')
      CLEAR_INPUT_SEARCH = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="circle-xmark"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      MEMBER_SEARCH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入手機號碼、姓名進行搜尋")')
      MEMBER_SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("972 205690")')
      MEMBER_SEARCH_NOT_FOUND = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查無資料")')
      PHONE_NUMBER_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入電話")')
      NICKNAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入別名")')
      MEMBER_DESCRIPTION_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入內容")')
      MEMBER_DESCRIPTION_MODAL_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
      MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      ADD_NEW_MEMBER_TOGGLE = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      SAVE_NEW_MEMBER_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      DELETE_MEMBER_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="會員"]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      PAYMENT_METHOD = (AppiumBy.ACCESSIBILITY_ID, '選擇支付方式')
      CASH_SECTION = {
        'edit_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
        'input_field': (AppiumBy.XPATH, '//android.widget.EditText')
      }
      CREDIT_CARD_SECTION = {
        'edit_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
        'input_field': (AppiumBy.XPATH, '//android.widget.EditText')
      }
      COMMON_BUTTONS = {
        'clear': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")'),
        'confirm': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      }
      PAYMENT_ERROR_MESSAGE = lambda self, is_above: (
        AppiumBy.ANDROID_UIAUTOMATOR, 
        f'new UiSelector().textContains("{("多" if is_above else "少")}收 NT$")'
      )
      ITEM_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商品")')
      SELECT_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇商品")')
      SELECT_TICKETS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇票券")')
      CLEAR_ITEMS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部清除")')
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
      RIGHT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(6)')
      PERFORMANCE_PERSONNEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("業績歸屬")')
      PERFORMANCE_CHANGE_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲')
      SALES_PERFORMANCE_EDIT_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="pen-to-square"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      TOTAL_PERFORMANCE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      CALCULATE_ICON = (AppiumBy.XPATH, '//android.widget.TextView[@text="找零"]')
      CALCULATE_CHANGE_BACK_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView")')
    
      BONUS_POINTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紅利點數")')
      BONUS_POINTS_QUICK_SELECT_OPTIONS = [
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$1 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$10 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$50 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$100 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$200 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$250 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$500 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$1,000 : 1")')
            ]
      BONUS_POINTS_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      CHECKOUT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("結帳 NT$")')
      MOVE_TO_SIGNATURE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '進行簽名')
      SIGNATURE_PAD = (AppiumBy.CLASS_NAME, "android.widget.Image")
      CLEAR_SIGNATURE = (AppiumBy.ACCESSIBILITY_ID, "清除簽名")
      CONFIRM_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, '確認結帳')
    
      # Sell ticket use ID
      TICKET_ELEMENTS = {
        'ticket1': {
            'select': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票券")'),
            'input': (AppiumBy.XPATH, '//android.widget.EditText')
        },
        'ticket2': {
            'select': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票卷2")'),
            'plus': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="plus"])[2]/com.horcrux.svg.SvgView')
        }
      }
      TICKET_INFO = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-info"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      TICKET_INFO_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票券")')
      TICKET_INFO_BACK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView")')
      SELECT_TICKETS_SAVE_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="check"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    
      DEPOSIT_AMOUNT_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
      EDIT_DEPOSIT_AMOUNT_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      EDIT_SALES_AMOUNT_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')