#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:26:23 2021

@author: lukas
"""

from abc import ABC, abstractmethod


class Myclass(ABC):
    """ """

    @abstractmethod  # dekorator
    def wylicz_objetosc(self):
        pass

    def wyswietl_objetosc(self):
        print(f"obwod kola wynosi:  {self.wylicz_objetosc()}.")


class ObjPolKolo(Myclass):
    """calculate volume of circle"""

    def wylicz_objetosc(self):

        val = 2*3.14*4
        return val


def main():
    """main function"""
    kolo = ObjPolKolo()
    kolo.wyswietl_objetosc()


if __name__ == "__main__":
    main()

# output
# =============================================================================
# obwod kola wynosi:  25.12.
# =============================================================================
