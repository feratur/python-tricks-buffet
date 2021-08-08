#!/usr/bin/env python3
if __name__ == '__main__':
    class MyClass:
        def method(self):
            return 'instance method called', self
        @classmethod
        def classmethod(cls):
            return 'class method called', cls
        @staticmethod
        def staticmethod():
            return 'static method called'
    
    MyClass.method(MyClass()) # same as MyClass().method()
    MyClass().classmethod() # same as MyClass.classmethod()
    # or MyClass().__class__.classmethod()
    # MyClass.method() causes TypeError
    #
    # Instance methods need a class instance and can access the instance through self.
    #
    # Class methods don’t need a class instance. They can’t access the instance (self)
    # but they have access to the class itself via cls.
    #
    # Static methods don’t have access to cls or self. They work like regular functions
    # but belong to the class’ namespace.
    #
    # Static and class methods communicate and (to a certain degree) enforce developer
    # intent about class design. This can have definite maintenance benefits.
