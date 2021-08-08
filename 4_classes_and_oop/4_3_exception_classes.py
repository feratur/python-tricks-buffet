#!/usr/bin/env python3
if __name__ == '__main__':
    class NameTooShortError(ValueError):
        pass
    
    def validate(name):
        if len(name) < 10:
            raise NameTooShortError(name)

    # Whenever you’re publicly releasing a Python package,
    # or even if you’re creating a reusable module for your company,
    # it’s good practice to create a custom exception base class for
    # the module and then derive all of your other exceptions from it

    # Derive your custom exceptions from Python’s built-in Exception class or
    # from more specific exception classes like ValueError or KeyError.
    # You can use inheritance to define logically grouped exception hierarchies.
