Feature: Searching for a product

  Background:
    Given the user is on the home page

  @search
  Scenario Outline: Searching for a valid product
    When the user enters a valid product as '<productname>'
    And the user clicks on the search button
    Then the valid product '<productname>' is displayed
    Examples:
      | productname             |
      | HP LP3065               |
      | Samsung Galaxy Tab 10.1 |
      | iPhone                  |

  @search
  Scenario: Searching for an invalid product
    When the user enters an invalid product
    And the user clicks on the search button
    Then a proper warning message is displayed

  @search
  Scenario: Searching without entering any product
    When the user leaves the search box blank
    And the user clicks on the search button
    Then a proper warning message is displayed