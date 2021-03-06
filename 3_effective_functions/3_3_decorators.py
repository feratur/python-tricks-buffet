#!/usr/bin/env python3
if __name__ == '__main__':
    # a decorator is a callable that takes a callable as input and returns another callable
    def null_decorator(func):
        return func
    def greet():
        return 'Hello!'
    greet = null_decorator(greet)
    
    @null_decorator
    def greet():
        return 'Hello!'
    greet()
    
    def uppercase(func):
        def wrapper():
            original_result = func()
            modified_result = original_result.upper()
            return modified_result
        return wrapper

    @uppercase
    def greet():
        return 'Hello!'
    print(greet())

    def strong(func):
        def wrapper():
            return '<strong>' + func() + '</strong>'
        return wrapper
    def emphasis(func):
        def wrapper():
            return '<em>' + func() + '</em>'
        return wrapper
    
    @strong
    @emphasis
    def greet():
        return 'Hello!'
    print(greet())

    def trace(func):
        def wrapper(*args, **kwargs):
            print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
            original_result = func(*args, **kwargs)
            print(f'TRACE: {func.__name__}() returned {original_result!r}')
            return original_result
        return wrapper

    @trace
    def say(name, line):
        return f'{name}: {line}'
    say('Jane', 'Hello, World')

    # the original function name, its docstring, and parameter list are hidden by the wrapper closure
    # You can use functools.wraps in your own decorators to copy over the lost metadata from the
    # undecorated function to the decorator closure
    import functools
    def uppercase(func):
        @functools.wraps(func)
        def wrapper():
            return func().upper()
        return wrapper
