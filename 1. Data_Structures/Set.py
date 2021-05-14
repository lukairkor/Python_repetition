# -*- coding: utf-8 -*-
"""
-like list but cant contain duplicate values
-chceckin if we have duplicate in list with this data structure
"""

sett = {1, "a", 2, 2, 4}

print(type(sett))
print(sett,"\n")

### adding items to sets:
x = set()
x.add("zaba")
print(x)
x.update(["krowa", "slon"])
print(x)

### deleting from set:
# delete specific one
x.remove("krowa")
print(x)
# delete any
y = x.pop()
print(x, " removed: ", y,"\n")

### set operations:
set1 = {1, 2, 3, 4}
set2 = {1, 5, 6, 7, "b"}
set_union = set1.union(set2)
print(set_union)
set_intersection = set1.intersection(set2)
print(set_intersection)
set_difference = set1.difference(set2)
print(set_difference)
set_difference = set1.symmetric_difference(set2)
print(set_difference)  
print(1 in set1)      
print(12 in set1)