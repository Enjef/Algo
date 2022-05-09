class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:  # 28.44% 60.86%
        levels = defaultdict(int)
        result = 0
        for task in tasks:
            levels[task] += 1
        for level in levels:
            cur = levels[level]
            if cur-4 > 0 and (cur-4) % 3 == 0:
                result += 2 + (cur-4) // 3
            elif cur % 3 == 0:
                result += cur // 3
            elif cur % 3 and cur // 3 and cur % 3 % 2 == 0:
                result += cur // 3 + cur % 3 // 2
            elif cur-3 > 0 and (cur-3) % 2 == 0:
                result += 1 + (cur-3) // 2
            elif cur % 2 == 0:
                result += cur // 2
            else:
                return -1
        return result

    def minimumRounds_best_speed(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        if 1 in count.values():
            return -1
        minimum = 0
        for i in count.values():
            if i % 3 == 0:
                minimum += i//3
            elif i % 3 == 1:
                minimum += (i//3)-1 + (i-(i//3-1)*3)//2
            elif i % 3 == 2:
                minimum += i//3 + 1
        return minimum

    def minimumRounds_2nd_best_speed(self, tasks: List[int]) -> int:
        a, res = Counter(tasks), 0
        for count in a.values():
            if count <= 1:
                return -1
            res += ceil(count/3)
        return res

    def minimumRounds_3d_best_speed(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        ret = 0
        for cnt in c.values() :
            if cnt == 1 :
                return -1
            if cnt % 3 == 0 :
                ret += cnt // 3
            else :
                ret += cnt // 3 + 1
        return ret
