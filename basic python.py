"""
basic python knowledges to be learned
"""

import re

# regex
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid US 64')
        print (test_string, 'rejected')
        
        
parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
    
    
def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')


# list comprehension
lst = [1,2,3,4,5,6,7,8,9,10]
# with if condition
c = [x for x in lst if x > 4]
print(c)
 
# with multiple if 
d = [x for x in lst if x > 4 if x%2 == 0]
print(d)

# with if and else condition
e = [x if x > 4 else 'less than 4' for x in lst]
print(e)

# with more than one if and else condition
f = ['Two' if x%2 == 0 else "Three" if x%3 == 0 else 'not 2 & 3' for x in lst]
print(f)

# nested for loop. 
lst = [1,2,3]
lst_rev = [3,2,1]
g = [(x,y) for x in lst for y in lst_rev]
print(g)

# a set comprehension
quote = "life, uh, finds a way"

st = {char for char in quote if char in "aeiou"}
print(st)

# a dictionary comprehension
dc = {number:number * 2 for number in range(10)}
print(dc)

# enumerate function 
"""
Equivalent to:

def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
"""

seasons = ["Sprint", "Summer", "Autumn", "Winter"]
a = enumerate(seasons,1)
print(f"a is {a}")
b = list(enumerate(seasons))
print(f"b is {b}")

print(eval("33 + 22"))
# print(eval(input("bla...")))


array = [1,-1,-2,1,-3]
array.sort()
print(f"array.sort() : {array}")
print(f"runner up score is :{array[len(array)-2]}")

largest  = max(array)
print(f"max of array is {largest}")

array = sorted(array)
print(f"array sorted as {array}")

"""
Linked to, but not explicitly mentioned here, 
is exactly when __all__ is used. It is a list of strings 
defining what symbols in a module will be exported 
when from <module> import * is used on the module.

For example, the following code in a foo.py explicitly 
exports the symbols bar and baz:
NOTE: __all__ affects the from <module> import * behavior only. 
Members that are not mentioned in __all__ are still accessible 
from outside the module and can be imported with 
from <module> import <member>.

"""

__all__ = ['bar', 'baz']

waz = 5
bar = 10
def baz(): return 'baz'

"""
Single Underscore
In a class, names with a leading underscore indicate to other programmers 
that the attribute or method is intended to be be used inside that class. 
However, privacy is not enforced in any way. Using leading underscores for 
functions in a module indicates it should not be imported from somewhere else.

_single_leading_underscore: weak "internal use" indicator. 
E.g. from M import * does not import objects whose name starts with an 
underscore.



Double Underscore (Name Mangling)

From the Python docs:

Any identifier of the form __spam (at least two leading underscores, 
at most one trailing underscore) is textually replaced with _classname__spam,
 where classname is the current class name with leading underscore(s) stripped.
   This mangling is done without regard to the syntactic position of the 
   identifier, so it can be used to define class-private instance and class 
   variables, methods, variables stored in globals, and even variables 
   stored in instances. private to this class on instances of other classes.

"""


class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"


mc = MyClass()
""" 
>>> print mc.__superprivate
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: myClass instance has no attribute '__superprivate'
"""

print(mc._semiprivate)
# , world!
print(mc.__dict__)
# {'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}


"""
__future__ — Future statement definitions
Imports of the form from __future__ import feature are 
called future statements. These are special-cased by the 
Python compiler to allow the use of new Python features in 
modules containing the future statement before the release in 
which the feature becomes standard.


"""