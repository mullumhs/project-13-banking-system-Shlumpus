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
        
    def remove_account(self):
        get_account_number(self)
        
        
    def display_accounts(self):
        print()