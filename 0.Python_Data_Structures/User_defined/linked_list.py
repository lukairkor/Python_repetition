#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:20:09 2022
- first node of list is called Head
- last is caled Tail points to Null
- nodes contain data and pointer to next or previous node
- linear data struct
@author: lukas
"""

from collections import deque

dq = deque([1, 2, 3, 4, 5, 6])

print(dq)

dq.appendleft(0)
print(dq)

dq.popleft()
print(dq)
