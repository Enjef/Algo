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

    def findRightInterval_best_speed(self, intervals):
        startTimeIdxMap = {x[0]: i for i, x in enumerate(intervals)}
        sortedStartTime = sorted(list(startTimeIdxMap.keys()))
        idx = 0
        times = [-1]*len(intervals)
        for start, end in intervals:
            insertIdx = bisect_left(sortedStartTime, end)
            if insertIdx <= len(intervals)-1:
                nextStartTime = sortedStartTime[insertIdx]
                times[idx] = startTimeIdxMap[nextStartTime]
            idx += 1
        return times

    def findRightInterval_4th_best_speed(self, intervals):
        temp_ind = sorted([(t[0], i) for i, t in enumerate(intervals)])
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] > temp_ind[len(temp_ind)-1][0]:
                res.append(-1)
            else:
                low_start = bisect_left(temp_ind, (intervals[i][1], 0))
                res.append(temp_ind[low_start][1])
        return res
