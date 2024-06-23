""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from bank import BankManager

def __main__():
    bank = BankManager()
    add_bank_ui(bank)


def add_bank_ui(bank):
    name = input("Please enter the name of your new account: ")
    password = input("Please set a password: ")
    bank.add_account(name, password)

__main__()