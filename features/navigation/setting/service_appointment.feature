Feature: Service Appointment Settings
  As a merchant user
  I want to manage service appointment settings
  So that I can provide better booking experience for customers

  @regression @service_appointment @navigation_to_service_appointment_page
  Scenario: Navigate to Service Appointment Page
    Given I am on the branch settings page
    When I tap on the service appointment
    Then I should see the service appointment page

  @regression @service_appointment @share_appointment_link
  Scenario: Share Appointment Link
    Given I am on the service appointment page
    When I share the appointment link
    And I click to apply for a LINE Official Account
    Then I should see the service appointment page

  @regression @service_appointment @service_item
  Scenario: Service Item
    Given I am on the service appointment page
    When I tap on the service items
    And I delete all service category
    And I add a new service category named "新的分類<current_datetime>"
    And I edit the service category named "新的分類<current_datetime>" to "要被刪除的分類<current_datetime>"
    And I delete the service category named "要被刪除的分類<current_datetime>"
    And I add a new service category named "服務項目分類<current_datetime>"
    And I select a service category named "服務項目分類<current_datetime>"
    And I click the add service item button
    And I enter the service item name "60分鐘100元固定價單選子任務<current_datetime>"
    And I enter the service code name "S1"
    And I enter the service introduction "Service Introduction<current_datetime>"
    And I select the service category "服務項目分類<current_datetime>" in the add service item
    And I enter the service duration "60" minutes
    And I enter the service price "100"
    And I select the service display type "固定價"
    And I select the sub service type "單選"
    And I add sub service items name "我是子服務" and duration "30" minutes and price "50"
    And I edit the sub service items "我是子服務" to "我是要被刪掉的子服務" and duration "50" minutes and price "100"
    And I delete the sub service items "我是要被刪掉的子服務"
    And I add sub service items name "我是子任務1" and duration "30" minutes and price "50"
    And I add sub service items name "我是子任務2" and duration "60" minutes and price "100"
    And I click the save add service item button
    And I copy the service item name "60分鐘100元固定價單選子任務<current_datetime>"
    And I delete the service item "60分鐘100元固定價單選子任務<current_datetime>"
    And I copy the service item name "60分鐘100元固定價單選子任務<current_datetime>"
    And I edit the service item "60分鐘100元固定價單選子任務<current_datetime>"
    And I enter the service item name "180分鐘500元起標價複選子任務<current_datetime>"
    And I enter the service code name "S2"
    And I enter the service introduction "我被更改過了<current_datetime>"
    And I select the service category "服務項目分類<current_datetime>" in the add service item
    And I enter the service duration "180" minutes
    And I enter the service price "500"
    And I select the service display type "起標價"
    And I select the sub service type "複選"
    And I add sub service items name "我是子服務3" and duration "90" minutes and price "300"
    And I click the save add service item button
    And I tap on the close button on the service item page
    Then I should see the service appointment page

  @regression @service_appointment @online_booking_settings
  Scenario: Online Booking Settings
    Given I am on the service appointment page
    And I have a service personnel named "服務人員1_<current_datetime>"
    And I have a service personnel named "服務人員2_<current_datetime>"
    And I have a service item "服務項目分類<current_datetime>" and "主服務<current_datetime>"
    And I have a service item "服務項目分類<current_datetime>" and "加購<current_datetime>"
    When I tap on the online booking
    And I delete all appointment combinations
    And I add a new appointment combination named "刪除不指定組合<current_datetime>" and introduction "組合介紹<current_datetime>" and service personnel "全部選取"
    And I delete the appointment combination named "刪除不指定組合<current_datetime>"
    And I add a new appointment combination named "我是不指定組合<current_datetime>" and introduction "組合介紹<current_datetime>" and service personnel "全部選取"
    And I edit the appointment combination "我是不指定組合<current_datetime>" and select the main service item "服務項目分類<current_datetime>" "主服務<current_datetime>" and the online booking type "複選" and select the additional service item "服務項目分類<current_datetime>" "加購<current_datetime>"
    And I modify the service personnel "服務人員1_<current_datetime>" open settings to set available date "每月10日" "開放下1個月" and latest booking time "10分鐘前" and online booking quantity range "1" to "5"
    And I modify the service personnel "服務人員1_<current_datetime>" open time to set today open time "9:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:10, 23:00"
    And I modify the service personnel "服務人員1_<current_datetime>" open item to set the main service item "服務項目分類<current_datetime>" "主服務<current_datetime>" and the online booking type "單選" and select the additional service item "服務項目分類<current_datetime>" "加購<current_datetime>"
    And I modify the service personnel "服務人員2_<current_datetime>" open settings to set available date "每月17日" "全部開放" and latest booking time "10分鐘前" and online booking quantity range "1" to "5"
    And I modify the service personnel "服務人員2_<current_datetime>" open time to set today open time "9:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00"
    And I modify the service personnel "服務人員2_<current_datetime>" open item to set the main service item "服務項目分類<current_datetime>" "主服務<current_datetime>" and the online booking type "單選" and select the additional service item "服務項目分類<current_datetime>" "加購<current_datetime>"
    And I tap on the close button on the online booking page
    Then I should see the service appointment page
  
  @regression @service_appointment @booking_note_settings
  Scenario: Booking Note Settings
    Given I am on the service appointment page
    When I tap on the booking note
    And I turn off the booking note switch
    And I turn on the booking note switch
    And I enter the booking note "Booking Note"
    And I tap on the confirm button in the booking note
    Then I should see the service appointment page

  @regression @service_appointment @deposit_management_settings
  Scenario: Deposit Management Settings
    Given I am on the service appointment page
    And I have a service item "服務項目分類<current_datetime>" and "一般日期指定收定金服務項目<current_datetime>"
    And I have a service item "服務項目分類<current_datetime>" and "指定日期指定收定金服務項目<current_datetime>"
    When I tap on the deposit management
    And I tap on the general deposit settings
    And I turn off the general date deposit switch
    And I turn on the general date deposit switch
    And  I set the default member status to no receive deposit
    And  I set the default member status to receive deposit and set the receive type "全部收取"
    And  I set the default member status to receive deposit and set the receive type "來訪3次，下次不收取"
    When I set the payable service item scope to "全部服務"
    When I set the payable service item scope to "指定服務" and service item "服務項目分類<current_datetime>" "一般日期指定收定金服務項目<current_datetime>" and clear all
    And I go to integration payment method
    And I set the payment method to "銀行匯款"
    And I set the payment method to "儲值金"
    And I set the payment method to "信用卡"
    And I set the payment method to "LINE Pay"
    And I set the payment amount pricing method to "固定值" and amount "100"
    And I set the payment amount pricing method to "比例" and minimum amount "50" and percentage "50%"
    And I set the auto cancel if unpaid to "1 小時"
    And I set the payment instructions to "請於預約時間前1小時付款<current_datetime>"
    And I tap on the confirm button in the deposit settings page
    And I tap on the specific date deposit settings
    And I turn off the specific date deposit switch
    And I turn on the specific date deposit switch
    And I set the specific date name "測試<current_datetime>" "<current_datetime>" to "tomorrow"
    And I set the default member status to receive deposit and set the receive type "全部收取"
    And I set the payable service item scope to "指定服務" and service item "服務項目分類<current_datetime>" "指定日期指定收定金服務項目<current_datetime>" and clear all
    And I go to integration payment method
    And I set the payment method to "銀行匯款"
    And I set the payment method to "儲值金"
    And I set the payment method to "信用卡"
    And I set the payment method to "LINE Pay"
    And I set the payment amount pricing method to "固定值" and amount "100"
    And I set the payment amount pricing method to "比例" and minimum amount "50" and percentage "50%"
    And I set the auto cancel if unpaid to "1 小時"
    And I set the payment instructions to "這是指定區間，請於預約時間前1小時付款<current_datetime>"
    And I tap on the confirm button in the deposit settings page
    And I tap on the close button in the deposit management page
    Then I should see the service appointment page

  @regression @service_appointment @reservation_restriction_settings
  Scenario: Advanced Feature Settings
    Given I am on the service appointment page
    And I have a service item "服務項目分類<current_datetime>" and "需要緩衝時間的服務項目<current_datetime>"
    And I have a service item "服務項目分類<current_datetime>" and "設備連動服務1<current_datetime>"
    And I have a service item "服務項目分類<current_datetime>" and "設備連動服務2<current_datetime>"
    When I tap on the advanced feature settings
    And I tap on the reservation restriction
    And I set the cancellation time to "當天可取消"
    And I turn off the upcoming reservation switch
    And I turn on the upcoming reservation switch
    And I set the upcoming reservation count to "3"
    And I turn off the no show switch
    And I turn on the no show switch
    And I set the no show count to "3"
    And I turn off the monthly reservation cancellation limit switch
    And I turn on the monthly reservation cancellation limit switch
    And I set the monthly reservation cancellation limit to "3"
    And I turn off customer score limit switch
    And I turn on customer score limit switch
    And I set the customer score limit to "3.1"
    And I tap on the confirm button in the reservation restriction page

    When I tap on the post reservation buffer
    And I turn off the post reservation buffer switch
    And I turn on the post reservation buffer switch
    And I set the post reservation buffer time to "30" minutes
    And I set the need post reservation buffer service item to "服務項目分類<current_datetime>" "需要緩衝時間的服務項目<current_datetime>"
    And I tap on the confirm button in the post reservation buffer page

    When I tap on the business hours
    And I turn off the business hours switch
    And I turn on the business hours switch
    And I set the business hours to "週一" 9:00-21:00
    And I set the business hours to "週二" 9:00-21:00
    And I set the business hours to "週三" 9:00-21:00
    And I set the business hours to "週四" 9:00-21:00
    And I set the business hours to "週五" 9:00-21:00
    And I set the business hours to "週六" 9:00-21:00
    And I set the business hours to "週日" 9:00-21:00
    And I tap on the close button in the business hours page

    When I tap on the equipment management
    And I Delete the equipment
    And I add a new equipment named "設備1_<current_datetime>" and set the equipment number to "3" and select the service item "服務項目分類<current_datetime>" "設備連動服務1<current_datetime>"
    And I edit the equipment "設備1_<current_datetime>" to "設備2_<current_datetime>" and set the equipment number to "1" and select the service item "服務項目分類<current_datetime>" "設備連動服務2<current_datetime>"
    And I tap on the close button in the equipment management page
    And I tap on the close button in the advanced feature settings page
    And I tap on the close button in the service appointment page
    Then I should see the Branch Settings page




