#!/usr/bin/env python3
if __name__ == '__main__':
    # list is implemented as dynamic array
    arr = ['one', 'two', 'three']
    # Lists are mutable:
    arr[1] = 'hello'
    del arr[1]
    # arr == ['one', 'three']
    # Lists can hold arbitrary data types:
    arr.append(23)
    # arr == ['one', 'three', 23]

    # tuple objects are immutable.
    # This means elements can’t be added or removed dynamically
    # all elements in a tu- ple must be defined at creation time.
    arr = 'one', 'two', 'three'
    # Tuples can hold arbitrary data types:
    # (Adding elements creates a copy of the tuple)
    new_tuple = arr + (23,)
    # ('one', 'two', 'three', 23)

    # array.array – Basic Typed Arrays
    # Arrays created with the array.array class are mutable
    # and behave similarly to lists, except for one important difference
    # they are “typed arrays” constrained to a single data type.
    # array.array objects with many elements are more space-efficient
    # than lists and tuples
    import array
    arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
    assert arr[1] == 1.5
    arr[1] = 23.0
    assert arr[1] == 23.0
    del arr[1]
    # array('f', [1.0, 2.0, 2.5])
    arr.append(42.0)
    # array('f', [1.0, 2.0, 2.5, 42.0])
    # Arrays are "typed":
    # arr[1] = 'hello'
    # TypeError: "must be real number, not str"

    # str – Immutable Arrays of Unicode Characters
    # Python 3.x uses str objects to store textual data
    # as immutable sequences of Unicode characters.
    # Because strings are immutable in Python, modifying
    # a string requires creating a modified copy
    # Strings can be unpacked into a list to # get a mutable representation:
    s = list('abcd')
    assert ''.join(s) == 'abcd'
    # Strings are recursive data structures:
    # type('abc') "<class 'str'>
    # type('abc'[0]) "<class 'str'>"

    # bytes – Immutable Arrays of Single Bytes
    # Bytes objects are immutable sequences of
    # single bytes (integers in the range of 0<=x<=255).
    # Like strings, bytes have their own literal syntax for
    # creating objects and they’re space-efficient
    # Bytes objects are immutable, but unlike strings,
    # there’s a dedicated “mutable byte array” data type
    # called bytearray that they can be unpacked into
    arr = bytes((0, 1, 2, 3))
    assert arr[1] == 1
    # Bytes literals have their own syntax:
    arr = b'x00x01x02x03'
    # bytearray – Mutable Arrays of Single Bytes
    # They’re closely related to bytes objects
    # with the main difference being that bytearrays
    # can be modified freely — you can overwrite elements,
    # remove existing elements, or add new ones.
    arr = bytearray((0, 1, 2, 3))
    arr[1] = 23
    # bytearray(b'x00x17x02x03')
    del arr[1]
    # bytearray(b'x00x02x03')
    arr.append(42)
    # Bytearrays can be converted back into bytes objects:
    # (This will copy the data)
    bytes(arr)
    #
    # You need to store arbitrary objects, potentially with mixed data types?
    # Use a list or a tuple, depending on whether you want an immutable data structure or not.
    #
    # You have numeric (integer or floating point) data and tight packing and performance is important?
    # Try out array.array and see if it does everything you need.
    # Also, consider going beyond the standard library and try out packages like NumPy or Pandas.
    #
    # You have textual data represented as Unicode characters?
    # Use Python’s built-in str. If you need a “mutable string,” use a list of characters.
    #
    # You want to store a contiguous block of bytes?
    # Use the immutable bytes type, or bytearray if you need a mutable data structure.
