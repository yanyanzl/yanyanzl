'''
The Built-In Namespace
The built-in namespace contains the names of all of Python’s built-in objects. 
These are available at all times when Python is running. 
You can list the objects in the built-in namespace with the following command:
dir(__builtins__)

The Python interpreter creates the built-in namespace when it starts up. 
This namespace remains in existence until the interpreter terminates.

'''




print("hello".replace("e",'aaaa'))

price = 59 
txt = f"The price is {price} dollars" 
print(txt)


price = 59 
txt = f"The price is {price:.2f} dollars" 
print(txt)

# print(memoryview(5))

list_n = [1,2,3,4,5,2,2,2]
set_n = (1,2,3,4,4,5)

print(f"number of 2 in the list is {list_n.count(2)}")

print(f"min of list is {min(list_n)}, max of list is {max(list_n)}")

print(f"index of the occurence of 2 in list is {list_n.index(2,6,7)}")

print(f"length of list is : {len(list_n)}")

print(f" 3 * list is {3 * list_n}")

print(f"[3] + list is {[3] + list_n}")

print(f"slice of the list from 2 to 6 is {list_n[2:6]}")

print(f"slice of the list from 2 to 6 with step of 2 is {list_n[2:6:2]}")


print(f"binary format of 100 is {bin(100)}")

print(f"chr(19999) is {chr(19999)}")
print(f"好 ord() is {ord('好')}")

print(f"ascii('this is 好') is {ascii('this is 好')}")
print(f"hex(22909) is {hex(22909)}")

print(f"int(597d,16) is {int('597d',16)}")

print(f"dir(int) is {dir(int)}")


      

''' 
i = 1
while i < 7:
    print(next(list_n, 6))
    i += 1

'''