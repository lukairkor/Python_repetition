#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:56:47 2022
-none linear data structure 
(more than one way to traverse)
-collection of nodes and edges
-root node
-not any cyccle
-decision tree
-binary tree has only two node in each child branche
- bottom of tree are caled leaves
from: www.section.io/engineering-education/binary-tree-data-structure-python/
@author: lukas
"""

# node class
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
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

def inorder(node):
    if node:       
        inorder(node.left)          
        print(node.data)        
        inorder(node.right)   
        
def postorder(node):
    if node:       
        postorder(node.left)           
        postorder(node.right)  
        print(node.data)       
     
def preorder(node):
    if node:  
        print(node.data)   
        preorder(node.left)           
        preorder(node.right)         
        
inorder(root)
print("\n")
postorder(root)       
print("\n")
preorder(root)    