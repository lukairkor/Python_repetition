#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 04:11:55 2023

@author: lukas
"""

import pytest
from linked_list import LinkedList


def test_add_front():
    lis = LinkedList()
    
    lis.add_front(0)
    assert lis.head.data == 0
    lis.add_front(1)
    assert lis.head.data == 1
    assert lis.head.next.data == 0


def test_add_back():
    lis = LinkedList()
    
    lis.add_back(0)
    assert lis.head.data == 0
    lis.add_back(1)
    assert lis.head.data == 0
    assert lis.head.next.data == 1


def test_del_front():
    lis = LinkedList()
    
    lis.add_back(0)
    lis.add_back(1)
    lis.del_front()
    assert lis.head.data == 1
    lis.del_front()
    assert lis.head is None


def test_del_end():
    lis = LinkedList()
    
    lis.add_back(0)
    lis.add_back(1)
    lis.del_end()
    assert lis.head.next is None
    lis.del_end()
    assert lis.head is None
