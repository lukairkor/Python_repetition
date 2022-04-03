#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:26:23 2021

@author: lukas
"""
import math

class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2 + y**2)
        
    # klasa sumuje sama siebie
    def __add__(self, sec_):
        return Punkt2D(self.x + sec_.x, self.y + sec_.y)
        
    def __lt__(self, sec_):
        return self.distance < sec_.distance
        
    def __len__(self):
        return int(round(self.distance, 0))
    
    
p1 = Punkt2D(2, 5)
p2 = Punkt2D(4, 5)
p3 = p1 + p2

print(p3.x) # 6
print(p3.y) # 10

print(p1 < p2) # True
print(p1 > p2) # False
print(p1 == p1) # True


print(len(p3)) # using function len 12
print(p3.distance) # 11.661