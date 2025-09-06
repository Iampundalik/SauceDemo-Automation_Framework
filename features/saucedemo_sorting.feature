@sorting
Feature: Inventory Sorting

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"

  Scenario: Verify sorting by price low to high
    When I sort products by "lohi"
    Then the product prices should be in ascending order
