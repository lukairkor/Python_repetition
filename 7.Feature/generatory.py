# -*- coding: utf-8 -*-
"""
-we can iterate over generators only once
-they reduce the necessary amount of memory
"""


def generator_1():
    """generating"""
    for i in range(4):
        yield i


gen = generator_1()

# example one: next()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print("\n")


def generator_2(num):
    """generating"""
    for i in range(num):
        yield i


for j in generator_2(10):
    print(j)
