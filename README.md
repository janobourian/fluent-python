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

## Important modules

* collections: it has some common options to manage built-in containers like list, sets, dicts, and tuples
    * `collections.OrderedDict`
    * `collections.ChainMap`
    * `collections.Counter`
    * `collections.UserDict`: To create your own `dict` classes
* random: some operations to create random options