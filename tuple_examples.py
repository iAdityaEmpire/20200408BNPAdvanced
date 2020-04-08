#!/usr/bin/env python
from collections import namedtuple

lat_lon = 43.233, 87.893

person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(lat_lon[0], lat_lon[1])

print(person[-1])

Person = namedtuple("Person", "first_name last_name product dob")

p1 = Person("Bill", "Gates", "Microsoft", "1955-10-28")
print(p1.first_name, p1.last_name)

p2 = Person("Steve", "Jobs", "Apple", "1955-02-24")
print(p2.first_name, p2.last_name)

for person in p1, p2:
    print(person.last_name, person.dob)
print()

first_name, last_name, product, dob = person   # unpack an iterable

print(first_name, last_name, '\n')

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

for first_name, last_name, product, dob in people:
    print(first_name, last_name, dob)
print()

first_name, last_name, product, dob = people[0]

