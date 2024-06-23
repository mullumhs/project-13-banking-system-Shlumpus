""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from account import Account

class BankManager():
    def __init__(self):
        self.accounts = []
        
    def add_account(self, name, password, balance=0):
        new_account = Account(name, password, balance)
        self.accounts.append(new_account)
        
    def remove_account(self, target):
        for i in self.accounts():
            if i == target:
                self.accounts.remove(target)
            else:
                print("That account doesn't exist")
                
    def acc_check(self, number):
        for i in self.accounts():
            if i == self.accounts(number):
                return True
        return None
                
        
    def display_accounts(self):
        for account in self.accounts:
            print(account)
        
    def deposit(self, number, deposit_amount):
        print()
        
    def withdraw(self, number, withdraw_amount):
        existing_account = self.acc_check(number)
        if existing_account is not None:
            existing_account.withdraw(withdraw_amount)
            return True
        print("Unable to locate account")
        return False
        
    def transfer(self, account1, account2, transfer_amount):
        existing_account = self.acc_check(account1)
        existing_account2 = self.acc_check(account2)
        if existing_account is not None and existing_account2 is not None:
            try:
                existing_account.withdraw(account1, transfer_amount)
                existing_account.deposit(account2, transfer_amount)
            except ValueError as e:
                print(e)
    
        