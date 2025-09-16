#!/usr/bin/env python                   
def main():
    try:
        num = int(input("Enter a number less than 25\n"))

        if (num > 25):
            print("Error\n")
            return

        while num <= 25:
            print(f"Inside the loop, my variable is {num}")
            num += 1
    except:
        print("Error: invalid input.")

main()