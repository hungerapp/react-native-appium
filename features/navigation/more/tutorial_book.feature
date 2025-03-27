Feature: Tutorial Book

  # [USER GUIDE]
  @regression @user_guide_in_more
  Scenario: Opening the User Guide
    Given I click on the user guide
    Then I can successfully redirect to the user guide
    Then I can return to the calendar page
