#!/usr/bin/env python3
if __name__ == '__main__':
    # *args collects extra positional arguments as a tuple.
    # **kwargs collects the extra keyword arguments as a dictionary
    # args and kwargs are just recommended names
    def foo(x, *args, **kwargs):
        kwargs['name'] = 'Alice'
        new_args = args + ('extra', )
        bar(x, *new_args, **kwargs)
    
    # also useful for subclass constructors
    class Car:
        def __init__(self, color, mileage):
            self.color = color 
            self.mileage = mileage
    
    class AlwaysBlueCar(Car):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.color = 'blue'
    
    import functools
    # useful for decorators
    def trace(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            print(f, args, kwargs)
            result = f(*args, **kwargs)
            print(result)
        return decorated_function