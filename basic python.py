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

