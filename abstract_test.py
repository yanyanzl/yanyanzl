'''

Use the abc module to create abstract classes. 
Use the abstractmethod decorator to declare a method abstract, 
and declare a class abstract using one of three ways, depending upon your Python version.

In Python 3.4 and above, you can inherit from ABC. In earlier versions of Python, 
you need to specify your class's metaclass as ABCMeta. 
Specifying the metaclass has different syntax in Python 3 and Python 2. 
The three possibilities are shown below:

Whichever way you use, you won't be able to instantiate an abstract class that has abstract methods, 
but will be able to instantiate a subclass that provides concrete definitions of those methods:

'''


# Python 3.4+
from abc import ABC, abstractmethod

class Abstract(ABC):
    # pass
    @abstractmethod
    def foo(self):
        pass

# ab = Abstract()

class StillAbstract(Abstract):
    pass

# ab = StillAbstract()

class Concrete(Abstract):
    def foo(self):
        print("this is a concrete class")

ab = Concrete()
ab.foo()



# Python 3.0+
from abc import ABCMeta, abstractmethod
class Abstract(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

# Python 2
from abc import ABCMeta, abstractmethod
class Abstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass




