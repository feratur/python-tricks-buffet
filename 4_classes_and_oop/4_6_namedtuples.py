#!/usr/bin/env python3
if __name__ == '__main__':
    from collections import namedtuple
    Car = namedtuple('Car' , 'color mileage')
    # same as
    # Car = namedtuple('Car', ['color', 'mileage'])
    my_car = Car('red', 3812.4)
    assert my_car.color == 'red'
    assert my_car.mileage == 3812.4
    assert my_car[0] == 'red'
    assert my_car[1] == 3812.4
    # tuple(my_car) == ('red', 3812.4)
    color, mileage = my_car
    print(color, mileage)
    # red 3812.4
    #
    # Like tuples, namedtuples are immutable. 
    # When you try to overwrite one of their fields,
    # you’ll get an AttributeError exception
    #
    # namedtuples are a memoryefficient shortcut
    # to defining an immutable class in Python manually.
    #
    # you can extend a namedtuple’s class like any
    # other class and add methods and new properties to it that way.
    class MyCarWithMethods(Car):
        def hexcolor(self):
            if self.color == 'red':
                return '#ff0000'
            else:
                return '#000000'
    c = MyCarWithMethods('red', 1234)
    assert c.hexcolor() == '#ff0000'
    # But the easiest way to create hierarchies of namedtuples
    # is to use the base tuple’s _fields property
    ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
    print(ElectricCar('red', 1234, 45.0))
    # ElectricCar(color='red', mileage=1234, charge=45.0)
    # Besides the _fields property, each namedtuple instance
    # also provides a few more helper methods you might find useful.
    # Their names all start with a single underscore character (_)
    # which usually signals that a method or property is “private”
    # and not part of the stable public interface of a class or module.
    #
    # _asdict() helper method. It returns the contents of a
    # namedtuple as a dictionary
    print(my_car._asdict())
    # OrderedDict([('color', 'red'), ('mileage', 3812.4)])
    #
    # useful helper is the _replace() function. It creates a
    # (shallow) copy of a tuple and allows you to selectively
    # replace some of its fields
    print(my_car._replace(color='blue'))
    # Car(color='blue', mileage=3812.4)
    #
    # Lastly, the _make() classmethod
    # can be used to create new instances
    # of a namedtuple from a sequence or iterable:
    print(Car._make(['red', 999]))
    # Car(color='red', mileage=999)
    #
    # collection.namedtuple is a memory-efficient shortcut to
    # manually define an immutable class in Python.
    # 
    # Namedtuples can help clean up your code by enforcing
    # an easier-to-understand structure on your data.
    # 
    # Namedtuples provide a few useful helper methods that
    # all start with a single underscore, but are part of the
    # public interface. It’s okay to use them.
