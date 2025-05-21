from appium.webdriver.common.appiumby import AppiumBy

class CreateRequestLocators:
      CREATE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'calendar-fab-trigger')
      CREATE_REQUEST_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("請領")')
      QA_TEST_REQUESTER_SELECT = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
      SALLY_REQUESTER_SELECT = (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲')
      REQUEST_PERSONNEL_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請領人員")')
      ITEM_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商品")')
      SELECT_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇商品")')
    
      REQUESTER_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
      TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
      AUTO_TEST_TAB = (AppiumBy.ACCESSIBILITY_ID, '自動化測試商品')
      SAVE_PRODUCT_BTN = (AppiumBy.ACCESSIBILITY_ID, 'check')
      
      TEST_PRODUCT_OPTIONS = [
              'new UiSelector().text("測試1")',
              'new UiSelector().text("測試2")',
              'new UiSelector().text("測試3")',
              'new UiSelector().text("測試4")',
              'new UiSelector().text("測試5")',
      ]
    
      CONFIRM_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("請領商品")')
      PERSONNEL_SIGN_BTN = (AppiumBy.ACCESSIBILITY_ID, '請領人員進行簽名')
      CONFIRM_REQUEST_BTN = (AppiumBy.ACCESSIBILITY_ID, '確認請領')
      CLEAR_ITEMS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部清除")')
      QUANTITY_INPUT = (AppiumBy.ACCESSIBILITY_ID, '數量輸入')
      AMOUNT_EDIT_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(0)')
      AMOUNT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
      AMOUNT_CLEAR_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")')
      AMOUNT_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'circle-check')
      EDIT_ITEM_QUANTITY_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down").instance(1)')
      QUANTITY_PLUS_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@resource-id, "plus")]')
      QUANTITY_REVISE_INPUT2 = (AppiumBy.XPATH, "//*[@resource-id='undefined-number-field-input']")
      QUANTITY_REVISE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
      
      
      QUANTITY_PLUS = [
              'new UiSelector().className("com.horcrux.svg.PathView").instance(4)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(7)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(10)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(13)',
              'new UiSelector().className("com.horcrux.svg.PathView").instance(16)'
      ]  
    
      REMOVE_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("circle-minus").instance(0)')
      REMOVE_CONFIRM_BTN = (AppiumBy.ACCESSIBILITY_ID, '移除')
      BACK_TO_PREVIOUS_PAGE_ICON = (AppiumBy.ACCESSIBILITY_ID, 'xmark')
      SIGNATURE_PAD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.webkit.WebView")')
      CLEAR_SIGNATURE_BTN = (AppiumBy.ACCESSIBILITY_ID, '清除簽名')
