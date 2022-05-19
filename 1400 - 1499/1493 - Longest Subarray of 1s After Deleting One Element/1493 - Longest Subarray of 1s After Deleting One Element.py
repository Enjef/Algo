class Solution:
    def longestSubarray(self, nums: List[int]) -> int:  # 18.08% 46.28%
        result = 0
        cur_union = 0
        cur_chunk = 0
        prev = 0
        all_ones = True
        for num in nums:
            if num:
                cur_union += 1
                cur_chunk += 1
                result = max(result, cur_union)
            else:
                all_ones = False
                if prev:
                    cur_union = cur_chunk
                    cur_chunk = 0
                    continue
                else:
                    cur_union = 0
                    cur_chunk = 0
            prev = num
        if all_ones:
            result -= 1
        return result

    def longestSubarray_best_speed(self, nums: List[int]) -> int:
        min_cur, prev_qt, res  = -1, 0, 0
        for cur, item in enumerate(nums):
            if item == 0:
                res = max(cur - min_cur -1 + prev_qt, res)
                prev_qt = cur - min_cur -1
                min_cur = cur
        if min_cur == -1:
            return cur
        return max(cur - min_cur + prev_qt, res)


    def longestSubarray_2nd_best_speed(self, nums: List[int]) -> int:
        ans, past_n, curr_n = 0, 0, 0
        for n in nums:
            if n == 0:
                ans = max(past_n + curr_n, ans)
                past_n = curr_n
                curr_n = 0
            else:
                curr_n += 1
        ans = max(past_n + curr_n, ans)
        return ans if ans < len(nums) else ans - 1

    def longestSubarray_3d_best_speed(self, nums: List[int]) -> int:
        groups = [(n, len([*g])) for n, g in groupby(nums)]
        if len(groups) == 1:
            return 0 if groups[0][0] == 0 else (groups[0][1] - 1)
        max_so_far = 0
        for i, (n, gl) in enumerate(groups):
            if n == 0:
                continue
            max_starting_here = gl
            if i + 2 < len(groups) and groups[i+1][1] == 1:
                max_starting_here = gl + groups[i+2][1]
            max_so_far = max(max_so_far, max_starting_here)
        return max_so_far

    def longestSubarray_best_memory(self, arr: list[int]) -> int:
        global_max_len = 0
        used_change = 0
        last_ones_idx = None
        current_max_len = 0 
        for idx, el in enumerate(arr):
            if el == 1:
                current_max_len += 1
            else:
                if idx <= len(arr) - 2 and arr[idx + 1] == 1:
                    if used_change == 0:
                        used_change = 1
                        last_ones_idx = idx + 1
                    else:
                        if current_max_len > global_max_len:
                            global_max_len = current_max_len
                        current_max_len = idx - last_ones_idx
                        last_ones_idx = idx + 1
                else:
                    if current_max_len > global_max_len:
                        global_max_len = current_max_len
                    current_max_len = 0
                    used_change = 0
        if current_max_len > global_max_len:
            global_max_len = current_max_len
        if global_max_len == len(arr):
            global_max_len -= 1
        return global_max_len

    def longestSubarray_2nd_best_memory(self, nums: List[int]) -> int:
        ans = 0
        p0 = p1 = 0
        for num in nums:
            if num == 0:
                p1, p0 = p0, 0
            else:
                p0 += 1
                p1 += 1
            ans = max(ans, p1)
        if ans == len(nums):
            ans -= 1
        return ans
