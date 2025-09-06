@cart @negative
Feature: Cart and Checkout

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"

  @negative
  Scenario: Checkout with all fields empty shows validation
    When I add the first item to the cart
    When I proceed to checkout with all fields blank
    Then I should see a checkout error containing "Error: First Name is required"
