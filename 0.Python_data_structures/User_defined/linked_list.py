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
# |2|  | | --> | |  | | --> None
#  ^ head pointer             ^ tail pointer


class Node:
    """Node template"""

    def __init__(self, data):
        # attributes
        self.data = data  # hold a value nof node
        self.next = None  # hold reference to next node


class LinkedList:
    """List methodes"""

    def __init__(self):
        self.head = None  # point to first node in the list

    def add_front(self, data):
        """add element to the front of a list"""
        new_node = Node(data)  # node object
        new_node.next = self.head
        self.head = new_node

    def add_back(self, data):
        """add element to the end of a list"""
        new_node = Node(data)  # all data into new_node

        if self.head is None:  # check if list is empty
            self.head = new_node  # set first node
        else:
            actual_node = self.head
            while actual_node.next:
                actual_node = actual_node.next
            actual_node.next = new_node

    def del_front(self):
        """add element at a list front"""
        if self.head is None:
            print("empty list")
            return

        actual_node = self.head
        self.head = self.head.next
        actual_node.next = None

    def del_end(self):
        """delete elemnet from a list end"""
        if self.head is None:
            print("empty list")
            return

        if self.head.next is None:
            self.head = None
            return

        actual_node = self.head
        prev_node = None
        while actual_node.next:
            prev_node = actual_node
            actual_node = actual_node.next
        prev_node.next = None

    def show_all(self):
        """printing list"""
        actual_node = self.head
        while actual_node:  # is not None
            print(actual_node.data)
            actual_node = actual_node.next


if __name__ == "__main__":
    lis = LinkedList()
    
    lis.add_front(0)
    lis.add_front(1)
    lis.add_front(2)
    lis.add_front(3)
    lis.add_back(33)
    lis.del_front()
    lis.del_end()
    lis.show_all()
    
    # prints 2 1 0 33
