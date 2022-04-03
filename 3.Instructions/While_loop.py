#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 00:20:13 2021
-
@author: lukas
"""
lista = []

#
def biggest(l):
    largest = None
    for n in l:
        
        if largest is None or n > largest:
            largest = n
    return largest
 
   
#
def notbiggest(l):
    smallest = None
    for n in l:
           
        if smallest is None or n < smallest:
            smallest = n
    return smallest

    
#
while True:
    wpis = input("Enter a number: ")
    if wpis == 'done' : 
        break
    else: 
        try:
            wpis = int(wpis)
            lista.append(wpis)
        except:
            print("Invalid input")
            continue
        
largest = biggest(lista)
smallest = notbiggest(lista)

# odczyt = len(lista)
# for i in range(odczyt):
#     koniec = lista[i]
#     print(koniec," ")
    
print("Maximum is", largest)
print("Minimum is", smallest)


