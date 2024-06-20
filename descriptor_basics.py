"""
this module we will learn descriptors and property

In general, a descriptor is an attribute value that has one of the
methods in the descriptor protocol. Those methods are __get__(),
__set__(), and __delete__(). If any of those methods are defined
for an attribute, it is said to be a descriptor.

The default behavior for attribute access is to get, set, or delete
 the attribute from an object's dictionary. For instance, a.x has a
   lookup chain starting with a.__dict__['x'],
   then type(a).__dict__['x']
   and continuing through the method resolution order of type(a).
   If the looked-up value is an object defining one of
   the descriptor methods, then Python may override the default
   behavior and invoke the descriptor method instead.
   Where this occurs in the precedence chain depends on
   which descriptor methods were defined.

"""
import logging
from abc import ABC, abstractmethod

file_name = __file__.split('.').pop(0)

log = logging.getLogger(file_name)
logging.basicConfig(
    filename=f'{file_name}.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

def test():
    log.info("this is a test!")

test()

# logger = logging.getLogger("test")
# handler = logging.FileHandler("testlog.log")
# logger.addHandler(handler)
# print(logger.handlers[0].baseFilename)


class Validator(ABC):
    """
    A validator is a descriptor for managed attribute access.
    Prior to storing any data, it verifies that the new value
    meets various type and range restrictions. If those restrictions
    aren't met, it raises an exception to prevent data corruption
    at its source.

    This Validator class is both an abstract base class and a
    managed attribute descriptor:
    """

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {self.options!r}")


class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value!r} to be an int or float")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Expected {value!r} to be at least {self.minvalue!r}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Expected {value!r} to be no more than {self.maxvalue!r}")


class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r} to be an str")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f"Expected {value!r} to be no smaller than {self.minsize!r}"
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f"Expected {value!r} to be no bigger than {self.maxsize!r}"
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f"Expected {self.predicate} to be true for {value!r}")


class Component:

    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf("wood", "metal", "plastic")
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity


"""
    Component('Widget', 'metal', 5)  # Blocked: Widget is not all uppercase
    Traceback (most recent call last):
        ...
    ValueError: Expected <method 'isupper' of 'str' objects> to be true for 
    'Widget'

    Component('WIDGET', 'metle', 5)      # Blocked: 'metle' is misspelled
    Traceback (most recent call last):
        ...
    ValueError: Expected 'metle' to be one of {'metal', 'plastic', 'wood'}

    Component('WIDGET', 'metal', -5)     # Blocked: -5 is negative
    Traceback (most recent call last):
        ...
    ValueError: Expected -5 to be at least 0

    Component('WIDGET', 'metal', 'V')    # Blocked: 'V' isn't a number
    Traceback (most recent call last):
        ...
    TypeError: Expected 'V' to be an int or float
"""

c = Component("WIDGET", "metal", 5)  # Allowed:  The inputs are valid

print(f"vars(c) is :{vars(c)}")

print(f"c.__dict__ is :{c.__dict__}")

print(f"dir(c) is : {dir(c)}")

print(f"c.name is {c.name}")


"""
class property(fget=None, fset=None, fdel=None, doc=None)
Return a property attribute.

fget is a function for getting an attribute value. fset is a function 
for setting an attribute value. fdel is a function for deleting 
an attribute value. And doc creates a docstring for the attribute.

A typical use is to define a managed attribute x:
"""


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


examplec = C()

# examplec.x = value will invoke the setter,
examplec.x = 10

# examplec.x will invoke the getter
print(f"examplec.x is {examplec.x}")

# This makes it possible to create read-only properties easily using
# property() as a decorator:


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


parrot = Parrot()
print(f"parrot.voltage is {parrot.voltage}")

# AttributeError: property 'voltage' of 'Parrot' object has no setter
try:
    parrot.voltage = 200000
except AttributeError as e:
    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    log.warning(f"{e.name} and {e.args}")
    # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


"""
@getter
@setter
@deleter
A property object has getter, setter, and deleter methods usable 
as decorators that create a copy of the property with 
the corresponding accessor function set to the decorated function. 
This is best explained with an example:

"""


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


"""


This code is exactly equivalent to the first example. 
Be sure to give the additional functions the same name 
as the original property (x in this case.)

The returned property object also has the attributes fget, fset, 
and fdel corresponding to the constructor arguments.

"""
