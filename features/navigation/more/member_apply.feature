Feature: Member Apply

  # [MEMBER APPLY] VOUCHER_MANAGEMENT
  @regression @general_voucher_management_in_member_apply
  Scenario: Manage General Vouchers in Membership Application
    Given I tap on membership application
    When I tap on voucher management
    Then I can add a general voucher
    Then I can edit and delete a general voucher

  # [MEMBER APPLY] BONUS_POINT_VOUCHER_MANAGEMENT
  @regression @bonus_point_voucher_management_in_member_apply
  Scenario: Manage Bonus Point Vouchers in Membership Application
    Given I am in the voucher management section
    When I switch to the bonus point redemption tab
    Then I can add a bonus point voucher
    Then I can edit and delete a bonus point voucher

  # [MEMBER APPLY] MEMBERSHIP_GIFT_VOUCHER_MANAGEMENT
  @regression @membership_gift_voucher_management_in_member_apply
  Scenario: Manage Membership Gift Vouchers in Membership Application
    Given I am in the voucher management section
    When I switch to the membership gift tab
    Then I can add a membership gift voucher
    Then I can edit and delete a membership gift voucher

  # [MEMBER APPLY] BIRTHDAY_GIFT_VOUCHER_MANAGEMENT
  @regression @birthday_gift_voucher_management_in_member_apply
  Scenario: Manage Birthday Gift Vouchers in Membership Application
    Given I am in the voucher management section
    When I switch to the birthday gift tab
    Then I can add a birthday gift voucher
    Then I can edit and delete a birthday gift voucher
    Then I can return to the membership application page

  


  # [MEMBER APPLY] DOCUMENT_MANAGEMENT
  @regression @document_management_in_member_apply
  Scenario: Manage Documents in Membership Application
    Given I am on the membership application page
    When I tap on document management
    Then I can add a document
    Then I can edit, preview, and share a document
    Then I can view the signing history


  # [MEMBER APPLY] DISABLED_DOCUMENT_MANAGEMENT
  @regression @disabled_document_management_in_member_apply
  Scenario: Manage Disabled Documents
    Given I am in the document management section
    When I tap on the disabled tab
    Then I can edit a disabled document
    Then I can reactivate a disabled document
    Then I can return to the membership application page


  # [MEMBER APPLY] BONUS_POINT_RATIO_MANAGEMENT
  @regression @bonus_point_ratio_in_member_apply
  Scenario: Configure Bonus Point Ratio in Membership Application
    Given I am on the membership application page
    When I tap on bonus points
    Then I can freely set the bonus point ratio
    Then I can return to the membership application page

  # [MEMBER APPLY] CUSTOM_MEMBERSHIP_REGISTRATION
  @regression @custom_membership_registration_in_member_apply
  Scenario: Configure Custom Membership Registration in Membership Application
    Given I am on the membership application page
    When I tap on custom membership registration fields
    Then I can add a new field
    Then I can edit or delete a field
    Then I can return to the membership application page
    Then I can tap the return to calendar button to go back to the calendar page
  

  
