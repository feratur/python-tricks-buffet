#!/usr/bin/env python3
if __name__ == '__main__':
    # values = [expression for item in collection if condition]
    squares = [x * x for x in range(10)]
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    even_squares = [x * x for x in range(10) if x % 2 == 0]
    # values = []
    # for item in collection:
    #   if condition:
    #     values.append(expression)
    
    # set comprehension
    { x * x for x in range(-9, 10) }
    # set([64, 1, 36, 0, 49, 9, 16, 81, 25, 4])

    # dictionary comprehension
    { x: x * x for x in range(5) }
    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    # Comprehensions are a key feature in Python.
    # Understanding and applying them will make your code much more Pythonic.
    #
    # Comprehensions are just fancy syntactic sugar for a simple for-loop pattern.
    # Once you understand the pattern, you’ll develop an intuitive understanding for comprehensions.
    #
    # There are more than just list comprehensions.
