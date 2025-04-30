from appium.webdriver.common.appiumby import AppiumBy

class CreateEventLocators:
  
      CREATE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'calendar-fab-trigger')
      CREATE_EVENT_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("事件")')
      SERVICE_PERSONNEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
      QA_TEST_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
      SELECT_ALL_OPTION = (AppiumBy.ACCESSIBILITY_ID, '全部選取')
      PERSONNEL_OPTIONS = [
        (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲'),
        (AppiumBy.ACCESSIBILITY_ID, 'Bella #美甲'),
        # Add more personnel options as needed
      ]
      EVENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("事件")')
      EVENT_TITLE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    
      QUICK_OPTIONS = ['教學', '請假', '休息', '外出', '忙碌1', '忙碌2', 
                        '幫寶寶', '執政者', '課程', '2', '3', '4', '我是新增事件1', '我是新增事件2']
    
      # May change frequently
      # (//com.horcrux.svg.GroupView)[2]
      # new UiSelector().className("com.horcrux.svg.PathView").instance(1)
      SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      NEW_EVENT_PAGE_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      TIME_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(1)')
      TIME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("時間")')
      ALL_DAY_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '整日-switch-button')
      CLICK_START_TIME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("開始時間")')
      CLICK_END_TIME = (AppiumBy.ACCESSIBILITY_ID, '結束時間, 選擇時間')
      SELECTED_DATE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇日期")')
      LEFT_DATE_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-left")')
      RIGHT_DATE_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right")')
      REPEAT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("重複")')
      REPEAT_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(1)')
      REPEAT_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '重複-switch-button')
      WEEKDAYS = [
        '週一', '週二', '週三', '週四', '週五', '週六', '週日'
      ]
      ERROR_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "此欄位為必填")]')
      ERROR_ICON1 = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-exclamation"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      ERROR_ICON2 = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-exclamation"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      ERROR_ICON3 = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-exclamation"])[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      REPEAT_BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("xmark").instance(1)')
      BACK_TO_CALENDAR = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      WINDOW_LEAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '離開')
    
      MODIFY_QUICK_SELECT_ICON = (AppiumBy.ID, 'pen_to_square')