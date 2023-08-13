#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- *args and **kwargs are used in function definition:
"""


def test(f_arg, *argv):
    """pass a variable number of non-keyword arguments"""
    print("first arg", f_arg)
    for arg in argv:
        print("other arguments:", arg)


def greet_me(**kwargs):
    """pass a variable number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key} = {value}")


def concatenate(**kwargs):
    """Iterating over the Python kwargs dictionary"""
    result = ""
    for arg in kwargs:
        result.join(arg)
    return result


if __name__ == "__main__":
    test('1', '2', '3', '4')
    print("\n")
    greet_me(name="yasoob")
    print("\n")
    print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
