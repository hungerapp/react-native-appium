from appium.webdriver.common.appiumby import AppiumBy

class CheckoutPageLocators:
    # Branch Settings Page
    CHECKOUT_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="結帳"]')

    # Checkout Settings Page
    BACK_BUTTON_IN_CHECKOUT_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@resource-id="arrow-left"]')
    CHECKOUT_SIGNATURE_IN_CHECKOUT_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="結帳簽名"]')
    # Checkout Settings Page/Checkout Signature Page
    CLOSE_BUTTON_IN_CHECKOUT_SIGNATURE_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    CHECKOUT_SIGNATURE_SWITCH_IN_CHECKOUT_SIGNATURE_PAGE = (AppiumBy.ACCESSIBILITY_ID, '結帳簽名-switch-button')
