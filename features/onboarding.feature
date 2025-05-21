Feature: First launch onboarding flow
  As a first-time user
  I want to see the onboarding animation
  And be navigated to the onboarding page
  
  @regression  @onboarding  @login
  Scenario: Display onboarding animation and start using the app
    Given the app is launched for the first time
    When I select my language and click sure button
    Then I can start using the app
