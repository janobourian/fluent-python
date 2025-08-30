# fluent-python
A complete guide to learn, implement and development well python code. 

## Information

* The Python Data Model is the API that we use to make our own objects play well with the most idiomatic language features. The data model is a description of Python as a framework. It formalizes the interfaces of the building blocks of the language itself. 

## Data Model

* The Python Data Model: It describes the API that you can use to make your own objects play well with the most idiomatic language
* The dunder methods are so important and you have not touch them
* Collections module provides specialized container datatypes that offer enhanced functionality or performance for specific cases
* Container are data structures that can hold multiple objects or values
    * List
    * Dicts
    * Sets
    * Strings
    * Tuples
* Remember this three levels:
    * First:
        * Iterable `__iter__`
        * Sized `__len__`
        * and Container `__contains__` (to have `in` operation)
    * Second:
        * Reversible 
        * and Collections
    * Third:
        * Sequence, 
        * Mapping, 
        * and Set

## Sequences

* Sequences
    * Container: Different types
    * Flat: Same tipe and you can use `array` module
    * Mutable: You can change the content
    * Immutable: You can not change the content
* `collections.abc` provides the abstract base classes to implement functions for python containers
* listcomp is better than `map` and `filter`
* Remember: you can use `genexp`
* Tuples are no just Immutable Lists
* Tuples as records
* Unpack information and match cases like Elixir are best practices
* `slice` is useful to slice items
* Be careful using `+`, `+=`, and `*` in Sequences, the behaivor can change.
* `import dis` and use `dis.dis()` give you a good way to analyze some operations
* `import timeit` and use `timeit.repeat()` can help you to test code snippets
* Remember the key differences between `sort` and `list.sort`
* `collections.deque` and `collections` module (in general) are a good way to perform operations over `collections` 

## Dictionaries and Sets

* dict comprehension is key in all aspects
* `**dict_var` to unpack dicts
* `d1 | d2` to merge dicts
* Also you can use Match operations
* The UML information:
    * Collections
    * Mapping
    * MutableMapping
* Hashable is an object that has hash code which never changes during its lifetime:
    * `__hash__`
    * `__eq__`
* `__missing__` is a deep way to works with `d.get('any', None)`
* The basic use case for sets is remove duplicatation
* Sets work as math sets with operation like:
    * union |
    * intersection &
    * difference -
    * symmetric difference ^

## Unicode vs Bytes

* In general bytes has less size than Unicode
* `bytes`: This is an immutable sequence of bytes
* `bytearray`: This is a mutable sequence of bytes
* Basic encoders:
    * ascii
    * latin1
    * cp1252
    * cp437
    * gb2312
    * utf-8
    * utf-16le
* The Unicode sandwich:
    * bytes -> str
    * 100% str
    * str -> bytes

## Dataclass builders

* If your classes do not have `__repr__` or `__eq__` method it will not be clearly
* If your classes do not have `__eq__` you can not compare `==` objects because the comparaison will be over the `id`
* Also you can use `typing.NamedTuple` to inheritance
* `dataclass` is not immutable, for that reason you have to use `frozen=True`
* `__annotations__` is useful when you have the type hints
* `__doc__` to work with the docs

## Object references, mutability, and Recycling

* Variables are labels, not boxes.
* Aliasing: two variables bound to the same object.
* `==` comparaissons
* `is` to check the identities
* To (shallow) copy list you should use `c = list(a)`
* `copy()` to shallow and `deepcopy()` for deep copy.
* The only mode of parameter passing in Python is call by sharing 
* Mutable types as parameter defaults: Bad Idea
* Objects are never explicity destroyed; however, when they become unreachable they may be garbage-collected

## Functions ad First-Class Objects

* Higher-Order Function is a function that takes a function as an argument or returns a function as the result.
* The nine Flavors of Callable Objects:
    * User-defined functions
    * Built-in functions
    * Built-in methods
    * Methods
    * Classes
    * Class instances with a `__call__()` method
    * Generator functions
    * Native coroutine functions
    * Asyncronous generator functions

## Type Hints

* Python is gradual typing in practice
* `flake8`, `blue`, and `black` are good options to enhance your code
* duck typing in runtime
* normal typing in compile-time

## Decorators and Closures

* The function decorators are executed as soon as the module is imported, but the decorated functions only run when they are explicitly invoked.
* It is so important respect `nonlocal` variables and be carefull when and where the var is assigned
* The basic decorators does not support `**kwargs`
* To solve the not `**keywords` argument we can use `functools`
* If you will work using recursivity consider to use `@functools.cache`

## Important modules

* collections: it has some common options to manage built-in containers like list, sets, dicts, and tuples
    * `collections.OrderedDict`
    * `collections.ChainMap`
    * `collections.Counter`
    * `collections.UserDict`: To create your own `dict` classes
* random: some operations to create random options
* typing
* dataclasses
* functools: several higher order functions
* operator: intrinsic operators in Python
* typing