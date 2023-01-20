#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:48:53 2022
- non linear data structure
- collection of vertices and edges
- finding shorting path, networking
@author: lukas
"""


class Vertex:
    """vertex templete"""

    def __init__(self, data):
        """vertex value and his two neighbours """
        self.data = data
        self.neighb = []


class Graph:
    """Graph template"""

    def __init__(self):
        """all vertices"""
        self.vertices = []

    def add_vertex(self, data):
        """create vertex and add to graph"""
        new_verte = Vertex(data)
        self.vertices.append(new_verte)

    def add_edges(self, ver_1, ver_2):
        """pair two vertex"""
        ver_1_obj = next(
            (ver for ver in self.vertices if ver.data == ver_1), None)
        ver_2_obj = next(
            (ver for ver in self.vertices if ver.data == ver_2), None)
        if ver_1_obj and ver_2_obj:
            ver_1_obj.neighb.append(ver_2_obj)
            ver_2_obj.neighb.append(ver_1_obj)

    def show(self):
        """Prints out the graph in a simple format"""
        for vertex in self.vertices:
            print(f"{vertex.data} -->", end=" ")
            for neighbor in vertex.neighb:
                print(f"{neighbor.data}", end=" ")
            print()


if __name__ == "__main__":
    graf = Graph()
    graf.add_vertex(1)
    graf.add_vertex(2)
    graf.add_vertex(3)
    graf.add_vertex(4)
    graf.add_vertex(5)
    graf.add_edges(1, 2)
    graf.add_edges(2, 3)
    graf.add_edges(1, 4)
    graf.add_edges(4, 5)
    graf.show()
