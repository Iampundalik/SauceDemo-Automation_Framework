@logout @positive
Feature: Logout functionality

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"

Scenario: User can logout successfully
  When I logout from the application
  Then I should see the login page