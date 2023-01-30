#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- string
"""

CON_TEXT = "DD kdsreS:    0.3423"
COLON = CON_TEXT.find(':')
LICZBA = CON_TEXT[COLON + 1:]
LICZBA_1 = LICZBA.strip()
LICZBA__2 = float(LICZBA_1)

print(COLON)
print(LICZBA)
print(LICZBA_1)
print(LICZBA__2)
