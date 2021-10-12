class CustomStack:

    def __init__(self, maxSize: int):  # 77.77% 17.34%
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) <= k:
            self.stack = [x+val for x in self.stack]
        else:
            for i in range(k):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


class CustomStack_best_s_and_m:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append([x, 0])

    def pop(self) -> int:
        if self.stack:
            val, inc = self.stack.pop()
            if self.stack:
                self.stack[-1][1] += inc
            return val + inc
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.stack[min(k-1, len(self.stack)-1)][1] += val
