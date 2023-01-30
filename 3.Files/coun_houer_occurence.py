#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- counts the occurance of different houers and show this in console
"""

# if len(a) < 1 : a = "mbox-short.txt"
FNAME = ('mbox-short.txt')

counts = {}

with open(FNAME, encoding='UTF-8') as file:
    for line in file:
        if not line.startswith('From '):
            continue
        words = line.split()  # lista podzielonych zdan
        words = words[5:6]  # mamy godziny
        # words=str(words)
        words = words.pop()  # zwraca pierwszy element
        #bez formy listy
        words = words.split(':')
        words = words[0:1]  # tworzy liste
        # words = words.pop() z tym zle
        for word in words:  # zapisuje do slownika
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

lst = list(counts.keys())  # tworzenie listy kluczy
lst.sort()  # sortujemy po kluczach

for key in lst:  # key to indeks od 0
    print(key, counts[key])
