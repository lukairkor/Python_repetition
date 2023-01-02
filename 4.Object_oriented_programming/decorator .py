from datetime import datetime

'''
Dekoratory w Pythonie opierają się przede wszystkim
na dwóch założeniach:
-funkcja może przyjąć jako argument inną funkcję
-wewnątrz funkcji można stworzyć kolejną funkcję
*dekorator to wzorzec
'''
#-----------------------------------------------------------------------
# 1. Withjout decorator
print("example 1")

def say_something():
    print("Hello!!")

def disable_at_night(func):
    x = datetime.now().hour
    def wrapper():
        if 4 > x > 1:
            func()
        else:
            print('cos nie dziala')  
    return wrapper

disable_at_night(say_something())


#----------------------------------------------------------------------
print("example 2")

def disable_at_night(func):
    def wrapper():
        if 1 <= datetime.now().hour < 4:
            func()
        else:
            print('jest noc')  
    return wrapper

@disable_at_night #  <--- dekorator
def say_something():
    print('Hello!!')

say_something()

#-----------------------------------------------------------------------
# 3. Dekorator z argumentami
# ten dekorator jest bardziej generyczny

'''
run_only_between(7, 21) – zwróci funkcję real_decorator
zwrócona funkcja real_decorator nie ma nadpisanych argumentów 
więc przyjmie w argumencie funkcję którą ma dekorować
funkcja real_decorator zwróci funkcję wrapper która dodaje
nową funkcjonalność, uruchamiając warunkowo dekorowaną funkcję
'''
print("example 3")

def run_only_between(_from=7, _to=22):
    def real_decorator(func):
        def wrapper():
            if _from <= datetime.now().hour < _to:
                func()
            else:
                pass
        return wrapper
    return real_decorator

@run_only_between(7,  21)
def say_something():
    print("Hello!!")

say_something() #  <---

#------------------------------------------------------------------------
print("example 4")

def log_before_and_after(func):
    def wrapper():
        print("before")
        result = func()
        print("after")
        return result
    return wrapper

def run_only_between(_from=7, _to=22):
    def real_decorator(func):
        def wrapper():
            if _from <= datetime.now().hour < _to:
                func()
            else:
                pass
        return wrapper
    return real_decorator

@log_before_and_after
@run_only_between(7, 22)
def say_something():
    print("Hello!!")

say_something() #  <---

#--------------------------------------------------------------------------