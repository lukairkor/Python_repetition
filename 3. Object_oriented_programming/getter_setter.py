#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:43:31 2021

@author: lukas
"""

class Fruits:
    def __init__(self, amount = 0):
        self.amount = amount
            
    # we treat it like  property not function anymore
    # we can only read this property
    @property
    def show_amount(self):
        print("getting value ..")
        return self.amount

    # show data
    @show_amount.getter
    def show_amount(self):
        return "I have " + str(self.amount) + " fruits"
     
    # add data
    @show_amount.setter
    def show_amount(self, value):
        print("Adding some fruits to our basket ..")
        self.amount += value
        
    
obj = Fruits(5)
print(obj.show_amount)
# set value
obj.show_amount = 5
# show value
print(obj.show_amount)

# print(obj.add_fruit())