Feature: Appointment System Functionality
  In order to allow users to successfully book services
  As a user
  I want to view, make, cancel, and modify my appointment times

  @Manual_Test @branch_list_page @Guest
  Scenario: Guest user views branch list page
    Given the user is not logged in
    When the user visits the branch list page
    Then show all clickable branch list items

  @Manual_Test @branch_list_page @Guest
  Scenario: User clicks login on the Branch List Page and logs in successfully
    Given the user is not logged in
    And the user is on the Branch List Page
    When the user clicks the "Login" button
    And enters correct username and password
    Then the system should log the user in successfully
    And return to the original Branch List Page
    And the "Login" button should be replaced with the user's avatar)

  @Manual_Test @branch_list_page @branch_online_booking_page @Guest
  Scenario: Guest user clicks on a branch to enter the Branch Online Booking Page
    Given the user is not logged in
    And the user is on the Branch List Page
    When the user clicks on one of the branches
    Then the system should navigate to the Branch Online Booking Page for that branch
    And display the branch's details and booking notes

  @Manual_Test @branch_online_booking_page @Guest
  Scenario: Guest user clicks "Start Booking" and enters the Booking Process Page
    Given the user is not logged in
    And the user is on the Branch Online Booking Page
    When the user clicks the "Start Booking" button
    Then the system should navigate to the Booking Process Page for that branch

  @Manual_Test @branch_online_booking_page @Guest
  Scenario: User clicks login on the Branch Online Booking Page and logs in successfully
    Given the user is not logged in
    And the user is on the Branch Online Booking Page
    When the user clicks the "Login" button
    And enters the correct username and password
    Then the system should log the user in successfully
    And return the user to the same Branch Online Booking Page
    And the "Login" button should be replaced with the user's avatar

  @Manual_Test @branch_online_booking_page @branch_list_page @Guest
  Scenario: Guest user clicks switch button on Branch Online Booking Page to return to Branch List Page
    Given the user is not logged in
    And the user is on the Branch Online Booking Page
    When the user clicks the switch button
    Then the system should navigate back to the Branch List Page
    And the user should be able to click on other branches

  @Manual_Test @branch_list_page @LoggedIn
  Scenario: Logged-in user views branch list page
    Given the user is logged in
    When the user visits the branch list page
    Then show all clickable branch list items
    And display the user's avatar instead of the "Login" button

  @Manual_Test @branch_list_page @branch_online_booking_page @LoggedIn
  Scenario: Logged-in user clicks on a branch to enter the Branch Online Booking Page
    Given the user is logged in
    And the user is on the Branch List Page
    When the user clicks on one of the branches
    Then the system should navigate to the Branch Online Booking Page for that branch
    And display the branch's details and booking notes

  @Manual_Test @branch_online_booking_page @LoggedIn
  Scenario: Logged-in user clicks "Start Booking" and enters the Booking Process Page
    Given the user is logged in
    And the user is on the Branch Online Booking Page
    When the user clicks the "Start Booking" button
    Then the system should navigate to the Booking Process Page for that branch

  @Manual_Test @branch_online_booking_page @branch_list_page @LoggedIn
  Scenario: Logged-in user clicks switch button on Branch Online Booking Page to return to Branch List Page
    Given the user is logged in
    And the user is on the Branch Online Booking Page
    When the user clicks the switch button
    Then the system should navigate back to the Branch List Page
    And the user should be able to click on other branches

