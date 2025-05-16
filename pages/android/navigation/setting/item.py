from pages.locators.android.navigation.setting.item_locators import ItemPageLocators
from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection

# noinspection DuplicatedCode
class ItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.common_use = CommonUseSection(driver)
        self.item_locators = ItemPageLocators()

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_BRANCH_SETTINGS_PAGE)
        return self

    def tap_on_item(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.ITEM_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_ITEM_SETTINGS_PAGE)
        return self

    def verify_item_page(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.INVENTORY_IN_ITEM_SETTINGS_PAGE)
        return self

    def tap_on_item_in_item_page(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.ITEM_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        return self

    def delete_item_category(self, category_name=None, delete_all=False):
        self.common_actions.wait_for_element_visible(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        if self.common_actions.is_element_present(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE):
            self.common_actions.click_element(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE)
            self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
            if delete_all:
                while self.common_actions.is_element_present(*self.item_locators.CATEGORY_MODAL_DELETE_ALL_CATEGORY_BUTTON):
                    self.common_actions.wait_for_element_clickable(*self.item_locators.CATEGORY_MODAL_DELETE_ALL_CATEGORY_BUTTON)
                    self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_DELETE_ALL_CATEGORY_BUTTON)
                    self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_DELETE_BUTTON)
                    self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_DELETE_BUTTON)
                    self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_DELETE_BUTTON)
            else:
                self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_DELETE_CATEGORY_BUTTON(category_name))
                self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_DELETE_CATEGORY_BUTTON(category_name))
                self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_DELETE_BUTTON)
                self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_DELETE_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_DELETE_BUTTON)
            self.common_actions.wait_for_element_clickable(*self.item_locators.CATEGORY_MODAL_CLOSE_BUTTON)
            self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_CLOSE_BUTTON)
        return self

    def add_item_category(self, category_name):
        self.common_actions.wait_for_element_visible(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        if self.common_actions.is_element_present(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE):
            self.common_actions.click_element(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE)
        else:
            self.common_actions.click_element(*self.item_locators.ADD_FIRST_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
        self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_FIELD, category_name)
        self.common_actions.wait_for_element_clickable(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_DELETE_CATEGORY_BUTTON(category_name))
        self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
        self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(category_name))
        return self

    def edit_item_category(self, old_category_name, new_category_name):
        self.common_actions.wait_for_element_visible(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_EDIT_CATEGORY_BUTTON(old_category_name))
        self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_EDIT_CATEGORY_BUTTON(old_category_name))
        self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_FIELD, new_category_name)
        self.common_actions.wait_for_element_clickable(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_DELETE_CATEGORY_BUTTON(new_category_name))
        self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
        self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(new_category_name))
        return self

    def add_item(self, item_category_name, item_name, item_introduction, item_sale_price, item_cost_price):
        self.common_actions.wait_for_element_visible(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_NAME_FIELD_IN_ITEM_LIST_PAGE)
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_NAME_FIELD_IN_ITEM_LIST_PAGE, item_name)
        self.common_actions.click_element(*self.item_locators.ITEM_INTRODUCTION_IN_ITEM_DETAIL_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_INTRODUCTION_FIELD)
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_INTRODUCTION_FIELD, item_introduction)
        self.common_actions.wait_for_element_clickable(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_IN_ITEM_DETAIL_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_SALE_PRICE_IN_ITEM_DETAIL_PAGE, item_sale_price)
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_INTERNAL_PRICE_IN_ITEM_DETAIL_PAGE, item_cost_price)
        self.common_actions.wait_for_element_clickable(*self.item_locators.CONFIRM_BUTTON_IN_ITEM_DETAIL_PAGE)
        self.common_actions.click_element(*self.item_locators.CONFIRM_BUTTON_IN_ITEM_DETAIL_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(item_name))
        return self

    def delete_item(self, item_category_name =None,item_name=None, delete_all=False):
        self.common_actions.wait_for_element_visible(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        if delete_all:
            while self.common_actions.is_element_present(*self.item_locators.DELETE_ALL_ITEM_BUTTON_IN_ITEM_LIST_PAGE):
                self.common_actions.wait_for_element_clickable(*self.item_locators.DELETE_ALL_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
                self.common_actions.click_element(*self.item_locators.DELETE_ALL_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
                self.common_actions.wait_for_element_visible(*self.item_locators.DELETE_ITEM_DELETE_BUTTON_IN_ITEM_LIST_PAGE)
                self.common_actions.click_element(*self.item_locators.DELETE_ITEM_DELETE_BUTTON_IN_ITEM_LIST_PAGE)
                self.common_actions.wait_for_element_disappear(*self.item_locators.DELETE_ITEM_DELETE_BUTTON_IN_ITEM_LIST_PAGE)
        else:
            self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
            self.common_actions.click_element(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
            self.common_actions.scroll_to_element_left(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(item_name))
            self.common_actions.wait_for_element_visible(*self.item_locators.DELETE_ITEM_BUTTON_IN_ITEM_LIST_PAGE(item_name))
            self.common_actions.click_element(*self.item_locators.DELETE_ITEM_BUTTON_IN_ITEM_LIST_PAGE(item_name))
            self.common_actions.wait_for_element_visible(*self.item_locators.DELETE_ITEM_DELETE_BUTTON_IN_ITEM_LIST_PAGE)
            self.common_actions.click_element(*self.item_locators.DELETE_ITEM_DELETE_BUTTON_IN_ITEM_LIST_PAGE)
            self.common_actions.wait_for_element_disappear(*self.item_locators.DELETE_ITEM_DELETE_BUTTON_IN_ITEM_LIST_PAGE)
        return self

    def copy_item(self, item_category_name, item_name):
        self.common_actions.wait_for_element_visible(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
        self.common_actions.scroll_to_element_left(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(item_name))
        self.common_actions.click_element(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.item_locators.COPY_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.item_locators.COPY_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_disappear(*self.item_locators.COPY_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        assert self.common_actions.get_element_count(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(item_name)) >= 2, "Service item name not copied successfully"
        return self

    def edit_item(self, item_category_name, old_item_name, new_item_name, item_introduction, item_sale_price, item_cost_price):
        self.common_actions.wait_for_element_visible(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
        self.common_actions.scroll_to_element_left(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(old_item_name))
        self.common_actions.click_element(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(old_item_name))
        self.common_actions.wait_for_element_visible(*self.item_locators.EDIT_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.item_locators.EDIT_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_NAME_FIELD_IN_ITEM_LIST_PAGE)
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_NAME_FIELD_IN_ITEM_LIST_PAGE, new_item_name)
        self.common_actions.click_element(*self.item_locators.ITEM_INTRODUCTION_IN_ITEM_DETAIL_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_INTRODUCTION_FIELD)
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_INTRODUCTION_FIELD, item_introduction)
        self.common_actions.wait_for_element_clickable(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_IN_ITEM_DETAIL_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_SALE_PRICE_IN_ITEM_DETAIL_PAGE, item_sale_price)
        self.common_actions.send_keys_to_element(*self.item_locators.ITEM_INTERNAL_PRICE_IN_ITEM_DETAIL_PAGE, item_cost_price)
        self.common_actions.wait_for_element_clickable(*self.item_locators.CONFIRM_BUTTON_IN_ITEM_DETAIL_PAGE)
        self.common_actions.click_element(*self.item_locators.CONFIRM_BUTTON_IN_ITEM_DETAIL_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(new_item_name))
        return self

    def tap_on_close_button_in_item_list_page(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_disappear(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        return self

    def verify_item(self, item_category_name, item_name, item_introduction, item_sale_price, item_cost_price):
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.ITEM_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        if not self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name)):
            if self.common_actions.is_element_present(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE):
                self.common_actions.click_element(*self.item_locators.EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE)
            else:
                self.common_actions.click_element(*self.item_locators.ADD_FIRST_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE)
            self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
            self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
            self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_FIELD)
            self.common_actions.send_keys_to_element(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_FIELD,item_category_name)
            self.common_actions.wait_for_element_clickable(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
            self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_visible(*self.item_locators.CATEGORY_MODAL_DELETE_CATEGORY_BUTTON(item_category_name))
            self.common_actions.click_element(*self.item_locators.CATEGORY_MODAL_CLOSE_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.item_locators.CATEGORY_MODAL_ADD_CATEGORY_BUTTON)
            self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
        else:
            self.common_actions.click_element(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
        if not self.common_actions.scroll_to_element(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(item_name)):
            self.common_actions.wait_for_element_visible(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
            self.common_actions.click_element(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
            self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_NAME_FIELD_IN_ITEM_LIST_PAGE)
            self.common_actions.send_keys_to_element(*self.item_locators.ITEM_NAME_FIELD_IN_ITEM_LIST_PAGE, item_name)
            self.common_actions.click_element(*self.item_locators.ITEM_INTRODUCTION_IN_ITEM_DETAIL_PAGE)
            self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_INTRODUCTION_FIELD)
            self.common_actions.send_keys_to_element(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_INTRODUCTION_FIELD, item_introduction)
            self.common_actions.wait_for_element_clickable(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
            self.common_actions.click_element(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON)
            self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_IN_ITEM_DETAIL_PAGE)
            self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
            self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
            self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE(item_category_name))
            self.common_actions.send_keys_to_element(*self.item_locators.ITEM_SALE_PRICE_IN_ITEM_DETAIL_PAGE, item_sale_price)
            self.common_actions.send_keys_to_element(*self.item_locators.ITEM_INTERNAL_PRICE_IN_ITEM_DETAIL_PAGE, item_cost_price)
            self.common_actions.wait_for_element_clickable(*self.item_locators.CONFIRM_BUTTON_IN_ITEM_DETAIL_PAGE)
            self.common_actions.click_element(*self.item_locators.CONFIRM_BUTTON_IN_ITEM_DETAIL_PAGE)
            self.common_actions.wait_for_element_visible(*self.item_locators.ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE)
            self.common_actions.scroll_to_element_left(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
            self.common_actions.click_element(*self.item_locators.CATEGORY_IN_ITEM_LIST_PAGE(item_category_name))
            self.common_actions.scroll_to_element(*self.item_locators.ITEM_IN_ITEM_LIST_PAGE(item_name))
        self.common_actions.click_element(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_disappear(*self.item_locators.CLOSE_BUTTON_IN_ITEM_LIST_PAGE)
        return self

    def tap_on_inventory_in_item_page(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.INVENTORY_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.INVENTORY_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.wait_for_element_disappear(*self.item_locators.SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        return self

    def reset_all_inventory(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.RESET_INVENTORY_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.RESET_INVENTORY_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.item_locators.RESET_INVENTORY_MODAL_FIELD)
        self.common_actions.send_keys_to_element(*self.item_locators.RESET_INVENTORY_MODAL_FIELD, "Reset")
        self.common_actions.wait_for_element_clickable(*self.item_locators.RESET_INVENTORY_MODAL_RESET_BUTTON)
        self.common_actions.click_element(*self.item_locators.RESET_INVENTORY_MODAL_RESET_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.RESET_INVENTORY_MODAL_RESET_BUTTON)
        return self

    def add_inventory(self, item_category_name, item_name, date, quantity, cost_price):
        self.common_actions.wait_for_element_visible(*self.item_locators.SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.scroll_to_element_left(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.scroll_to_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.click_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_ADD_INVENTORY)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_ADD_INVENTORY)
        self.common_actions.wait_for_element_visible(*self.item_locators.ADD_INVENTORY_MODAL_DATE(date))
        self.common_actions.send_keys_to_element(*self.item_locators.ADD_INVENTORY_MODAL_QUANTITY, quantity)
        self.common_actions.send_keys_to_element(*self.item_locators.ADD_INVENTORY_MODAL_COST_PRICE, cost_price)
        self.common_actions.wait_for_element_clickable(*self.item_locators.ADD_INVENTORY_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.ADD_INVENTORY_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.ADD_INVENTORY_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        return self

    def set_safety_stock(self, item_category_name, item_name, safety_stock_num):
        self.common_actions.wait_for_element_visible(*self.item_locators.SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.scroll_to_element_left(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.scroll_to_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.click_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_SAFETY_STOCK)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_SAFETY_STOCK)
        self.common_actions.wait_for_element_visible(*self.item_locators.SAFETY_STOCK_MODAL_STOCK_NOTIFICATION_SWITCH)
        if not self.common_actions.is_element_present(*self.item_locators.SAFETY_STOCK_MODAL_SAFETY_STOCK):
            self.common_actions.click_element(*self.item_locators.SAFETY_STOCK_MODAL_STOCK_NOTIFICATION_SWITCH)
            self.common_actions.wait_for_element_visible(*self.item_locators.SAFETY_STOCK_MODAL_SAFETY_STOCK)
        self.common_actions.send_keys_to_element(*self.item_locators.SAFETY_STOCK_MODAL_SAFETY_STOCK, safety_stock_num)
        self.common_actions.wait_for_element_clickable(*self.item_locators.SAFETY_STOCK_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.item_locators.SAFETY_STOCK_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.SAFETY_STOCK_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        return self

    def return_inventory(self, item_category_name, item_name, date, quantity):
        self.common_actions.wait_for_element_visible(*self.item_locators.SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.scroll_to_element_left(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.scroll_to_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.click_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_RETURN_INVENTORY)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_RETURN_INVENTORY)
        self.common_actions.wait_for_element_visible(*self.item_locators.RETURN_INVENTORY_MODAL_RETURN_INVENTORY(quantity, date))
        self.common_actions.click_element(*self.item_locators.RETURN_INVENTORY_MODAL_RETURN_INVENTORY(quantity, date))
        self.common_actions.wait_for_element_visible(*self.item_locators.RETURN_INVENTORY_BUTTON)
        self.common_actions.click_element(*self.item_locators.RETURN_INVENTORY_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.RETURN_INVENTORY_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.RETURN_INVENTORY_MODAL_RETURN_INVENTORY_ZERO(date))
        self.common_actions.click_element(*self.item_locators.RETURN_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.RETURN_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        return self

    def inventory_record(self, inventory_operation, item_category_name, item_name, quantity, cost_price):
        self.common_actions.wait_for_element_visible(*self.item_locators.SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.scroll_to_element_left(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.click_element(*self.item_locators.ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE(item_category_name))
        self.common_actions.scroll_to_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.click_element(*self.item_locators.ITEM_IN_INVENTORY_SETTINGS_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_INVENTORY_RECORD)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_INVENTORY_RECORD)
        quantity_value = float(quantity) if isinstance(quantity, str) else quantity
        cost_price_value = float(cost_price) if isinstance(cost_price, str) else cost_price
        price_value = quantity_value * cost_price_value
        price = f"{int(price_value):,}" if price_value % 1 == 0 else f"{price_value:,.2f}"
        if inventory_operation == "新增庫存":
            self.common_actions.wait_for_element_visible(*self.item_locators.INVENTORY_RECORD_MODAL_INVENTORY_RECORD_ADD(quantity, price))
        else:
            self.common_actions.wait_for_element_visible(*self.item_locators.INVENTORY_RECORD_MODAL_INVENTORY_RECORD_RETURN(quantity, price))
        self.common_actions.click_element(*self.item_locators.INVENTORY_RECORD_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.INVENTORY_RECORD_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_visible(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.click_element(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.item_locators.ITEM_INVENTORY_MODAL_CLOSE_BUTTON)
        return self

    def tap_on_close_button_in_inventory_page(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.CLOSE_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.CLOSE_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        self.common_actions.wait_for_element_disappear(*self.item_locators.CLOSE_BUTTON_IN_INVENTORY_SETTINGS_PAGE)
        return self

    def tap_on_back_button_in_item_page(self):
        self.common_actions.wait_for_element_visible(*self.item_locators.BACK_BUTTON_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.click_element(*self.item_locators.BACK_BUTTON_IN_ITEM_SETTINGS_PAGE)
        self.common_actions.wait_for_element_disappear(*self.item_locators.BACK_BUTTON_IN_ITEM_SETTINGS_PAGE)
        return self




