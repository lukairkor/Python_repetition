#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:51:15 2023

@author: lukas
"""

from tree import Node


def test_inorder():
    """traverse order 3 1 4 0 5 2 6"""
    # creating tree
    root = Node(0)

    root.left = Node(1)
    a = root.left
    root.right = Node(2)
    b = root.right
    a.left = Node(3)
    a.right = Node(4)
    b.left = Node(5)
    b.right = Node(6)

    result = root.inorder(root)

    assert result == [3, 1, 4, 0, 5, 2, 6]


def test_postorder():
    """traverse order 3 4 1 5 6 2 0"""
    # creating tree
    root = Node(0)

    root.left = Node(1)
    a = root.left
    root.right = Node(2)
    b = root.right
    a.left = Node(3)
    a.right = Node(4)
    b.left = Node(5)
    b.right = Node(6)

    result = root.postorder(root)
    print(result)

    assert result == [3, 4, 1, 5, 6, 2, 0]


def test_preorder():
    """traverse order 0 1 3 4 2 5 6 """
    # creating tree
    root = Node(0)

    root.left = Node(1)
    a = root.left
    root.right = Node(2)
    b = root.right
    a.left = Node(3)
    a.right = Node(4)
    b.left = Node(5)
    b.right = Node(6)

    result = root.preorder(root)

    assert result == [0, 1, 3, 4, 2, 5, 6]
