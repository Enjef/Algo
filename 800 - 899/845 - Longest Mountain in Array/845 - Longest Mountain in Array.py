class Solution:
    def longestMountain(self, arr: List[int]) -> int:  # 59.17% 87.74%
        if len(arr) < 3:
            return 0
        left = None
        cur = 1
        right = 0
        res = 0
        n = len(arr)
        while cur < n-1:
            if left is None and arr[cur-1] < arr[cur]:
                left = cur-1
            elif arr[cur-1] >= arr[cur] < arr[cur+1]:
                left = cur
            if arr[cur-1] < arr[cur] > arr[cur+1]:
                right = cur+1
                while right < n and arr[right-1] > arr[right]:
                    right += 1
                res = max(res, right - left)
                left = right
            cur += 1
        return res

    def longestMountain_best_speed(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        # 1 if increasing
        # 0 if constant
        # -1 if decreasing after increasing
        curr, ans, state = 1, 0, 0
        matrix = [[0, 0, 0], [1, 1, 1], [0, -1, -1]]
        for i in range(len(arr)-1):
            darr = arr[i+1]-arr[i]
            sgn = (darr > 0) - (darr < 0)
            new_state = matrix[sgn][state]
            if new_state != -1 and state == -1:
                if curr > ans:
                    ans = curr
                curr = 1
            if new_state == 0:
                curr = 0
            curr += 1
            state = new_state
        if state == -1 and curr > ans:
            ans = curr
        return ans if ans >= 3 else 0

    def longestMountain_2nd_best_speed(self, arr: List[int]) -> int:
        asc = 0
        des = 0
        longest = 0
        n = len(arr)
        for i in range(n):
            if not i or arr[i] > arr[i - 1]:
                if des:
                    asc, des = 2, 0
                else:
                    asc += 1
            elif arr[i] < arr[i - 1]:
                if asc == 1:
                    continue
                des += 1
                longest = max(longest, asc + des)
            else:
                asc, des = 1, 0
        return longest

    def longestMountain_3d_best_speed(self, arr: List[int]) -> int:
        output = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                length = 3
                start = i-1
                end = i+1
                while start-1 >= 0 and arr[start-1] < arr[start]:
                    length += 1
                    start -= 1
                while end+1 <= len(arr)-1 and arr[end+1] < arr[end]:
                    length += 1
                    end += 1
                output = max(output, length)

        return output

    def longestMountain_best_memory(self, arr: List[int]) -> int:
        i = ans = 0
        while i < len(arr):
            base = i
            while i+1 < len(arr) and arr[i] < arr[i+1]:
                i += 1
            have_we_climbed_up_at_all = i > base
            if have_we_climbed_up_at_all:
                peak = i
            else:
                i += 1
                continue
            while i+1 < len(arr) and arr[i] > arr[i+1]:
                i += 1
            have_we_gone_at_all = i > peak
            if have_we_gone_at_all:
                end = i
            else:
                i += 1
                continue
            ans = max(ans, end - base + 1)
        return ans
