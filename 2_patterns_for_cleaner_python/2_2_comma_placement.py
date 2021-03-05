#!/usr/bin/env python3
if __name__ == '__main__':
    # Don't write lists like that
    names = [
        'Alice',
        'Bob',
        'Dilbert'
    ]

    # Check this (forgot comma)
    # (string literal concatenation happens)
    names = [
        'Alice',
        'Bob',
        'Dilbert'
        'Jane'
    ]
    assert str(names) == "['Alice', 'Bob', 'DilbertJane']"

    # Better to always put comma at the end of every item
    names = [
        'Alice',
        'Bob',
        'Dilbert',
        'Jane',
    ]
    assert str(names) == "['Alice', 'Bob', 'Dilbert', 'Jane']"

