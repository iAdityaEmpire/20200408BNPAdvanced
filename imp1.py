#!/usr/bin/env python
import sys
# from pkg.pkg import module
from bnp.risk import scopex

print(scopex.X)  # global var in scopex.py

scopex.spam()   # functions in scopex.py
scopex.alpha()

# searching for modules:
# 1. current folder
# 2. folders in environment variable PYTHONPATH  if it exists
#      Windows:   DIR1;DIR2;DIR3
#      Mac/Linux: DIR1:DIR2:DIR3
# 3. folders under sys.prefix

print(sys.prefix)
