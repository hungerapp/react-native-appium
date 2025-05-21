Feature: Tutorial Book

  # [USER BOOK]
  @regression @user_book_in_more @navigation @navigation_more @navigation_more_user_book
  Scenario: Opening the User Book
    Given I click on the user book
    Then I can successfully redirect to the user book
    Then I can return to the calendar page
