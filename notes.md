* `__import__('mysum.py')` does not require __init__ function

* `__init__.py` ensures directory becomes a module

* Raise error on 6th iteration

* Test throwing of errors

* '-s' flag to show all the prints

* unittest
    * In unittest, setUp and tearDown methods run before each test
        * @classmethod

            def `setUpClass`(self):

    * class inherits unittest.TestCase

* pytest
    * @pytest.fixture for setUp and pass the method as param
    * `@pytest.mark.<markername>`
        * `pytest -m <markername>`
    * To make a fixture available to multiple test files, we have to define the fixture function in a file called conftest.py
    * Parameterizing Tests: Eg in test_parameterize
    * @pytest.mark.xfail: Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests. Details of these tests will not be printed even if the test fails
    * `@pytest.mark.skip`: Skipping a test means that the test will not be executed
    * run tests in parallel:
        * pip install pytest-xdist
        * pytest -n <num>

* String formatting
    * % operator:

        variable = 12

        string = "Variable as integer = %d 
        Variable as float = %f" %(variable, variable)

        print (string)

    * format() Method:

        ‘String here {} then also {}’.format(‘something1′,’something2’)

        print('a: {a}, b: {b}, c: {c}'.format(a = 1, b = 'Two', c = 12.3))

    * f-string:
        *   name = "Vishesh"

            f"My name is {name}."
        
        *   a = 5

            b = 10

            print(f"He said his age is {2 * (a + b)}.")

        * print(f"Formatted number: {num:.2f}")

            prints 2 decimal places

* ASCII value using ord('a')

* lambda functions:

    x = lambda a, b, c : a + b + c

    print(x(5, 6, 2))

* Dictionaries in python:
    * To delete an item:
        * del dict['key']
        * removed_value = my_dict.pop("key2")
        * val = my_dict.get("key", -1) --> for default value of -1
        * The `dict1.setdefault(key, defVal)` method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value.

* Set:
    * Sets in {}
    * For a set, True and 1 is considered the same value; 0 & False are same

* DefaultDict
    * defaultdict never raises a KeyError
    *   Syntax: d = defaultdict(default_factory)
        Parameters:  
        default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
    *   `__missing__` method
    *   from collections import defaultdict

* Inheritence:
    * child's `__init__()` function overrides the inheritance of the parent's `__init__()` function.

* Iterator:
To make a class/object iterator, implement `__iter()__` and `__next__()` methods
    * `__iter__()`: initializes the iteration
    * `__next__()`: Return next item
    * To prevent the iteration from going on forever, we can use the StopIteration statement. By raise StopIteration in next
    * Example in `iterator.py`

* JSON
    * JSON to Python: If you have a JSON string, you can parse it by using the json.loads() method.
    * Python to JSON: If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

* private members in a class start with double underscore
    * can be accessed as obj._ClassName__pvt_member
        * ClassName is the name of the class

* The Static methods neither use self nor cls parameter; general utility methods perform the task in isolation. Static methods in Python are similar to those found in Java and C++, and they can't modify the behavior of the class or instance.

* @staticmethod decorator
* @classmethod decorator

* Decorators:

        @gfg_dec
        def hello():
            print("Hello")
        ''' Equivalent to:
        def hello():
            print("Hello")
        hello = gfg_dec(hello)
        '''
    * In the above code, gfg_decorator is a callable function, that will add some code on the top of some another callable function, hello_decorator function and return the wrapper function.
    * Eg:

            def hello_decorator(func):
                
                def inner1(*args, **kwargs):
                    
                    print("before Execution")
                    
                    # getting the returned value
                    returned_value = func(*args, **kwargs)
                    print("after Execution")
                    
                    # returning the value to the original frame
                    return returned_value
                    
                return inner1
    
    
            # adding decorator to the function
            @hello_decorator
            def sum_two_numbers(a, b):
                print("Inside the function")
                return a + b
            
            a, b = 1, 2
    
            # getting the value through return of the function
            print("Sum =", sum_two_numbers(a, b))


    '''Output:
        before Execution
        Inside the function
        after Execution
        Sum = 3
    '''

* sorting using comparators:
    * reverse = True
    * sorted() sorts in a new list; l.sort() is inplace
    * using comparator function (old way):
        import functools

        def cmp(p1: Person, p2: Person):
            if p1.name == p2.name:
                return p1.age-p2.age
            return p1.name > p2.name

        l.sort(key=functools.cmp_to_key(cmp))

    * new way:
        l.sort(key=lambda p: (p.name, -p.age))

* *args receives values as a tuple
* **kwargs receives values as a dictionary

* JSON parsing:
    * handle KeyError exception

* Python Regex:
    
    * import re
    * re.findall(): list of all matches
    * re.search(): Returns a match object (span, string, group)
    * re.split(): Returns list where string split at each match
    * re.sub(): Replaces one or many string with match
    * Dot(.) symbol matches only a single character except for the newline character (\n).

* divmod(29, 7) = (4, 1)

* Try... Except...
    * try, except, else, finally

* To throw an exception:
    * Eg1- raise Exception('Message')
    * Eg2- raise TryError('Message)

* User Input:
    * x, y = map(int, input().split())

* Exceptions:
    * SyntaxError
    * TypeError: Raised when an operation or function on obj of wrong data type
    * NameError: When function or variable not found in scope
    * IndexError: index out of range
    * KeyError: when key not found in dictionary
    * ValueError: function or method called with invalid argument/input.
        * Eg: int('12a3')
    * AttributeError: method or attribute not found on object
    * IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
    * ZeroDivisionError
    * ImportError

* `strip()` function to trim white space

* URL:
    * from url.parse import urlsplit
        * splits into scheme, netloc, path, query, fragments
    * To split the query into dictionary:
        * use parse_qs(spliturl.query)

## BugSquash Tips:

* First look for reason for the test

* See what is executed before test:
    * setUp/TearDown function
    * pytest.fixtures
        * fixtures may be in `conftest.py` module
        * Look for `autouse` param in fixtures
        * see `PythonTesting/test_fixture_autouse.py` to understand about setUp and TearDown of PyTest
        * 