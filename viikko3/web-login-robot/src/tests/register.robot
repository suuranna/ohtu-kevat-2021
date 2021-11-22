** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  maisa
    Set Password  maisa123
    Set Password Confirmation  maisa123
    Submit Credentials
    Register Should Succeed

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password2}
    Input Password  password  ${password2}


