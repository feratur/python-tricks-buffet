#!/usr/bin/env python3
if __name__ == '__main__':
    def repeater(value):
        while True:
            yield value
    # Infinite iterator
    for x in repeater('Hi'):
        print(x)
    
    # calling a generator function doesn’t even run the function.
    # It merely creates and returns a generator object
    # The code in the generator function only executes when next()
    # is called on the generator object

    # When a yield is invoked, it also passes control back to
    # the caller of the function — but it only does so temporarily.
    # local variables and the execution state of the generator function
    # are only stashed away temporarily and not thrown out completely.
    # Execution can be resumed at any time by calling next() on the generator

    # Generators are fully compatible with class-based iterators,
    # they also throw StopIteration exception behind the scenes.
    # Generators stop generating values as soon as control flow
    # returns from the generator function by any means other than a yield statement.
    def repeat_three_times(value):
        yield value
        yield value
        yield value
    # As soon as we reach the end of the generator function,
    # it keeps raising StopIteration to signal that it has no more values to provide
    def bounded_repeater(value, max_repeats):
        count = 0
        while True:
            if count >= max_repeats:
                return
            count += 1
            yield value
    def bounded_repeater_new(value, max_repeats):
        for i in range(max_repeats):
            yield value
    
    # Generator functions are syntactic sugar for writing objects that
    # support the iterator protocol. Generators abstract away much of
    # the boilerplate code needed when writing class-based iterators.
    #
    # The yield statement allows you to temporarily suspend execution
    # of a generator function and to pass back values from it.
    #
    # Generators start raising StopIteration exceptions after control
    # flow leaves the generator function by any means other than a yield statement.
