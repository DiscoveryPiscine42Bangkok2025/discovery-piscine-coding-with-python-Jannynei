#!/usr/bin/env python
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    suffix = args[1][-3:] if len(args) > 1 else ""
    for w in args:
        if w != args[1]:
            print(w + suffix)