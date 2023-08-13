#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 05:58:31 2023

@author: lukas
"""

import pytest
from stack import Stack


def test_push():
    """add an element at the end of the list"""
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    assert stack.items == [1, 2]
    stack.push(3)
    assert stack.items == [1, 2, 3]


def test_pop():
    """retrieve and delete last list element"""
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack.items == [1]
    stack.pop()
    assert stack.items == []


def test_if_empty():
    """check if a list is empty"""
    stack = Stack()
    
    assert stack.if_empty() == 0
    stack.push(1)
    assert stack.if_empty() == 1


def test_size():
    """check the size of the list"""
    stack = Stack()
    
    stack.size() == "list  length is equal to: 0"
    stack.push(1)
    stack.size() == "list  length is equal to: 1"


def test_show():
    """show list content"""
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.show()
    assert stack.items == [1, 2]


def test_top():
    """show last list element without deleting"""
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.top() == 2
    stack.pop()
    stack.top() == 1
