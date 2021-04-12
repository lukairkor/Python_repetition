# -*- coding: utf-8 -*-
"""
-allow us to combine 2 lists
-improves readability of for loops
"""

list_1 = ["a", "b", "c", "d", "e"]
list_2 = [1, 2, 3, 4, 5]
list_3 = [11, 22, 33, 44, 55]

x = zip(list_1, list_2, list_3)

# print(x)

# for i, j, k in x:
#     print(i, j, k)
    
##########unzip
print(x)
unziped_object = zip(*x)
print(unziped_object)
unziped_list = list(unziped_object)
print(unziped_list)


####### zip how use properly
lista_1 = [1, 2, 3, 4]
lista_2 = ["Ala", "Ola", "Kasia", "Basia"]

for x, y in zip(lista_1, lista_2):
    print(x, y)