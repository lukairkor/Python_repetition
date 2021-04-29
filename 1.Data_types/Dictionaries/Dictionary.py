#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 02:56:14 2021
-Iterowanie po słowniku
@author: lukas
"""
# Iterowanie po słowniku
my_dict = {1 : "Ala", 2 : "Ola", 3 : "Kasia", 4 : "Basia"}

for key, val in my_dict.items():
    print("{} have value {}".format(key, val))
# metoda get
x = my_dict.get(1,"") 
print(x)