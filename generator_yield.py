"""
this is a module to learn Generators and yield
producer and consumer

Have you ever had to work with a dataset so large that it overwhelmed 
your machine’s memory? Or maybe you have a complex function that needs 
to maintain an internal state every time it’s called, but the function 
is too small to justify creating its own class. In these cases and 
more, generators and the Python yield statement are here to help.

There are differences among these, but the basic idea is the same:
 provide a kind of function that can return an intermediate 
 result (“the next value”) to its caller, but maintaining 
 the function’s local state so that the function can be resumed 
 again right where it left off. A very simple example:

"""

from __future__ import generators

def fib():
    a, b = 0, 1
    # while True: or 
    while b < 10000:
       
       yield b
       a, b = b, a+b

"""
When fib() is first invoked, it sets a to 0 and b to 1, then yields b 
back to its caller. The caller sees 1. When fib is resumed, from its 
point of view the yield statement is really the same as, say, a print 
statement: fib continues after the yield with all local state intact. 
a and b then become 1 and 1, and fib loops back to the yield, yielding
 1 to its invoker. And so on. From fib’s point of view it’s just 
 delivering a sequence of results, as if via callback. But from its 
 caller’s point of view, the fib invocation is an iterable object that
   can be resumed at will. As in the thread approach, this allows both
     sides to be coded in the most natural ways; but unlike the thread
       approach, this can be done efficiently and on all platforms. 
       Indeed, resuming a generator should be no more expensive 
       than a function call.
a Python generator is a kind of Python iterator, but of an 
especially powerful kind.

This looks like a typical function definition, except for the 
Python yield statement and the code that follows it. 
yield indicates where a value is sent back to the caller, 
but unlike return, you don’t exit the function afterward.

Instead, the state of the function is remembered. That way, 
when next() is called on a generator object (either explicitly or 
implicitly within a for loop), the previously yielded variable num is 
incremented, and then yielded again. Since generator functions look 
like other functions and act very similarly to them, you can assume 
that generator expressions are very similar to other comprehensions 
available in Python.

"""


print(f"fib() is {fib()}")
for i in range(10):
    print(f"the {i}th element in fib() is {fib()}")

for i in fib():
    print(i)


x = fib()
print(f"x is {x}")
for i in range(10):
    print(f"x is {next(x)}")


"""
Take a closer look at that last call to next(). 
You can see that execution has blown up with a traceback. 
This is because generators, like all iterators, can be exhausted.
 Unless your generator is infinite, you can iterate through it 
 one time only. Once all values have been evaluated, 
 iteration will stop and the for loop will exit. If you used next(), 
 then instead you’ll get an explicit StopIteration exception.

"""
def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))


# try except to handle the exception
letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)


"""

Like list comprehensions, generator expressions allow you to quickly
 create a generator object in just a few lines of code. They’re also 
 useful in the same cases where list comprehensions are used, with 
 an added benefit: you can create them without building and holding 
 the entire object in memory before iteration. In other words, 
 you’ll have no memory penalty when you use generator expressions. 
 Take this example of squaring some numbers:

"""
# this is a list comprehension
nums_squared_lc = [num**2 for num in range(100)]
print(f"nums_squared_lc is : {nums_squared_lc} ")

# this is a generator
nums_squared_gc = (num**2 for num in range(100))
print(f"nums_squared_gc is : {nums_squared_gc} and next is {next(nums_squared_gc)}")
print(f"nums_squared_gc is : {nums_squared_gc} and next is {next(nums_squared_gc)}")

import sys
print(f" the size of nums_squared_lc is {sys.getsizeof(nums_squared_lc)}")
print(f" the size of nums_squared_gc is {sys.getsizeof(nums_squared_gc)}")


"""
In addition to yield, generator objects can make use of the following
 methods:
    .send()
    .throw()
    .close()

generator.send(value)
Resumes the execution and “sends” a value into the generator function. 
The value argument becomes the result of the current yield expression.
 The send() method returns the next value yielded by the generator, 
 or raises StopIteration if the generator exits without yielding 
 another value. When send() is called to start the generator, 
 it must be called with None as the argument, because there is no 
 yield expression that could receive the value.

This program will print numeric palindromes like before, but with a few
 tweaks. Upon encountering a palindrome, your new program will add a 
 digit and start a search for the next one from there. You’ll also 
 handle exceptions with .throw() and stop the generator after a given 
 amount of digits with .close()

"""

def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                print("start from here")
                value = (yield value)  # it stops here everytime and back here also.
                print(f"end with value  {value}")
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")

generator = echo(1)

print(next(generator))

# print(next(generator))

print(generator.send(100))

generator.throw(TypeError, "spam")

generator.close()





import math
def rooter():
    while True:
        x = yield
        print(f"x is {x}")
        yield math.sqrt(x)

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False
    
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()
root = rooter()
next(root)
for i in range(10):
    num = root.send(i)
    print(f"num is {num}")
    
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
        # alternatively, you can use a throw to do the same. 
        # pal_gen.throw(ValueError("We don't like large palindromes"))
    # root.send(digits)
    pal_gen.send(10 ** (digits))


"""
producer and consumer solution
"""

from time import sleep
from random import random
from threading import Thread
from queue import Queue
 
# producer task
def producer(queue):
    print('Producer: Running')
    # generate items
    for i in range(10):
        # generate a value
        value = random()
        # block, to simulate effort
        sleep(value)
        # create a tuple
        item = (i, value)
        # add to the queue
        queue.put(item)
        # report progress
        print(f'>producer added {item}')
    # signal that there are no further items
    queue.put(None)
    print('Producer: Done')
 
# consumer task
def consumer(queue):
    print('Consumer: Running')
    # consume items
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        # block, to simulate effort
        sleep(item[1])
        # report
        print(f'>consumer got {item}')
    # all done
    print('Consumer: Done')

def main():
    # create the shared queue
    queue = Queue()
    # start the consumer
    consumer = Thread(target=consumer, args=(queue,))
    consumer.start()
    # start the producer
    producer = Thread(target=producer, args=(queue,))
    producer.start()
    # wait for all threads to finish
    producer.join()
    consumer.join()