# -*- coding: utf-8 -*-
"""
- when you need function for short peroid of time
- pass function as a argument
"""
#111###########################
numbers = [1, 2, 3, 4, 5]
result = map(lambda number: number ** 2, numbers)

print(list(result))

#222###########################
def function(number):
    return lambda x : x + number

x = function(2)
print(x(6))
