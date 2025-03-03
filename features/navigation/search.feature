Feature: Search Functionality
  
  @regression @search_valid_number
  Scenario: Search with a valid complete number
     Given I tap on the Search option in the navigation bar
     When I enter a valid complete number
     Then I tap on the corresponding result
     Then I scroll down to view the relevant search results
     Then I tap on the Member tab
     Then I tap on the corresponding result again
     Then I click back button to return to the previous page

  @regression @existing_name_search
  Scenario: Search with an existing name
     Given I tap on the Search option in the navigation bar
     When I enter an existing name
     Then I tap on the corresponding result
     Then I tap on the Member 
     Then I tap on the corresponding result again
     Then I click back button to return to the previous page

  @regression @invalid_name_search
  Scenario: Search with an invalid name
     Given I tap on the Search option in the navigation bar
     When I enter an invalid name
     Then I see no data indicating that the name is invalid
     Then I switch to the Member tab
     Then I see no data indicating that the name is invalid
     Then I click back button to return to the previous page

  @regression @invalid_number_search 
  Scenario: Search with an invalid complete number
     Given I tap on the Search option in the navigation bar
     When I enter an invalid complete number
     Then I see no data indicating that the number is invalid
     Then I switch to the Member tab
     Then I see no data indicating that the number is invalid
     Then I click back button to return to the previous page