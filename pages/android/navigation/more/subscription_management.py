import time

from pages.locators.android.navigation.more.subscription_management_locators import SubscriptionManagementLocators

class SubscriptionManagementPage():
    def __init__(self, driver):
        self.driver = driver
        self.subscription_management_locators = SubscriptionManagementLocators()

    def click_subscription_management(self):
        self.driver.find_element(*self.subscription_management_locators.SUBSCRIPTION_MANAGEMENT).click()
        time.sleep(0.5)
        return self
      
    def return_to_calendar_page(self):
        self.driver.find_element(*self.subscription_management_locators.RETURN_TO_CALENDAR_PAGE).click()
        time.sleep(0.5)
        return self
    
    
    