#!/usr/bin/env python3
if __name__ == '__main__':
    snippet = {True: 'yes', 1: 'no', 1.0: 'maybe'}
    # This assertion is True
    assert snippet == {True: 'maybe'}

    # When Python processes our dictionary expression, it first constructs
    # a new empty dictionary object; and then it assigns the keys and values
    # to it in the order given in the dict expression.
    
    # This is what happens
    xs = dict()
    xs[True] = 'yes'
    xs[1] = 'no'
    xs[1.0] = 'maybe'

    # Python considers all dictionary keys used in this example to be equal
    assert True == 1 == 1.0

    # Python treats bool as a subclass of int.
    # Boolean values behave like the values 0 and 1, respectively, in almost
    # all contexts, the exception being that when converted to a string,
    # the strings ‘False’ or ‘True’ are returned, respectively.

    assert ['no', 'yes'][True] == 'yes'

    # Python’s dictionaries don’t update the key object itself
    # when a new value is associated with it (only value is rewritten)
    ys = {1.0: 'no'}
    ys[True] = 'yes'
    assert ys == {1.0: 'yes'}

    class AlwaysEquals:
        def __eq__(self, other):
            return True
        def __hash__(self):
            # id() returns the address of the object in memory
            return id(self)

    assert AlwaysEquals() == AlwaysEquals()
    assert AlwaysEquals() == 42
    assert AlwaysEquals() == 'waaat?'
    objects = [
        AlwaysEquals(),
        AlwaysEquals(),
        AlwaysEquals()
    ]
    hash_values = [hash(obj) for obj in objects]
    assert hash_values[0] != hash_values[1] != hash_values[2]

    # The keys in the next example are not getting overwritten,
    # even though they always compare as equal
    assert len({AlwaysEquals(): 'yes', AlwaysEquals(): 'no'}) == 2

    class SameHash:
        def __hash__(self):
            return 1
    # Instances of this SameHash class will compare as non-equal with each
    # other but they will all share the same hash value of 1
    a = SameHash()
    b = SameHash()
    assert a != b
    assert (hash(a), hash(b)) == (1, 1)

    # The “keys get overwritten” effect isn’t caused by hash value collisions alone either
    assert len({a: 'a', b: 'b'}) == 2

    # Because dictionaries check for equality AND compare the hash value to determine if two keys are the same.
    assert True == 1 == 1.0
    assert (hash(True), hash(1), hash(1.0)) == (1, 1, 1)

    # Dictionaries treat keys as identical if their __eq__ comparison
    # result says they’re equal and their hash values are the same.
    #
    # Unexpected dictionary key collisions can and will lead to surprising results.
