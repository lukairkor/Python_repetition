#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:34:15 2022
- LIFO
- push(), pop(), peek(), isEmpty(), isFull(), size()
@author: lukas
"""

from collections import deque
queue = deque()

queue.appendleft("a")
queue.appendleft("b")
queue.appendleft("c")
queue.appendleft("d")
print(queue,"\n")

queue.popleft()
queue.popleft()
print(queue)
