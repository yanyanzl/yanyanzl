

'''
this is a module to learn the basics for the decorators in Python

'''

'''
First-Class Objects
Python supports many functional programming concepts, 
including treating functions as first-class objects.

This means that functions can be passed around and used as arguments, 
just like any other object like str, int, float, list, and so on. 
Consider the following three functions:

'''

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(f"greet_bob(say_hello) is {greet_bob(say_hello)}")
print(f"greet_bob(be_awesome) is {greet_bob(be_awesome)}")

'''
This is an important distinction that’s crucial for how functions work as first-class objects.
A function name without parentheses is a reference to a function, 
while a function name with trailing parentheses calls the function and refers to its return value.


Functions as Return Values
Python also allows you to return functions from functions. 
In the following example, you rewrite parent() to return one of the inner functions:
you didn’t add parentheses to the inner functions, such as first_child, upon returning. 
That way, you got a reference to each function that you could call in the future.

'''
def parent(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child
    else:
        return second_child
    
first = parent(1)
second = parent(2)

print(f"first() is {first()}")
print(f"second() is {second()}")



''' 
Simple Decorators in Python
Now that you’ve seen that functions are just like any other object in Python, 
you’re ready to move on and see the magical beast that is the Python decorator. You’ll start with an example:

'''

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)

'''
Here, you have defined two regular functions, decorator() and say_whee(), 
and one inner wrapper() function. 
Then you redefined say_whee() to apply decorator() to the original say_whee().
In effect, the name say_whee now points to the wrapper() inner function. 
Remember that you return wrapper as a function when you call decorator(say_whee):

However, wrapper() has a reference to the original say_whee() as func, 
and it calls that function between the two calls to print().

Put simply, a decorator wraps a function, modifying its behavior.
wrapper() is a regular Python function, the way a decorator modifies a function can change dynamically.
'''
print(f"id(say_whee) is {id(say_whee)}")

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 18:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
say_whee()

'''
Adding Syntactic Sugar
Python allows you to use decorators in a simpler way with the @ symbol, 
sometimes called the pie syntax. 
The following example does the exact same thing as the first decorator example:
@decorator is just a shorter way of saying say_whee = decorator(say_whee). 
It’s how you apply a decorator to a function.
'''
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee! with @ as decorator")

say_whee()

# So, @decorator is just a shorter way of saying say_whee = decorator(say_whee). 
# It’s how you apply a decorator to a function.

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_hello():
    print("hello decorator!")

say_hello() 


'''
Decorating Functions With Arguments
the inner function wrapper_do_twice() doesn’t take any arguments, 
but you passed name="World" to it. You could fix this by letting wrapper_do_twice() accept one argument, 
but then it wouldn’t work for the say_whee() function that you created earlier.

The solution is to use *args and **kwargs in the inner wrapper function. 
Then it’ll accept an arbitrary number of positional and keyword arguments
'''

def do_twice_args(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice_args
def say_hello(name):
    print("hello decorator with name: !", name)

@do_twice_args
def say_hello_no():
    print("hello decorator with name: !")


say_hello("steven") 
say_hello_no()

'''
You use the same decorator, @do_twice, to decorate two different functions. 
This hints at one of the powers of decorators. 
They add behavior that can apply to many different functions.

'''

'''
Returning Values From Decorated Functions
What happens to the return value of decorated functions? Well, 
that’s up to the decorator to decide. Say you decorate a simple function as follows:
you need to make sure the wrapper function returns the return value of the decorated function.
'''

def do_twice_return(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice_return
def say_hi(name):
    print("say hi with return to :", name)
    return f"Hi {name}"


name  = say_hi("Steven")
print(f"name is : {name}")

'''
A great convenience when working with Python, especially in the interactive shell, 
is its powerful introspection ability. 
Introspection is the ability of an object to know about its own attributes at runtime. 
For instance, a function knows its own name and documentation:

'''
print(f"say_hi is : {say_hi}")

print(f"say_hi.__name__ is : {say_hi.__name__}")

# print(f"help(say_hi) : {help(say_hi)}") 


'''
However, after being decorated, say_whee() has gotten very confused about its identity. 
It now reports being the wrapper_do_twice() inner function inside the do_twice() decorator. 
Although technically true, this isn’t very useful information.

To fix this, decorators should use the @functools.wraps decorator, 
which will preserve information about the original function. 

the following will be a good boilerplate template for building more complex decorators.
'''
import functools

def do_twice_intro(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice_intro
def say_intro():
    '''
    this is a function keep it's own introduction
    '''
    print("intro infomation kept for itself now!")

print(f"say_intro is : {say_intro}")
print(f"say_intro.__name__ is : {say_intro.__name__}")
# print(f"help(say_intro) : {help(say_intro)}") 


'''
Timing Functions
You’ll start by creating a @timer decorator. 
It’ll measure the time a function takes to execute and then print the duration to the console. 
Here’s the code:

'''

import functools
import time

def timer(func):
    ''' Print the runtime of the decorated function. '''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_time(num_times):
    x = 0
    for _ in range(num_times):
        x += sum([number ** 2 for number in range(10000)])
    print(f"x is {x}")

waste_time(1)
waste_time(1000)

'''
Debugging Code
The following @debug decorator will print a function’s arguments and 
its return value every time you call the function:

'''
import functools

def debug(func):
    ''' Print the function signature and return value '''
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"how are you, {name}"
    else:
        return f"whoa, {name}! {age} already, you are growing up"
    
make_greeting("steven")

make_greeting("steven", 116)

'''
you also apply a decorator to a function that has already been defined. 
below you decorate factorial() from the math standard library. 
You can’t use the pie syntax, but you can still manually apply the decorator.

'''
import math

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

print(f"approximate_e(6) is : {approximate_e(6)}")


'''
Slowing Down Code
In this section, you’ll create a decorator that slows down your code. 
This might not seem very useful. Why would you want to slow down your Python code?

Probably the most common use case is that you want to rate-limit a function 
that continuously checks whether a resource—like a web page—has changed. 
The @slow_down decorator will sleep one second before it calls the decorated function:


'''

import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(5)
''' 
Registering Plugins
Decorators don’t have to wrap the function that they’re decorating. 
They can also simply register that a function exists and return it unwrapped. 
You can use this, for example, to create a lightweight plugin architecture:
'''
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

# print(register.__code__)

@register
def say_hi1(name):
    return f"Hi {name} !"

@register
def say_hi2(name):
    return f"Yo {name}, together we are brilliant!"

print(f"PLUGINS is :\n {PLUGINS}")
import random

def randomly_greet(name):
    # print(list(PLUGINS.items()))
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"using {greeter!r}")
    return greeter_func(name)

for i in range(6):
    print(f"randomly_greet('steven') is {randomly_greet('Steven')}")

''' 
Decorating Classes
There are two different ways that you can use decorators on classes. 
The first one is very close to what you’ve already done with functions: 
you can decorate the methods of a class. 
This was one of the motivations for introducing decorators back in the day.

Some commonly used decorators are even built-ins in Python, 
including @classmethod, @staticmethod, and @property. 
The @classmethod and @staticmethod decorators are used to define methods 
inside a class namespace that aren’t connected to a particular instance of that class. 
The @property decorator is used to customize getters and setters for class attributes. 
Expand the box below for an example using these decorators:
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("radius must be non-negative")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
    
'''
Inside Circle you can see several different kinds of methods.
Decorators are used to distinguish them:

    .cylinder_volume() is a regular method.
    .radius is a mutable property. It can be set to a different value. 
        However, by defining a setter method, 
        you do some error testing to make sure .radius isn’t 
        set to a nonsensical negative number. 
        Properties are accessed as attributes without parentheses.
    .area is an immutable property. Properties without .setter() methods 
        can’t be changed. Even though it’s defined as a method, 
        it can be retrieved as an attribute without parentheses.
    .unit_circle() is a class method. It’s not bound to one particular instance of Circle. 
        Class methods are often used as factory methods 
        that can create specific instances of the class.
    .pi() is a static method. It’s not really dependent on the Circle class, 
        except that it’s part of its namespace. 
        You can call static methods on either an instance or the class.
'''

'''
Nesting Decorators
    You can apply several decorators to a function at once by stacking them on top of each other:

'''
@debug
@do_twice_intro
def greetings(name):
    print(f"Hello hello {name}!")

greetings("Steven")

'''
The greeting is printed twice because of @do_twice. 
However, the output from @debug is only shown once, 
since it’s called before the @do_twice decorator. 
Observe the difference if you change the order of @debug and @do_twice:

'''

@do_twice_intro
@debug

def greetings1(name):
    print(f"Hello hello {name}!")

greetings1("Steven")

'''
Defining Decorators With Arguments
Sometimes, it’s useful to pass arguments to your decorators. 
For instance, @do_twice could be extended to a @repeat(num_times) decorator. 
The number of times to execute the decorated function could then be given as an argument.

'''
import functools
def repeat(num_times):
    def decorate_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorate_repeat

@repeat(6)
def greetings2(name):
    print(f"Greetings {name}!")

greetings2("Steven")


'''
Creating Decorators With Optional Arguments
With a little bit of care, you can also define decorators 
that can be used both with and without arguments. Most likely, 
you don’t need this, but it is nice to have the flexibility.

'''
import functools

def repeat1(_func=None, *, num_times=2):
    '''
    If you’ve called @name without arguments, 
    then the decorated function will be passed in as _func. 
    If you’ve called it with arguments, 
    then _func will be None, and some of the keyword arguments 
    may have been changed from their default values. 
    The asterisk in the argument list means that 
    you can’t call the remaining arguments as positional arguments.
    '''
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
    


'''
Using Classes as Decorators
The typical way to maintain state in Python is by using classes.
Recall that the decorator syntax @decorator is just a quicker way of 
saying func = decorator(func)
Therefore, if decorator is a class, 
it needs to take func as an argument in its .__init__() initializer. 
Furthermore, the class instance needs to be callable so that 
it can stand in for the decorated function.


'''
def greetings3():
    print("callable greetings3")
greetings3.__call__()

'''
Now, how does all this work internally? 
When you run something like callable_object(*args, **kwargs), 
Python internally translates the operation into callable_object.__call__(*args, **kwargs). 
The arguments to the regular function are the same as those used in .__call__(). 
In other words, whenever you call a callable object, 
Python automatically runs its .__call__() method 
behind the scenes using the arguments you’ve passed into the callable.


'''
class SampleClass:
    def method(self):
        print("You called method()!")

'''
In Python, everything is an object. 
    1. Classes like SampleClass are objects of type, 
    which you can confirm by calling type() with the class object as an argument or 
    by accessing the .__class__ attribute.
    
    2. The class constructor of SampleClass falls back to using type.__call__(). 
    That’s why you can call SampleClass() to get a new instance.

    3. So, class constructors are callable objects that 
    return new instances of the underlying class.

    4. In the example above, you can observe that method objects, 
    like sample_instance.method, also have a .__call__() special method that 
    turns them into callable objects. The main takeaway here is that to be callable, 
    an object needs to have a .__call__() method.

If you ever need to check whether a Python object is callable, 
    then you can use the built-in callable() function like in the following examples:

'''
sample_instance = SampleClass()
print(f"sampleclass is callable? {callable(SampleClass)}")
print(f"sample_instance is callable? {callable(sample_instance)}")

'''
If you want the instances of a given class to be callable, 
then you need to implement the .__call__() special method in the underlying class. 
This method enables you to call the instances of your class 
as you’d call regular Python functions.

Unlike other special methods, .__call__() doesn’t have special requirements for 
what arguments it must accept. It works like any other instance method in the sense 
that it takes self as its first argument and can take as many extra arguments as you need.


'''

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __call__(self):
        self.increment()

counter = Counter()
counter.increment()

print(f"counter.count is {counter.count}")

counter()
print(f"counter.count is {counter.count}")

counter()
print(f"counter.count is {counter.count}")

''' 
 there are no restrictions on how to write the .__call__() method in your custom classes. 
 So, you can make them take arguments, return values, and even cause side effects 
 like in your Counter class example.
'''

class PowerFactory:
    def __init__(self, exponent=2):
        self.exponent = exponent

    def __call__(self, base):
        return base**self.exponent
    
square_of = PowerFactory(2)
print(f"square_of(2) is {square_of(2)}")
print(f"square_of(6) is {square_of(6)}")


cube_of = PowerFactory(3)
print(f"cube_of(2) is {cube_of(2)}")
print(f"cube_of(6) is {cube_of(6)}")

'''
Defining a .__call__() method in custom classes allows 
you to use the instances of those classes as regular Python functions.

'''


