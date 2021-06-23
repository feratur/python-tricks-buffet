#!/usr/bin/env python3
if __name__ == '__main__':
    # cloning standard collections (shallow copies though)
    from abc import ABCMeta, abstractmethod
    class Base(metaclass=ABCMeta):
        @abstractmethod
        def foo(self):
            pass
        @abstractmethod
        def bar(self):
            pass
    class Concrete(Base):
        def foo(self):
            pass
    # OR
    from abc import ABC
    class Base(ABC):
        @abstractmethod
        def foo(self):
            pass
        @abstractmethod
        def bar(self):
            pass
    class Concrete(Base):
        def foo(self):
            pass

    assert issubclass(Concrete, Base)

    # >>> c = Concrete()
    # TypeError:
    # "Can't instantiate abstract class Concrete
    # with abstract methods bar"

    # Subclasses of Base raise a TypeError at instantiation time whenever
    # we forget to implement any abstract methods.
