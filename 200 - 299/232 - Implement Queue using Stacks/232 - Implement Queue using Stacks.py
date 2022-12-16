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


class MyQueue_mock:  # 94.52%  45.44%

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)
        self.second = self.first[::-1]

    def pop(self) -> int:
        cur = self.second.pop()
        self.first = self.second[::-1]
        return cur

    def peek(self) -> int:
        return self.second[-1]

    def empty(self) -> bool:
        return not(bool(self.second))


# 91.33% 98.86% (77.73% 98.86%)
class MyQueue_daily:

    def __init__(self):
        self.add_el = []
        self.pop_el = []
        self.last = None

    def push(self, x: int) -> None:
        if self.last == 'pop':
            self.add_el = self.pop_el[::-1]
        self.add_el.append(x)
        self.last = 'push'

    def pop(self) -> int:
        if self.last == 'push':
            self.pop_el = self.add_el[::-1]
        self.last = 'pop'
        return self.pop_el.pop()

    def peek(self) -> int:
        if self.last == 'pop':
            return self.pop_el[-1]
        return self.add_el[0]

    def empty(self) -> bool:
        if self.last == 'pop':
            return not self.pop_el
        return not self.add_el


class MyQueue_best_speed:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)


class MyQueue_best_memory:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        self._shiftItems()
        return self.outstack.pop()

    def peek(self) -> int:
        self._shiftItems()
        return self.outstack[-1]

    def empty(self) -> bool:
        return self.instack == [] and self.outstack == []

    def _shiftItems(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())


class MyQueue_best_speed_new:

    def __init__(self):
        self.input_s = []
        self.output_s = []

    def push(self, x: int) -> None:
        self.input_s.append(x)

    def pop(self) -> int:
        self.rearrange()
        return self.output_s.pop()

    def peek(self) -> int:
        self.rearrange()
        return self.output_s[-1]

    def empty(self) -> bool:
        return not self.output_s and not self.input_s

    def rearrange(self):
        if not self.output_s:
            while self.input_s:
                self.output_s.append(self.input_s.pop())


class MyQueue_best_speed_new_3d:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack = [x] + self.stack

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


class MyQueue_best_memory_new:
    def __init__(self):
        self.Q = []

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        return self.Q.pop(0)

    def peek(self) -> int:
        return self.Q[0]

    def empty(self) -> bool:
        return not self.Q
