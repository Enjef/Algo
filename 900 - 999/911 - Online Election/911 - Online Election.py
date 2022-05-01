class TopVotedCandidate:  # 34.63% 65.07%
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        count = defaultdict(int)
        leader = None
        leader_score = -1
        for i in range(len(times)):
            count[persons[i]] += 1
            if not leader_score or count[persons[i]] >= leader_score:
                leader = persons[i]
                leader_score = count[persons[i]]
            self.persons[i] = leader

    def q(self, t: int) -> int:
        left, right = 0, len(self.persons) - 1
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            if self.times[mid] > t:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return self.persons[ans]


class TopVotedCandidate_v2:  # 38.21% 100.00%
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        count = defaultdict(int)
        leader = None
        leader_score = -1
        for i in range(len(times)):
            count[persons[i]] += 1
            if not leader_score or count[persons[i]] >= leader_score:
                leader = persons[i]
                leader_score = count[persons[i]]
            self.persons[i] = leader

    def q(self, t: int) -> int:
        left, right = 0, len(self.persons)
        while left < right:
            mid = (left+right) // 2
            if self.times[mid] > t:
                right = mid
            else:
                left = mid + 1
        return self.persons[left-1]


class TopVotedCandidate_best_speed:
    def __init__(self, people: List[int], times: List[int]):
        tops = []
        voteCounts = defaultdict(int)
        voteCounts[-1] = -1
        top = -1
        for person in people:
            voteCounts[person] += 1
            if voteCounts[person] >= voteCounts[top]:
                top = person
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, time: int) -> int:
        # l, r = 0, len(self.times) - 1
        # # 找到满足 (find satisfaction) times[l] <= t 的最大的 (the largest) l
        # while l < r:
        #     m = l + (r - l + 1) // 2
        #     if self.times[m] <= time:
        #         l = m
        #     else:
        #         r = m - 1
        # # 也可以使用内置的二分查找的包来确定 l
        # You can also use the built-in binary search package to determine l
        # # l = bisect.bisect(self.times, t) - 1
        return self.tops[bisect.bisect(self.times, time) - 1]


class TopVotedCandidate_best_memory:
    def __init__(self, persons: List[int], times: List[int]):
        self.maxes = []
        counter = defaultdict(int)
        tp = sorted(zip(times, persons))
        for t, p in tp:
            counter[p] += 1
            if not self.maxes or counter[self.maxes[-1][1]] <= counter[p]:
                self.maxes.append((t, p))
            else:
                self.maxes.append((t, self.maxes[-1][1]))

    def q(self, t: int) -> int:
        l = 0
        h = len(self.maxes)-1
        found = -1
        while(l <= h):
            mid = int((l+h)/2)
            if self.maxes[mid][0] == t:
                found = self.maxes[mid]
                break
            if self.maxes[mid][0] > t:
                h = mid - 1
            else:
                l = mid + 1
        if self.maxes[mid][0] > t:
            mid = mid - 1
        return self.maxes[mid][1]
