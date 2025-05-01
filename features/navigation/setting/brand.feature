Feature: Brand Management in Branch Settings
    As a branch administrator
    I hope to manage the brand information of the branch
    To provide a better customer experience
    TODO: 這邊是不是需要先進入分店設定頁？ 預設是會在行事曆頁,然後點擊導覽列設定進入分店設定頁為第一條scenario的given(被你mark掉的Background)

#    Background:
#        Given I am on the Branch Settings page
#        When I tap on the Branch Name
#        Then I should see the Branch and Brand Information page

    @regression @branch_name @branch_brand_info_page  #todo: 建議mark取同一名字以外可再多一個獨立的名稱, 這樣如果只要測試單一scenario, 其他scenario會一起跑執行不好debug
    Scenario: Clear Branch Name and See Required Field Warning
        Given I am on the Branch and Brand Information page
        When I clear the Branch Name field
        Then I should see an error message "This field is required"

    @regression @branch_name @branch_brand_info_page  #todo: 建議mark取同一名字以外可再多一個獨立的名稱, 這樣如果只要測試單一scenario, 其他scenario會一起跑執行不好debug
    Scenario Outline: Input Text in Branch Name Field and Display Text
        Given I am on the Branch and Brand Information page
        When I enter "Robot_Branch_Name" in the Branch Name field
        Then I should see "Test Branch Name" in the branch name field

    @regression @branch_introduction @branch_brand_info_page #todo: 建議mark取同一名字以外可再多一個獨立的名稱, 這樣如果只要測試單一scenario, 其他scenario會一起跑執行不好debug
    Scenario: Clear Branch Introduction
        Given I am on the Branch and Brand Information page
        When I clear the branch introduction text
        Then the branch introduction field should be empty

    @regression @branch_introduction @branch_brand_info_page #todo: 建議mark取同一名字以外可再多一個獨立的名稱, 這樣如果只要測試單一scenario, 其他scenario會一起跑執行不好debug
    Scenario: Input Robot Introduction and Verify Text
        Given I am on the Branch and Brand Information page
        When I enter "🤖 Welcome to our AI-powered store! We provide 24/7 automated service." in the branch introduction
        Then I should see "🤖 Welcome to our AI-powered store! We provide 24/7 automated service." in the branch introduction

    @regression @branch_phone @branch_brand_info_page 
    Scenario: Modify Branch Phone Number
        Given I am on the Branch and Brand Information page
        When I turn off the branch phone display switch
        And I turn on the branch phone display switch
        And I select "+886" as the country code
        And I enter "0912345678" in the branch phone number field
        Then I should see "+886" "0912345678" in the branch phone field

    @regression @branch_address @branch_brand_info_page
    Scenario: Update Branch Address
        Given I am on the Branch and Brand Information page
        When I turn off the branch address display switch
        And I turn on the branch address display switch
        And I select "臺北市" as the city
        And I select "中正區" as the district
        And I enter "地球路1號" in the branch address field
        Then I should see "臺北市" "中正區" "地球路1號" in the branch address field

    @regression @brand_setting_section @branch_brand_info_page
    Scenario: Expand Brand Settings Page
        Given I am on the Branch and Brand Information page
        When I tap on the Expand Brand Settings button
        Then I should see the Brand Settings section

    @regression @close_branch_brand_info_page
    Scenario: Close Branch and Brand Information Page
        Given I am on the Branch and Brand Information page
        When I tap on the Close button
        Then I should see the Branch Settings page
    
    #TODO: 這條scenario的given會是點擊進入分店和品牌資訊頁後開始, 目前你是直接預設你在分店設定頁
    @regression @save_branch_brand_info
    Scenario: Save Branch and Brand Information
        Given I am on the Branch and Brand Information page
        When I enter "Robot_Branch_Name" in the Branch Name field
        And I enter "🤖 Welcome to our AI-powered store! We provide 24/7 automated service." in the branch introduction
        And I turn on the branch phone display switch
        And I select "+886" as the country code
        And I enter "0912345678" in the branch phone number field
        And I turn on the branch address display switch
        And I select "臺北市" as the city
        And I select "中正區" as the district
        And I enter "地球路1號" in the branch address field
        And I tap on the confirm button
        Then I should see the Branch Settings page

        # TODO: Add Subscription Plan Management



