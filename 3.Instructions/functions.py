#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 00:20:13 2021
- calculate payment
@author: lukas
"""

def calcul_paym(hour, rate):
    """calculculate employee wages"""
    if hour.isnumeric() and rate.isnumeric():

        hour = float(hour)
        rate = float(rate)
        czt = float(40)
        if hour <= czt:
            return hour * rate

        naddatek = hour - czt
        naddatek *= 1.5
        naddatek *= rate
        sum_1 = czt * rate
        sum_2 = sum_1 + naddatek
        return sum_2

    return "ERROR: Please enter valid numbers for hours and rate."


if __name__ == "__main__":
    hrs = input("Enter Hours:")
    rat = input("Enter Rate:")

    print(calcul_paym(hrs, rat))
