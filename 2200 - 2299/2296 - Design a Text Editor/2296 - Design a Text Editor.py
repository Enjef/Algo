# 48.4% 37.66% (53.67% 37.66%)
class TextEditor:
    def __init__(self):
        self.text = []
        self.i = 0

    def addText(self, text: str) -> None:
        self.text[self.i: self.i] = list(text)
        self.i += len(text)

    def deleteText(self, k: int) -> int:
        if self.i < k:
            k = self.i
        self.text[self.i-k: self.i] = []
        self.i -= k
        return k

    def cursorLeft(self, k: int) -> str:
        if k > self.i:
            k = self.i
        self.i -= k
        return ''.join(self.text[self.i-min(10, self.i): self.i])

    def cursorRight(self, k: int) -> str:
        if self.i + k > len(self.text):
            k = len(self.text) - self.i
        self.i += k
        return ''.join(self.text[self.i-min(10, self.i): self.i])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)


class TextEditor_best_speed:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        delete = min(k, len(self.left))
        for _ in range(delete):
            self.left.pop()
        return delete

    def get10(self):
        res = ''
        for i in range(max(len(self.left)-10, 0), len(self.left)):
            res += self.left[i]
        return res

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        return self.get10()

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())
        return self.get10()


class TextEditor_best_memory:
    def __init__(self):
        self.s = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        new_cursor = max(0, self.cursor - k)
        noOfChars = k if self.cursor - k >= 0 else self.cursor
        self.s = self.s[:new_cursor] + self.s[self.cursor:]
        self.cursor = new_cursor
        return noOfChars

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        start = max(0, self.cursor-10)
        return self.s[start:self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.s), self.cursor + k)
        start = max(0, self.cursor - 10)
        return self.s[start:self.cursor]
