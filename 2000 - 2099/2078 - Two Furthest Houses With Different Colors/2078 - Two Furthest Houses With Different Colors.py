class Solution:
    def maxDistance(self, colors: List[int]) -> int:  # 13.32% 68.15 %
        n = len(colors)
        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if colors[i] != colors[j]:
                    res = max(res, j-i)
        return res

    def maxDistance_v2(self, colors: List[int]) -> int:  # 96.16% 23.31%
        n = len(colors)
        res = 0
        i, j = 0, n-1
        while colors[i] == colors[j]:
            i += 1
        res = max(res, j-i)
        i = 0
        while colors[i] == colors[j]:
            j -= 1
        res = max(res, j-i)
        return res

    def maxDistance_best_speed(self, colors: List[int]) -> int:
        left, right = 0, len(colors) - 1
        if colors[left] != colors[right]:
            return len(colors) - 1
        for i in range(len(colors)):
            if colors[i] != colors[right]:
                break
        for j in range(len(colors)-1, -1, -1):
            if colors[j] != colors[left]:
                break
        return max(j, right - i)

    def maxDistance_best_memory(self, colors: List[int]) -> int:
        max_distance = 0
        for i in range(len(colors)):
            for j in range(1, len(colors)):
                if colors[i] != colors[j]:
                    distance = abs(j-i)
                    max_distance = max(max_distance, distance)
        return max_distance
