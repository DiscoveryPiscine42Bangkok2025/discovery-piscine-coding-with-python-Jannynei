#!/usr/bin/env python
def main():
    msg = input("")
    for char in msg:
        if char.islower():
            print(char.upper(), end="")
        elif char.isupper():
            print(char.lower(), end="")
        else:
            print(char, end="")
main()