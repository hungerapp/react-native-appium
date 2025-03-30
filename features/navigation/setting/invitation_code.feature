Feature: Invitation Code

  @regression @invitation_code @invitation_code_page
  Scenario: Verify Invitation Code Management Flow
    Given I am on the Branch Settings page
    When I tap on Invitation Code in the Branch Settings page
    Then I should be navigated to the Invitation Code page
    When I tap on Invitation Code Sharing
    Then the Invitation Code Sharing dialog is displayed
    When I tap on Copy in the Invitation Code Sharing dialog
    Then the Invitation Code Sharing dialog is dismissed
    When I tap on Invited List in the Invitation Code page
    Then I should be navigated to the Invited List page
    When I tap on Close Button in the Invited List page
    Then I should be navigated back to the Invitation Code page
    When I tap on Close Button in the Invitation Code page
    Then I should be navigated back to the Branch Settings page
