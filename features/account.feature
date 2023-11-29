Feature: Modifying user account information

    Background:
        Given the user is logged in

    @account
    Scenario Outline: Changing the user email to an email that already exists
        Given the user is on the my account page
        And the user clicks on 'Edit your account information option'
        And the user enters a new email as <email>
        When the user clicks on the email continue button
        Then an error message is displayed
        Examples:
            | email       |
            | y2k@y2k.com |
            | abc@abc.com |

    @account
    Scenario: Changing the user email
        Given the user is on the my account page
        And the user clicks on 'Edit your account information option'
        And the user enters a new email
        When the user clicks on the email continue button
        Then a proper message is displayed

    @account
    Scenario: Changing the user password
        Given the user is on the my account page
        And the user clicks on the 'Changing your password' option
        And the user enters a new password
        And the user confirms the new password
        When the user clicks on the password continue button
        Then a proper message is displayed
