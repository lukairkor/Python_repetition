#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:48:53 2022
- non linear data structure
- collection of nodes, vertices and edges
- finding shorting path, networking
@author: lukas
"""

graf = {}
graf["ja"] = ["Michal", "Tomek", "Joannam"]
graf["Michal"] = ["Jan"]
graf["Tomek"] = ["Alicja"]
graf["Joannam"] = ["Jakub"]
graf["Jan"] = []
graf["Alicja"] = []
graf["Jakub"] = []

#display graph
print(graf,"\n")

#display graph vertices
print(graf.keys())

#display graph edges
