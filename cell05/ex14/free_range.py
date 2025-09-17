#!/usr/bin/env python
import sys
args = sys.argv[1:]
if len(args) < 2:
    print("none")
else:
    start, end = map(int, args[:2])
    print(list(range(start, end + 1)))