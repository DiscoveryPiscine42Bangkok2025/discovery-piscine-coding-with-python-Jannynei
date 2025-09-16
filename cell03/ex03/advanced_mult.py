#!/usr/bin/env python
def main():
    for a in range(0, 11):
        print(f"Table de {a}:", end=" ")
        for b in range(0, 11):
            result = a * b
            print(f"{result}", end=" ")
        print()

main()