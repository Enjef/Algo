class BrowserHistory:  # 77.09% 30.13%

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        while self.pos < len(self.history)-1:
            self.history.pop()
        self.history.append(url)
        self.pos = len(self.history)-1
        
    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos-steps)
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.history)-1, self.pos+steps)
        return self.history[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


class BrowserHistory_best_speed(object):

    def __init__(self, homepage):
        self.stack = [homepage]
        self.pointer = 0
        

    def visit(self, url):
        if self.pointer == len(self.stack) - 1:
            self.stack.append(url)
            self.pointer += 1
        else:
            self.stack = self.stack[0:self.pointer+1]
            self.stack.append(url)
            self.pointer += 1
        

    def back(self, steps):
        maxBack = self.pointer
        if steps > maxBack:
            self.pointer = 0
        else:
            self.pointer -= steps
        return self.stack[self.pointer]
        

    def forward(self, steps):
        maxFord = len(self.stack) - self.pointer - 1
        if steps > maxFord:
            self.pointer = len(self.stack) - 1
        else:
            self.pointer += steps
        return self.stack[self.pointer]
