#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:23:41 2021

@author: lukas
"""
import re

##
a = ('aktualne.txt')
fhandle = open(a)
lista = list()
for line in fhandle:
    line = line.rstrip()
    print(line)
    pattern = re.findall(r'[0-9]+',line)
    lista = lista + pattern

print(lista)

##
a = ('aktualne.txt')
fhandle = open(a)
lista = list()

print(sum(map(int,re.findall('[0-9]+',fhandle.read())))) 


