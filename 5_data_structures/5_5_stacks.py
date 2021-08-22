#!/usr/bin/env python3
if __name__ == '__main__':
    # list – Simple, Built-In Stacks
    # supports push and pop operations in amortized O(1) time
    # dynamic array allocation makes their performance less consistent
    # than the stable O(1) inserts and deletes provided by a linked list
    # based implementation (like collections.deque, see below). On the other
    # hand, lists do provide fast O(1) time random access to elements on the stack,
    # and this can be an added benefit.
    #
    # To get the amortized O(1) performance for inserts and deletes, new items
    # must be added to the end of the list with the append() method and removed
    # again from the end using pop(). For optimum performance, stacks based on
    # Python lists should grow towards higher indexes and shrink towards lower ones
    # (Adding and removing from the front is much slower and takes O(n) time, as the
    # existing elements must be shifted around to make room for the new element)
    s = []
    s.append('eat')
    s.append('sleep')
    s.append('code')
    popped = s.pop()
    assert popped == 'code'

    # collections.deque – Fast & Robust Stacks
    # The deque class implements a double-ended queue that supports adding
    # and removing elements from either end in O(1) time (non- amortized).
    # Because deques support adding and removing elements from either end equally well,
    # they can serve both as queues and as stacks
    #
    # Python’s deque objects are implemented as doubly-linked lists which gives them
    # excellent and consistent performance for inserting and deleting elements, but poor
    # O(n) performance for randomly accessing elements in the middle of a stack.
    from collections import deque
    s = deque()
    s.append('eat')
    s.append('sleep')
    s.append('code')
    popped = s.pop()
    assert popped == 'code'

    # queue.LifoQueue – Locking Semantics for Parallel Computing
    # This stack implementation in the Python standard library is synchronized
    # and provides locking semantics to support multiple concurrent producers and consumers.
    # Depending on your use case, the locking semantics might be helpful,
    # or they might just incur unneeded overhead.
    from queue import LifoQueue
    s = LifoQueue()
    s.put('eat')
    s.put('sleep')
    s.put('code')
    popped = s.get()
    assert popped == 'code'
    s.get() # 'sleep'
    s.get() # 'eat'
    s.get_nowait() # queue.Empty
    s.get() # Blocks / waits forever...

    # list is backed by a dynamic array which makes it great for fast random access,
    # but requires occasional resizing when elements are added or removed.
    # The list over-allocates its backing storage so that not every push or pop requires resizing,
    # and you get an amortized O(1) time complexity for these operations.
    # But you do need to be careful to only insert and remove items “from the right side”
    # using append() and pop(). Otherwise, performance slows down to O(n).
    #
    # collections.deque is backed by a doubly-linked list which optimizes appends and deletes
    # at both ends and provides consis- tent O(1) performance for these operations.
    # Not only is its performance more stable, the deque class is also easier to use because
    # you don’t have to worry about adding or removing items from “the wrong end.”
