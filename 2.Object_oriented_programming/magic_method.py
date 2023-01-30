#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:26:23 2021

@author: lukas
"""

import math


class Punkt2D:
    """create points"""

    def __init__(self, val_x, val_y):
        self.val_x = val_x
        self.val_y = val_y
        self.distance = math.sqrt(val_x**2 + val_y**2)

    def __add__(self, sec_):
        """self summing class"""
        return Punkt2D(self.val_x + sec_.val_x, self.val_y + sec_.val_y)

    def __lt__(self, sec_):
        return self.distance < sec_.distance

    def __len__(self):
        return int(round(self.distance, 0))


if __name__ == "__main__":

    p1 = Punkt2D(2, 5)
    p2 = Punkt2D(4, 5)
    p3 = p1 + p2

    print("point 3 val x", p3.val_x)
    print("point 3 val x", p3.val_y)

    print("p1 < p2", p1 < p2)
    print("p1 > p2", p1 > p2)
    print("p1 == p1", p1 == p1)

    print("len(p3)", len(p3))
    print("p3.distance", p3.distance)


# output
# =============================================================================
# point 3 val x 6
# point 3 val x 10
# p1 < p2 True
# p1 > p2 False
# p1 == p1 True
# len(p3) 12
# p3.distance 11.661903789690601
# ===
