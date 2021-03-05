#!/usr/bin/env python3
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], 'Discount must be lower than initial price, but not negative'
    return price

if __name__ == '__main__':
    shoes = {'name': 'Fancy Shoes', 'price': 14900}
    
    assert apply_discount(shoes, 0.25) == 11175
    print('apply_discount() positive scenario passed')
    
    try:
        apply_discount(shoes, 2.0)
    except AssertionError:
        print('apply_discount() negative scenario passed')
    
    # Assertions are for unrecoverable errors, internal self-checks
    # indicate bugs in the code

    # assert_stmt ::= "assert" expression1 ["," expression2]

    # AssertionError is fired only if __debug__ global variable is set

    # if __debug__:
    #   if not expression1:
    #       raise AssertionError(expression2)

    # assertions can be globally disabled with the -O and -OO command line switches
    # as well as the PYTHONOPTIMIZE environment variable in CPython

    # Don't use assertions for data validation

    # assert(1 == 2, 'This should fail') - it won't fail
    # because non-empty tuple evaluates to True

    # assert 1 == 2, 'This should fail' - this would fail
