class Solution:
    def findRightInterval(self, intervals):  # 79.85% 70.61%
        n = len(intervals)
        result = [-1] * n
        intervals = sorted(
            [(start, end, idx) for idx, (start, end) in enumerate(intervals)])
        for i, (cur_start, cur_end, cur_idx) in enumerate(intervals):
            if cur_start == cur_end:
                result[cur_idx] = cur_idx
                continue
            left, right = i + 1, n
            while left < right:
                mid = (left+right)//2
                if intervals[mid][0] == cur_end:
                    left = mid
                    break
                if intervals[mid][0] > cur_end:
                    right = mid
                else:
                    left = mid + 1
            if left == n:
                continue
            result[cur_idx] = intervals[left][2]
        return result
