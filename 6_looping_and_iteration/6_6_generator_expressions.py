#!/usr/bin/env python3
if __name__ == '__main__':
    iterator = ('Hello' for i in range(3))
    # Once a generator expression has been consumed, it can’t be restarted or reused.
    l1 = list(iterator)
    # ['Hello', 'Hello', 'Hello']
    l2 = list(iterator)
    # []
    even_squares = (x * x for x in range(10) if x % 2 == 0)
    # you can define an iterator and consume it right away with a for-loop
    for x in ('Bom dia' for i in range(3)):
        print(x)
    # The parentheses surrounding a generator expression can be dropped if
    # the generator expression is used as the single argument to a function.
    sum((x * 2 for x in range(10)))
    sum(x * 2 for x in range(10))

    # (expr
    #   for x in xs if cond1
    #   for y in ys if cond2
    #   ...
    #   for z in zs if condN
    # )
    #
    # for x in xs:
    #   if cond1:
    #       for y in ys:
    #           if cond2:
    #               ...
    #                   for z in zs:
    #                       if condN:
    #                           yield expr

    # Generator expressions are similar to list comprehensions.
    # However, they don’t construct list objects. Instead, generator
    # expressions generate values “just in time” like a class-based
    # iterator or generator function would.
    #
    # Once a generator expression has been consumed, it can’t be
    # restarted or reused.
    #
    # Generator expressions are best for implementing simple “ad-hoc” iterators.
    # For complex iterators, it’s better to write a generator function or a class-based iterator.
