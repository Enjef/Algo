class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_val = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if val < self.min_val:
            self.min_val = val
        self.stack.append([val, self.min_val])

    def pop(self) -> None:
        pop_temp = self.stack.pop()
        if pop_temp[0] == self.min_val:
            self.min_val = self.stack[-1][1] if self.stack else float('inf')

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
