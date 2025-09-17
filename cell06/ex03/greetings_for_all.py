#!/usr/bin/env python

def greetings(name=None):
    if name is None:
        print("Hello, noble stranger.")
    elif isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")
greetings("Alexandra")
greetings("Will")
greetings()
greetings(42)