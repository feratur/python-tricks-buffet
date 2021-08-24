#!/usr/bin/env python3
if __name__ == '__main__':
    mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
    str(mapping)
    # {'b': 42, 'c': 12648430, 'a': 23}

    import json
    json.dumps(mapping, indent=4, sort_keys=True)
    # {
    #     "a": 23,
    #     "b": 42,
    #     "c": 12648430
    # }

    # However, the json module only works with dicts that contain
    # primitive types — you’ll run into trouble trying to print a
    # dictionary that contains a non-primitive data type, like a function.
    # Also, you might run into trouble with how Unicode text is represented.

    # classical solution
    import pprint
    mapping['d'] = {1, 2, 3}
    pprint.pprint(mapping)
    # {'a': 23, 'b': 42, 'c': 12648430, 'd': set([1, 2, 3])}
    # OR {'a': 23, 'b': 42, 'c': 12648430, 'd': {1, 2, 3}}

    # However, compared to json.dumps(), it doesn’t represent nested
    # structures as well visually (but using pprint.pformat may help).

    # The default to-string conversion for dictionary objects in
    # Python can be difficult to read.
    #
    # The pprint and json module are “higher-fidelity” options built
    # into the Python standard library.
    #
    # Be careful with using json.dumps() and non-primitive keys
    # and values as this will trigger a TypeError.
