#!/usr/bin/env python
first_number = int(input("Enter the first number: \n" ))
second_number= int(input("Enter the second number: \n"))
print(f"{first_number} x {second_number} = {first_number * second_number}")
if (first_number * second_number) > 0 :
    print("The result is positve.")
elif (first_number * second_number) < 0 :
    print("The result is negative.")
else :
    print("The result is positive and negative.")