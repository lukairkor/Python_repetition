#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:13:50 2023

@author: lukas
"""

import pytest
from hashmap import HashMap


def test_set_val():
    """set new value"""
    hashmap = HashMap()

    hashmap.set_val(0, 1)
    hashmap.set_val(1, 2)

    assert hashmap.table[0] == 1
    assert hashmap.table[1] == 2


def test_get_val():
    """get value"""
    hashmap = HashMap()

    hashmap.set_val(0, 1)
    hashmap.set_val(1, 2)

    assert hashmap.get_val(0) == 1
    assert hashmap.get_val(1) == 2


def test_delete_value():
    """delete value"""
    hashmap = HashMap()

    hashmap.set_val(0, 1)
    hashmap.set_val(1, 2)
    hashmap.delete_value(0)

    with pytest.raises(KeyError):
        hashmap.get_val(0)
        assert hashmap.table[0] == 2
