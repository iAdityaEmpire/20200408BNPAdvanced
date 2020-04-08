#!/usr/bin/env python
import bnp

X = 100  # global variable

def main():
    spam()
    print("main: x is", X)
    b = alpha()
    b()

def spam():
    y = 42   # local variable
    x = "abc"  # ALSO local variable
    # g = globals()
    print("spam(): local x is", x)
    # print("spam(): global x is", g['x'])

def alpha():
    z = 3333   # nonlocal variables (from beta()'s POV)
    print("animal is", bnp.ANIMAL)
    print("alpha(): x is", X)

    def beta():
        print("in beta(): z is", z)

    return beta

def _toast():  #  "private"
    print("Toasty....")

print("my name is", __name__)

# levels of scope:
#  local -> nonlocal -> global -> builtin

if __name__ == '__main__': # if this file run as script, but not imported
    main()
