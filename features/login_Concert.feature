Feature: Login Concert
  Scenario: Verify title of concert web client
    Given Open Concert
    Then Login concert
    Then Verify title of concert
    And Close the browser