from pages.locators.android.navigation.more.tutorial_book_locators import TutorialBookLocators

class TutorialBookPage():
    def __init__(self, driver):
        self.driver = driver
        self.tutorial_book_locators = TutorialBookLocators()
        
    def click_tutorial_book(self):
        self.driver.find_element(*self.tutorial_book_locators.TUTORIAL_BOOK_BUTTON).click()
        return self
    
    def return_to_calendar_page(self):
        self.driver.back()
        return self
    
