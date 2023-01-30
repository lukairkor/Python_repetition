#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:49:26 2022
- a little like dictionaries but faster
- hash function compute a index value that store searched element
- are indexed data structure
- SHA
- non-linear
@author: lukas
"""

# keys  ->  hashing  ->  hash_table


class HashMap:
    """HashMaps"""

    def __init__(self):
        self.table = {}

    def set_val(self, key, value):
        """set new value"""
        key = self.__hash_fun(key)
        self.table[key] = value

    def get_val(self, key):
        """get value"""
        print(self.table[key])
        return self.table[key]

    def delete_value(self, key):
        """delete value"""
        del self.table[key]

    def __hash_fun(self, key):
        """privat hashing methode"""
        return hash(key)

    def show(self):
        """showing content of hashmap"""
        for i, (key, value) in enumerate(self.table.items()):
            print(f"number: {i}, key: {key}, value: {value}")


if __name__ == "__main__":
    has_map = HashMap()

    has_map.set_val(0, 1)
    has_map.set_val(1, 2)
    has_map.set_val(2, 3)

    has_map.get_val(1)

    has_map.show()

    has_map.delete_value(0)

    has_map.show()
