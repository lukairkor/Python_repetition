#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 8, 02:05:35 2021

@author: lukas
"""
import functools

myresult = [("1", "2", "3", "4")]
print(myresult)
# reduce(function, sequence)
myresult = functools.reduce(lambda sub, ele: sub + ele, myresult)
print(myresult)

# lambda remainder


def myresult(sub, ele): return sub + ele


print(myresult(2, 4))
