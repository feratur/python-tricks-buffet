#!/usr/bin/env python3
if __name__ == '__main__':
    xs = {'a': 1, 'b': 2}
    ys = {'b': 3, 'c': 4}
    
    # Classical solution to merge
    zs = {}
    zs.update(xs)
    zs.update(ys)

    # Update does something like this
    def update(dict1, dict2):
        for key, value in dict2.items():
            dict1[key] = value

    # this approach only works for merging two dictionaries
    zs = dict(xs, **ys)
    # OR this approach for merging arbitrary number of dictionaries
    zs = {**xs, **ys}
    assert zs == {'a': 1, 'c': 4, 'b': 3}

    # Using the **-operator is also faster than using chained
    # update() calls, which is yet another benefit.

    # In Python 3.5 and above you can use the **-operator to merge
    # multiple dictionary objects into one with a single expression,
    # overwriting existing keys left-to-right.
    #
    # To stay compatible with older versions of Python, you might
    # want to use the built-in dictionary update() method instead.
