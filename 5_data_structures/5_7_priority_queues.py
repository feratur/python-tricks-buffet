#!/usr/bin/env python3
if __name__ == '__main__':
    # A priority queue is a container data structure that manages a set
    # of records with totally-ordered keys (for example, a numeric weight value)
    # to provide quick access to the record with the smallest or largest key in the set.
    # instead of retrieving the next element by insertion time,
    # it retrieves the highest-priority element.
    # The priority of individual elements is decided by the ordering applied to their keys.

    # list – Maintaining a Manually Sorted Queue
    # You can use a sorted list to quickly identify and delete the smallest or largest element
    q = []
    q.append((2, 'code'))
    q.append((1, 'eat'))
    q.append((3, 'sleep'))
    # NOTE: Remember to re-sort every time
    # a new element is inserted, or use
    # bisect.insort().
    q.sort(reverse=True)
    while q:
        next_item = q.pop()
        print(next_item)
    # Result:
    # (1, 'eat')
    # (2, 'code')
    # (3, 'sleep')

    # heapq – List-Based Binary Heaps
    # heapq is a binary heap, with O(log n) push and O(log n) pop
    # a[0] is always its smallest element
    import heapq
    q = []
    heapq.heappush(q, (2, 'code'))
    heapq.heappush(q, (1, 'eat'))
    heapq.heappush(q, (3, 'sleep'))
    while q:
        next_item = heapq.heappop(q)
        print(next_item)
    # Result:
    # (1, 'eat')
    # (2, 'code')
    # (3, 'sleep')

    # queue.PriorityQueue – Beautiful Priority Queues
    # This priority queue implementation uses heapq internally and shares the same time and space complexities.
    # The difference is that PriorityQueue is synchronized and provides locking
    # semantics to support multiple concurrent producers and consumers.
    # Depending on your use case, this might be helpful
    # or just slow your program down slightly. In any case,
    # you might prefer the class-based interface provided by
    # PriorityQueue over using the function-based interface provided by heapq.
    from queue import PriorityQueue
    q = PriorityQueue()
    q.put((2, 'code'))
    q.put((1, 'eat'))
    q.put((3, 'sleep'))
    while not q.empty():
        next_item = q.get()
        print(next_item)
    # Result:
    # (1, 'eat')
    # (2, 'code')
    # (3, 'sleep')

    # Python includes several priority queue implementations for you to use.
    #
    # queue.PriorityQueue stands out from the pack with a nice object-oriented
    # interface and a name that clearly states its intent. It should be your preferred choice.
    #
    # If you’d like to avoid the locking overhead of queue.PriorityQueue,
    # using the heapq module directly is also a good option.
