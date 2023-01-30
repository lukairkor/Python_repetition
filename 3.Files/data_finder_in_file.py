#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- find emails adress in text and there amount
"""

# fname = input("Enter file name: ")
FNAME = "mbox-short.txt"

# fname = input(fname)
counter = 0

with open(FNAME, encoding='UTF-8') as file:
    for line in file:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        words = line.split()
        print(words[1])
        counter += 1

print(f"There were, {counter}, lines in the file with From as the first word")
