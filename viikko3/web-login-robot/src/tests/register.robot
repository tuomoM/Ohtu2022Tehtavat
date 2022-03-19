
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Start testing

*** Test Cases *** 
Register With Valid Username And Password
    Set Username  Urho777
    Set Password  Urkki747
    Set Confirmation password  Urkki747
    Submit Registration
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  U
    Set Password  Urkki747
    Set Confirmation password  Urkki747
    Submit Registration
    Register Page Should Be Open
# ...

Register With Valid Username And Too Short Password
    Set Username  Urho777
    Set Password  Ur
    Set Confirmation password  Ur
    Submit Registration
    Register Page Should Be Open

Register With Nonmatching Password And Password Confirmation
    Set Username  Urho777
    Set Password  Urkki747
    Set Confirmation password  Urkki7477
    Submit Registration
    Register Page Should Be Open

Login After Successful Registration
    Set Username  Urho7777
    Set Password  Urkki747
    Set Confirmation password  Urkki747
    Submit Registration
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  Urho7777
    Set Password  Urkki747
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  Urho7776
    Set Password  Urkki747
    Set Confirmation password  Urkki7477
    Submit Registration
    Click Link  Login
    Set Username  Urho7776
    Set Password  Urkki747
    Submit Login
    Login Should Fail With Message  Invalid username or password
*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Login
    Click Button  Login

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}
Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
Set Confirmation password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
Start testing
    Go To Register Page
    
