# -*- coding: utf-8 -*-

# unpack list
list_0 = ["Ala", "Ola", "Kasia", "Basia"]

a, b, c, d = list_0

print(list_0)
print(a,"1\n")


list_1 = list_0.copy()
list_1.reverse()
print(list_1,"2\n" )

list_1 = list_0.copy()
show = list_1.pop(0)
print(show,"3\n")

list_1 = list_0.copy()
list_1.insert(0, '2')
print(list_1,"4\n")

list_1 = list_0.copy()
show = list_1.count("Ala")
print(show,"5\n")

list_1 = list_0.copy()
list_1.extend([1,2,3,4,5])
print(list_1,"6\n")