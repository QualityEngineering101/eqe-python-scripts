Feature: Log in and out of the <site> with <credentials>

Scenario Outline: Successful login and logout
  Given the browser is open
  And the user navigates to the <site>
  When the user enters <username> into the username field
  And the user enters <password> into the password field
  And the user clicks the login button
  Then the user should see the Dashboard page
  When the user logs out
  Then the user should see the login form

  Examples: Login Credentials
    |site        | username | password |
    |https://opensource-demo.orangehrmlive.com/web/index.php/auth/login| Admin | admin123 |

