Feature: Home Page Visitor Experience

  As a visitor, I want to view and interact with the home page, So that I can understand what the site offers before logging in.

  Background:
    Given I am on the home page

  Scenario: Visitor should see the login form
    Then I should see the login form containing fields for username and password
    And I should see a "Login" button
    And I should see a "Forgot your password?" link

  Scenario: Visitor should see the company branding and header elements
    Then I should see the "OrangeHRM" logo
    And I should see the application title

  Scenario: Visitor should see social media links
    Then I should see links to OrangeHRM's social media pages
    And The links should include LinkedIn, Facebook, and Twitter

  Scenario: Visitor should see an error when trying to log in with empty credentials
    When I click the "Login" button without entering any credentials
    Then I should see an error message prompting me to enter my username and password

  Scenario: Visitor should see an error when entering invalid credentials
    When I enter an invalid username and password
    And I click the "Login" button
    Then I should see an error message indicating that my login credentials are incorrect

  Scenario: Visitor should be able to navigate to the password recovery page
    When I click on the "Forgot your password?" link
    Then I should be taken to the password recovery page