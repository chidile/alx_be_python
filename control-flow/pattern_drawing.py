#!/bin/bash

pattern_size = int(input("Enter the size of the pattern: "))

# Draw the pattern using for loop
count = 0
while count < pattern_size:
    for i in range(pattern_size):
        print("*", end="")
        
    print()
    count += 1
      

