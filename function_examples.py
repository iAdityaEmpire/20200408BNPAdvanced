#!/usr/bin/env python

def doit(a, b=10):
    return a + b


result = doit(5, 37)
print(result)

result = doit('big', 'deal')
print(result)

print(doit(5))
print()

def spam(p1, p2, *p3, p4, p5, **p6):
    print(p1, p2)
    print(p3)
    print(p4, p5)
    print(p6)


spam(5, 10, 15, 20, 25, p4=30, p5=35, p6="wombat", color="blue", file_name="foo.txt")
print()


def  ham(*, folder, file_name):
    print(folder, file_name)

ham(folder="DATA", file_name="mary.txt")
ham(file_name="mary.txt", folder="DATA")

def toast(file_name, *, access_mode="r", max_lines=100, start_line=1):
    pass

toast('foo.txt')
toast('foo.txt', start_line=10)

toast("bar.txt", start_line=10, access_mode="w", max_lines=25)





