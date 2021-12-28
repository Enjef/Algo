class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:  # 97.88% 29.30%
        def perm(arr, cur):
            if not arr:
                if 0 <= cur[0]*10+cur[1] <= 23 and 0 <= cur[2]*10+cur[3] <= 59:
                    valid.add(f'{cur[0]}{cur[1]}:{cur[2]}{cur[3]}')
            for i in range(len(arr)):
                perm(arr[:i]+arr[i+1:], cur+[arr[i]])
            return
        valid = set()
        perm(arr, [])
        return max(valid) if valid else ''

    def largestTimeFromDigits_best_memory(self, A: List[int]) -> str:
        max_time = -1
        for h, i, j, k in itertools.permutations(A):
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        if max_time == -1:
            return ''
        else:
            return '{:02d}:{:02d}'.format(max_time // 60, max_time % 60)
