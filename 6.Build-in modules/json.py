#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:10:32 2021

@author: lukas
"""
import json

# convert from json to python
# json
x = '{"Tom":20, "Angelica":30, "Johan":24}'

print(type(x))
# parse json
y = json.loads(x)

print(y)
print(type(y))
# convert from python to json
x = {"Tom": 20, "Angelica": 30, "Johan": 24}

y = json.dumps(x)

print(y)
