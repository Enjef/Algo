class Solution:
    # 29.15% 86.85%
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        i = 0
        prev = 0
        prev_c = None
        n = len(colors)
        while i < n:
            while i < n and colors[i] == prev_c:
                i += 1
            if i-prev > 1:
                result += sum(neededTime[prev:i])-max(neededTime[prev:i])
            if i < n:
                prev_c = colors[i]
            prev = i
            i += 1
        return result

    def minCost_3d_best_speed(self, colors: str, neededTime: List[int]) -> int:
        pval = 0
        prev = 0
        ln = len(colors)
        for i in range(1, ln):
            if colors[i] == colors[prev]:
                if neededTime[i] > neededTime[prev]:
                    pval += neededTime[prev]
                    prev = i
                else:
                    pval += neededTime[i]
            else:
                prev = i
        return pval

    def minCost_2nd_best_speed(self, colors: str, neededTime: List[int]) -> int:
        s = 0
        pre = colors[0]
        min_time = 0
        for e in range(1, len(colors)):
            color = colors[e]
            if pre != color:
                if e-s >= 2:
                    time = sum(neededTime[s:e])-max(neededTime[s:e])
                    min_time += time
                s = e
                pre = color
        time = sum(neededTime[s:len(colors)])-max(neededTime[s:len(colors)])
        min_time += time
        return min_time

    def minCost_best_memory(self, colors: str, neededTime: List[int]) -> int:
        l = len(neededTime)
        res = 0
        for i in range(l-1):
            if colors[i] == colors[i+1]:
                big = max(neededTime[i], neededTime[i+1])
                small = min(neededTime[i], neededTime[i+1])
                res += small
                neededTime[i+1] = big
        return res
