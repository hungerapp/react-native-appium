Feature: Service Appointment Settings
  As a merchant user
  I want to manage service appointment settings
  So that I can provide better booking experience for customers

  @regression @navigation_to_service_appointment_page
  Scenario: Navigate to Service Appointment Page
    Given I am on the branch settings page
    When I tap on the service appointment
    Then I should see the service appointment page

  @regression @share_appointment_link
  Scenario: Share Appointment Link
    Given I am on the service appointment page
    When I share the appointment link
    And I click to apply for a LINE Official Account
    Then I should see the service appointment page

  @regression @service_item
  Scenario: Service Item
    Given I am on the service appointment page
    When I tap on the service items
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

  @regression @online_booking_settings
  Scenario: Online Booking Settings
    Given I am on the service appointment page
    And I have a service personnel named "服務人員1_<current_datetime>"
    And I have a service personnel named "服務人員2_<current_datetime>"
    And I have a service item "服務項目分類<current_datetime>" and "主服務<current_datetime>"
    And I have a service item "服務項目分類<current_datetime>" and "加購<current_datetime>"
    When I tap on the online booking
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
  
  @regression @booking_note_settings
  Scenario: Booking Note Settings
    Given I am on the service appointment page
    When I tap on the booking note
    And I turn off the booking note switch
    And I turn on the booking note switch
    And I enter the booking note "Booking Note"
    And I tap on the confirm button in the booking note
    Then I should see the service appointment page

  @regression @deposit_management_settings
  Scenario: Deposit Management Settings
#    Given I am on the service appointment page
#    And I have a service item "服務項目分類<current_datetime>" and "一般日期指定收定金服務項目<current_datetime>"
#    When I tap on the deposit management
#    When I tap on the general deposit settings
#    And I turn off the general date deposit switch
#    And I turn on the general date deposit switch
#    When  I set the default member status to no receive deposit
#    When  I set the default member status to receive deposit and set the receive type "全部收取"
#    When  I set the default member status to receive deposit and set the receive type "來訪3次，下次不收取"
#    When I set the payable service item scope to all service items
#    When I set the payable service item scope to "服務項目分類<current_datetime>" "一般日期指定收定金服務項目<current_datetime>"
#    When I go to integration payment method
    When I set the payment method to "銀行匯款"
    When I set the payment method to "儲值金"
    When I set the payment method to "信用卡"
    When I set the payment method to "LINE Pay"
    When


