class Solution:
    def countLargestGroup(self, n: int) -> int:  # 60.57% 69.33%
        groups = {}
        for i in range(1, n+1):
            num = i
            cur = 0
            while num:
                cur += num % 10
                num //= 10
            if cur not in groups:
                groups[cur] = 0
            groups[cur] += 1
        return list(groups.values()).count(max(groups.values()))

    def countLargestGroup_best(self, n: int) -> int:
        groups: list[int] = [0] * 46
        cache: dict[int, int] = defaultdict(int)
        for i in range(1, n + 1):
            q, r = divmod(i, 10)
            cache[i] = r + cache[q]
            groups[cache[i]] += 1
        return groups.count(max(groups))
