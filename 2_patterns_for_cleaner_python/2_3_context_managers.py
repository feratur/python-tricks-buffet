#!/usr/bin/env python3
import os
from contextlib import contextmanager

class ManagedFile:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self.file:
            self.file.close()

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)

if __name__ == '__main__':
    f = open('hello.txt', 'w')
    try:
        f.write('hello, world')
    finally:
        f.close()

    # Below is the same
    with ManagedFile('hello.txt') as f:
        f.write('hello, world!')

    with managed_file('hello.txt') as f:
        f.write('hello, world!')
    
    os.remove('hello.txt')

    with Indenter() as indent:
        indent.print('hi!')
        with indent:
            indent.print('hello')
            with indent:
                indent.print('bonjour')
        indent.print('hey')
