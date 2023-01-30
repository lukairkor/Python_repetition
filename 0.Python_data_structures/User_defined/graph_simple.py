#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:54:17 2023

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

if __name__ == "__main__":
    # print the edges
    edges(graf)
