# -*- coding: utf-8 -*-
"""
-we can iterate over generators only once the
-they reduce necessary amount of memory
"""

#example 1:###################################
             
# def generator():
#     for i in range(4):
#         yield i
        
# gen = generator()

# #example one: next()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#example 2:###################################
    
def generator(n):
    for i in range(n):
        yield i    

for i in generator(44):
    print(i)