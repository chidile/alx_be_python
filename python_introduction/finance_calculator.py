#!/bin/bash

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

# Calculating the Annual Savings
projected_annual_savings = (monthly_savings*12 + (monthly_savings *12 *0.05))

# The output
print("Your monthly savings are ", monthly_savings)
print("Projected savings after one year, with interest, is", projected_annual_savings)

