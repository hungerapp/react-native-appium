from appium.webdriver.common.appiumby import AppiumBy

class IpadDeviceLocators:
    # Branch Settings Page
    IPAD_DEVICE_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="iPad 裝置管理"]')

    # Ipad Device Page
    CLOSE_BUTTON_IN_IPAD_DEVICE_PAGE = (AppiumBy.XPATH, '//*[@resource-id="xmark"]')
    ADD_IPAD_DEVICE_BUTTON_IN_IPAD_DEVICE_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="新增 iPad (產生開通碼)"]')
    # Ipad Device Page / Add Ipad Device Dialog
    NEXT_BUTTON_IN_ADD_IPAD_DEVICE_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="下一步：產生 iPad 開通碼"]')
    IPAD_PASS_CODE_IN_ADD_IPAD_DEVICE_DIALOG = (AppiumBy.XPATH, '//android.widget.TextView[@text="iPad 開通碼"]')
    CLOSE_BUTTON_IN_ADD_IPAD_DEVICE_DIALOG = (AppiumBy.XPATH, '(//*[@resource-id="xmark"])[2]')