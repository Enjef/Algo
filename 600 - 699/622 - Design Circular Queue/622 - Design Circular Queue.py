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


class MyCircularQueue_best_speed:
    def __init__(self, k: int):
        self.size = 0
        self.k = k
        self.head = 0
        self.tail = -1
        self.data = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.tail = (self.tail + 1) % self.k            
        self.data[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


class MyCircularQueue_best_memory:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*self.k
        self.head = 0
        self.tail = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            self.size += 1
            self.tail = (self.tail + 1) % self.k
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = None
            self.size -= 1
            self.head = (self.head + 1) % self.k
            return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.k else False
