class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.temp.append(x)
        while self.queue:
            self.temp.append(self.queue.pop(0))
        self.queue, self.temp = self.temp, self.queue
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()