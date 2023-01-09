#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:49:26 2022
- a little like dictionaries but faster
- hash function compute a index value that store searched element
- are indexed data structure
- SHA
@author: lukas
"""

text = "Hello everybody"
tup = (0, 2, 4, 6, 7)
func = hash(text)
func_ = hash(tup)
print(func, '\n', func_)