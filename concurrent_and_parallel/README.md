# Concurrent

## Considerations

* Global Interpretet Lock
    * Only one thread can be running at one time
* Threads safe
    * An entity can handle multiple threads using it, or threads deal with data in way that does not interfere with other threads.
* Race conditions
    * Unpredictable result

* Threads
    * Share the same memory
    * Smalloverhead associated with thread switching
* Multiprocessing
    * Processes do not share memory, each process has its own python interpreter and GIL
    * Higher overhead, memory duplications
* Concurrency in general
    More complex to write and debug

## Threading

* `t.join()` blocks the thread until ends the execution