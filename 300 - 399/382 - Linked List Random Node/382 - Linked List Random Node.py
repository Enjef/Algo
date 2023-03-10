import random


# 23.79% 35.13% (30.48% 73.23%, 90.71% 35.13%)
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.size = 0
        while head:
            head = head.next
            self.size += 1

    def getRandom(self) -> int:
        target = random.randrange(self.size)
        cur = self.head
        while target:
            target -= 1
            cur = cur.next
        return cur.val


# 98.14% 49.63% (62.83% 73.23%)
class Solution_v2:
    def __init__(self, head: Optional[ListNode]):
        self.nodes = []
        while head:
            self.nodes.append(head)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.nodes).val


class Solution_best_speed:
    def __init__(self, head: Optional[ListNode]):
        self.stack = []
        while head != None:
            self.stack.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        val = int(random.random() * len(self.stack))
        return self.stack[val]


class Solution_best_memory:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        reservoir = self.head.val
        i = 2
        next = self.head.next
        while next:
            if random.random() < 1 / i:
                reservoir = next.val
            i += 1
            next = next.next
        return reservoir


class Solution_2nd_best_memory:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.count = 0
        self.curr = self.head
        while self.curr:
            self.count += 1
            self.curr = self.curr.next

    def getRandom(self) -> int:
        rand = random.randint(0, self.count - 1)
        self.curr = self.head
        for _ in range(rand):
            self.curr = self.curr.next
        return self.curr.val
