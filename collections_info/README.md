# Collections Module

The collections module in Python provides specialized containers (different from general purpose built-in containers like `dict`, `list`, `tuple`, and `set`).

* collections:
    * `ChainMap`: allows the combination of multiple dictionaries or other mappings; one use case is manage multiple context effectively
    * `Counter`
    * `deque`
    * `defaultdict`
    * `namedtuple()`
    * `OrderedDict`
    * `UserDict`
    * `UserList`
    * `UserString`

But `collections.abc` defines Abstract Base Classes for container types. It serves as interface or contract that defines the expected behaivor and methods for various types of collections.