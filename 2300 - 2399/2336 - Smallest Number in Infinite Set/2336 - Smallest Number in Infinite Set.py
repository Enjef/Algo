# 79.62% 25.52% (98.40% 58.91%)
import heapq as h
from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.cap = 1
        self.backers = []

    def popSmallest(self) -> int:
        if self.backers:
            return self.backers.pop(0)
        prev = self.cap
        self.cap += 1
        return prev

    def addBack(self, num: int) -> None:
        if num < self.cap:
            if num not in self.backers:
                insort_left(self.backers, num)


class SmallestInfiniteSet_best_speed:
    def __init__(self):
        self.i = 1
        self.q = []
        heapq.heapify(self.q)

    def popSmallest(self) -> int:
        if len(self.q) > 0:
            return heapq.heappop(self.q)
        else:
            self.i += 1
            return self.i - 1

    def addBack(self, num: int) -> None:
        if num < self.i and num not in self.q:
            heapq.heappush(self.q, num)


class SmallestInfiniteSet_2nd_best_speed:
    def __init__(self):
        self.hp = []
        self.s = set({})
        self.cont_smallest = 1

    def popSmallest(self) -> int:
        if len(self.hp) == 0:
            sm = self.cont_smallest
            self.cont_smallest += 1
            return sm
        sm = heappop(self.hp)
        self.s.remove(sm)
        return sm

    def addBack(self, num: int) -> None:
        if num >= self.cont_smallest or num in self.s:
            return
        if num == self.cont_smallest - 1:
            self.cont_smallest -= 1
            return
        self.s.add(num)
        heappush(self.hp, num)


class SmallestInfiniteSet_best_memory:
    def __init__(self):
        self.infinite_set = set({i for i in range(1, 1000+1)})
        self.heap = [i for i in range(1, 1000+1)]

    def popSmallest(self) -> int:
        pop = h.heappop(self.heap)
        self.infinite_set.remove(pop)
        return pop

    def addBack(self, num: int) -> None:
        if num not in self.infinite_set:
            h.heappush(self.heap, num)
            self.infinite_set.add(num)
