Feature: Invitation Code
    As a merchant user
    I want to share my invitation code and manage my invitations
    So that I can invite other merchants to join

    @regression @invitation_code
    Scenario: Invitation Code
        Given I am on the Branch Settings page
        When I tap on the invitation code
        And I tap on the invitation code share button
        And I tap on the invited list
        And I tap on the invited list close button
        And I tap on the invitation code close button
        Then I should see the Branch Settings page
