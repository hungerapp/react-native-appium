Feature: Invitation Code
    As a merchant user
    I want to share my invitation code and manage my invitations
    So that I can invite other merchants to join

    @regression @invitation_code @invitation_code_page
    Scenario: Copy Invitation Code
        Given I am on the invitation code page
        When I tap on the invitation code share button
        Then I should see the invitation code page
