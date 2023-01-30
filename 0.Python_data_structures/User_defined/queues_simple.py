#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:55:26 2023

@author: lukas
"""

from collections import deque
queue = deque()

queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
print(queue,"\n")

queue.popleft()
queue.popleft()
print(queue)
