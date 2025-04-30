import time

from pages.locators.android.navigation.more.tutorial_guide_locators import TutorialGuideLocators

class TutorialGuidePage():
    def __init__(self, driver):
        self.driver = driver
        self.tutorial_guide_locators = TutorialGuideLocators()

    def click_tutorial_guide(self):
        self.driver.find_element(*self.tutorial_guide_locators.TUTORIAL_GUIDE_BUTTON).click()
        time.sleep(0.5)
        return self
      
    def click_tutorial_video(self):
        self.driver.find_element(*self.tutorial_guide_locators.TUTORIAL_VIDEO_BUTTON).click()
        time.sleep(0.5)
        self.driver.back()
        return self
      
    def click_service_staff_section(self):
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.SERVICE_STAFF_SECTION).click()
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.CANCEL_BUTTON).click()
        return self
    
    def click_service_items_section(self):
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.SERVICE_ITEMS_SECTION).click()
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.CANCEL_BUTTON).click()
        return self
    
    def click_online_reservation_management_section(self):
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.ONLINE_RESERVATION_MANAGEMENT_SECTION).click()
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.CANCEL_BUTTON).click()
        return self
      
    def click_connect_line_official_account_section(self):
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.CONNECT_LINE_OFFICIAL_ACCOUNT_SECTION).click()
        time.sleep(1)
        self.driver.find_element(*self.tutorial_guide_locators.CANCEL_BUTTON).click()
        return self
      
    def click_tutorial_book_button(self):
        self.driver.find_element(*self.tutorial_guide_locators.TUTORIAL_BOOK_BUTTON).click()
        time.sleep(1)
        self.driver.back()
        return self
      
    def return_to_calendar_page(self):
        self.driver.find_element(*self.tutorial_guide_locators.CANCEL_BUTTON).click()
        return self