#!/usr/bin/env python3
if __name__ == '__main__':
    my_items = list(range(0, 3)) # == [0, 1, 2]
    for i, item in enumerate(my_items):
        print(f'{i}: {item}')
    # Iterations can return tuples with an arbitrary number of values
    # that can then be unpacked right inside the for-statement.
    emails = {
        'Bob': 'bob@example.com',
        'Alice': 'alice@example.com',
    }
    for name, email in emails.items():
        print(f'{name} -> {email}')

    # loop (a), the stop value (n), and the step size (s)
    # for i in range(a, n, s):

    # Writing C-style loops in Python is considered unpythonic.
    # Avoid managing loop indexes and stop conditions manually if possible.
    #
    # Python’s for-loops are really “for-each” loops that can iterate
    # directly over items from a container or sequence.
