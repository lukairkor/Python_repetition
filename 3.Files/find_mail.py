#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- getting mail adress
"""

from pathlib import Path


def get_email(filename, name):
    """getting mail adress"""
    count = 0
    user = {}
    with open(FNAME, encoding='UTF-8') as file:
        for line in file:
            if name in line and 'From' in line and 'From:' not in line:
                arr = line.split(' ')
                count += 1
                user['email'] = count

        email = ''.join(arr[1])
        print(email, count)


# if len(name) < 1 : name = "mbox-short.txt"
FNAME = Path('mbox-short.txt')
get_email(FNAME, 'cwen')
