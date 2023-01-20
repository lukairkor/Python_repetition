#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
-dekoratory w Pythonie opierają się przede wszystkim
na dwóch założeniach:
-funkcja może przyjąć jako argument inną funkcję
-wewnątrz funkcji można stworzyć kolejną funkcję
*dekorator to wzorzec
'''

from datetime import datetime


class Examp1:
    """without decorator"""

    def say_something(self):
        """print text"""
        print(f"Hello!! it is {datetime.now().hour}")

    def disable_at_night(self, func):
        """calculate current hour"""
        tim_e = datetime.now().hour

        def wrapper():
            if 6 <= tim_e < 24:
                func(self)
            else:
                print('something wrong')
        return wrapper


class Examp2:
    """with decorator"""
    def _disable_at_night(func):
        """methode is decorator"""

        def wrapper(self):
            """chceck cuurent hour"""
            tim_e = datetime.now().hour
            if 6 <= tim_e < 24:
                func(self)
            else:
                print('its night')
        return wrapper

    @_disable_at_night
    def say_something(self):
        """is called when wrapper is in range 1<= wrapper<4"""
        print(f"Hello!! it is {datetime.now().hour}")


class Examp3:
    """more generic decorator"""
    def _run_only_between(_from=6, _to=24):
        """ """
        def _real_decorator(func):
            def wrapper(self):
                tim_e = datetime.now().hour
                if _from <= tim_e < _to:
                    return func(self)
            return wrapper
        return _real_decorator

    @_run_only_between()
    def say_something(self):
        """ """
        print("Hello!!")
        print(f"Hello!! it is {datetime.now().hour}")


class Examp4:
    """Two decorators"""
    def _log_before_and_after(func):
        """ """

        def wrapper(self):
            print("before")
            result = func(self)
            print("after")
            return result
        return wrapper

    def _run_only_between(_from=7, _to=22):
        """ """
        def _real_decorator(func):
            def wrapper(self):
                tim_e = datetime.now().hour
                if _from <= tim_e < _to:
                    func(self)
                else:
                    pass
            return wrapper
        return _real_decorator

    @_log_before_and_after
    @_run_only_between()
    def say_something(self):
        """ """
        print(f"Hello!! it is {datetime.now().hour}")


if __name__ == "__main__":

    print("example 1")
    obj1 = Examp1()
    obj1.disable_at_night(obj1.say_something())

    print("example 2")
    obj2 = Examp2()
    obj2.say_something()

    print("example 3")
    obj3 = Examp3()
    obj3.say_something()

    print("example 4")
    obj4 = Examp4()
    obj4.say_something()

    
# =============================================================================
# example 1
# Hello!! it is 14
# example 2
# Hello!! it is 14
# example 3
# Hello!!
# Hello!! it is 14
# example 4
# before
# Hello!! it is 14
# after
# =============================================================================
