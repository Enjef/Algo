class MyCircularQueue:
    def __init__(self, k: int):  # 79.65% 59.32%
        self.size = k
        self.q = []

    def enQueue(self, value: int) -> bool:
        if len(self.q) < self.size:
            self.q.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.q.pop(0)
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
