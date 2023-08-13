#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- like list but can't contain duplicate values
- checking if your set contains duplicates
"""


def typ_fun():
    """type function"""
    print("check type of structure:")
    print(type(set_org))


def add_item():
    """adding items to sets"""
    print("adding items to sets:", "\n")
    set_2 = set()
    set_2.add("zaba")
    print(set_2)
    set_2.update(["krowa", "slon"])
    print(set_2, "\n")
    return set_2


def del_item():
    """deleting from a set"""
    set_2 = add_item()
    print("deleting from set:", "\n")
    # delete specific one
    set_2.remove("krowa")
    print(set_2)
    set_2.add("krowa")
    # delete last one
    pop_las = set_2.pop()
    print(set_2, " removed: ", pop_las, "\n")


def oper_set():
    """set operations"""
    print("set operations:", "\n")
    set1 = {1, 2, 3, 4}
    set2 = {1, 5, 6, 7, "b"}
    print(f"our first set: {set1}, our second set: {set2}\n")

    set_union = set1.union(set2)
    print(set_union, "set union")

    set_intersection = set1.intersection(set2)
    print(set_intersection, "set intersection\n")

    set_difference = set1.difference(set2)
    print(set_difference, "set difference\n")

    set_difference = set1.symmetric_difference(set2)
    print(set_difference, "symmetric difference\n")

    print("boolean operation")
    print(1 in set1)
    print(12 in set1)


if __name__ == "__main__":
    set_org = {1, "a", 2, 2, 4}
    print(set_org, "\n")
    typ_fun()
    add_item()
    del_item()
    oper_set()
