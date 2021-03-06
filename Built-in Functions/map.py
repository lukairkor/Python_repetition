# -*- coding: utf-8 -*-
"""
- they facilitate functional programming
- performing action on evry item in iterable
- more memory efficient then comprehension because 
do not store all values at once 
"""
liczby = [1, 2, 3, 4, 5]

def suma(skladnik):
    return skladnik + skladnik

wynik1 = map(suma, liczby)
# convert to other colection
wynik = list(map(suma, liczby))

# its iterable we can unpack it
print(*wynik1, sep=", ")
print(wynik)