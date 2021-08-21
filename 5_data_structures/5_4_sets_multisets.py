#!/usr/bin/env python3
if __name__ == '__main__':
    # In a “proper” set implementation, membership tests are expected
    # to run in fast O(1) time. Union, intersection, difference,
    # and subset operations should take O(n) time on average
    vowels = {'a', 'e', 'i', 'o', 'u'}
    squares = {x * x for x in range(10)}
    # But be careful: To create an empty set you’ll need to call the set() constructor.
    # Using empty curly-braces {} is ambiguous and will create an empty dictionary instead.
    # The set type is mutable and allows for the dynamic insertion and deletion of elements.
    assert 'e' in vowels
    letters = set('alice')
    letters.intersection(vowels)
    # {'a', 'e', 'i'}
    vowels.add('x')
    # vowels == {'i', 'a', 'u', 'o', 'x', 'e'}

    # frozenset – Immutable Sets
    # Frozensets are static and only allow query operations on their elements
    # Because frozensets are static and hashable, they can be used as
    # dictionary keys or as elements of another set, something that isn’t
    # possible with regular (mutable) set objects
    vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
    d = { frozenset({1, 2, 3}): 'hello' }
    assert d[frozenset({1, 2, 3})] == 'hello'

    # collections.Counter – Multisets
    # multiset (or bag) type that allows elements in the set to have more than one occurrence
    # This is useful if you need to keep track of not only if an element is part of a set,
    # but also how many times it is included in the set
    from collections import Counter
    inventory = Counter()
    loot = {'sword': 1, 'bread': 3}
    inventory.update(loot)
    # Counter({'bread': 3, 'sword': 1})
    more_loot = {'sword': 1, 'apple': 1}
    inventory.update(more_loot)
    # Counter({'bread': 3, 'sword': 2, 'apple': 1})
    # Here’s a caveat for the Counter class: You’ll want
    # to be careful when counting the number of elements in a Counter object. Calling len()
    # returns the number of unique elements in the multiset, whereas the total number of
    # elements can be retrieved using the sum function:
    assert len(inventory) == 3
    assert sum(inventory.values()) == 6

    # Sets are another useful and commonly used data structure included with Python and its standard library.
    # Use the built-in set type when looking for a mutable set.
    # frozenset objects are hashable and can be used as dictionary or set keys.
    # collections.Counter implements multiset or “bag” data structures.
