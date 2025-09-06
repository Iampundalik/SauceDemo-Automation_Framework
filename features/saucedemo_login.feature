@login @positive @negative
Feature: Login to SauceDemo

  Background:
    Given I am on the SauceDemo login page

  @positive
  Scenario: Valid login shows inventory
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the inventory page

  @negative
  Scenario Outline: Invalid login shows error
    When I login with username "<user>" and password "<pass>"
    Then I should see an error containing "<message>"

    Examples:
      | user            | pass          | message                         |
      | standard_user   | wrongpass     | Username and password do not    |
      | locked_out_user | secret_sauce  | Sorry, this user has been locked|
