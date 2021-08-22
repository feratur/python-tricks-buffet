#!/usr/bin/env python3
if __name__ == '__main__':
    # Python’s iterator protocol:
    # Objects that support the __iter__ and __next__
    # dunder methods automatically work with for-in loops.
    class RepeaterIterator:
        def __init__(self, source):
            self.source = source
        def __next__(self):
            return self.source.value
    class Repeater:
        def __init__(self, value):
            self.value = value
        def __iter__(self):
            return RepeaterIterator(self)
    repeater = Repeater('Hello')
    for item in repeater:
        print(item) # Prints Hello indefinitely
    # same as
    repeater = Repeater('Hello')
    iterator = repeater.__iter__()
    while True:
        item = iterator.__next__()
        print(item)
    # same as
    repeater = Repeater('Hello')
    iterator = iter(repeater)
    while True:
        item = next(iterator)
        print(item)
    # len(x) is a shortcut for calling x.__len__

    # A Simpler Iterator Class
    # We needed RepeaterIterator to host the __next__ method for
    # fetching new values from the iterator. But it doesn’t really
    # matter where __next__ is defined. In the iterator protocol,
    # all that matters is that __iter__ returns any object with a __next__ method on it.
    class Repeater:
        def __init__(self, value):
            self.value = value
        def __iter__(self):
            return self
        def __next__(self):
            return self.value

    my_list = [1, 2, 3]
    iterator = iter(my_list)
    next(iterator) # 1
    next(iterator) # 2
    next(iterator) # 3
    # next(iterator) causes StopIteration exception

    class BoundedRepeater:
        def __init__(self, value, max_repeats):
            self.value = value
            self.max_repeats = max_repeats
            self.count = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.count >= self.max_repeats:
                raise StopIteration
            self.count += 1
            return self.value
    repeater = BoundedRepeater('Hello', 3)
    for item in repeater:
        print(item)
    # Hello
    # Hello
    # Hello
    repeater = BoundedRepeater('Hello', 3)
    iterator = iter(repeater)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        print(item)
    
    # Python 2 compatibility
    # method next() is used instead of __next__()
    # Class definition is modified to inherit from object in order to ensure
    # we’re creating a new-style class on Python 2
    class InfiniteRepeater(object):
        def __init__(self, value):
            self.value = value
        def __iter__(self):
            return self
        def __next__(self):
            return self.value
        # Python 2 compatibility:
        def next(self):
            return self.__next__()

    # Iterators provide a sequence interface to Python objects that’s memory efficient
    # and considered Pythonic. Behold the beauty of the for-in loop!
    #
    # To support iteration an object needs to implement the iterator protocol by
    # providing the __iter__ and __next__ dunder methods.
    #
    # Class-based iterators are only one way to write iterable objects in Python.
    # Also consider generators and generator expressions.
