Feature: Service Appointment Settings
  As a merchant user
  I want to manage service appointment settings
  So that I can provide better booking experience for customers
  #TODO: 每個scenario要加tag, 這樣比較好debug
  #TODO: 這邊預設是在分店設定頁, 點擊服務預約區塊進入服務預約頁

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

  Scenario: Online Booking
    Given I am on the service appointment page
    And I have a service personnel named "U"
    And I have a service item named "60分鐘100元固定價單選子任務<current_datetime>"
    When I tap on the online booking
    Then I should see the online booking page

  
  Scenario: Add Online Booking Without Appointment Combination
    Given I am on the online booking page
    When I tap on the add unspecified appointment combination
    And I enter the appointment combination name "New Combination"
    And I enter the appointment combination introduction "Combination Introduction"
    And I select the appointment combination service personnel "全部選取"
    And I tap on the confirm button on the add appointment combination
    Then I should see the appointment combination name "New Combination" on the online booking page
  #TODO: 這邊要確認前置條件main service都有存在, 不然會fail
  Scenario: Edit Online Booking Appointment Combination
    Given I am on the online booking page
    When I tap on the edit appointment combination named "New Combination"
    And I tap on the open item tab
    And I select the main service item and clear all options "New Category" "Service Name"
    And I select the main service item "New Category" "Service Name 2"
    And I select the online booking type "單選"
    And I select the online booking type "複選"
    And I select the additional service item and clear all options "New Category" "Service Name 4"
    And I tap on the close button on the edit appointment combination
    Then I should see the appointment combination name "New Combination" on the online booking page
 
  Scenario: Delete Online Booking Appointment Combination
    Given I am on the online booking page
    When I tap on the edit appointment combination named "New Combination"
    And I delete the appointment combination
    Then I should not see the appointment combination name "New Combination" on the online booking page

  Scenario: Edit Online Booking Personnel
    Given I am on the online booking page
    When I tap on the edit service personnel "U"
    And I set the available date to "每月10日" "開放下1個月"
    And I set the available date to "每月10日" "全部開放"
    And I set the latest booking time to "10分鐘前"
    And I set the range of online booking quantity "1" to "5"
    And I set today open time "9:00, 20:00, 21:00, 22:10, 23:00"
    And I tap on the open item tab
    And I select the main service item and clear all options "New Category" "Service Name"
    And I select the main service item "New Category" "Service Name 2"
    And I select the online booking type "單選"
    And I select the additional service item and clear all options "New Category" "Service Name 4"
    And I tap on the close button on the edit appointment combination
    Then I should see the online booking page
  
 
  Scenario: Navigate to Booking Note Page
    Given I am on the service appointment page
    When I tap on the booking note
    Then I should see the booking note page

  Scenario: Add Booking Note
    Given I am on the booking note page
    When I turn off the booking note switch
    And I turn on the booking note switch
    And I enter the booking note "Booking Note"
    And I tap on the confirm button in the booking note
    Then I should see the service appointment page

  @haha
  Scenario: Navigate to Deposit Management Page
    Given I am on the service appointment page
    When I tap on the deposit management
    Then I should see the deposit management page
