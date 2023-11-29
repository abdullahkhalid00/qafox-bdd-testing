Feature: User registration

  Background:
    Given the user is on the registration page

  @register
  Scenario Outline: Registering with valid data
    When the user enters the firstname as '<firstname>'
    And the user enters the lastname as '<lastname>'
    And the user enters the email
    And the user enters the telephone number as '<telephonenumber>'
    And the user enters the password as '<password>'
    And the user checks the privacy policy option
    And the user clicks on the continue button
    Then the user is registered
    Examples:
      | firstname | lastname | telephonenumber | password |
      | ABC       | XYZ      | 12345           | ABCXYZ   |

  @register
  Scenario Outline: Registering with invalid data
    When the user enters the firstname as '<firstname>'
    And the user enters the lastname as '<lastname>'
    And the user enters the telephone number as '<telephonenumber>'
    And the user enters the registration email as '<email>'
    And the user enters the registration password as '<password>'
    And the user checks the privacy policy option
    And the user clicks on the continue button
    Then a '<warningmessage>' is displayed
    Examples:
      | firstname | lastname | telephonenumber | email       | password | warningmessage                                  |
      | ABC       | XYZ      | 12345           | y2k@y2k.com | ABCXYZ   | Warning: E-Mail Address is already registered!  |
      |           |          | 1               |             |          | Telephone must be between 3 and 32 characters!  |
      |           |          |                 |             | ABC      | Password must be between 4 and 20 characters!   |

  @register
  Scenario: Registering without entering any data
    When the user leaves every field blank
    And the user clicks on the continue button
    Then a proper warning message for each field is displayed