*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  ansku  ansku123
    Output Should Contain  New user registered 

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

