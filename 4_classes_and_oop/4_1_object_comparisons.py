#!/usr/bin/env python3
if __name__ == '__main__':
    # == operator compares by checking for equality
    # is operator, however, compares identities
    a = [1, 2, 3]
    b = a
    c = list(a)
    assert a == b
    assert a is b
    assert a == c
    assert a is not c
