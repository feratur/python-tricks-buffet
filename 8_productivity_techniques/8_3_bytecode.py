#!/usr/bin/env python3
if __name__ == '__main__':
    # the bytecode resulting from this compilation step is cached on disk in 
    # .pyc (cached bytecode of imported modules) and .pyo (same, but for optimised flag -O), also .pyd (Windows only)
    # files so that executing the same Python file is faster the second time around.
    def greet(name):
        return 'Hello, ' + name + '!'
    
    # Each function has a __code__ attribute (in Python 3) that we can use
    # to get at the virtual machine instructions, constants, and variables
    # used by our greet function
    greet.__code__.co_code
    # b'dx01|x00x17x00dx02x17x00Sx00'
    greet.__code__.co_consts
    # (None, 'Hello, ', '!')
    greet.__code__.co_varnames
    # ('name',)

    import dis
    dis.dis(greet)
    # 2 0 LOAD_CONST 1 ('Hello, ')
    # 2 LOAD_FAST 0 (name)
    # 4 BINARY_ADD
    # 6 LOAD_CONST 2 ('!')
    # 8 BINARY_ADD
    # 10 RETURN_VALUE

    # CPython executes programs by first translating them into an intermediate bytecode
    # and then running the bytecode on a stack-based virtual machine.
    #
    # You can use the built-in dis module to peek behind the scenes and inspect the bytecode.
    #
    # Study up on virtual machines — it’s worth it
    # (book Compiler Design: Virtual Machines by Wilhelm and Seidl).
