#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:56:47 2022
- none linear data structure
(more than one way to traverse)
- collection of nodes and edges
- root node
- not any cycle
- decision tree
- binary tree has only two node in each child branche
- bottom nodes of tree are caled leaves they have not children nodes
from: www.section.io/engineering-education/binary-tree-data-structure-python/
@author: lukas
"""

# node class
class Node:
    """Node constructopr, traversing"""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def inorder(self, node):
        result = []
        """traverse order 3 1 4 0 5 2 6"""
        if node:
            result += self.inorder(node.left)
            print(node.data)
            result += self.inorder(node.right)
            result.append(node.data)
        return result

    def postorder(self, node):
        """traverse order 3 4 1 5 6 2 0"""
        result = []
        if node:
            result += self.postorder(node.left)
            result += self.postorder(node.right)
            print(node.data)
            result.append(node.data)
        return result


    def preorder(self, node):
        """traverse order 0 1 3 4 2 5 6 """
        result = []
        if node:
            print(node.data)
            result += self.preorder(node.left)
            result += self.preorder(node.right)
            result.append(node.data)
        return result

if __name__ == "__main__":
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
    
    # Tree Structure
    #            0
    #        /      \
    #       1        2
    #     /   \    /   \
    #    3     4  5     6
    
    
    root.inorder(root)
    print("\n")
    root.postorder(root)
    print("\n")
    root.preorder(root)
        