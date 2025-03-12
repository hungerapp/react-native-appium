import random
import time

from selenium.webdriver.common.action_chains import ActionChains

from appium.webdriver.common.appiumby import AppiumBy



class CalendarPage:
    def __init__(self, driver):
        self.driver = driver
        self.current_display_mode = None

  
    DATE_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(2)')
    ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(21)')
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
    FILTER_ICON = (AppiumBy.ACCESSIBILITY_ID, '篩選')
    SELECT_ALL_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, '全部選取')
    EDIT_COLOR = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="QA測試人員"]/android.view.ViewGroup[3]/android.view.ViewGroup')
    FILTER_SAVE_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="篩選"]/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    TODAY_ICON = (AppiumBy.ACCESSIBILITY_ID, '今天')
    REFRESH_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="arrow-rotate-right"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    BACK_TO_CALENDAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '返回')  
    ADD_APPOINTMENT_OPTION = (AppiumBy.ACCESSIBILITY_ID, '新增預約')
    ADD_EVENT_OPTION = (AppiumBy.ACCESSIBILITY_ID, '新增事件')
    
    
    def open_month_selection(self):
        self.driver.find_element(*self.DATE_SELECTOR).click()
        time.sleep(2)

    def change_month_display_mode(self):
        clicks_arrow = random.randint(1, 3)
        for _ in range(clicks_arrow):
            self.driver.find_element(*self.ARROW).click()
            time.sleep(0.5)
        
        time.sleep(0.5)
        random_month = random.choice(self.MONTHS)
        self.driver.find_element(*random_month).click()
    
    def change_calendar_display(self):
        self.driver.find_element(*self.DISPLAY_MODES[0]).click()
        
    def select_target_display_mode(self):
        """Select a random display mode from the window"""
        select_window = self.driver.find_element(*self.SELECT_WINDOW)
        if select_window.is_displayed() and select_window.is_enabled():
            self.current_display_mode = 5
            self.driver.find_element(*self.DISPLAY_MODES[5]).click()

    def switch_back_to_month_mode(self):
        """Switch back to the month display mode"""
        if self.current_display_mode is None:
            time.sleep(2)
            current_mode_button = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="列表 (日)"]')
            current_mode_button.click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="月"]').click() 

    def filter_personnel(self):
        time.sleep(0.5)
        self.driver.find_element(*self.FILTER_ICON).click()

    def select_personnel(self):
        options = {
            "Dami": ['Dami #美容 #美甲'],
            "Ella及Sally": ['Ella #熱蠟除毛 #美容', 'Sally #美睫 #美甲'],
            "Bella": 'Bella #美甲'
        }
        
        choice = random.choice(list(options.keys()))
        
        if isinstance(options[choice], list):
            time.sleep(0.5)
            for element_id in options[choice]:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, element_id).click()
        else:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, options[choice]).click()
            
        
            
            
    def edit_personnel_colors(self):
        color_xpaths = [
        '(//android.view.ViewGroup[@resource-id="circle"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[9]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[6]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[10]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[11]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
        '(//android.view.ViewGroup[@resource-id="circle"])[5]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
    ]
       
        edit_color = self.driver.find_element(*self.EDIT_COLOR)
        edit_color.click()
       
        color_xpath = random.choice(color_xpaths)
        time.sleep(0.5)
        color_choice = self.driver.find_element(AppiumBy.XPATH, color_xpath)
        color_choice.click()
        
        self.driver.find_element(*self.FILTER_SAVE_BUTTON).click()
        
    def change_personnel_filter(self):
        time.sleep(0.5)
        self.driver.find_element(*self.FILTER_ICON).click()
        self.driver.find_element(*self.SELECT_ALL_PERSONNEL).click()
        time.sleep(0.5)
        self.driver.find_element(*self.FILTER_SAVE_BUTTON).click()
    
    def perform_swipe_left_or_right(self, direction=None, times=None):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        # 定義滑動的中心位置
        start_x = width * 0.6 if direction == 'left' else width * 0.4
        y = height * 0.6

        swipe_times = times if times else random.randint(3, 4)
        swipe_direction = direction if direction else random.choice(['left', 'right'])

        for _ in range(swipe_times):
            self.driver.execute_script("mobile: swipeGesture", {
                'left': start_x,
                'top': y,
                'width': width * 0.5,
                'height': 10,
                'direction': swipe_direction,
                'percent': 0.6
            })
            time.sleep(1) 
    
    def navigate_to_today(self):
        time.sleep(0.5)
        self.driver.find_element(*self.TODAY_ICON).click()


    def view_orders(self):
        """Click on a random point in the calendar area"""
        try:

            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            
            # Calculate the coordinates of the calendar area
            calendar_top = height * 0.3     # Avoid the top title area
            calendar_bottom = height * 0.7   # Avoid the bottom navigation area
            calendar_left = width * 0.1      # Left boundary
            calendar_right = width * 0.9     # Right boundary
            
            # Randomly select a point in the calendar area
            x = random.uniform(calendar_left, calendar_right)
            y = random.uniform(calendar_top, calendar_bottom)
            
            # Execute click gesture
            self.driver.execute_script('mobile: clickGesture', {
                'x': x,
                'y': y
            })
            
            time.sleep(2)
            
        except Exception as e:
            raise Exception(f"Cannot click on the calendar area: {str(e)}")

    def click_back_button(self):
        self.driver.back()
        time.sleep(1)
        
    def long_press_date(self):
        time.sleep(1)
        try:
            element = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("6")'
            )
        
            actions = ActionChains(self.driver)
            actions.click_and_hold(element)
            actions.pause(2)  
            actions.release()
            actions.perform()
        
        except Exception as e:
            print(f"長按操作失敗: {str(e)}")
            raise
    
    def add_appointment(self):
        time.sleep(1)
        add_appointment_option = self.driver.find_element(*self.ADD_APPOINTMENT_OPTION)
        if add_appointment_option.is_displayed():
            time.sleep(0.5)
            add_appointment_option.click()
        else:
            print("Add appointment option is not visible or enabled")
              
        
    def add_event(self):
        self.driver.find_element(*self.ADD_EVENT_OPTION).click()

    def refresh_calendar(self):
        self.driver.find_element(*self.REFRESH_BUTTON).click()
