#!/bin/bash

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            self.account_balance -= amount
            return False
        else:
            return True
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")