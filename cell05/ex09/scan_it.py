#!/usr/bin/env python
import sys
if len(sys.argv) <= 2:
    print("none")
else:
    print(sys.argv[2].count(sys.argv[1]))
