Feature: User login

  Background:
    Given the user is on the login page

  @login
  Scenario Outline: Logging in with valid data
    When the user enters the email as '<email>'
    And the user enters the password as '<password>'
    And the user clicks on the login button
    Then the user is logged in
    Examples:
      | email       | password  |
      | y2k@y2k.com | 1234      |

  @login
  Scenario Outline: Logging in with invalid data
    When the user enters the email as '<email>'
    And the user enters the password as '<password>'
    And the user clicks on the login button
    Then a '<warningmessage>' is displayed
    Examples:
      | email       | password | warningmessage                                        |
      | y2k@y2k.com |          | Warning: No match for E-Mail Address and/or Password. |
      |             | 1234     | Warning: No match for E-Mail Address and/or Password. |
      |             |          | Warning: No match for E-Mail Address and/or Password. |
