#!/usr/bin/env python
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    for s in args:
        print(s.lower())