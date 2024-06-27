#!/bin/bash

task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time_bond = input("Is it time-bound? (yes/no) ")

match priority:
    case "high":
        if time_bond == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bond == "yes":
            print(f"{task} is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a meduim priority task. Consider completing it when you have free time.")
    case "low":
        if time_bond == "yes":
            print(f"{task} is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    

