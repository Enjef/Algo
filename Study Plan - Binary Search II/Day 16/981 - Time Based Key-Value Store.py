class TimeMap:  # 65.25% 80.41%
    def __init__(self):
        self.storage = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if (
                key not in self.storage or
                self.storage and self.storage[key][0][0] > timestamp):
            return ''
        left, right = 0, len(self.storage[key]) - 1
        while left < right:
            mid = (left+right+1)//2
            if self.storage[key][mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        return self.storage[key][left][1]
