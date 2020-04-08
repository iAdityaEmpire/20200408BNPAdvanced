#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

# [EXPR for VAR in ITERABLE ... if CONDITION ...]
f1 = tuple([f.upper() for f in fruits])
print("f1: {}\n".format(f1))

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = 'Clubs Diamonds Hearts Spades'.split()

cards = [f"{r}-{s}" for s in suits for r in ranks]
print("cards: {}\n".format(cards))

short_fruits = [f for f in fruits if len(f) < 6]
print("short_fruits: {}\n".format(short_fruits))

short_fruits = [f.title() for f in fruits if len(f) < 6]
print("short_fruits: {}\n".format(short_fruits))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[3] for p in people]
print("dobs: {}\n".format(dobs))


colors = ["Blue", "red", "RED", 'green', 'RED', 'Red', 'blue', 'GREEN', 'orange', 'ORANGE']
c1 = set(colors)
print("c1: {}\n".format(c1))
#    {EXPR for VAR in ITERABLE if CONDITION}
c2 = {c.lower() for c in colors if c.lower() != 'orange'}
print("c2: {}\n".format(c2))

#               {KEY:VALUE for VAR in ITERABLE if CONDITION}
fruit_lengths = {f:len(f) for f in fruits}
print("fruit_lengths: {}\n".format(fruit_lengths))

person_info = {f"{p[0]} {p[1]}":f"{p[3]}" for p in people}
print("person_info: {}\n".format(person_info))

