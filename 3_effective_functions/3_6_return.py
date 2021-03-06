#!/usr/bin/env python3
if __name__ == '__main__':
    # Python adds an implicit return None statement to the end of any function.
    # Therefore, if a function doesn’t specify a return value, it returns None by default.
    def foo1(value):
        if value:
            return value
        else:
            return None
    def foo2(value):
        """Bare return statement implies `return None`"""
        if value:
            return value
        else:
            return
    def foo3(value):
        """Missing return statement implies `return None`"""
        if value:
            return value
    
    # If a function doesn’t specify a return value, it returns None.
    # Whether to explicitly return None is a stylistic decision

    # This is a core Python feature but your code might communicate
    # its intent more clearly with an explicit return None statement.

