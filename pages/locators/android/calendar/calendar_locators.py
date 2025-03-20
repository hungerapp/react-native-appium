from appium.webdriver.common.appiumby import AppiumBy

class CalendarLocators:
      DATE_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down")')
      ARROW = (AppiumBy.ACCESSIBILITY_ID, 'arrow-right')
      MONTHS = [
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
        (AppiumBy.ACCESSIBILITY_ID, '11月'),
        (AppiumBy.ACCESSIBILITY_ID, '12月'),
      ]
      SELECT_WINDOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(7)')
      DISPLAY_MODES = [
        (AppiumBy.ACCESSIBILITY_ID, '月'),
        (AppiumBy.ACCESSIBILITY_ID, '週'),
        (AppiumBy.ACCESSIBILITY_ID, '3日'),
        (AppiumBy.ACCESSIBILITY_ID, '1日'),
        (AppiumBy.ACCESSIBILITY_ID, '服務人員 (日)'),
        (AppiumBy.ACCESSIBILITY_ID, '列表 (日)'),
      ]
    
      MODE_XPATHS = {
        0: '//android.widget.TextView[@text="月"]',
        1: '//android.widget.TextView[@text="週"]',
        2: '//android.widget.TextView[@text="3日"]',
        3: '//android.widget.TextView[@text="1日"]',
        4: '//android.widget.TextView[@text="服務人員 (日)"]',
        5: '//android.widget.TextView[@text="列表 (日)"]',
      }
      
      PERSONNEL_OPTIONS = {
            "Dami": ['Dami #美容 #美甲'],
            "Ella及Sally": ['Ella #熱蠟除毛 #美容', 'Sally #美睫 #美甲'],
            "Bella": 'Bella #美甲'
        }
      
      COLOR_XPATHS = [
        '(//android.view.ViewGroup[@resource-id="circle"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[9]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[6]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[10]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[11]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[5]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
    ]
      
      FILTER_ICON = (AppiumBy.ACCESSIBILITY_ID, '篩選')
      SELECT_ALL_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, '全部選取')
      EDIT_COLOR = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="QA測試人員"]/android.view.ViewGroup[3]/android.view.ViewGroup')
      FILTER_SAVE_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="篩選"]/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      TODAY_ICON = (AppiumBy.ACCESSIBILITY_ID, '今天')
      REFRESH_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="arrow-rotate-right"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
      BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
      BACK_TO_CALENDAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '返回')  
      ADD_APPOINTMENT_OPTION = (AppiumBy.ACCESSIBILITY_ID, '新增預約')
      LONG_PRESS_DATE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("6")')
      ADD_EVENT_OPTION = (AppiumBy.ACCESSIBILITY_ID, '新增事件')
    
    
