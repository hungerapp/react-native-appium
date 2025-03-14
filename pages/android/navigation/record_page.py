import random
import string
import time

from appium.webdriver.common.appiumby import AppiumBy


class RecordPage:
    def __init__(self, driver):
        self.driver = driver

    RECORD_ELEMENTS = {
        'records_nav_option': (AppiumBy.ACCESSIBILITY_ID, "紀錄"),
        'appointments_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("預約")'),
        'billing_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帳單")'),
        'recently_added_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近新增")'),
        'recently_canceled_tab': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近取消")'),
        'claim_request_tab': (AppiumBy.ACCESSIBILITY_ID, '請領'),
        'filter_icon': (AppiumBy.ACCESSIBILITY_ID, '篩選'),
        'search_icon': (AppiumBy.ACCESSIBILITY_ID, '搜尋帳單編號'),
        'input_save': (AppiumBy.XPATH, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'view_details': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視明細")'),
        'view_request_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視請領")'),
        'expand_details': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(2)'),
        'export_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'view_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("檢視結帳")'),
        'delete_checkout': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除結帳")'),
        'delete_request': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("刪除請領")'),
        'checkout_note_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入結帳備注")'),
        'edit_remark': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(7)'),
        'save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
        'search_field': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)'),
        'search_result': (AppiumBy.ACCESSIBILITY_ID, '搜尋結果'),
        'check_payment': (AppiumBy.ACCESSIBILITY_ID, '查看支付方式'),
        'delete_checkout_confirm': (AppiumBy.ACCESSIBILITY_ID, '刪除')
    }
    
    FILTER_STAFF_OPTIONS = [
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("QA")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Wen")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Sally")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Bella")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Ella")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Dami")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains ("918")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Test")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("新人1")')
        ]


    def tap_records_option(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['records_nav_option']).click()
        time.sleep(0.5)
        return self

    def tap_recent_appointment(self):
        appointments = self.driver.find_elements(
            AppiumBy.XPATH,
            "//android.view.ViewGroup[contains(@content-desc, '20')]"
        )
        if appointments:
            random.choice(appointments).click()
        time.sleep(2)
        # back to record page
        self.driver.back()
        return self

    def switch_to_canceled_tab(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['recently_canceled_tab']).click()
        time.sleep(0.5)
        return self

    def tap_canceled_order(self):
        canceled_orders = self.driver.find_elements(
            AppiumBy.XPATH,
            "//android.view.ViewGroup[contains(@content-desc, '20')]"
        )
        if canceled_orders:
            random.choice(canceled_orders).click()
        time.sleep(1)
        # back to record page
        self.driver.back()
        
        return self

    def click_billing_tab(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['billing_tab']).click()
        time.sleep(0.5)
        return self
    
    def click_filter_icon(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['filter_icon']).click()
        time.sleep(0.5)
        return self

    def click_filter_and_select_staff(self):
        
        random_staff = random.choice(self.FILTER_STAFF_OPTIONS)
        self.driver.find_element(*random_staff).click()
        time.sleep(0.5)
        
        # click save button
        self.driver.find_element(*self.RECORD_ELEMENTS['save_button']).click()
        time.sleep(1)
        return self
      
      
    def claim_request_tab(self):
        time.sleep(1)
        self.driver.find_element(*self.RECORD_ELEMENTS['claim_request_tab']).click()
        return self

    def search_billing_number(self, number):
        search_icon = self.driver.find_element(
            *self.RECORD_ELEMENTS['search_icon']
        )
        search_icon.click()
        time.sleep(1)
        
        search_field = self.driver.find_element(*self.RECORD_ELEMENTS['search_field'])
        search_field.send_keys(number)
        time.sleep(2)
        self.driver.back()
        return self

    def view_billing_details(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['view_details']).click()
        time.sleep(0.5)
        return self

    def export_details(self, is_expand=False):
        if is_expand:
            self.driver.find_element(*self.RECORD_ELEMENTS['expand_details']).click()
            time.sleep(3)
            self.driver.find_element(*self.RECORD_ELEMENTS['export_button']).click()
            self.navigate_back(times=3)
        else:
            time.sleep(1)
            self.driver.find_element(*self.RECORD_ELEMENTS['export_button']).click()
            time.sleep(2)
            self.navigate_back(times=2)
       
        return self
    
    def navigate_back(self, times):
        for _ in range(times):
            self.driver.back()
            time.sleep(0.5)
        return self

    def check_payment_method(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['check_payment']).click()
        time.sleep(1)
        self.navigate_back(times=2)
        
        return self


    def view_checkout_details(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['view_checkout']).click()
        time.sleep(0.5)

        return self
      
    def view_request_checkout(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['view_request_checkout']).click()
        time.sleep(0.5)

        return self

    def delete_checkout_request(self):
        self.driver.find_element(*self.RECORD_ELEMENTS['delete_request']).click()
        self.driver.find_element(*self.RECORD_ELEMENTS['delete_checkout_confirm']).click()
        time.sleep(1)
        return self

    def return_to_calendar(self):
        self.navigate_back(times=1)
        return self