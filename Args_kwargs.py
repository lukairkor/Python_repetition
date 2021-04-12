#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sending non-keyword
def test(f_arg, *argv):
    print("first arg", f_arg)
    for arg in argv:
        print("other arguments:", arg)

test('1', '2', '3', '4')


###################################

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
        
greet_me(name="yasoob")

###################3
# def funkcja(*args):
#     suma = 0
#     for x in args:
#         suma+=x
#     return suma

# # tupla = [1, 2, 3, 4, 5] 

# print(funkcja(1,2,3,4,5))
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))