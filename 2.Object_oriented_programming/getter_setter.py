#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:43:31 2021

@author: lukas
"""


class Fruits:
    """Fruit class"""

    def __init__(self, amount=0):
        self.amount = amount

    # we treat it like  property not function anymore
    # we can only read this property
    @property
    def show_amount(self):
        """getting data"""
        print("getting value ..")
        return self.amount

    @show_amount.getter
    def show_amount(self):
        """showing data"""
        return "I have " + str(self.amount) + " fruits"

    @show_amount.setter
    def show_amount(self, value):
        """adding data"""
        print("Adding some fruits to our basket ..")
        self.amount += value


if __name__ == "__main__":

    obj = Fruits(5)
    print(obj.show_amount)
    # set value
    obj.show_amount = 5
    # show value
    print(obj.show_amount)


# =============================================================================
# output
#
# I have 5 fruits
# Adding some fruits to our basket ..
# I have 10 fruits
# =============================================================================
