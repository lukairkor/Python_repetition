#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:46:02 2021
- comprehension list
@author: lukas
"""

# comprehension for filtering
values = [1, 4, 3, 3, 77, 32, 11, 24]
greater_than = [value for value in values if value > 12]
print(greater_than)
