#!/bin/bash

import datetime
now = datetime.datetime.now()

def display_current_datetime():
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")

    print("Current Date and Time: ", current_date)


def calculate_future_date():
    display_current_datetime()
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = now + datetime.timedelta(days=days_to_add)

    print("Future Date: ", future_date.strftime("%Y-%m-%d"))

calculate_future_date()
