#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 00:52:07 2023

@author: lukas
"""

import pytest
from queues import Queue


def test_enqueue():
    """insert new item"""
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    
    assert len(queue.items) == 2
    assert queue.items[0] == 1
    assert queue.items[1] == 2


def test_dequeue():
    """retrieve and remove an element from the end of the queue"""
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    
    assert len(queue.items) == 1
    assert queue.items[0] == 1


def test_if_empty():
    """check if a list is empty"""
    queue = Queue()
    
    assert queue.if_empty() == 0


def test_front():
    """return a first element from queue"""
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    
    assert queue.front() == 1


def test_rear():
    """return last element without deleting"""
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.rear() == 2
