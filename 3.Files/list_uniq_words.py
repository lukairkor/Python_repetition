#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- list all unique words from file
"""

# fname = input("Enter file name: ")

FNAME = ('romeo.txt')

with open(FNAME, encoding='UTF-8') as file:
    file_read = file.read()
    lst = []
    for line in file_read.split():
        line_1 = line
        if line_1 in lst:
            continue
        lst.append(line_1)
lst.sort()
print(lst)
