class Solution:
    # 27.79% 17.72% (12.35% 98.38%)
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        n = len(str(num))
        for i in range(n-k+1):
            cur = int(str(num)[i:i+k])
            if cur:
                res += int(not num % cur)
        return res


class Solution_best_speed:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        cnt = 0
        for i in range(0, len(num_str)-k+1):
            temp_num = int(num_str[i:i+k])
            if temp_num != 0 and num % temp_num == 0:
                cnt += 1
        return cnt

    def divisorSubstrings_3d(self, num: int, k: int) -> int:
        count = 0
        nums = str(num)
        i,j = 0,0
        while j < len(nums):
            if j - i + 1 < k: j += 1
            else:
                n = int(nums[i:j+1])
                if n > 0 and num % n == 0: count += 1
                i += 1
                j += 1        
        return count


class Solution_best_memory:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snumber = str(num)
        current = ''
        window_end, count = 0, 0
        for window_end in range(len(snumber)):
            current += snumber[window_end]
            if len(current) == k:
                if int(current) != 0 and num % int(current) == 0:
                    count += 1
                current = current[1:]
        return count
