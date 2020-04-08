#!/usr/bin/env python

def spam(a, b, c):
    print(a)
    print(b)
    print(c)
    print("---")

spam(1, 2, 3)
spam("fee", "fi", "fo")

args = ["alpha", "beta", "gamma"]

spam(args[0], args[1], args[2])
spam(*args)

def config(**data):
    print(data)

config(folder="DATA", count=12, country="Bulgaria")

values = {"folder": "JUNK", "count": 42, "country": "Burkina Faso"}

config(**values)
