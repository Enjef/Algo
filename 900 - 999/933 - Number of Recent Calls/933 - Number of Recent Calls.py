class RecentCounter:  # 11.46% 88.69%

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests = [x for x in self.requests if t - 3000 <= x <= t]
        self.requests.append(t)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class RecentCounter_while:  # 47.92% 70.98%

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        while self.requests:
            if t - 3000 > self.requests[0]:
                self.requests.pop(0)
            else:
                break
        self.requests.append(t)
        return len(self.requests)


class RecentCounter_best:  # 98.07% 44.05%

    def __init__(self):
        self.p = collections.deque()

    def ping(self, t: int) -> int:
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.popleft()
        return len(self.p)
