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
             self.driver.find_element(*self.member_locators.PASSPORT_RETURN_BUTTON).click()
            
          else:
             raise Exception("No member phone numbers found")
        
          return self
      
      def add_member(self):
          self.driver.find_element(*self.member_locators.ADD_MEMBER).click()
          time.sleep(0.5)
          self.new_member()
        
      def apply_member_filters(self):
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.APPLY_FILTERS).click()
        
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
                time.sleep(1)
                self.driver.find_element(*self.member_locators.MEMBER_FILTER_SECTIONS['save_button']).click()
              
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
            scroll_to_view = ('new UiScrollable(new UiSelector().scrollable(true)).setMaxSearchSwipes(15).scrollIntoView(new UiSelector().description("排除條件-multi-select-field"))')
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_to_view)
          
            assert self.driver.find_element(*self.member_locators.DELETE_CONDITION).is_displayed()
              
              
            # click filter button
            time.sleep(2)
            self.driver.find_element(*self.member_locators.FILTER_BUTTON).click()
          
    
            for _ in range(2):
                self.driver.back()
                time.sleep(0.5)
          
          
          except Exception as e:
            print(f"Error in apply_member_filters: {str(e)}")
            raise
       
                      
      def check_scheduling_records(self):
          self.driver.find_element(*self.member_locators.CHECK_SCHEDULING_RECORDS).click()
          try:
            sent_tag = self.driver.find_element(*self.member_locators.SENT_TAG)
            assert sent_tag.is_displayed()
          except Exception as e:
            print(f"Error in check_scheduling_records: {str(e)}")
            raise
          finally:
            self.driver.find_element(*self.member_locators.SCHEDULING_RECORDS_BACK).click()

    
      def verify_on_member_page(self):
          assert all ([
          self.driver.find_element(*self.member_locators.ADD_MEMBER).is_displayed(),
          self.driver.find_element(*self.member_locators.APPLY_FILTERS).is_displayed(),
          self.driver.find_element(*self.member_locators.CHECK_SCHEDULING_RECORDS).is_displayed(),
          self.driver.find_element(*self.member_locators.SEARCH_MEMBER).is_displayed()
          ]), "Not all required member page functions are displayed"
        
        
        
      def tap_search_button(self):
          self.driver.find_element(*self.member_locators.SEARCH_MEMBER).click()
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
          self.driver.find_element(*self.member_locators.MEMBER_TAGS).click()
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
          self.driver.find_element(*self.member_locators.CUSTOM_TAG_ADD_TAG).click()
          time.sleep(1)
        
          # add new tag
          tag_input = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
          random_tag = "自動化測試標籤" +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(5, 10)))
          time.sleep(0.5)
          tag_input.send_keys(random_tag)
        
          self.driver.find_element(*self.member_locators.CUSTOM_TAG_SAVE_NEW_TAG).click()
          time.sleep(0.5)
        
          # edit tag
          self.driver.find_element(*self.member_locators.CUSTOM_TAG_EDIT_TAG).click()
          tag_input = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
          tag_input.click()
          tag_input.clear()
          time.sleep(0.5)
        
          # verify error message
          error_msg = self.driver.find_element(*self.member_locators.CUSTOM_TAG_ERROR_MSG)
          assert error_msg.is_displayed(), "Error message not displayed"
        
          # reenter tag name
          tag_input.send_keys(random_tag)
          self.driver.find_element(*self.member_locators.CUSTOM_TAG_SAVE_NEW_TAG).click()
          time.sleep(0.5)
        
          # remove tag
          self.driver.find_element(*self.member_locators.CUSTOM_TAG_DELETE_TAG).click()
          self.driver.find_element(*self.member_locators.CUSTOM_TAG_CONFIRM_DELETE).click()
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
          self.driver.find_element(*self.member_locators.TOP_UP_SECTION).click()
          time.sleep(0.5)
        
          return self
    
      def edit_top_up_amount(self):
          
          self.driver.find_element(*self.member_locators.EDIT_TOP_UP_ICON).click()
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.INPUT_TOP_UP_AMOUNT).click()
          amount = random.randint(1, 1000)
          self.driver.find_element(*self.member_locators.INPUT_TOP_UP_AMOUNT).send_keys(amount)
        
          if random.choice([True, False]):
             self.driver.find_element(*self.member_locators.INCREASE_BUTTON).click()
          else:
             self.driver.find_element(*self.member_locators.DECREASE_BUTTON).click()
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.BALANCE_CONFIRM_BUTTON).click()
        
          return self
    
      def click_top_up_button(self):
          self.driver.find_element(*self.member_locators.TOP_UP_BUTTON).click()
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
          time.sleep(0.5)
          self.driver.back()
        
          return self
      
      def click_bonus_points_section(self):
          self.driver.find_element(*self.member_locators.BONUS_POINTS_SECTION).click()
          time.sleep(0.5)
        
          return self
    
      def edit_bonus_points(self):
          time.sleep(1)
          self.edit_top_up_amount()
          time.sleep(0.5) 
        
          return self
    
      def click_tickets_section(self):
          self.driver.find_element(*self.member_locators.TICKETS_SECTION).click()
          time.sleep(0.5)
        
          return self
    
      def click_sell_ticket_button(self):
          self.driver.find_element(*self.member_locators.SELL_TICKET_BUTTON).click()
          time.sleep(0.5)
        
          return self
      
      def select_performance_personnel(self):
          self.create_checkout_page.select_sales_owner()
        
      def choose_ticket_type(self):
          self.create_checkout_page.select_ticket()
    
      def finish_checkout_process(self):
          self.create_checkout_page.select_payment_method()
          self.create_checkout_page.proceed_to_checkout()
          self.create_checkout_page.confirm_checkout()
        
          return self
    
      def tap_ticket(self):
          self.driver.find_element(*self.member_locators.TICKET).click()
          time.sleep(0.5)
        
          return self
    
      def use_ticket(self):
          self.driver.find_element(*self.member_locators.USE_BUTTON).click()
          time.sleep(0.5)
        
          if random.choice([True, False]):
             plus_button = self.driver.find_element(*self.member_locators.PLUS_BUTTON)
             clicks = random.randint(3,6)
             for _ in range(clicks):
                plus_button.click()
        
          else:
            input_field = self.driver.find_element(*self.member_locators.INPUT_FIELD)
            random_number = str(random.randint(10, 100))
            input_field.clear()
            input_field.send_keys(random_number)
        
          time.sleep(1)
          self.driver.find_element(*self.member_locators.CONFIRM_BUTTON).click()
        
          # click confirm again
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.CONFIRM_BUTTON).click()
          return self
    
      def switch_to_history_tab(self):
          self.driver.find_element(*self.member_locators.HISTORY_TAB).click()
          time.sleep(0.5)
        
          return self
      
      def click_gift_ticket_button(self):
          self.driver.find_element(*self.member_locators.GIFT_TICKET_BUTTON).click()
          time.sleep(0.5)
        
          return self
    
      def select_tickets_for_sending(self):
          self.create_checkout_page.select_ticket()
          time.sleep(0.5)
        
          # click confirm btn
          time.sleep(1)
          self.driver.find_element(*self.member_locators.CONFIRM_BUTTON).click()
         
          return self
      
      def ticket_page_return_to_member_passport(self):
          self.driver.find_element(*self.member_locators.TICKET_PAGE_RETURN_BUTTON).click()
          time.sleep(0.5)
          return self
      
      def edit_basic_info(self):
          time.sleep(1)
          self.driver.find_element(*self.member_locators.EDIT_INFO_ICON).click()
          time.sleep(0.5)
        
          # edit name
          name_input = self.driver.find_element(*self.member_locators.OTHER_NAME_INPUT)
          name_input.clear()
          random_nickname = "自動化測試" + ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(3, 10)))
          name_input.send_keys(random_nickname)
        
          self.select_random_gender()
          
          # click birthday field to open date picker
          self.driver.find_element(*self.member_locators.EDIT_BASIC_INFO_CHOOSE_DATE_FIELD).click()
          time.sleep(0.5)
          self.swipe_calendar_component()
        
          # click save
          self.driver.find_element(*self.member_locators.EDIT_SAVE).click()
          self.driver.find_element(*self.member_locators.CONFIRM_BUTTON).click()
        
          return self
    
      def edit_custom_fields(self):
          time.sleep(1)
          self.driver.find_element(*self.member_locators.EDIT_CUSTOM_INFO_ICON).click()
          time.sleep(0.5)
        
          selected_choice = random.choice(self.member_locators.SINGLE_CHOICE)
          self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_choice}').click()
        
          num_selections = random.randint(1, 2)
          selected_music = random.sample(self.member_locators.MUSIC_CHOICE, num_selections)
          for music in selected_music:
              self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, music).click()
            
          option_input = self.driver.find_element(*self.member_locators.OPTION_INPUT)
          option_input.click()
        
        
          random_option = "自動化測試" + ''.join(random.choice(
            string.ascii_letters + string.digits + "!@#$%^&*" + "測試回饋意見"
          ) for _ in range(random.randint(3, 10)))
          option_modal = self.driver.find_element(*self.member_locators.INPUT)
          option_modal.clear()
          option_modal.send_keys(random_option)
        
          # click save
          self.driver.find_element(*self.member_locators.MODAL_SAVE_BUTTON).click()
        
        
        
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
          fourth_question = self.driver.find_element(*self.member_locators.FOURTH_QUESTION_INPUT)
          fourth_question.click()
        
        
          random_answer = "自動化測試" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 8)))
          fourth_question_modal = self.driver.find_element(*self.member_locators.INPUT)
          fourth_question_modal.clear()
          fourth_question_modal.click()
          fourth_question_modal.send_keys(random_answer)
          time.sleep(1)
        
          self.driver.find_element(*self.member_locators.MODAL_SAVE_BUTTON).click()
        
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.CUSTOM_MODAL_SAVE_BUTTON).click()
        
          return self
    
      def edit_member_description(self):
          # scroll to bottom
          time.sleep(1)
          for _ in range(3):
              self.driver.execute_script('mobile: scrollGesture', {
                'left': 100,
                'top': 100,
                'width': 200,
                'height': 800,
                'direction': 'down',
                'percent': 0.9
              })
          time.sleep(1)
        
          self.driver.find_element(*self.member_locators.EDIT_MEMBER_DESCRIPTION_ICON).click()
          time.sleep(0.5)
        
          # edit member description
          member_description = self.driver.find_element(*self.member_locators.MEMBER_DESCRIPTION_INPUT)
          member_description.click()
        
          member_modal = self.driver.find_element(*self.member_locators.INPUT)
          member_modal.clear()
          member_modal.click()
        
          random_description = "自動化測試" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 8)))
          member_modal.send_keys(random_description)
          self.driver.find_element(*self.member_locators.MODAL_SAVE_BUTTON).click()
        
          # click save
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON).click()
        
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
          time.sleep(0.5)
          self.driver.find_element(*self.member_locators.BOTTOM_NAVIGATION['member_review_icon']).click()
        
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
          self.driver.find_element(*self.member_locators.LINK_ACCOUNT).click()
        
          self.driver.find_element(*self.member_locators.LINE_SECTION).click()
        
          self.driver.find_element(*self.member_locators.SEND_LINE_MESSAGE_BTN).click()
        
          self.driver.find_element(*self.member_locators.INPUT_MESSAGE_CONTENT).click()
          time.sleep(0.5)
        
        
          random_msg = "自動化測試" + ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(random.randint(5, 10)))
          self.driver.find_element(*self.member_locators.INPUT_MODAL).clear()
          self.driver.find_element(*self.member_locators.INPUT_MODAL).send_keys(random_msg)
        
          self.driver.find_element(*self.member_locators.MODAL_SAVE_BUTTON).click()
        
          #use message template after entering message content
          self.driver.find_element(*self.member_locators.USE_MESSAGE_TEMPLATE).click()
        
          # randomly select a message template
          selected_option = random.choice(self.member_locators.MESSAGE_TEMPLATE_OPTIONS)
          self.driver.find_element(*selected_option).click()
          time.sleep(0.5)
        
          # manage message template
          self.driver.find_element(*self.member_locators.MANAGE_MESSAGE_TEMPLATE).click()
          time.sleep(0.5)
        
        
          # add new message template
          self.driver.find_element(*self.member_locators.ADD_NEW_MESSAGE_TEMPLATE_BUTTON).click()
          time.sleep(0.5)
        
          title_input = self.driver.find_element(*self.member_locators.TITLE_INPUT)
          title_input.click()
          title_input.send_keys(random_msg)
          time.sleep(0.5)
        
          content_input = self.driver.find_element(*self.member_locators.CONTENT_INPUT)
          content_input.click()
          content_input_modal = self.driver.find_element(*self.member_locators.INPUT_MODAL)
          content_input_modal.clear()
          content_input_modal.click()
          content_input_modal.send_keys(random_msg)
          time.sleep(0.5)
        
          self.driver.find_element(*self.member_locators.MODAL_SAVE_BUTTON).click()
        
          self.driver.find_element(*self.member_locators.SAVE_BUTTON).click()
          time.sleep(0.5)

          # remove tag
          self.driver.find_element(*self.member_locators.DELETE_TAG).click()
          self.driver.find_element(*self.member_locators.CONFIRM_DELETE).click()
          time.sleep(0.5)
        
          # back to message template page
          self.driver.back()
          time.sleep(0.5)
        
        
          self.driver.find_element(*self.member_locators.MESSAGE_SAVE_BUTTON).click()
          time.sleep(1)
        
          # click to save again
          self.driver.find_element(*self.member_locators.MESSAGE_SAVE_BUTTON).click()
          self.driver.find_element(*self.member_locators.CONFIRM).click()
        
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
              item = self.driver.find_elements(*self.member_locators.SELECT_ITEM_BUTTON)
              if item:
                  item[0].click()
                  self.create_checkout_page.select_item()
                  time.sleep(0.5)
                  return True
              
              # ticket
              ticket = self.driver.find_elements(*self.member_locators.SELECT_TICKET_BUTTON)
              if ticket:
                  ticket[0].click()
                  self.create_checkout_page.select_ticket()
                  time.sleep(0.5)
                  return True
            
              # deposit
              deposit = self.driver.find_elements(*self.member_locators.DEPOSIT_TITLE)
              if deposit:
                  self.create_checkout_page.enter_deposit_amount()
                  time.sleep(0.5)
                  return True


          except Exception as e:
              print(f"Failed to choose the item I have bought before: {e}")
              return False

        
      def add_member_to_blacklist(self):
          self.driver.find_element(*self.member_locators.BOTTOM_NAVIGATION['more_icon']).click()
          self.driver.find_element(*self.member_locators.ADD_TO_BLACKLIST).click()
          self.driver.find_element(*self.member_locators.CONFIRM).click()
          time.sleep(0.5)
        
          return self
    
      def remove_member_from_blacklist(self):
          self.driver.find_element(*self.member_locators.REMOVE_FROM_BLACKLIST).click()
          self.driver.find_element(*self.member_locators.CONFIRM).click()
          time.sleep(0.5)
        
          return self