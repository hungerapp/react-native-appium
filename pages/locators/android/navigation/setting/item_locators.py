from appium.webdriver.common.appiumby import AppiumBy

class ItemPageLocators:
    # Branch Settings Page
    ITEM_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="商品, 建立商品庫和庫存管理"]')

    # Item Settings Page
    ITEM_IN_ITEM_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="商品項目"]')
    INVENTORY_IN_ITEM_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="進存貨管理"]')
    BACK_BUTTON_IN_ITEM_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="arrow-left"]')

    # Item Settings Page / Item List Page
    CLOSE_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    ADD_FIRST_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="新增第一個分類"]')
    CATEGORY_IN_ITEM_LIST_PAGE = lambda self, category: (AppiumBy.XPATH, f'//android.widget.HorizontalScrollView//android.widget.TextView[@text="{category}"]')
    EDIT_CATEGORY_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//*[@resource-id="pen-to-square"]')
    ADD_ITEM_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="新增商品項目"]')
    ITEM_IN_ITEM_LIST_PAGE = lambda self, item_name: (AppiumBy.XPATH, f'//android.widget.ScrollView//android.widget.TextView[@text="{item_name}"]')
    DELETE_ITEM_BUTTON_IN_ITEM_LIST_PAGE = lambda self, item_name: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{item_name}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')
    DELETE_ALL_ITEM_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//*[@resource-id="circle-minus"]')
    DELETE_ITEM_DELETE_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="刪除"]')
    COPY_ITEM_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="複製商品項目"]')
    EDIT_ITEM_BUTTON_IN_ITEM_LIST_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="編輯商品項目"]')
    # Item Settings Page / Item List Page / Category Modal
    CATEGORY_MODAL_ADD_CATEGORY_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="新增分類"]')
    CATEGORY_MODAL_DELETE_CATEGORY_BUTTON = lambda self, category: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{category}"]/../android.view.ViewGroup//*[@resource-id="circle-minus"]')
    CATEGORY_MODAL_EDIT_CATEGORY_BUTTON = lambda self, category: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{category}"]/../android.view.ViewGroup//*[@resource-id="pen-to-square"]')
    CATEGORY_MODAL_DELETE_ALL_CATEGORY_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="新增分類"]/../../android.view.ViewGroup/android.widget.ScrollView//*[@resource-id="circle-minus"]')
    CATEGORY_MODAL_DELETE_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="刪除"]')
    CATEGORY_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH, '(//*[@resource-id="xmark"])[2]')
    CATEGORY_MODAL_CATEGORY_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
    CATEGORY_MODAL_CATEGORY_NAME_CONFIRM_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    # Item Settings Page / Item List Page / Item Detail Page
    ITEM_NAME_FIELD_IN_ITEM_LIST_PAGE = (AppiumBy.ACCESSIBILITY_ID, '商品名稱-text-input')
    ITEM_INTRODUCTION_IN_ITEM_DETAIL_PAGE = (AppiumBy.ACCESSIBILITY_ID, '商品介紹-textarea-field')
    ITEM_CATEGORY_IN_ITEM_DETAIL_PAGE = (AppiumBy.ACCESSIBILITY_ID, '商品分類-select-field')
    ITEM_CATEGORY_SELECTION_IN_ITEM_DETAIL_PAGE = lambda self, category: (AppiumBy.XPATH, f'//*[@resource-id="商品分類-option"]/android.widget.TextView[@text="{category}"]')
    ITEM_SALE_PRICE_IN_ITEM_DETAIL_PAGE = (AppiumBy.ACCESSIBILITY_ID, '販售單價-text-input')
    ITEM_INTERNAL_PRICE_IN_ITEM_DETAIL_PAGE = (AppiumBy.ACCESSIBILITY_ID, '請領單價-text-input')
    CONFIRM_BUTTON_IN_ITEM_DETAIL_PAGE = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    # Item Settings Page / Item List Page / Item Detail Page / Introduction Detail Modal
    ITEM_INTRODUCTION_DETAIL_MODAL_CONFIRM_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="circle-check"]')
    ITEM_INTRODUCTION_DETAIL_MODAL_INTRODUCTION_FIELD = (AppiumBy.ACCESSIBILITY_ID, '商品介紹-textarea-input')

    # Item Settings Page / Inventory Settings Page
    CLOSE_BUTTON_IN_INVENTORY_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    ITEM_CATEGORY_IN_INVENTORY_SETTINGS_PAGE = lambda self, category: (AppiumBy.XPATH, f'//android.widget.HorizontalScrollView//android.widget.TextView[@text="{category}"]')
    ITEM_IN_INVENTORY_SETTINGS_PAGE = lambda self, item_name: (AppiumBy.XPATH, f'//android.widget.ScrollView//android.widget.TextView[@text="{item_name}"]')
    SETTING_BUTTON_IN_INVENTORY_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="gear"]')
    RESET_INVENTORY_BUTTON_IN_INVENTORY_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@text="重置所有庫存"]')
    # Item Settings Page / Inventory Settings Page / Reset Inventory Modal
    RESET_INVENTORY_MODAL_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
    RESET_INVENTORY_MODAL_RESET_BUTTON = (AppiumBy.XPATH, '//*[@text="重置"]')
    # Item Settings Page / Inventory Settings Page / Item Inventory Modal
    ITEM_INVENTORY_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH, '(//*[@resource-id="xmark"])[2]')
    ITEM_INVENTORY_MODAL_ADD_INVENTORY = (AppiumBy.XPATH, '//*[@text="新增存貨"]')
    ITEM_INVENTORY_MODAL_SAFETY_STOCK = (AppiumBy.XPATH, '//*[@text="安全庫存量"]')
    ITEM_INVENTORY_MODAL_RETURN_INVENTORY = (AppiumBy.XPATH, '//*[@text="退倉"]')
    ITEM_INVENTORY_MODAL_INVENTORY_RECORD = (AppiumBy.XPATH, '//*[@text="進存紀錄"]')
    # Item Settings Page / Inventory Settings Page / Item Inventory Modal / Add Inventory Modal
    ADD_INVENTORY_MODAL_CONFIRM_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    ADD_INVENTORY_MODAL_DATE =  lambda self, date: (AppiumBy.XPATH, f'//*[@text="進貨日期"]/../android.widget.TextView[@text="{date}"]')
    ADD_INVENTORY_MODAL_QUANTITY = (AppiumBy.ACCESSIBILITY_ID, '進貨數量-text-input')
    ADD_INVENTORY_MODAL_COST_PRICE = (AppiumBy.ACCESSIBILITY_ID, '進貨單價-text-input')
    # Item Settings Page / Inventory Settings Page / Item Inventory Modal / Add Inventory Modal / Date Dialog
    DATE_DIALOG_CONFIRM_BUTTON = (AppiumBy.XPATH, '//*[@text="確定"]')
    # Item Settings Page / Inventory Settings Page / Item Inventory Modal / safety stock Modal
    SAFETY_STOCK_MODAL_CONFIRM_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="check"]')
    SAFETY_STOCK_MODAL_STOCK_NOTIFICATION_SWITCH = (AppiumBy.XPATH, '//*[@resource-id="庫存提醒-switch-button"]')
    SAFETY_STOCK_MODAL_SAFETY_STOCK = (AppiumBy.ACCESSIBILITY_ID, '安全庫存量-text-input')
    # Item Settings Page / Inventory Settings Page / Item Inventory Modal / return inventory Modal
    RETURN_INVENTORY_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH, '(//*[@resource-id="xmark"])[3]')
    RETURN_INVENTORY_MODAL_RETURN_INVENTORY = lambda self, add_inventory, date: (AppiumBy.XPATH, f'//android.widget.TextView[@text="{add_inventory}"]/../android.widget.TextView[@text="新增存貨 · {date}"]/../android.view.ViewGroup//*[@text="退倉"]')
    RETURN_INVENTORY_MODAL_RETURN_INVENTORY_ZERO = lambda self, date: (AppiumBy.XPATH,f'//android.widget.TextView[@text="0"]/../android.widget.TextView[@text="新增存貨 · {date}"]')
    RETURN_INVENTORY_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//android.widget.TextView[@text="退倉"]')
    # Item Settings Page / Inventory Settings Page / Item Inventory Modal / inventory record Modal
    INVENTORY_RECORD_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH, '(//*[@resource-id="xmark"])[3]')
    INVENTORY_RECORD_MODAL_INVENTORY_RECORD_RETURN = lambda self, quantity, price: (AppiumBy.XPATH, f'//android.widget.TextView[@text="退倉"]/../android.widget.TextView[@text="-{quantity} (NT${price})"]')
    INVENTORY_RECORD_MODAL_INVENTORY_RECORD_ADD = lambda self, quantity, price: (AppiumBy.XPATH,f'//android.widget.TextView[@text="新增庫存"]/../android.widget.TextView[@text="+{quantity} (NT${price})"]')