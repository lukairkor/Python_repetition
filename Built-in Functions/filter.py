#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:48:04 2021

@author: lukas
"""

values = [1, 4, 3, 3, 77, 32, 11, 24]
greater_than = filter(lambda value: value > 12, values)
print(*greater_than)