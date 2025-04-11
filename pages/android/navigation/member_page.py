import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains

from pages.android.create.create_checkout_page import CreateCheckoutPage
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.member_locators import Member_Locators

class MemberPage(CommonUseSection):
      def __init__(self, driver):
          self.driver = driver
          self.create_checkout_page = CreateCheckoutPage(driver)
          self.member_locators = Member_Locators()
    
    
      def click_member_option(self):
          try:
             member_option = self.driver.find_element(*self.member_locators.MEMBER_OPTION)
             if member_option.is_displayed() and member_option.is_enabled():
                member_option.click()
                time.sleep(1)
                return self
             else:
                raise Exception("Member option not found or not enabled")
          except Exception as e:
             raise Exception(f"Error clicking member option: {e}")

      def click_member_item(self):
          tab = random.choice(list(self.member_locators.MEMBER_TABS.values()))
          self.driver.find_element(*tab).click()
          time.sleep(1)
        
          phone_elements = self.driver.find_elements(*self.member_locators.MEMBER_PHONE_NUMBERS)
          if phone_elements:
             random.choice(phone_elements).click()
             time.sleep(1)
             self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['passport_return_button']).click()
            
          else:
             raise Exception("No member phone numbers found")
        
          return self
      
      def add_member(self):
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['add_member']).click()
          time.sleep(0.5)
          self.new_member()
        
      def apply_member_filters(self):
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['apply_filters']).click()
          time.sleep(0.5)
        
          try:
          
            # get all filter sections except last one
            filter_sections = list(self.member_locators.MEMBER_FILTER_SECTIONS.items())[:-1]
          
            # handle each section
            for section_name, section_locator in filter_sections:
                self.driver.find_element(*section_locator).click()
                time.sleep(0.5)
              
                # member tags, birthday month, sign, age
                if section_name in self.member_locators.MEMBER_FILTER_OPTIONS:
                   options = self.member_locators.MEMBER_FILTER_OPTIONS[section_name]
                   num_selections = random.randint(1, min(3, len(options)))
                   selected_options = random.sample(options, num_selections)
                 
                   for option in selected_options:
                       self.driver.find_element(*option).click()
                       time.sleep(0.5)
              
                # click save button
                self.driver.find_element(*self.member_locators.MEMBER_FILTER_SECTIONS['save_button']).click()
                time.sleep(0.5)
              
            # handle cost amount menu
            self.driver.find_element(*self.member_locators.COST_AMOUNT_MENU).click()
            time.sleep(0.5)
          
            amount_options = random.choice(self.member_locators.MEMBER_FILTER_OPTIONS['amount'])
            self.driver.find_element(*amount_options).click()
            time.sleep(0.5)
          
            # handle come amount menu
            self.driver.find_element(*self.member_locators.COME_AMOUNT_MENU).click()
            time.sleep(0.5)
          
            come_amount_options = random.choice(self.member_locators.MEMBER_FILTER_OPTIONS['amount'])
            self.driver.find_element(*come_amount_options).click()
            time.sleep(2)
    
            # randomly select one pair
            selected_pair = random.choice(self.member_locators.INPUT_PAIRS)

            # handle selected input pair
            min_field, max_field = selected_pair
            min_value = random.randint(1, 1000)
            max_value = random.randint(min_value + 10, min_value + 100)

            # input min value
            time.sleep(1)
            min_input = self.driver.find_element(*self.member_locators.INPUT_AMOUNT[min_field])
            min_input.click()
            min_input.send_keys(str(min_value))
            time.sleep(0.5)

            # input max value
            time.sleep(1)
            max_input = self.driver.find_element(*self.member_locators.INPUT_AMOUNT[max_field])
            max_input.click()
            max_input.send_keys(str(max_value))
            time.sleep(0.5)
          
          
                  
            # Scroll to find delete condition section   
            scroll_to_view = ('new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1)')
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_to_view)
          
            assert self.driver.find_element(*self.member_locators.DELETE_CONDITION).is_displayed()
              
              
            # click filter button
            self.driver.find_element(*self.member_locators.FILTER_BUTTON).click()
            time.sleep(0.5)
          
            # click back to button
            self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['member_filer_back']).click()
          
            self.driver.back()
          
          
          except Exception as e:
            print(f"Error in apply_member_filters: {str(e)}")
            raise
       
                      
      def check_scheduling_records(self):
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['check_scheduling_records']).click()
          time.sleep(1)
          sent_tag = self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['sent_tag'])
          assert sent_tag.is_displayed()
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['scheduling_records_back']).click()
    
      def verify_on_member_page(self):
          assert all ([
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['add_member']).is_displayed(),
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['apply_filters']).is_displayed(),
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['check_scheduling_records']).is_displayed(),
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['search_member']).is_displayed()
          ]), "Not all required member page functions are displayed"
        
        
        
      def tap_search_button(self):
          self.driver.find_element(*self.member_locators.MEMBER_PAGE_FUNCTIONS['search_member']).click()
          time.sleep(0.5)
        
      def search_phone_number(self, phone_number):
          self.driver.find_element(*self.member_locators.SEARCH_ELEMENTS['input']).send_keys(phone_number)
          time.sleep(0.5)
          self.driver.press_keycode(66)
          time.sleep(0.5)
        
      def tap_search_result(self):
          self.driver.find_element(*self.member_locators.SEARCH_ELEMENTS['result']).click()
          time.sleep(0.5)
        
      def select_member_tags(self):
          self.click_more_icon()
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['member_tags']).click()
          time.sleep(0.5)
        
          return self

      def modify_tag_setting(self):
          # system tag section
          for section_name, section_locator in self.member_locators.SYSTEM_TAGS_SECTION.items():
              self.driver.find_element(*section_locator).click()
              time.sleep(0.5)
            
              if section_name in self.member_locators.SYSTEM_TAGS_OPTIONS:
                 options = self.member_locators.SYSTEM_TAGS_OPTIONS[section_name]
                 selected_option = random.choice(options)
                 self.driver.find_element(*selected_option).click()
                 time.sleep(0.5)
         
          # customize tag section
          selected_tag = random.choice(self.member_locators.CUSTOMIZE_TAGS)
          self.driver.find_element(*selected_tag).click()
          time.sleep(0.5)
            
          return self
    
      def click_custom_tag_settings(self):
          self.driver.find_element(*self.member_locators.MANAGE_CUSTOM_TAG).click()
          time.sleep(0.5)
        
      def modify_custom_tag(self):
          self.driver.find_element(*self.member_locators.CUSTOM_TAGS_FUNCTIONS['add_tag']).click()
          time.sleep(1)
        
          # add new tag
          tag_input = self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')
          random_tag = "自動化測試標籤" +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(5, 10)))
          time.sleep(0.5)
          tag_input.send_keys(random_tag)
        
          self.driver.find_element(*self.member_locators.CUSTOM_TAGS_FUNCTIONS['save_new_tag']).click()
          time.sleep(0.5)
        
          # edit tag
          self.driver.find_element(*self.member_locators.CUSTOM_TAGS_FUNCTIONS['edit_tag']).click()
          tag_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
          tag_input.click()
          tag_input.clear()
          time.sleep(0.5)
        
          # verify error message
          error_msg = self.driver.find_element(*self.member_locators.CUSTOM_TAGS_FUNCTIONS['error_msg'])
          assert error_msg.is_displayed(), "Error message not displayed"
        
          # reenter tag name
          tag_input.send_keys(random_tag)
          self.driver.find_element(*self.member_locators.CUSTOM_TAGS_FUNCTIONS['save_new_tag']).click()
          time.sleep(0.5)
        
          # remove tag
          self.driver.find_element(*self.member_locators.CUSTOM_TAGS_FUNCTIONS['delete_tag']).click()
          self.driver.find_element(*self.member_locators.CUSTOM_TAGS_FUNCTIONS['confirm_delete']).click()
          time.sleep(0.5)
          self.driver.back()
        
          # confirm member tag
          self.driver.find_element(*self.member_locators.SELECT_MEMBER_CONFIRM).click()
        
          # click outside the window to close the dialog
          self.driver.find_element(*self.member_locators.MEMBER_PASSPORT_TITLE).click()
        
          return self
      
      def tap_billing_tab(self):
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.PASSPORT_TABS['billing_tab']).click()
    
          return self
    
      def tap_view_details(self):
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['view_details']).click()
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['expand_details']).click()
          time.sleep(1.5)
        
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['export_details']).click()
          time.sleep(0.5)
          for _ in range(3):
              self.driver.back()
              time.sleep(0.5)
        
          return self
    
      def tap_view_checkout(self):
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['view_checkout']).click()
          time.sleep(0.5)
        
          return self
    
      def delete_and_reprocess_checkout(self):
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['delete_checkout']).click()
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['delete_checkout_again_option']).click()
    
      def delete_checkout(self):
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['delete_checkout']).click()
          time.sleep(1)
        
          self.driver.find_element(*self.member_locators.BILLING_FUNCTIONS['delete_checkout_option']).click()
          return self
    
      def verify_on_member_passport_page(self):
          self.driver.find_element(*self.member_locators.PASSPORT_TABS['info_tab']).click()
        
      def click_top_up_section(self):
          self.driver.find_element(*self.member_locators.TOP_UP_SECTION['top_up_section']).click()
          time.sleep(0.5)
        
          return self
    
      def edit_top_up_amount(self):
          
          self.driver.find_element(*self.member_locators.TOP_UP_SECTION['edit_top_up_icon']).click()
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.TOP_UP_SECTION['input_top_up_amount']).click()
          amount = random.randint(1, 1000)
          self.driver.find_element(*self.member_locators.TOP_UP_SECTION['input_top_up_amount']).send_keys(amount)
        
          if random.choice([True, False]):
             self.driver.find_element(*self.member_locators.TOP_UP_SECTION['increase_button']).click()
          else:
             self.driver.find_element(*self.member_locators.TOP_UP_SECTION['decrease_button']).click()
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.TOP_UP_SECTION['confirm_button']).click()
        
          return self
    
      def click_top_up_button(self):
          self.driver.find_element(*self.member_locators.TOP_UP_SECTION['top_up_button']).click()
          time.sleep(0.5)
        
          return self
    
      def finish_top_up_process(self):
          self.create_checkout_page.select_sales_owner()
          self.create_checkout_page.enter_deposit_amount()
          self.create_checkout_page.select_payment_method()
          self.create_checkout_page.proceed_to_checkout()
          self.create_checkout_page.confirm_checkout()
          time.sleep(1)
        
          return self
      
      def return_to_member_passport(self):
          self.driver.back()
          time.sleep(0.5)
        
          return self
      
      def click_bonus_points_section(self):
          self.driver.find_element(*self.member_locators.BONUS_POINTS_SECTION['bonus_points_section']).click()
          time.sleep(0.5)
        
          return self
    
      def edit_bonus_points(self):
          time.sleep(1)
          self.edit_top_up_amount()
          time.sleep(0.5) 
        
          return self
    
      def click_tickets_section(self):
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['tickets_section']).click()
          time.sleep(0.5)
        
          return self
    
      def click_sell_ticket_button(self):
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['sell_ticket_button']).click()
          time.sleep(0.5)
        
          return self
      
      def select_performance_personnel(self):
          self.create_checkout_page.select_sales_owner()
        
      def choose_ticket_type(self):
          self.create_checkout_page.select_ticket()
    
      def finish_checkout_process(self):
          #todo: 舊版有bug點擊選擇支付方式無反應
          self.create_checkout_page.select_payment_method()
          self.create_checkout_page.proceed_to_checkout()
          self.create_checkout_page.confirm_checkout()
        
          return self
    
      def tap_ticket(self):
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['ticket']).click()
          time.sleep(0.5)
        
          return self
    
      def use_ticket(self):
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['use_button']).click()
          time.sleep(0.5)
        
          if random.choice([True, False]):
             plus_button = self.driver.find_element(*self.member_locators.TICKETS_SECTION['plus_button'])
             clicks = random.randint(3,6)
             for _ in range(clicks):
                plus_button.click()
        
          else:
            input_field = self.driver.find_element(*self.member_locators.TICKETS_SECTION['input_field'])
            random_number = str(random.randint(10, 100))
            input_field.clear()
            input_field.send_keys(random_number)
        
          time.sleep(1)
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['save_button']).click()
        
          # click confirm again
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['save_button']).click()
          return self
    
      def switch_to_history_tab(self):
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['history_tab']).click()
          time.sleep(0.5)
        
          return self
      
      def click_gift_ticket_button(self):
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['gift_ticket_button']).click()
          time.sleep(0.5)
        
          return self
    
      def select_tickets_for_sending(self):
          self.create_checkout_page.select_ticket()
          time.sleep(0.5)
        
          # click confirm btn
          self.driver.find_element(*self.member_locators.TICKETS_SECTION['save_button']).click()
          time.sleep(1)
          return self
      
      def edit_basic_info(self):
          time.sleep(1)
          self.driver.find_element(*self.member_locators.EDIT_SECTION['edit_info_icon']).click()
          time.sleep(0.5)
        
          # edit name
          name_input = self.driver.find_element(*self.member_locators.EDIT_SECTION['input'])
          name_input.clear()
          random_nickname = "自動化測試" + ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(3, 10)))
          name_input.send_keys(random_nickname)
        
          self.select_random_gender()
          self.select_random_date()
        
          # click save
          self.driver.find_element(*self.member_locators.EDIT_SECTION['edit_save']).click()
          self.driver.find_element(*self.member_locators.EDIT_SECTION['confirm_button']).click()
        
          return self
    
      def edit_custom_fields(self):
          time.sleep(1)
          self.driver.find_element(*self.member_locators.EDIT_SECTION['edit_custom_info_icon']).click()
          time.sleep(0.5)
        
          selected_choice = random.choice(self.member_locators.SINGLE_CHOICE)
          self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_choice}').click()
        
          num_selections = random.randint(1, 2)
          selected_music = random.sample(self.member_locators.MUSIC_CHOICE, num_selections)
          for music in selected_music:
              self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, music).click()
            
          option_input = self.driver.find_element(*self.member_locators.EDIT_SECTION['option_input'])
          option_input.click()
        
        
          random_option = "自動化測試" + ''.join(random.choice(
            string.ascii_letters + string.digits + "!@#$%^&*" + "測試回饋意見"
          ) for _ in range(random.randint(3, 10)))
          option_modal = self.driver.find_element(*self.member_locators.EDIT_SECTION['input'])
          option_modal.clear()
          option_modal.click()
          option_modal.send_keys(random_option)
        
          # click save
          self.driver.find_element(*self.member_locators.EDIT_SECTION['modal_save_button']).click()
        
        
        
          # scroll to bottom
          for _ in range(2):
              self.driver.execute_script('mobile: scrollGesture', {
                'left': 100,
                'top': 100,
                'width': 200,
                'height': 800,
                'direction': 'down',
                'percent': 0.9
              })
          time.sleep(1)
        
          # fourth question
          fourth_question = self.driver.find_element(*self.member_locators.EDIT_SECTION['fourth_question_input'])
          fourth_question.click()
        
        
          random_answer = "自動化測試" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 8)))
          fourth_question_modal = self.driver.find_element(*self.member_locators.EDIT_SECTION['input'])
          fourth_question_modal.clear()
          fourth_question_modal.click()
          fourth_question_modal.send_keys(random_answer)
          time.sleep(1)
        
          self.driver.find_element(*self.member_locators.EDIT_SECTION['modal_save_button']).click()
        
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.EDIT_SECTION['modal_save_button']).click()
        
          return self
    
      def edit_member_description(self):
          # scroll to bottom
          time.sleep(1)
          for _ in range(1):
              self.driver.execute_script('mobile: scrollGesture', {
                'left': 100,
                'top': 100,
                'width': 200,
                'height': 800,
                'direction': 'down',
                'percent': 0.9
              })
          time.sleep(1)
        
          self.driver.find_element(*self.member_locators.EDIT_SECTION['edit_member_description_icon']).click()
          time.sleep(0.5)
        
          # edit member description
          member_description = self.driver.find_element(*self.member_locators.EDIT_SECTION['member_description_input'])
          member_description.click()
        
          member_modal = self.driver.find_element(*self.member_locators.EDIT_SECTION['input'])
          member_modal.clear()
          member_modal.click()
        
          random_description = "自動化測試" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 8)))
          member_modal.send_keys(random_description)
          self.driver.find_element(*self.member_locators.EDIT_SECTION['modal_save_button']).click()
        
          # click save
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.EDIT_SECTION['modal_save_button']).click()
        
          return self
    
      def click_message_icon(self):
          self.driver.find_element(*self.member_locators.BOTTOM_NAVIGATION['send_message_icon']).click()
          time.sleep(0.5)
        
          return self
    
      def enter_send_message_page(self):
          self.driver.find_element(*self.member_locators.SEND_MESSAGE_FUNCTIONS['send_message_button']).click()
          time.sleep(0.5)
        
          # back to member passport page
          self.driver.back()
          time.sleep(0.5)
        
          self.driver.back()
        
          return self
    
    
      def click_sign_document_icon(self):
          self.driver.find_element(*self.member_locators.BOTTOM_NAVIGATION['sign_document_icon']).click()
          time.sleep(0.5)
        
          return self
    
      def sign_review_document(self):
          self.driver.find_element(*self.member_locators.SIGN_DOCUMENT_FUNCTIONS['signed_document']).click()
          time.sleep(1)
        
          return self
    
      def click_review_member_icon(self):
          self.driver.find_element(*self.member_locators.BOTTOM_NAVIGATION['member_review_icon']).click()
          time.sleep(0.5)
        
          return self
    
      def view_member_review(self):
          assert all([
            self.driver.find_element(*self.member_locators.MEMBER_REVIEW_FUNCTIONS['review_element']).is_displayed(),
            self.driver.find_element(*self.member_locators.MEMBER_REVIEW_FUNCTIONS['review_content']).is_displayed()
          ])
        
          # back to member passport page
          self.driver.back()
          time.sleep(0.5)

          return self
    
      def click_more_icon(self):
          self.driver.find_element(*self.member_locators.BOTTOM_NAVIGATION['more_icon']).click()
          time.sleep(0.5)
        
          return self
    
      def link_account_and_send_line_message(self):
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['link_account']).click()
        
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['line_section']).click()
        
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['send_line_message_btn']).click()
        
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['input_message_content']).click()
          time.sleep(0.5)
        
        
          random_msg = "自動化測試" + ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(random.randint(5, 10)))
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['input_modal']).clear()
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['input_modal']).send_keys(random_msg)
        
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['modal_save_button']).click()
        
          #use message template after entering message content
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['use_message_template']).click()
        
          # randomly select a message template
          selected_option = random.choice(self.member_locators.MESSAGE_TEMPLATE_OPTIONS)
          self.driver.find_element(*selected_option).click()
          time.sleep(0.5)
        
          # manage message template
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['manage_message_template']).click()
          time.sleep(0.5)
        
        
          # add new message template
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['add_new_message_template_button']).click()
          time.sleep(0.5)
        
          title_input = self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['title_input'])
          title_input.click()
          title_input.send_keys(random_msg)
          time.sleep(0.5)
        
          content_input = self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['content_input'])
          content_input.click()
          content_input_modal = self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['input_modal'])
          content_input_modal.clear()
          content_input_modal.click()
          content_input_modal.send_keys(random_msg)
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['modal_save_button']).click()
        
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['save_button']).click()
          time.sleep(0.5)

          # remove tag
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['delete_tag']).click()
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['confirm_delete']).click()
          time.sleep(0.5)
        
          # back to message template page
          self.driver.back()
          time.sleep(0.5)
        
        
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['message_save_button']).click()
          time.sleep(1)
        
          # click to save again
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['message_save_button']).click()
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['confirm']).click()
        
          return self
        
        
      def click_back_to_member_passport_page(self):
          self.driver.back()
          time.sleep(0.5)
        
          self.return_to_member_passport()
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.MEMBER_PASSPORT_TITLE).click()
        
        
      def return_to_calendar_page(self):
          self.driver.find_element(*self.member_locators.MEMBER_PASSPORT_TITLE).click()
          time.sleep(1) 
          for _ in range(3):
              self.driver.back()
              time.sleep(0.5)
        
      def can_choose_the_item_i_have_bought_before(self):
          try:
              # item
              item = self.driver.find_elements(*self.member_locators.MORE_OPTIONS_FUNCTIONS['selct_item_button'])
              if item:
                  item[0].click()
                  self.create_checkout_page.select_item()
                  time.sleep(0.5)
                  return True
              
              # ticket
              ticket = self.driver.find_elements(*self.member_locators.MORE_OPTIONS_FUNCTIONS['select_ticket_button'])
              if ticket:
                  ticket[0].click()
                  self.create_checkout_page.select_ticket()
                  time.sleep(0.5)
                  return True
            
              # deposit
              deposit = self.driver.find_elements(*self.member_locators.MORE_OPTIONS_FUNCTIONS['deposit_title'])
              if deposit:
                  self.create_checkout_page.enter_deposit_amount()
                  time.sleep(0.5)
                  return True


          except Exception as e:
              print(f"Failed to choose the item I have bought before: {e}")
              return False

        
      def add_member_to_blacklist(self):
          self.driver.find_element(*self.member_locators.BOTTOM_NAVIGATION['more_icon']).click()
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['add_to_blacklist']).click()
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['confirm']).click()
          time.sleep(0.5)
        
          return self
    
      def remove_member_from_blacklist(self):
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['remove_from_blacklist']).click()
          self.driver.find_element(*self.member_locators.MORE_OPTIONS_FUNCTIONS['confirm']).click()
          time.sleep(0.5)
        
          return self