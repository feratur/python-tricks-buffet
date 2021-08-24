#!/usr/bin/env python3
if __name__ == '__main__':
    # Functions are first-class citizens
    func_dict = {
        'cond_a': lambda x: x ** 2,
        'cond_b': lambda x: x * (-1),
    }
    def check_cond(cond, value):
        func_dict.get(cond, lambda x: x)(value)
    
    # Too verbose
    def dispatch_if(operator, x, y):
        if operator == 'add':
            return x + y
        elif operator == 'sub':
            return x - y
        elif operator == 'mul':
            return x * y
        elif operator == 'div':
            return x / y
    
    dispatch_if('mul', 2, 8)
    # 16
    dispatch_if('unknown', 2, 8)
    # None

    def dispatch_dict(operator, x, y):
        return {
            'add': lambda: x + y,
            'sub': lambda: x - y,
            'mul': lambda: x * y,
            'div': lambda: x / y,
        }.get(operator, lambda: None)()

    dispatch_dict('mul', 2, 8)
    # 16
    dispatch_dict('unknown', 2, 8)
    # None

    # Every time we call dispatch_dict(), it creates a temporary dictionary and
    # a bunch of lambdas for the opcode lookup. This isn’t ideal from a performance perspective.
    # For code that needs to be fast, it makes more sense to create the dictionary once as a constant
    # and then to reference it when the function is called. We don’t want to recreate the
    # dictionary every time we need to do a lookup.

    # The operator module provides implementations for all of Python’s operators, for
    # example operator.mul, operator.div, and so on.

    # Python doesn’t have a switch/case statement. But in some cases
    # you can avoid long if-chains with a dictionary-based dispatch
    # table.
    #
    # Once again Python’s first-class functions prove to be a powerful
    # tool. But with great power comes great responsibility.
