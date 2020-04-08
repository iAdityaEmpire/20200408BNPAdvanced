#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fgen = (f.upper() for f in fruits)

print(fgen)

fruits.append("marionberry")

for fruit in fgen:
    print(fruit)
print()

def colors():
    yield "blue"
    yield "red"
    yield "purple"
    yield "mauve"
    yield "aqua"

c = colors()
print(c)

for color in c:
    print(color)
print()

def trimmed(file_name):
    with open(file_name) as file_in:
        for raw_line in file_in:
            yield raw_line.rstrip()  # trim off \n


mary = trimmed("DATA/mary.txt")

for line in mary:
    print(line)
print()





