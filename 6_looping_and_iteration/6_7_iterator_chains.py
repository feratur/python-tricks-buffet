#!/usr/bin/env python3
if __name__ == '__main__':
    def integers():
        for i in range(1, 9):
            yield i
    def squared(seq):
        for i in seq:
            yield i * i
    def negated(seq):
        for i in seq:
            yield -i
    chain = negated(squared(integers()))
    list(chain)
    # [-1, -4, -9, -16, -25, -36, -49, -64]

    # data processing happens one element at a time.
    # There’s no buffering between the processing steps in the chain

    # Can also use gen expressions
    integers = range(8)
    squared = (i * i for i in integers)
    negated = (-i for i in squared)
    # The only downside to using generator expressions is that they can’t
    # be configured with function arguments, and you can’t reuse the same
    # generator expression multiple times in the same processing pipeline.

    # Generators can be chained together to form highly efficient and
    # maintainable data processing pipelines.
    #
    # Chained generators process each element going through the
    # chain individually.
    #
    # Generator expressions can be used to write concise pipeline definitions,
    # but this can impact readability.
