#!/usr/bin/env python3
if __name__ == '__main__':
    xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
    sorted(xs.items())
    # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
    # To sort by values:
    sorted(xs.items(), key=lambda x: x[1])
    # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

    # The concept is so common that Python’s standard library includes the operator module.
    # This module implements some of the most frequently used key funcs as plug-and-play building blocks, like
    # operator.itemgetter and operator.attrgetter.
    import operator
    sorted(xs.items(), key=operator.itemgetter(1))
    # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

    # Other examples:
    sorted(xs.items(), key=lambda x: abs(x[1]))
    sorted(xs.items(), key=lambda x: x[1], reverse=True)

    # When creating sorted “views” of dictionaries and other collections,
    # you can influence the sort order with a key func.
    #
    # Key funcs are an important concept in Python. The most frequently
    # used ones were even added to the operator module in the standard library.
    #
    # Functions are first-class citizens in Python. This is a powerful
    # feature you’ll find used everywhere in the language.
