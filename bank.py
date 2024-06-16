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
        
    def add_account(self, name, password):
        balance = '0'
        new_account = Account(name, balance, password)
        self.accounts.append(new_account)
        
    def remove_account(self, target):
        for i in self.accounts():
            if i == target:
                self.accounts.remove(target)
            else:
                print("That account doesn't exist")
                
    def acc_check(self, name):
        for i in self.accounts():
            if i == name:
            
                
        
    def display_accounts(self):
        print(self.accounts, sep='\n')
        
    def deposit(self, name, deposit_amount):
        print()
        
    def withdraw(self, name, withdraw_amount):
          
        
    def transfer(account1, account2, transfer_amount):
        
    
        