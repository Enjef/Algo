# 37.18% 20.72% (41.78% 18.75%)
from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.nums = defaultdict(int)
        self.coords = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if self.nums[index] == number:
            return
        cur = self.nums[index]
        if self.nums[index]:
            self.coords[cur].remove(index)
            if not self.coords[cur]:
                self.coords.pop(cur)
        self.nums[index] = number
        insort_left(self.coords[number], index)

    def find(self, number: int) -> int:
        if number not in self.coords:
            return -1
        return self.coords[number][0]


# 91.45% 18.75% (42.11% 24.34%)
class NumberContainers_v2:
    def __init__(self):
        self.nums = defaultdict(int)
        self.coords = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if self.nums[index] == number:
            return
        if self.nums[index]:
            self.coords[self.nums[index]].remove(index)
        self.nums[index] = number
        insort_left(self.coords[number], index)

    def find(self, number: int) -> int:
        if number not in self.coords or not len(self.coords[number]):
            return -1
        return self.coords[number][0]


class NumberContainers_best_speed:
    def __init__(self):
        self.data_ = {}
        self.lookup_ = {}

    def change(self, index: int, number: int) -> None:
        self.lookup_[index] = number
        if number in self.data_:
            heappush(self.data_[number], index)
        else:
            self.data_[number] = [index]

    def find(self, number: int) -> int:
        if number not in self.data_:
            return -1
        else:
            while self.data_[number]:
                candidate = self.data_[number][0]
                if candidate in self.lookup_:
                    if self.lookup_[candidate] == number:
                        return candidate
                    else:
                        heappop(self.data_[number])
            return -1


class NumberContainers_2nd_best_speed:
    def __init__(self):
        self.containers = defaultdict(list)
        self.idx = {}

    def change(self, index: int, number: int) -> None:
        heapq.heappush(self.containers[number], index)
        self.idx[index] = number

    def find(self, number: int) -> int:
        current = self.containers[number]
        while current:
            candidate = current[0]
            if self.idx[candidate] == number:
                return candidate
            else:
                heapq.heappop(current)
        return -1


class NumberContainers_3nd_best_speed:
    def __init__(self):
        self.db = dict()
        self.indexLookup = collections.defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.db[index] = number
        heapq.heappush(self.indexLookup[number], index)

    def find(self, number: int) -> int:
        indexHeap = self.indexLookup[number]
        while indexHeap and self.db.get(indexHeap[0], number) != number:
            heapq.heappop(indexHeap)
        return indexHeap[0] if indexHeap else -1


class NumberContainers_best_memory:
    def __init__(self):
        self.num_to_idx = collections.defaultdict(SortedSet)
        self.idx_to_num = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            self.num_to_idx[self.idx_to_num[index]].remove(index)

        self.num_to_idx[number].add(index)
        self.idx_to_num[index] = number

    def find(self, number: int) -> int:
        if number not in self.num_to_idx or len(self.num_to_idx[number]) == 0:
            return -1
        return self.num_to_idx[number][0]
