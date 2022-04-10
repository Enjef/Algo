class FreqStack:
    def __init__(self):  # 5.00% 9.90%
        self.stack = []
        self.counter = {}

    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1
        self.stack.append(val)

    def pop(self) -> int:
        max_count = max(self.counter.values())
        for i in range(len(self.stack)-1, -1, -1):
            if self.counter[self.stack[i]] == max_count:
                self.counter[self.stack[i]] -= 1
                return self.stack.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

class FreqStack_v2:  # 49.47% 81.13%
    def __init__(self):
        self.arr = []
        heapify(self.arr)
        self.counter = {}
        self.idx = 0

    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1
        heappush(self.arr, (-self.counter[val], -self.idx, val))
        self.idx += 1

    def pop(self) -> int:
        val = heappop(self.arr)[2]
        self.counter[val] -= 1
        return val


class FreqStack_best_speed:
    def __init__(self):
        self.stack = []
        self.count = {}

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val])
            self.count[val] = 1
        elif val not in self.count:
            self.count[val] = 1
            self.stack[0].append(val)
        else:
            self.count[val] += 1
            if len(self.stack) < self.count[val]:
                self.stack.append([])
            self.stack[self.count[val]-1].append(val)

    def pop(self) -> int:
        ret = self.stack[-1].pop()
        if not self.stack[-1]:
            self.stack.pop()
        self.count[ret] -= 1
        return ret


class FreqStack_best_memory:
    def __init__(self):
        self.counter = Counter()
        self.freq = defaultdict(list)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        if self.counter[val] > self.max_count:
            self.max_count = self.counter[val]
        count = self.counter[val]
        self.freq[count].append(val)

    def pop(self) -> int:
        most_common = self.freq[self.max_count]
        if len(most_common) == 1:
            self.max_count -= 1
        to_return = most_common.pop()
        self.counter[to_return] -= 1
        if self.counter == 0:
            del self.counter[to_return]
        return to_return
