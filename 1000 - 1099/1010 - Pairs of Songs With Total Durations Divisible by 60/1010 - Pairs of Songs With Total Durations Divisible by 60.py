class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:  # 72.72% 67.00%
        remainders = defaultdict(int)
        result = 0
        for el in time:
            result += remainders.get(-el % 60, 0)
            remainders[el % 60] += 1
        return result

    def numPairsDivisibleBy60_best_speed(self, time: List[int]) -> int:
        ans = 0
        cnt = {}
        for t in time:
            if t % 60 in cnt:
                cnt[t % 60] += 1
            else:
                cnt[t % 60] = 1
        ans += (cnt.get(0, 0)*(cnt.get(0, 0)-1)//2) + \
            (cnt.get(30, 0)*(cnt.get(30, 0)-1)//2)
        for i in range(1, 30):
            ans += cnt.get(i, 0)*cnt.get(60-i, 0)
        return ans

    def numPairsDivisibleBy60_2nd_best_speed(self, time: List[int]) -> int:
        rem = [t % 60 for t in time]
        c = Counter(rem)
        res = 0
        print(c)
        for i in range(1, 30):
            res += c[i] * c[60-i]
        res += (c[0] * (c[0] - 1)) // 2
        res += (c[30] * (c[30]-1)) // 2
        return res

    def numPairsDivisibleBy60_best_memory(self, time: List[int]) -> int:
        remainder = {}
        pairs = 0
        for num in time:
            res = num % 60
            if res == 0 and 0 in remainder:
                pairs += remainder[0]
            elif res != 0 and 60-res in remainder:
                pairs += remainder[60-res]
            if res in remainder:
                remainder[res] += 1
            else:
                remainder[res] = 1
        return pairs
