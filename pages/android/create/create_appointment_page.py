import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.create.create_appointment_locators import CreateAppointmentLocators

class CreateAppointmentPage(CommonUseSection):
    def __init__(self, driver):
        self.driver = driver
        self.create_appointment_locators = CreateAppointmentLocators()
    
    
    def personal_page_back_to_calendar(self):
        """Click back to calendar button"""
        self.driver.find_element(*self.create_appointment_locators.PERSONAL_PAGE_BACK_TO_CALENDAR_BTN).click()
        time.sleep(3)
        return self
    
    
    def create_appointment(self):
        """Click create appointment button"""
        
        try:
          time.sleep(1.5)
          create_button = self.driver.find_element(*self.create_appointment_locators.CREATE_BTN)
          if create_button.is_displayed() and create_button.is_enabled():
              create_button.click()
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create appointment button after multiple attempts")
      
        self.driver.find_element(*self.create_appointment_locators.CREATE_APPOINTMENT_OPTION).click()
        return self
      
    def click_contact_info_section(self):
        """Click contact info section"""
        self.driver.find_element(*self.create_appointment_locators.CONTACT_INFO_SECTION).click()
        return self

    def fill_anonymous_contact(self):
        """Fill in contact info as anonymous"""
        self.driver.find_element(*self.create_appointment_locators.CONTACT_INFO_SECTION).click()
        try: 
           name_save_btn = self.driver.find_element(*self.create_appointment_locators.SAVE_DEFAULT_CONTACT_BUTTON)
           if name_save_btn.is_displayed() and name_save_btn.is_enabled():
               name_save_btn.click()
        except NoSuchElementException:
            raise NoSuchElementException("Unable to find save contact button after multiple attempts")
        
        time.sleep(2)
        return self

    def fill_existing_contact(self, test_name, test_phone):
        """Fill in contact info with existing contact"""
        self.driver.find_element(*self.create_appointment_locators.CONTACT_INFO_SECTION).click()
        self.driver.find_element(*self.create_appointment_locators.PHONE_INPUT).send_keys(test_phone)
        self.driver.find_element(*self.create_appointment_locators.NAME_INPUT).send_keys(test_name)
        time.sleep(1)
        self.select_random_gender()
        self.driver.find_element(*self.create_appointment_locators.SAVE_CONTACT_BUTTON).click()
        return self
      
    def check_member_passport(self):
        """Check member passport"""
        self.driver.find_element(*self.create_appointment_locators.MEMBER_PASSPORT_BTN).click()
        assert self.driver.find_element(*self.create_appointment_locators.MEMBER_PASSPORT_TITLE).is_displayed()
        self.driver.find_element(*self.create_appointment_locators.MEMBER_PASSPORT_BACK_BTN).click()
        return self
      
    def select_service2_person(self):
        """Select second service person"""
        time.sleep(0.5)
        self.driver.find_element(*self.create_appointment_locators.SERVICE2_PERSON).click()
        self.driver.find_element(*self.create_appointment_locators.SERVICE_PAGE_TOGGLE_SWITCH).click()
        self.driver.find_element(*self.create_appointment_locators.SERVICE_OTHER_PERSON).click()
        self.driver.find_element(*self.create_appointment_locators.SERVICE_PAGE_SAVE_BTN).click()
        return self

    def handle_sub_services(self):
        """
        Handle sub-services modal if it appears:
        1. Always select 2 options from predefined options
        2. Click selected options using description
        3. Click save button
        """
        
        try:
            # Randomly select two options
            selected_keys = random.sample(list(self.create_appointment_locators.SUB_SERVICE_OPTIONS.keys()), 2)
            
            # Click selected options
            for key in selected_keys:
                option_locator = self.create_appointment_locators.SUB_SERVICE_OPTIONS[key]
                try:
                    self.driver.find_element(*option_locator).click()
                except NoSuchElementException:
                    continue
            
            # Click save button for sub-service
            sub_save_button = self.driver.find_element(*self.create_appointment_locators.SUB_SERVICE_SAVE_BTN)
            sub_save_button.click()
            
        except Exception as e:
            return False

    def select_service(self):
        """
        1. Click service selection button
        2. Immediately swipe through tabs
        3. Find and click AUTO_TEST_TAB
        4. Select specific services
        5. Handle sub-services if modal appears
        """
        # Click service selection button and wait for page to load
        time.sleep(1)
        self.driver.find_element(*self.create_appointment_locators.SERVICE).click()

        try:
            tab_container = self.driver.find_element(*self.create_appointment_locators.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 5
            found_target = False

            for _ in range(max_attempts):
                self.driver.swipe(start_x, y, end_x, y, 100)
                time.sleep(0.5)
                try:
                    auto_test_tab = self.driver.find_element(*self.create_appointment_locators.AUTO_TEST_TAB)
                    if auto_test_tab.is_displayed():
                        auto_test_tab.click()
                        found_target = True
                        break
                except NoSuchElementException:
                    continue

            if not found_target:
                print("Could not find AUTO_TEST_TAB after maximum attempts")
                return self

        except Exception as e:
            print(f"Error swiping tabs: {str(e)}")
            return self

        # Select specific services under AUTO_TEST_TAB
        try:
            service1 = self.driver.find_element(*self.create_appointment_locators.SERVICE_OPTION1)
            service4 = self.driver.find_element(*self.create_appointment_locators.SERVICE_OPTION4)
            
            service4.click()
            time.sleep(1)
            self.handle_sub_services()
            
            time.sleep(1)
            service1.click()
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")

        return self
    
    def save_service1_button(self):
        save_button = self.driver.find_element(*self.create_appointment_locators.SAVE_SERVICE1_BTN)
        save_button.click()
        return self
    
    def save_service2_button(self):
        save_button = self.driver.find_element(*self.create_appointment_locators.SAVE_SERVICE2_BTN)
        save_button.click()
        return self
  
    def change_service_time_and_service_person(self):
        """Randomly change service time and quantity"""
        
        # Randomly click service time plus or minus button
        time_clicks = random.randint(1, 5)
        for _ in range(time_clicks):
            if random.choice([True, False]):
                self.driver.find_element(*self.create_appointment_locators.SERVICE_TIME_PLUS_BTN).click()
            else:
                self.driver.find_element(*self.create_appointment_locators.SERVICE_TIME_MINUS_BTN).click()
            time.sleep(0.5)

        # Randomly click quantity plus or minus buttonick quantity plus or minus button
        quantity_clicks = random.randint(1, 5)
        for _ in range(quantity_clicks):
            if random.choice([True, False]):
                self.driver.find_element(*self.create_appointment_locators.QUANTITY_PLUS_BTN).click()
            else:
                self.driver.find_element(*self.create_appointment_locators.QUANTITY_MINUS_BTN).click()
            time.sleep(0.5)

        return self
        
    def note_input(self):
        """Input random note with mixed characters"""
        time.sleep(1)
        self.driver.find_element(*self.create_appointment_locators.NOTE_INPUT).click()
        
        time.sleep(0.5)
        # randomly click quick select 2 options
        options = list(self.create_appointment_locators.QUICK_SELECT_NOTE_CONTENT.keys())
        for option in random.sample(options, 2):
            self.driver.find_element(*self.create_appointment_locators.QUICK_SELECT_NOTE_CONTENT[option]).click()
            time.sleep(0.5)
        
        characters = string.ascii_letters + string.digits + string.punctuation + "夯客測試開發"
        random_note = ''.join(random.choices(characters, k=10))
        note_input_field = self.driver.find_element(*self.create_appointment_locators.NOTE_CONTENT_INPUT)
        note_input_field.click()
        time.sleep(0.5)
        note_modal_input_field = self.driver.find_element(*self.create_appointment_locators.MODAL_NOTE_CONTENT_INPUT)
        note_modal_input_field.click()
        note_modal_input_field.send_keys(random_note)
        
        self.driver.find_element(*self.create_appointment_locators.MODAL_NOTE_SAVE_BTN).click()
        self.driver.find_element(*self.create_appointment_locators.NOTE_CONTENT_SAVE_BTN).click()
        
        return self
    
    
    def click_one_more_service(self):
        time.sleep(1)
        add_service_element = self.driver.find_element(*self.create_appointment_locators.ADD_ONE_MORE_SERVICE)
        if add_service_element.is_displayed():
                add_service_element.click()
        
    
    def one_more_service(self):
        self.select_service2_person()
        self.select_service()
        self.save_service2_button()
        return self

    def delete_service(self):
        self.driver.find_element(*self.create_appointment_locators.DELETE_SERVICE_BTN).click()
        return self
      

    def select_appointment_time(self):
        """
        1. Must scroll to very bottom of screen first
        2. Only after reaching bottom, find and click time picker
        3. Select random time slot
        """
        try:
            
            window_size = self.driver.get_window_size()
            
            
            right_edge_x = window_size['width'] * 0.95
            
    
            start_y = window_size['height'] * 0.95  
            mid_y = window_size['height'] * 0.65    
            end_y = window_size['height'] * 0.35   
            
            
        
            self.driver.swipe(
                right_edge_x,
                start_y,
                right_edge_x,
                mid_y,
                2000
            )
            
          
            self.driver.swipe(
                right_edge_x,
                mid_y,
                right_edge_x,
                end_y,
                2000
            )
            
         
            self.driver.swipe(
                right_edge_x,
                end_y * 1.2,
                right_edge_x,
                end_y,
                500
            )
            
          
            time_element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '預約時間')
            time_element.click()
            time.sleep(10)
            
            # Add WebDriverWait to wait for the modal to fully render
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located(self.create_appointment_locators.DATE_BLOCK)
                )
                logger.info("Appointment time modal fully rendered")
            except TimeoutException:
                logger.error("Timeout waiting for appointment time modal to render")
                # Take a screenshot if modal doesn't appear
                self.driver.save_screenshot('screenshots/modal_load_error.png')
                raise
            
            # click date block
            date_block = self.driver.find_element(*self.create_appointment_locators.DATE_BLOCK)  
            date_block.click()
            time.sleep(1)
            
            # select random date
            direction = random.choice(['left', 'right'])
            if direction == 'left':
                arrow = self.driver.find_element(*self.create_appointment_locators.LEFT_DATE_ARROW)
            else:
                arrow = self.driver.find_element(*self.create_appointment_locators.RIGHT_DATE_ARROW)
            arrow.click()
            
            dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      
            random.choice(dates).click()
            
            # Control page (left, right, today button)

            today_button = self.driver.find_element(*self.create_appointment_locators.TODAY_TIME_BUTTON)
            left_arrow = self.driver.find_element(*self.create_appointment_locators.LEFT_TIME_ARROW)
            right_arrow = self.driver.find_element(*self.create_appointment_locators.RIGHT_TIME_ARROW)

            buttons = [today_button, left_arrow, right_arrow]


            random_buttons = random.sample(buttons, 2)
            for button in random_buttons:
                button.click()
                time.sleep(0.5)
            
            
            
            time_slots = self.driver.find_elements(*self.create_appointment_locators.TIME_SLOTS)
            if time_slots:
                random_slot = random.choice(time_slots)
                random_slot.click()
                time.sleep(1)
                
                save_btn = self.driver.find_element(*self.create_appointment_locators.SAVE_TIME_BTN)
                save_btn.click()
                try:
                    self.driver.find_element(*self.create_appointment_locators.SELECT_BUSY_TIME).click()
                except:
                        print("Unable to select time slot")
            else:
                print("No available time slots found")
        except Exception as e:
            print(f"Error selecting appointment time: {str(e)}")
        
        return self

    
    def select_deposit_options(self):
        """
        Randomly toggle two specific deposit options and save.
        """
        time.sleep(2)
        deposit_btn = self.driver.find_element(*self.create_appointment_locators.DEPOSIT_BTN)
        deposit_btn.click()
        
        try:
  
            toggle1 = self.driver.find_element(*self.create_appointment_locators.DEPOSIT_TOGGLE_1)
            toggle2 = self.driver.find_element(*self.create_appointment_locators.DEPOSIT_TOGGLE_2)

            # randomly click two specific deposit options
            for toggle in [toggle1, toggle2]:
                if random.choice([True, False]):
                    toggle.click()
                    time.sleep(1)

            # Click save button
            save_button = self.driver.find_element(*self.create_appointment_locators.DEPOSIT_SAVE_BTN)
            if save_button.is_displayed():
                save_button.click()
            else:
                print("Save button is not visible or enabled")

        except Exception as e:
            print(f"Error selecting deposit options: {str(e)}")
    
    
    def click_create_button(self):
        time.sleep(0.5)
        self.driver.find_element(*self.create_appointment_locators.CONFIRM_CREATE_BUTTON).click()
        return self


    # Contact related methods
    def enter_phone_number(self, phone_number):
        phone_input = self.driver.find_element(*self.create_appointment_locators.PHONE_INPUT)
        phone_input.send_keys(phone_number)
        return self
    
    def enter_name(self, name):
        name_input = self.driver.find_element(*self.create_appointment_locators.NAME_INPUT)
        name_input.send_keys(name)
        return self
      
    def verify_invalid_phone_error_message(self):
        error_element = self.driver.find_element(*self.create_appointment_locators.INVALID_PHONE_MSG)
        assert error_element.text == " 格式錯誤。", "Invalid phone error message is not correct"
        return error_element.text
      
    
    def click_contact_back_btn_to_appointment(self):
        self.driver.find_element(*self.create_appointment_locators.CONTACT_BACK_BTN).click()
        return self


    def search_by_phone(self):
        self.driver.find_element(*self.create_appointment_locators.PHONE_SEARCH_BUTTON).click()
        return self

    def search_by_name(self):
        self.driver.find_element(*self.create_appointment_locators.NAME_SEARCH_BUTTON).click()
        return self

    def select_search_result_and_save(self):
        try:

            specific_result = self.driver.find_element(*self.create_appointment_locators.SPECIFIC_SEARCH_RESULT)
            
            if specific_result:
                specific_result.click()
                time.sleep(1)
                
                save_button = self.driver.find_element(*self.create_appointment_locators.SAVE_CONTACT_BUTTON)
                save_button.click()
            else:
                print("No specific search result found")
                
            
        except Exception as e:
            print(f"Error selecting specific search result: {str(e)}")
            
        return self
      
    def contact_has_chosen(self):
        assert self.driver.find_element(*self.create_appointment_locators.CONTACT_HAS_CHOSEN).is_displayed(), "Contact has not chosen"
        return self
      
    def change_contact_info(self):
        self.driver.find_element(*self.create_appointment_locators.CONTACT_HAS_CHOSEN).click()
        self.driver.find_element(*self.create_appointment_locators.CONTACT_PHONE_CHANGE).clear()
        self.enter_phone_number("911111116")
        self.search_by_phone()
        try:

            specific_result = self.driver.find_element(*self.create_appointment_locators.CHANGE_SPECIFIC_SEARCH_RESULT)
            
            if specific_result:
                specific_result.click()
                time.sleep(0.5)
                
                save_button = self.driver.find_element(*self.create_appointment_locators.SAVE_CONTACT_BUTTON)
                save_button.click()
            else:
                print("No specific search result found")
                
            
        except Exception as e:
            print(f"Error selecting specific search result: {str(e)}")
            
        return self
        

    def work_as_expected_then_back_to_calendar(self):
        time.sleep(2)
        self.driver.find_element(*self.create_appointment_locators.BACK_TO_CALENDAR_BTN).click()
        try:
            self.driver.find_element(*self.create_appointment_locators.SERVICE_CANCEL_BTN).click()
        except:
            pass
        return self

   
   