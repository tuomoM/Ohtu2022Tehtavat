*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command
*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kalle  kulle123
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  kake  kalle123
    Output Should Contain  Invalid username or password
