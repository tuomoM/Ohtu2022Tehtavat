*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command
*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
 #   Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  paavo  pesusieni1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain   User with username already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  oa  password2
    Output Should Contain   Too short username

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  urpo  pa2
    Output Should Contain   Too short password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  urpo  paavolainen
    Output Should Contain   Only alphabets
# ...