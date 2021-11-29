class Solution:
    def merge(
            self,
            intervals: List[List[int]]) -> List[List[int]]:  # 92.50% 56.13%
        intervals.sort()
        out = []
        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] >= interval[0]:
                cur[1] = max(cur[1], interval[1])
            else:
                out.append(cur)
                cur = interval
        out.append(cur)
        return out
