#!/usr/bin/env python
import sys
if len(sys.argv) < 2:
    print("none")
else:
    param = input("What was the parameter? ")
    print("Good job!" if param == sys.argv[1] else "Nope, sorry...")