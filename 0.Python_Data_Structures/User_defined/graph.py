#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:48:53 2022
- non linear data structure
- collection of vertices and edges
- finding shorting path, networking
@author: lukas
"""

# define the graph
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
print(graf.keys(), "\n")

# display graph edges
def edges(graf):
    for node in graf:
        for neighbor in graf[node]:
            print(f"({node}, {neighbor})")

# print the edges
edges(graf)