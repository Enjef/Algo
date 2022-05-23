from sortedcontainers import SortedList


class SORTracker:  # 5.10% 98.21%
    def __init__(self):
        self.data = defaultdict(list)
        self.count = -1

    def add(self, name: str, score: int) -> None:
        self.data[score].append(name)
        self.data[score].sort()

    def get(self) -> str:
        self.count += 1
        temp = self.count
        for key in sorted(self.data, reverse=True):
            if temp <= len(self.data[key])-1:
                return self.data[key][temp]
            else:
                temp -= len(self.data[key])


class SORTracker_v2:  # 20.92% 71.17%
    def __init__(self):
        self.data = []
        self.count = -1

    def add(self, name: str, score: int) -> None:
        self.data.insert(
            bisect_left(
                self.data, (-score, name), 0, len(self.data)), (-score, name))

    def get(self) -> str:
        self.count += 1
        return self.data[self.count][1]


class SORTracker_v3:  # 49.75% 49.49%

    def __init__(self):
        self.data = []
        self.count = -1

    def idx_search(self, target):
        left, right = 0, len(self.data)
        while left < right:
            mid = (left+right)//2
            if self.data[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    def add(self, name: str, score: int) -> None:
        idx = self.idx_search((-score, name))
        self.data.insert(idx, (-score, name))

    def get(self) -> str:
        self.count += 1
        return self.data[self.count][1]


class SORTracker_best_memory:
    def __init__(self):
        self.counter = 0
        self.scores = []
        self.score2location = defaultdict(list)

    def add(self, name: str, score: int) -> None:
        if score not in self.score2location:
            self.scores.append(score)
            self.scores.sort(reverse=True)
        self.score2location[score].append(name)
        self.score2location[score].sort()

    def get(self) -> str:
        self.counter += 1
        index = self.counter - 1
        for score in self.scores:
            if index < len(self.score2location[score]):
                return self.score2location[score][index]
            else:
                index -= len(self.score2location[score])


class SORTracker_best_speed():
    def __init__(self):
        self.n = -1
        self.scenes = SortedList()

    def add(self, name: str, score: int) -> None:
        self.scenes.add((-score, name))

    def get(self) -> str:
        self.n += 1
        return self.scenes[self.n][1]
