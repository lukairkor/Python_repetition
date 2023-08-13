#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 1 14:07:51 2021

@author: lukas
"""


class Engine:
    def __init__(self, engin_type, engin_power):
        self.engin_type = engin_type
        self.engin_power = engin_power

    def describe_engin(self):
        print("Engine type is ", self.engin_type,
              " and its power is equal to", self.engin_power)


class Aircraft(Engine):
    def __init__(self, type_name, model_name, engin_type, engin_power):
        super().__init__(engin_type, engin_power)
        self.type_name = type_name
        self.model_name = model_name

    def name_of_aircraft(self):
        print("Aircraft name is ", self.type_name,
              "and model name is ", self.model_name)


class Glider(Aircraft):
    def __init__(self, towing_type, type_name, model_name, engin_type, engin_power):
        super().__init__(type_name, model_name, engin_type, engin_power)
        self.towing_type = towing_type

    def __del__(self):
        print("delete glider object")

    def describe_engin_glider(self):
        print("Have no engin")
        super().describe_engin()  # access function from previous class


if __name__ == "__main__":

    glider = Glider("by plane")
    glider.engin_type = None
    glider.engin_power = 0
    glider.type_name = "glider"
    glider.model_name = "Puchacz"
    glider.describe_engin_glider()
    glider.name_of_aircraft()

    # del glider
    print("end")


# output
# =============================================================================
# Have no engin
# Engine type is  None  and its power is equal to 0
# Aircraft name is  glider and model name is  Puchacz
# end
# delete glider object
# =============================================================================
