Feature: Brand Setting
  
  # [BRAND SETTING]
  @regression @brand_setting @navigate_more @navigate @navigate_more_brand_setting
  Scenario: Modify Brand Setting
    Given I tap on more in the bottom navigation bar
    When I tap on brand settings
    Then I can edit the brand name
    Then I can edit the brand description
