Feature: Home Page Visitor Experience
  As a visitor, I want to view and interact with the home page, So that I can understand what the site offers before logging in.

  Background:
    Given I am on the home page

  Scenario: Visitor should see the login form
    Then I should see the login form with fields
    And I should see a Login button
    And I should see a "Forgot your password?" link

  Scenario: Visitor should see the company branding and header elements
    Then I should see the "OrangeHRM" logo
    And I should see the application title

  Scenario: Visitor should see social media links
    Then I should see OrangeHRM social media links
    And The links should include LinkedIn, Facebook, Twitter, and YouTube

  Scenario: Visitor should see an error when trying to log in with empty credentials
    When I do not enter a username
    And I do not enter a password
    And I click the Login button
    Then I should see Password is Required 
    And I should see Username is Required

  Scenario: Visitor should see an error when trying to log in without entering a username
    When I enter a valid password
    And I do not enter a username
    And I click the Login button
    Then I should see Username is Required
    And I should not see Password is Required

  Scenario: Visitor should see an error when trying to log in without entering a password
    When I enter a valid username
    And I do not enter a password
    And I click the Login button
    Then I should see Password is Required
    And I should not see Username is Required

  Scenario: Visitor should see an error when entering invalid credentials
    When I enter an invalid username
    And I enter a valid password
    And I click the Login button
    Then I should see an invalid credentials error message
  
  Scenario: Visitor should see an error when entering invalid credentials
    When I enter a valid username
    And I enter an invalid password
    And I click the Login button
    Then I should see an invalid credentials error message

  Scenario: Visitor should be able to navigate to the password recovery page
    When I click on the "Forgot your password?" link
    Then I should be taken to the password recovery page

    
  