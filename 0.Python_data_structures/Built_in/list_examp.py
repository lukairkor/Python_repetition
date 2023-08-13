#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- primary operations on list
"""


def unp_lis():
    """unpacked list"""
    a_1, b_2, c_3, d_4 = name_list
    print(a_1, b_2, c_3, d_4, "\n")


def rev_list():
    """reversed list"""
    new_list = name_list.copy()
    new_list.reverse()
    print(new_list, "\n")


def pop_list():
    """pop elem out of a list"""
    new_list = name_list.copy()
    show = new_list.pop(0)
    print(show, "\n")


def ins_list():
    """insert elem into list"""
    new_list = name_list.copy()
    new_list.insert(0, '2')
    print(new_list, "\n")


def coun_list():
    """count the amount of spec elemen"""
    new_list = name_list.copy()
    show = new_list.count("Ala")
    print(show, "\n")


def ext_list():
    """extending our list"""
    new_list = name_list.copy()
    new_list.extend([1, 2, 3, 4, 5])
    print(new_list, "\n)")


if __name__ == "__main__":
    # our list
    name_list = ["Ala", "Ola", "Kasia", "Basia"]
    print(name_list, "\n")
    unp_lis()
    rev_list()
    pop_list()
    ins_list()
    ins_list()
    ext_list()
