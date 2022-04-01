#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 02:56:14 2021
-Iterowanie po słowniku
-key are unique (list cant be keys for example)
@author: lukas
"""
# iterating through dictionary
my_dict = {1 : "Ala", 2 : "Ola", 3 : "Kasia", 4 : "Basia"}

### iterating over dictionary
for key, val in my_dict.items():
    print("{} have value {}".format(key, val))
    
### metoda get if we unsure if key exist
x = my_dict.get(1,"") 
print(x,"\n")

### If not key == 5 than give someting else give value
print(my_dict.get(5,"Nothing like this"),"\n")

### add item to a dictionary
my_dict_1 = {}
my_dict_1["1"] = 1000
print(my_dict_1)
my_dict_1.update(my_dict)
print(my_dict_1)
del my_dict_1 ["1" ]
print(my_dict_1)