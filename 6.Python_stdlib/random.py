#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:59:29 2021

@author: lukas
"""
import random
import matplotlib.pyplot as plt

ra = random.randint(0,5)
print(ra)

list_ = [1, "a", 44, "b"]
ra = random.choice(list_)
print(ra)

print(random.random())

# gouss
print(random.gauss(100, 50))

ran = []
for i in range(10000):
    c = random.gauss(100, 50)
    ran.append(c)
    
plt.hist(ran, bins = 200) 
plt.show()