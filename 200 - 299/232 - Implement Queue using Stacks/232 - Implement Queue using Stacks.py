class MyQueue:

    def __init__(self):  # 81.23% 73.84%
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack:
            self.temp.append(self.stack.pop())
        pop = self.temp.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return pop

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack


class MyQueue_study_plan_day_9:  # 94.30% 44.31%

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0
