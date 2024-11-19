*** Settings ***
Resource  resource.robot
Test Setup  Create User And Something

*** Test Cases ***
Register With Valid Username And Password
    Input New User    niko    niko1234
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input New User    kalle   kalle1234
    Output Should Contain    User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New User    ni    niko1234
    Output Should Contain    Invalid username


Register With Enough Long But Invalid Username And Valid Password
    Input New User    niko1234    niko1234
    Output Should Contain    Invalid username

Register With Valid Username And Too Short Password
    Input New User    pena    niko12
    Output Should Contain    Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New User    pena    nikoniko
    Output Should Contain    Invalid password


*** Keywords ***
Create User And Something
    Create User  kalle    kalle1234
    Input New Command