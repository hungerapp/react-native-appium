Feature: Third Party Tools in Branch Settings
    As a branch administrator
    I want to manage the third party tools of the branch
    To provide a better customer experience

    Background:
      Given I have selected the target branch "測試用分店"
      And I Navigate to the branch settings page


    @regression @sms_settings @navigation_to_third_party_tools @navigate_settings @navigate
    Scenario: SMS Settings
        Given This branch is subscribed to "Pro商務方案"
        When I tap on the Third Party Tools
        When I tap on the SMS button
        When I turn on the appointment success SMS
        When I turn off the appointment success SMS
        When I turn on the appointment reminder SMS
        When I turn off the appointment reminder SMS
        When I tap on the close button in the SMS settings
        When I tap on the back to calendar button in the third party tools
        Then I should see the calendar page

    @regression @line_oa_settings @navigation_to_third_party_tools @navigate_settings @navigate
    Scenario: LINE OA Settings
        Given This branch is subscribed to "Pro商務方案"
        When I tap on the Third Party Tools
        When I tap on the LINE OA button
        When I tap on the LINE LIFF integration
        When I tap on the close button in the LINE LIFF integration
        When I tap on the LINE widget integration
        When I turn on the Hotcake rich menu
        When I turn off the Hotcake rich menu
        When I tap on the close button in the LINE widget
        When I tap on the notification settings
        When I turn on the appointment reminder notification
        When I turn off the appointment reminder notification
        When I set the appointment reminder time to "1 天前"
        When I set the appointment reminder time to "2 天前"
        When I set the appointment reminder custom message to "測試"
        When I turn on the appointment success notification
        When I turn off the appointment success notification
        When I set the appointment success custom message to "測試"
        When I turn on the appointment cancellation notification
        When I turn off the appointment cancellation notification
        When I turn on the ticket notification on manual send
        When I turn off the ticket notification on manual send
        When I turn on the ticket notification on auto send
        When I turn off the ticket notification on auto send
        When I tap on the close button in the notification settings
        When I tap on the close button in the LINE OA settings
        When I tap on the back to calendar button in the third party tools
        Then I should see the calendar page

    @regression @payment_integration_settings @navigation_to_third_party_tools @navigate_settings @navigate
    Scenario: Payment Integration Settings
        Given This branch is subscribed to "Pro商務方案"
        When I tap on the Third Party Tools
        When I tap on the Payment Integration button
        When I tap on the INSTO Integration
        When I tap on the close button in the INSTO integration
        When I tap on the LINE Pay integration
        When I tap on the close button in the LINE Pay integration
        When I tap on the close button in the Payment Integration settings
        When I tap on the back to calendar button in the third party tools
        Then I should see the calendar page









