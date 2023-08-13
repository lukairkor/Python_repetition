#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:34:15 2022
- LIFO
@author: lukas
"""


class Stack:
    """Creating Stack"""

    def __init__(self):
        """initialize an empty list"""
        self.items = []

    def push(self, item):
        """add an element at the end of the list"""
        self.items.append(item)

    def pop(self):
        """retrieve and delete last list element"""
        if self.if_empty() == 0:
            print("list is empty")
        else:
            self.items.pop()

    def if_empty(self):
        """check if a list is empty"""
        return len(self.items)

    def size(self):
        """check the size of the list"""
        return print(f"list  length is equal to: {len(self.items)}")

    def show(self):
        """show list content"""
        for item in self.items:
            print(item)

    def top(self):
        """show last list element without deleting"""
        if self.if_empty() == 0:
            print("list is empty")
            return
        print(self.items[-1])


if __name__ == "__main__":
    line = Stack()

    # line.pop()
    # line.push(2)
    line.push(1)
    line.push(3)
    # line.push("last")
    line.push(4)
    # line.pop()
    # line.size()

    # line.if_empty()
    line.top()
    # line.show()
