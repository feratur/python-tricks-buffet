#!/usr/bin/env python3
if __name__ == '__main__':
    # list — Terribly Sloooow Queues
    # shifting all of the other elements by one, requiring O(n) time.
    q = []
    q.append('eat')
    q.append('sleep')
    q.append('code')
    # Careful: This is slow!
    popped = q.pop(0)
    assert popped == 'eat'

    # collections.deque – Fast & Robust Queues
    # Python’sdequeobjectsareimplementedasdoubly-linkedlists.
    from collections import deque
    q = deque()
    q.append('eat')
    q.append('sleep')
    q.append('code')
    popped = q.popleft()
    assert popped == 'eat'

    # queue.Queue – Locking Semantics for Parallel Computing
    # This queue implementation in the Python standard library is
    # synchronized and provides locking semantics to support multiple
    # concurrent producers and consumers.
    from queue import Queue
    q = Queue()
    q.put('eat')
    q.put('sleep')
    q.put('code')
    q.get() # 'eat'
    q.get() # 'sleep'
    q.get() # 'code'
    q.get_nowait() # queue.Empty
    q.get() # Blocks / waits forever...

    # multiprocessing.Queue – Shared Job Queues
    # This is a shared job queue implementation that allows
    # queued items to be processed in parallel by multiple concurrent workers.
    # Process-based parallelization
    # queue implementation meant for sharing data between processes,
    # multiprocessing.Queue makes it easy to distribute work across
    # multiple processes in order to work around the GIL limitations
    # This type of queue can store and transfer any pickle-able object across process boundaries.
    from multiprocessing import Queue
    q = Queue()
    q.put('eat')
    q.put('sleep')
    q.put('code')
    q.get() # 'eat'
    q.get() # 'sleep'
    q.get() # 'code'
    q.get() # Blocks / waits forever...

    # Python includes several queue implementations as part of the core language and its standard library.
    #
    # list objects can be used as queues, but this is generally not recommended due to slow performance.
    #
    # Ifyou’re not looking for parallel processing support, the implementation offered by collections.deque
    # is an excellent de- fault choice for implementing a FIFO queue data structure in Python.
    # It provides the performance characteristics you’d expect from a good queue implementation
    # and can also be used as a stack (LIFO Queue).
