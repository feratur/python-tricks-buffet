#!/usr/bin/env python3
if __name__ == '__main__':
    # Class variables are declared inside the class definition
    # (but outside of any instance methods).
    # modifying a class variable affects all object instances at the same time
    #
    # Instance variables are always tied to a particular object instance.
    # Their contents are not stored on the class, but on each individual object created from the class.
    class Dog:
        num_legs = 4 # <- Class variable
        def __init__(self, name):
            self.name = name # <- Instance variabl
    jack = Dog('Jack')
    assert jack.name == 'Jack'
    assert jack.num_legs == 4
    assert Dog.num_legs == 4
    Dog.num_legs = 6
    assert Dog.num_legs == 6
    assert jack.num_legs == 6
    jack.num_legs = 8 # this is not assignment to class var, this is creation of instance var
    assert Dog.num_legs == 6
    assert jack.num_legs == 8
    assert jack.__class__.num_legs == 6
    class CountedObject:
        num_instances = 0
        def __init__(self):
            self.__class__.num_instances += 1
    print(CountedObject.num_instances) # 0
    print(CountedObject().num_instances) # 1
    print(CountedObject().num_instances) # 2
    print(CountedObject().num_instances) # 3
    print(CountedObject.num_instances) # 3
    # WARNING: This implementation contains a bug
    class BuggyCountedObject:
        num_instances = 0
        def __init__(self):
            self.num_instances += 1 # !!!
    print(BuggyCountedObject.num_instances) # 0
    print(BuggyCountedObject().num_instances) # 1
    print(BuggyCountedObject().num_instances) # 1
    print(BuggyCountedObject().num_instances) # 1
    print(BuggyCountedObject.num_instances) # 0
    # Class variables are for data shared by all instances of a class.
    # They belong to a class, not a specific instance and are shared among all instances of a class.
    #
    # Instance variables are for data that is unique to each instance.
    # They belong to individual object instances and are not shared
    # among the other instances of a class. Each instance variable
    # gets a unique backing store specific to the instance.
    #
    # Because class variables can be “shadowed” by instance variables of the same name,
    # it’s easy to (accidentally) override class variables in a way that introduces bugs and odd behavior.
