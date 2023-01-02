#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:45:23 2022

@author: lukas
"""

# def surname(fun):
#     fun()
   
# def name():
#     print("hello")
 
# name  = surname(name)

def sum(a,b):
    print(a+b)
    
def name(fun):
    fun()
    print("my name is Tom")

def surname(fun):
    fun()
    def wrap():
        print("What's u name")
    return wrap
    
@sum("arg1", "arg2")  
@name
@surname
def what(*args):
   "hello"
   for arg in args:
       print(arg)


print(what(1, 2))    
 

