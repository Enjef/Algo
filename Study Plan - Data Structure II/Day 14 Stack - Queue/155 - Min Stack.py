class MinStack:

    def __init__(self):  # 91.80% 35.75%
        """
        initialize your data structure here.
        """
        self.stack = []
        self.le = 0
        
    def push(self, val: int) -> None:
        cur_min = val if self.le == 0 else min(self.stack[-1][1], val)
        self.stack.append((val, cur_min))
        self.le += 1

    def pop(self) -> None:
        self.le -= 1
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
