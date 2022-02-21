class Solution:
    def earliestFullBloom(self, plantTime, growTime) -> int: # 35.66% 98.04%
        n = len(plantTime)
        planted, grown = 0, 0
        grow_ladder = sorted(range(n), key=lambda x: growTime[x], reverse=True)
        for i in grow_ladder:
            planted += plantTime[i]
            grown = max(grown, planted+growTime[i])
        return grown

    def earliestFullBloom_best_speed(self, plantTime, growTime) -> int:
        a = defaultdict(int)
        for g, p in zip(growTime, plantTime):
        a[g] += p
        t = 0
        x = 0
        for g in sorted(a, reverse=True):
        x += a[g]
        t = max(t, x + g)
        return t
