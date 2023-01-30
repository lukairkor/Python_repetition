#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:54:17 2023

@author: lukas
"""
from collections import deque
queue = deque()

queue.appendleft("a")
queue.appendleft("b")
queue.appendleft("c")
queue.appendleft("d")
print(queue, "\n")

queue.popleft()
queue.popleft()
print(queue)
