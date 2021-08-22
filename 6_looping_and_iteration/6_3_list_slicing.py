#!/usr/bin/env python3
if __name__ == '__main__':
    # [start:stop:step (or stride)]
    lst = [1, 2, 3, 4, 5]
    lst[1:3:1] # == [2, 3]
    # If you leave out the step size, it defaults to one:
    lst[1:3] # == [2, 3]
    lst[::2] # == [1, 3, 5]
    lst[::-1] # == [5, 4, 3, 2, 1]
    # You can use the :-operator to clear all elements from a list without destroying the list object itself
    # This is extremely helpful when you need to clear out a list
    # in your program that has other references pointing to it.
    del lst[:] # same as lst.clear()
    lst # == []
    lst = [1, 2, 3, 4, 5]
    original_lst = lst
    lst[:] = [7, 8, 9]
    lst # == [7, 8, 9]
    original_lst # == [7, 8, 9]
    assert original_lst is lst
    # Yet another use case for the sushi operator is creating (shallow) copies
    # of existing lists:
    copied_lst = lst[:]
    copied_lst # == [7, 8, 9]
    assert copied_lst is not lst

    # The : “sushi operator” is not only useful for selecting sublists of elements
    # within a list. It can also be used to clear, reverse, and copy lists.
    #
    # But be careful—this functionality borders on the arcane for many Python developers.
    # Using it might make your code less maintainable for everyone else on your team.
