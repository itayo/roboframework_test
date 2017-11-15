*** Settings ***
Library    funniest.testa  stefan  123456  1000
Library    funniest.testb  Mats  123457  1000

*** Test Cases ***
My Test
    
    Balance Account A
    Balance Account B
    Withdraw from account A  1000
    Withdraw from account A  1000
    Deposit to account B  	1000
    Deposit to account B  	1000
    Balance Account A
    Balance Account B
    Withdraw from account B  1000
    Deposit to account A  	1000
    Balance Account A
    Balance Account B
