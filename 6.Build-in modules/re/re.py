#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:23:41 2021

@author: lukas
"""
import re

text = """Alice was beginning to get very tired of sitting by 
    her sister on the bank. So she was considering in her own mind 
    (as well as she could, for the hot day made her feel very sleepy and stupid),
    whether the pleasure"""

# find all matches
x = re.findall("was", text)
print(x, "\n")

# return match obiect, only first found
x = re.search("was", text)
print(x, "\n")
x = x.group()  # return part of str with match
print(x, "\n")

# split at each blank character
x = re.split("\s", text)
print(x, "\n")

# replece the matches
x = re.sub("\s", "X", text)
print(x, "\n")

#
tekst = 'We just received $10.00 for cookies.'
sciezka = r'[0-9a-zA-Z.].+'
dopasowanie = re.findall(sciezka, tekst)

print(dopasowanie)
