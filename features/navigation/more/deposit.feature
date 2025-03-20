Feature: Deposit
  

  # [DEPOSIT] 
  @regression @deposit_status_in_more
  Scenario: Manage Deposits - Unpaid and Paid Tabs
    Given I tap on deposit
    When I tap on the unpaid tab
    Then I can edit the deposit amount
    Then I can tap on confirm payment, do not collect, or cancel appointment
    When I tap on the paid tab
    Then I can tap on any paid invoice
    Then I can return to the calendar page