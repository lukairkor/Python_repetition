# -*- coding: utf-8 -*-
"""
- when you need function for short peroid of time (one time use)
- pass function as a argument
- Np. w metodach map, filter, reduce i innych przyjmujących
funkcję lub wtedy gdy tą funkcję wykonujemy tylko raz.
- anonymouse functiobs (defined without name)
"""

def exa_1(number):
    result = map(lambda number: number ** 2, numbers)
    return print(list(result))


def function(number):
    return lambda x: x + number


def power(base): 
    return lambda exponent: base ** exponent


print(power(3)(2))

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    exa_1(numbers)

    x = function(2)
    print(x(6))
    
    numbers = [1, 2, 3, 4, 5]
    print(power(numbers))
