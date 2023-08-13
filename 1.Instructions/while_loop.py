#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 00:20:13 2021
- check the smallest and biggest number in list
@author: lukas
"""

lista = []


def biggest(lis):
    """return the biggest number"""
    largest = None
    for num in lis:

        if largest is None or num > largest:
            largest = num
    return largest


def notbiggest(lis):
    """return the smallest number"""
    smallest = None
    for num in lis:

        if smallest is None or num < smallest:
            smallest = num
    return smallest


def main():
    """populate the list with data"""
    print("Print \"d\" to finish,")
    while True:
        wpis = input("Enter a number: ")
        if wpis == 'd':
            break
        try:
            wpis = int(wpis)
            lista.append(wpis)
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
    larg_numb = biggest(lista)
    smal_numb = notbiggest(lista)

    print("Maximum is", larg_numb)
    print("Minimum is", smal_numb)
