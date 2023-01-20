#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:49:21 2021

@author: lukas
"""


class Engine:
    __compressor_power = 200

    def __init__(self, engin_type, engin_power):
        self.engin_type = engin_type
        self.engin_power = engin_power

    def describe_engin(self, numb_of_engin):
        print("Engine type is ", self.engin_type, " and its power is equal to",
              (self.engin_power + self.__compressor_power) * numb_of_engin)


class Aircraft(Engine):
    def __init__(self, type_name, model_name): 
        self.type_name = type_name
        self.model_name = model_name

    def name_of_aircraft(self):
        print("Aircraft name is ", self.type_name,
              "and model name is ", self.model_name)


class Glider(Aircraft):
    def __init__(self, towing_type):
        self.towing_type = towing_type

    def __del__(self):
        print("delete glider object")

    def describe_engin_glider(self):
        print("Have no engin")
        super().describe_engin(0)  # acces function from previous class


class jet_aircraft(Aircraft):
    __amount_of_engines = 2

    def __init__(self, manufac):
        self.manufac = manufac

    def describe_engin(self):
        super().describe_engin(self.__amount_of_engines)

    # usuful method in class, that we can call
    @classmethod
    def new_jet(cls, manufac):
        return cls(manufac)  # send to init

    @staticmethod
    def wing_type(arg):
        print("Jet wings type is " + arg)


if __name__ == "__main__":

    glider = Glider("by plane")  # creat object from class Glider
    glider.engin_type = None
    glider.engin_power = 0
    glider.type_name = "glider"
    glider.model_name = "Puchacz"
    glider.describe_engin_glider()
    glider.name_of_aircraft()

    print("----------------")
    # we can invoke method without creating object
    jet1 = jet_aircraft.new_jet("General Dynamics")
    jet1.engin_type = "jet engin"
    jet1.engin_power = 1500
    jet1.describe_engin()

    print("----------------")
    # we can create object from object
    jet2 = jet1.new_jet("SAAB")
    jet2.engin_type = "jet engin"
    jet2.engin_power = 1000
    jet2.describe_engin()
    jet2.wing_type("Delta")
    print("----------------")
    # we dont need object just class for static method
    jet2.wing_type("Eliptical")


# =============================================================================
# delete glider object
# Have no engin
# Engine type is  None  and its power is equal to 0
# Aircraft name is  glider and model name is  Puchacz
# ----------------
# Engine type is  jet engin  and its power is equal to 3400
# ----------------
# Engine type is  jet engin  and its power is equal to 2400
# Jet wings type is Delta
# ----------------
# Jet wings type is Eliptical
# =============================================================================

