# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 19:30:27 2018

@author: shurastogi
"""
class piggy():
    balance=0
    def __init__(self):
        print("---------------Start---------------")
        self.takeUserInput()

 #Method to take user action
    def takeUserInput(self):
        option=input("Start or End :")
        if option.lower()=='start':
            option2=input("Add , Withdraw or check :")
            if option2.lower()=='add':
                _add=float(input("Add Amount :"))
                self.addFunds(_add)
            elif option2.lower()=='withdraw':
                _withdraw=float(input("Withdraw Amount :"))
                self.withDrawFunds(_withdraw)
            elif option2.lower()=='check':
                    self.checkFunds()
            else:
                self.takeUserInput()
        elif option.lower()=='end':
            print("ending piggybank")
        else:
            self.takeUserInput()

 #Method to add fund,Takes amount to add
    def addFunds(self,amount_to_add):
        self.balance=self.balance+amount_to_add
        print("After adding,your updated balance is {} rupees".format(self.balance))
        self.takeUserInput()
 #Method to Take fund,Takes amount to withdraw
    def withDrawFunds(self,amount_to_withdraw):
        if(self.balance<amount_to_withdraw):
            print("InSufficient Balance to withdraw")
        else:
            self.balance=self.balance-amount_to_withdraw
            print("After Withdrawing,balance amount is {} rupees".format(self.balance))
            self.takeUserInput()
 #Method to check fund
    def checkFunds(self):
        print("Your current balance is {} rupees".format(self.balance))
        self.takeUserInput()
