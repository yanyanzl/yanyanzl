# Python basics


### data Types

    - A list in Python is an inbuilt collection of items that can contain elements of multiple data types, which may be either numeric, character logical values, etc. It is an ordered collection supporting negative indexing. A list can be created using [] containing data values. Contents of lists can be easily merged and copied using Python’s inbuilt functions. 
    - x = {"apple", "banana", "cherry"}     Set
    - x = ("apple", "banana", "cherry")     Tuples
    - x = {"name" : "John", "age" : 36}     dict
    - x = b"Hello"   Bytes
    - x = bytearray(5)    Bytes Array


### Using Requirement Files
- A requirements file is a list of all of a project’s dependencies. This includes the dependencies needed by the dependencies. It also contains the specific version of each dependency, specified with a double equals sign (==).

    - pip freeze will list the current projects dependencies to stdout.
    - This shell command will export this as a file named requirements.txt:
        - pip freeze > requirements.txt

    - Once you’ve got your requirements file, you can head over to a different computer or new virtual environment and run the following:
        - pip install -r requirements.txt
### arguments
    - By default, arguments may be passed to a Python function either by position or explicitly by keyword.

    ``` Python
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
    ```
    
    - Positional-only parameters are placed before a / (forward-slash). The / is used to logically separate the positional-only parameters from the rest of the parameters. If there is no / in the function definition, there are no positional-only parameters.
    - To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.

    ``` Python
    def standard_arg(arg):
         print(arg)
    
     def pos_only_arg(arg, /):
         print(arg)

     def kwd_only_arg(*, arg):
         print(arg)
        
     def combined_example(pos_only, /, standard, *, kwd_only):
         print(pos_only, standard, kwd_only)
    
    ```

    - When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a function like this:
    
    ``` Python
    def cheeseshop(kind, *arguments, **keywords):
        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
            print(arg)
        print("-" * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])
        
    ```

### **params

    - Consider a function with default arguments:
        ``` Python
        def func(foo=3):
            print(foo)
            
        The structure of the arguments is (in principle) very similar to a dictionary. 
        The function foo has (essentially) a dictionary of default arguments 
        (in this case {'foo':3}). Now, lets say that you don't want to use 
        the keyword in the function call, but you want to use a dictionary 
        instead -- then you can call foo as:
            d = {"foo":8}
            func(**d)
        
        This allows you to dynamically change what arguments you are passing to the function func.

        This become a little more interesting if you try the following:
            d = {"foo":8, "bar":12}
            func(**d)
        This doesn't work (it is equivalent to foo(foo=8, bar=12), but since bar isn't a valid argument, it fails).
        
        You can get around that problem by giving those extra arguments a place to go inside the definition of foo.
            def func( foo=3, **kwargs ):
                print(foo,kwargs)
        now try:
            d = {"foo":8, "bar":12}
            func(**d)  #prints (8, {'bar':12})        
            
        This can also be called as:
            func(foo=8, bar=12)
        
        This is often useful if funcA calls funcB and you want funcA to accept all of the keywords of funcB (plus a few extra) which is a very common thing when dealing with classes and inheritance:
            def funcA(newkey=None,**kwargs): 
                funcB(**kwargs)    
        ```
        
###     Lambda Expressions

    Small anonymous functions can be created with the lambda keyword. 
    This function returns the sum of its two arguments: lambda a, b: a+b. 
    Lambda functions can be used wherever function objects are required. 
    They are syntactically restricted to a single expression. 
    Semantically, they are just syntactic sugar for a normal function definition. 
    Like nested function definitions, lambda functions can reference variables 
    from the containing scope:
        def make_incrementor(n):
             return lambda x: x + n

### Arbitrary Argument Lists
 - the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see Tuples and Sequences). Before the variable number of arguments, zero or more normal arguments may occur.
    - def write_multiple_items(file, separator, *args):
        file.write(separator.join(args))















