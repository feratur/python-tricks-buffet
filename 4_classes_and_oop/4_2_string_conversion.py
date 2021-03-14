#!/usr/bin/env python3
if __name__ == '__main__':
    class Car:
        def __init__(self, color, mileage):
            self.color = color
            self.mileage = mileage
        def __str__(self):
            return f'a {self.color} car'
        def __repr__(self):
            return '__repr__ for Car'
    
    my_car = Car('red', 37281)
    # a red car
    print(my_car)
    assert str(my_car) == 'a red car'
    
    # Note
    # containers like lists and dicts always use the result of __repr__ to represent the objects they contain
    assert str([my_car]) == '[__repr__ for Car]'

    # With __repr__, the idea is that its result should be, above all, unambiguous
    # >>> repr(today)
    # 'datetime.date(2017, 2, 2)'
    # valid Python code to recreate the original date object

    # If you don’t add a __str__ method, Python falls back on the result of __repr__ when looking for __str__
    class Car:
        def __init__(self, color, mileage):
            self.color = color
            self.mileage = mileage
        def __repr__(self):
            # note !r
            # the output string uses repr(self.color) and repr(self.mileage)
            # instead of str(self.color) and str(self.mileage)
            
            #return f'Car({self.color!r}, {self.mileage!r})'
            def __repr__(self):
                return (f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})')

