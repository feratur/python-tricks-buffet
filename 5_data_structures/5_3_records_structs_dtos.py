#!/usr/bin/env python3
if __name__ == '__main__':
    # dict – Simple Data Objects
    # tuple – Immutable Groups of Objects
    # Writing a Custom Class – More Work, More Control
    # collections.namedtuple – Convenient Data Objects
    from collections import namedtuple
    from sys import getsizeof
    p1 = namedtuple('Point', 'x y z')(1, 2, 3)
    p2 = (1, 2, 3)
    assert getsizeof(p1) == getsizeof(p2)
    # typing.NamedTuple – Improved Namedtuples
    # It is very simi- lar to namedtuple,
    # the main difference being an updated syntax for defining new record types and added support for type hints
    # type annotations are not enforced without a separate type-checking tool like mypy
    from typing import NamedTuple
    class Car(NamedTuple):
        color: str
        mileage: float
        automatic: bool
    car1 = Car('red', 3812.4, True)
    # Instances have a nice repr:
    # Car(color='red', mileage=3812.4, automatic=True)
    assert car1.mileage == 3812.4
    # Fields are immutable
    # Type annotations are not enforced without
    # a separate type checking tool like mypy:

    # struct.Struct – Serialized C Structs
    # The struct.Struct class23 converts between Python values and
    # C structs serialized into Python bytes objects. For example,
    # it can be used to handle binary data stored in files or coming
    # in from network connections.
    from struct import Struct
    MyStruct = Struct('i?f')
    data = MyStruct.pack(23, False, 42.0)
    # MyStruct.unpack(data) == (23, False, 42.0)

    # types.SimpleNamespace – Fancy Attribute Access
    # It’s basically a glorified dictionary that allows attribute access
    # and prints nicely. Attributes can be added, modified, and deleted freely.
    from types import SimpleNamespace
    car1 = SimpleNamespace(color='red', mileage=3812.4, automatic=True)
    car1.mileage = 12
    car1.windshield = 'broken'
    del car1.automatic

    # You only have a few (2-3) fields: Using a plain tuple object may be okay if the field order
    # is easy to remember or field names are super- fluous. For example, think of an
    # (x, y, z) point in 3D space.
    #
    # You need immutable fields: In this case, plain tuples, collections.namedtuple,
    # and typing.NamedTuple would all make good options for implementing this type of data object.
    #
    # You need to lock down field names to avoid typos: collections.namedtuple and
    # typing.NamedTuple are your friends here.
    #
    # You want to keep things simple: A plain dictionary object might be a good choice
    # due to the convenient syntax that closely resembles JSON.
    #
    # You need full control over your data structure: It’s time to write a custom class
    # with @property setters and getters.
    #
    # You need to add behavior (methods) to the object: You should write a custom class,
    # either from scratch or by extending collections.namedtuple or typing.NamedTuple.
    #
    # You need to pack data tightly to serialize it to disk or to send it over the network:
    # Time to read up on struct.Struct because this is a great use case for it.
