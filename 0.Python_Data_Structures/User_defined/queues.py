#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:30:52 2022
- FIFO
-insertion and deletion on different ends
- enqueue(), dequeue(), front(), rear(), empty()
@author: lukas
"""

## enqueue -> | | | | | | -> dequeue
##       reaqr ^       ^ front


class Queue:
    """Queue template"""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """insert new item"""
        self.items.append(item)

    def dequeue(self):
        """retrieve and remove element from end of the queue"""
        if self.if_empty() == 0:
            print("list is empty")
        else:
            self.items.pop()

    def if_empty(self):
        """check if list is empty"""
        return len(self.items)

    def show(self):
        """show list content"""
        for item in self.items:
            print(item)

    def front(self):
        """return first element from queue"""
        print(f"First element: {self.items[0]}")
        return self.items[0]

    def rear(self):
        """return last element without deleting"""
        print(f"Last element: {self.items[-1]}")
        return self.items[-1]


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.show()

    print("\n")
    queue.dequeue()

    queue.front()
    queue.rear()
    queue.show()
