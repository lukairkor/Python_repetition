#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:30:52 2022
- FIFO
- enqueue(), dequeue(), front(), rear(), empty()
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
