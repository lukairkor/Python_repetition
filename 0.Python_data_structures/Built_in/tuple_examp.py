#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 00:20:13 2021
- its series of comma separated data
- ordered collection
- immutable (no pop, append.)
- + work, but we create new tuple
@author: lukas
"""

# tuple examples
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (1,)

# list of tuples
names = [
    ("John",),
    ("Alex",),
    ("Micheal",),
    ("Mike", "Eve")
]

# print all names
print(names, "\n")
# print only ("Mike", "Eve")
print(names[3], "\n")
# print only Eve
print(names[3][1], "\n")
