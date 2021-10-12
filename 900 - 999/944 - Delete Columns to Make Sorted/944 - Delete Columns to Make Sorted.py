class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:  # 81.87% 5.56%
        strs = list(zip(*[list(x) for x in strs]))
        count = 0
        for item in strs:
            if list(item) != sorted(item):
                count += 1
        return count

    def minDeletionSize_best_speed(self, strs: List[str]) -> int:
        return sum(list(i) != sorted(i) for i in zip(*strs))

    def minDeletionSize_best_memory(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        count = 0
        for i in range(n):
            for j in range(1, m):
                if strs[j][i] < strs[j-1][i]:
                    count += 1
                    break
        return count
