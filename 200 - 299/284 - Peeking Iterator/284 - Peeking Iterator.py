# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:  # 72.25% 29.71%
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peek_el = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_el:
            return self.peek_el
        self.peek_el = self.iterator.next()
        return self.peek_el

    def next(self):
        """
        :rtype: int
        """
        if self.peek_el:
            res = self.peek_el
            self.peek_el = None
            return res
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.iterator.hasNext() or self.peek_el)

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class PeekingIterator_best_speed:
    def __init__(self, iterator):
        self.peek_val = None
        self._iterator = iterator

    def peek(self):
        if self.peek_val:
            return self.peek_val

        self.peek_val = self._iterator.next()
        return self.peek_val

    def next(self):
        if self.peek_val:
            res = self.peek_val
            self.peek_val = None
            return res
        return self._iterator.next()

    def hasNext(self):
        if self.peek_val:
            return True
        return self._iterator.hasNext()


class PeekingIterator_2nd_best_speed:
    def __init__(self, iterator):
        self.queue = deque()
        self.iterator = iterator

    def peek(self):
        if not self.queue:
            self.queue.append(self.iterator.next())
        return self.queue[0]

    def next(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return self.iterator.next()

    def hasNext(self):
        return bool(self.queue or self.iterator.hasNext())


class PeekingIterator_best_memory:
    def __init__(self, iterator):
        self.iter=iterator
        self.cache=[]

    def peek(self):
        if not self.cache:
            self.cache.append(self.iter.next())
        return self.cache[0]

    def next(self):
        if self.cache:
            val=self.cache.pop(0)
            return val
        return self.iter.next()

    def hasNext(self):
        return len(self.cache)>0 or self.iter.hasNext()
