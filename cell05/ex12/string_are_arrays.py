#!/usr/bin/env python
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    s = "".join(args)
    zs = "".join([c for c in s if c == "z"])
    print(zs if zs else "none")
