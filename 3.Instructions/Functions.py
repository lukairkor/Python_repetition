#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 00:20:13 2021
- count payment
@author: lukas
"""
def computepay(h, r):

    h = float(h)
    r = float(r)
    czt = float(40)
    if h <= czt:
        return h * r
    elif h > czt:
        naddatek = h - czt
        naddatek *= 1.5
        naddatek *= r
        sum1 = czt * r
        sum2 = sum1 + naddatek
        return sum2
    else:
        print("ERROR")

hrs = input("Enter Hours:")
rat = input("Enter Rate:")

p = computepay(hrs,rat)
print(p)


