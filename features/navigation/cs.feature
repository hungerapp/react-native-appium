Feature: Customer Service Interaction

  @regression @message_cs @navigate_cs @navigate
  Scenario: Send and Check message via customer service
    Given I click on the Customer Service option in the navigation bar
    When I click on the message section
    Then I click on a past message to confirm it
    When I click on the recent message section
    Then I enter a message in the recent message input field

  @regression @cs_hyperlink @navigate_cs @navigate
  Scenario: Navigate Customer Service Links
    Then I tap on the follow Hotcake Instagram hyperlink
    Then I tap on the Pricing & Plans hyperlink
    Then I tap on the Help Center hyperlink
    Then I click back button to go back to calendar page

  