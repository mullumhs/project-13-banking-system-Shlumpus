""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account:
    def __init__(self, name, password, balance):
        self._name = name
        self._balance = balance
        self._password = password
        
    def get_account_name(self, name):
        return self._name  
    
    def get_account_password(self, password):
        return self._password
        
    def get_balance(self, balance):
        return self._balance    
        
    def change_password(self, password, new_password):
        password = new_password
        
    def deposit(self, addition):
        self._balance += addition
        
    def withdraw(self, balance, subtraction):
        if subtraction < balance:
            self._balance -= subtraction
        else:
            raise ValueError(f"Unable to withdraw, your balance is below {subtraction}")
        
    def __str__(self):
        return f"{self._name}, \n {self._balance}"
            
        
