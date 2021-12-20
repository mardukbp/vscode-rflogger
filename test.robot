*** Settings ***
Library    RFLogger.py

*** Keywords ***
Say Hello
    Log    Hallo ⊚

*** Test Cases ***
First Test
    Say Hello
    Fail
