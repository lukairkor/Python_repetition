#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 02:56:14 2021
- iterating over dictionaryu
- key are unique (list can't be keys for example)
@author: lukas
"""

def it_ov_dic():
    """iterating over dictionary"""
    for key, val in my_dict.items():
        print(f"Key {key} has value {val}.")


def if_we_un_key_exi():
    """method get if we unsure if key exist"""
    ke_y = my_dict.get(1,"")
    print(ke_y,"\n")


def if_not_key():
    """If not key == 5 than give someting else give value"""
    print(my_dict.get(5,"Nothing like this"),"\n")


def dic_operations():
    """add item to a dictionary"""
    my_dict_1 = {}
    my_dict_1["1"] = 1000
    print(my_dict_1)
    my_dict_1.update(my_dict)
    print(my_dict_1)
    del my_dict_1 ["1" ]
    print(my_dict_1)


if __name__ == "__main__":
    # terating over this dictionary
    my_dict = {1 : "Ala", 2 : "Ola", 3 : "Kasia", 4 : "Basia"}

    it_ov_dic()
    if_we_un_key_exi()
    if_not_key()
    dic_operations()
