""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account:
    def __init__(self, name, balance, password):
        self._name = name
        self._balance = balance
        self._password = password
        
    def get_account_number(self, number):
        return self._number
        
    def get_account_name(self, name):
        return self._name  
    
    def get_account_password(self, password):
        return self._password
        
    def get_balance(self, balance):
        return self._balance    
        
    def change_password(self, password, new_password):
        password = new_password
        
    def deposit(self, addition):
        self._get_balance()
        self._balance += addition
        
    def withdraw(self, balance, subtraction):
        if subtraction < balance:
            self._get_balance()
            self._balance -= subtraction
        else:
            print("You have insufficient funds, withdrawal failed")
        
