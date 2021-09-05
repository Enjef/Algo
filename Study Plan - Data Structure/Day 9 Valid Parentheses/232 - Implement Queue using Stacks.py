class MyQueue:

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
