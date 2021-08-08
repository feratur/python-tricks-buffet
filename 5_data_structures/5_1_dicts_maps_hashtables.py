#!/usr/bin/env python3
if __name__ == '__main__':
    phonebook = {
        'bob': 7387,
        'alice': 3719,
        'jack': 7052,
    }
    squares = {x: x * x for x in range(6)}
    # There are some restrictions on which objects can be used as valid keys.
    # Python’s dictionaries are indexed by keys that can be of any hashable type
    # A hashable object has a hash value which never changes during
    # its lifetime (see __hash__), and it can be compared to other objects
    # (see __eq__). In addition, hashable objects which compare as equal
    # must have the same hash value
    #
    # Immutable types like strings and numbers are hashable and work well
    # as dictionary keys. You can also use tuple objects as dictionary keys,
    # as long as they contain only hashable types themselves.
    #
    # class attributes and variables in a stack frame are both stored
    # internally in dictionaries.
    #
    # Python dictionaries are based on a well-tested and finely tuned hash
    # table implementation that provides the performance characteristics
    # you’d expect: O(1) time complexity for lookup, insert, update, and
    # delete operations in the average case
    #
    # collections.OrderedDict – Remember the Insertion Order of Keys
    #
    import collections
    # instances preserve the insertion order of keys
    d = collections.OrderedDict(one=1, two=2, three=3)
    # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
    d['four'] = 4
    # OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
    # d.keys() == odict_keys(['one', 'two', 'three', 'four'])
    #
    # collections.defaultdict – Return Default Values for Missing Keys
    #
    # The defaultdict class is another dictionary subclass that accepts
    # a callable in its constructor whose return value will be used if
    # a requested key cannot be found.
    from collections import defaultdict
    dd = defaultdict(list)
    dd['dogs'].append('Rufus')
    #
    # collections.ChainMap – Search Multiple Dictionaries as a Single Mapping
    #
    from collections import ChainMap
    dict1 = {'one': 1, 'two': 2}
    dict2 = {'three': 3, 'four': 4}
    chain = ChainMap(dict1, dict2)
    # ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
    # ChainMap searches each collection in the chain
    # from left to right until it finds the key (or fails):
    assert chain['three'] == 3
    # Insertions, updates, and deletions only affect the first
    # mapping added to the chain.
    #
    # types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries
    #
    from types import MappingProxyType
    # MappingProxyType is a wrapper around a standard dictionary that
    # provides a read-only view into the wrapped dictionary’s data.
    # can be used to create immutable proxy versions of dictionaries.
    writable = {'one': 1, 'two': 2}
    read_only = MappingProxyType(writable)
    assert read_only['one'] == 1
    # read_only['one'] = 23 causes TypeError
    writable['one'] = 42
    assert read_only['one'] == 42
    # Dictionaries are the central data structure in Python.
    # The built-in dict type will be “good enough” most of the time.
    # Specialized implementations, like read-only or ordered dicts,
    # are available in the Python standard library.
