@cart @positive
Feature: Cart and Checkout

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"

  @positive
  Scenario: Add first item and complete checkout
    When I add the first item to the cart
    And I proceed to checkout with "John" "Doe" "406091"
    Then I should see the order completion page

