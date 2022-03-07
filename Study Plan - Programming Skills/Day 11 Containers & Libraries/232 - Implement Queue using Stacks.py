class MyQueue:

    def __init__(self):  # 84.92% 54.23%
        self.add_el = []
        self.pop_el = []

    def push(self, x: int) -> None:
        self.add_el.append(x)

    def pop(self) -> int:
        self.pop_el = self.add_el[::-1]
        out = self.pop_el.pop()
        self.add_el = self.pop_el[::-1]
        return out

    def peek(self) -> int:
        return self.add_el[0]

    def empty(self) -> bool:
        return not self.add_el
