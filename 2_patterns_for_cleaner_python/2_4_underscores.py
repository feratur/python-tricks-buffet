#!/usr/bin/env python3
if __name__ == '__main__':
    # 1. Single Leading Underscore: "_var"
    # PEP 8 convention: variable for internal use

    # However, leading underscores do impact how names get imported from modules.
    # The following function
    #
    #  def _internal_func(): 
    #      return 42
    #
    # will not be imported in wildcard import case (unless overridden in __all__)
    # from my_module import *
    # _internal_func() - will not be available
    # BTW regular imports will work just fine
    # import my_module
    # my_module._internal_func()

    # 2. Single Trailing Underscore: "var_"
    # used for variables in case the name is already
    # taken by a Python keyword, ex "class_"

    # 3. Double Leading Underscore: "__var"
    # name mangling
    class Test:
        def __init__(self):
            self.foo = 11
            self._bar = 23
            self.__baz = 23
    t = Test()
    print(dir(t))
    # __baz is mangled -> '_Test__baz'
    
    # Mangling works even like that
    _MangledGlobal__mangled = 23
    class MangledGlobal:
        def test(self):
            # automatically expanded into _MangledGlobal__mangled
            return __mangled
    # Prints 23
    print(MangledGlobal().test())

    # PEP 8 recommends to use _var for non-public things
    # and __var only if class is intended for subclassing
    # and subclass should not see the attribute of the superclass

    # 4. Double Leading and Trailing Underscore: "__var__"
    # name mangling is not applied if a name starts and ends with double underscores
    # can be declared by user, but not recommended
    # because there are magic methods like __init__, __call__, etc.

    # 5. Single Underscore: "_"
    # indicate that a variable is temporary or insignificant
    # also special variable in most Python REPLs that represents
    # the result of the last expression evaluated by the interpreter
    # >>> 20 + 3
    # 23
    # >>> _
    # 23
    # >>> print(_)
    # 23