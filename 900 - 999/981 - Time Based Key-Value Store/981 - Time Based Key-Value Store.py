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


class TimeMap_best_speed:
    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''


class TimeMap_best_memory:
    def __init__(self):
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ''
        idx = bisect_right(self.timestamps[key], timestamp, key=lambda a: a[0])
        if idx > 0:
            self.timestamps[key] = self.timestamps[key][idx - 1:]
        return self.timestamps[key][0][1] if idx > 0 else ''
