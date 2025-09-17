#!/usr/bin/env python
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for a in args:
        print(f"{a}: {len(a)}")