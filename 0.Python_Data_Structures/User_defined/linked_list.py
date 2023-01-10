#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:20:09 2022
- first node of list is called Head
- last is caled Tail points to Null
- nodes contain data and pointer to next or previous node
- linear data struct
@author: lukas
"""
# data next
# |2|  | | --> | |  | | --> Null
#  ^ head pointer

class Node:
    """ """
    def __init__(self, data):
        # attributes
        self.data = data # hold a value nof node
        self.next = None # hold reference to next node


class LinkedList:
    """ """
    def __init__(self):
        self.head = None # point to first node in the list


    def add_front(self, data):
        """ """
        node = Node(data) # node object
        node.next = self.head
        self.head = node


    def add_back(self, data):
        """ """
        new_node = Node(data) # all data into ew_node
        
        if not self.head: # check if list is empty
            self.head = new_node 
            return
            
        
        None


    def show_all(self):
        """ """
        actu_nod = self.head

        while actu_nod: # is not None
            print(actu_nod.data)
            actu_nod = actu_nod.next



lis = LinkedList()

lis.add_front(1)
lis.add_front(2)
lis.add_front(3)
lis.show_all()

# prints 3, 2, 1

