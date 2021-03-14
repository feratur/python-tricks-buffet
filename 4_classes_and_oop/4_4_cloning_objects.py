#!/usr/bin/env python3
if __name__ == '__main__':
    # cloning standard collections (shallow copies though)
    new_list = list(original_list)
    new_dict = dict(original_dict)
    new_set = set(original_set)

    # shallow copy is 1 level deep
    # deep copy is recursive, copies child objects as well
    xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ys = list(xs) # Make a shallow copy

    xs.append(['new sublist'])
    # xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
    # ys = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    xs[1][0] = 'X'
    # xs = [[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
    # ys = [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]

    # deep copy
    import copy
    xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    zs = copy.deepcopy(xs)

    xs[1][0] = 'X'
    # xs = [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
    # zs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # copy.copy() function creates shallow copies of arbitrary objects

    # In order for a class to define its own copy implementation,
    # it can define special methods __copy__() and __deepcopy__().
    # The former is called to implement the shallow copy operation;
    # no additional arguments are passed. The latter is called to
    # implement the deep copy operation; it is passed one argument,
    # the memo dictionary. If the __deepcopy__() implementation needs
    # to make a deep copy of a component, it should call the deepcopy()
    # function with the component as first argument and the memo dictionary
    # as second argument.