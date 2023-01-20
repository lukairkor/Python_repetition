#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 07:36:06 2023

@author: lukas
"""

import pytest
from graph import Graph


def test_add_vertex():
    """create vertex"""
    graf = Graph()
    
    graf.add_vertex(1)
    graf.add_vertex(2)
    graf.add_vertex(3)
    
    assert len(graf.vertices) == 3
    assert graf.vertices[0].data == 1
    assert graf.vertices[1].data == 2
    assert graf.vertices[2].data == 3


def test_add_edges():
    """add_edges"""
    graf = Graph()
    
    graf.add_vertex(1)
    graf.add_vertex(2)
    graf.add_vertex(3)
    graf.add_edges(1, 2)
    graf.add_edges(2, 3)
    
    assert len(graf.vertices[0].neighb) == 1
    assert graf.vertices[0].neighb[0].data == 2
    assert len(graf.vertices[1].neighb) == 2
    assert graf.vertices[1].neighb[0].data == 1
    assert graf.vertices[1].neighb[1].data == 3
    assert len(graf.vertices[2].neighb) == 1
    assert graf.vertices[2].neighb[0].data == 2


def test_show(capsys):
    """show graph"""
    graf = Graph()
    
    graf.add_vertex(1)
    graf.add_vertex(2)
    graf.add_vertex(3)
    graf.add_edges(1, 2)
    graf.add_edges(2, 3)
    graf.show()
    captured = capsys.readouterr()
    
    assert captured.out == "1 --> 2 \n2 --> 1 3 \n3 --> 2 \n"
