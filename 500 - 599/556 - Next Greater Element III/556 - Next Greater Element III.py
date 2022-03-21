class Solution:
    def nextGreaterElement(self, n: int) -> int:  # 85.19% 85.19%
        if n < 10:
            return -1
        num = list(map(int, str(n)))
        size = len(num)
        i = size-2
        while i > 0 and num[i] >= num[i+1]:
            i -= 1
        if num[i] < num[i+1]:
            target = 10
            for el in num[i+1:]:
                if num[i] < el < target:
                    target = el
            j = i+num[i+1:].index(target)+1
            num[i], num[j] = num[j], num[i]
            num[i+1:] = sorted(num[i+1:])
        num = int(''.join(map(str, num)))
        return num if n < num < 2**31 else -1

    def nextGreaterElement_best_speed(self, n: int) -> int:
        nums = list(map(int, str(n)))
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            return -1
        j = len(nums)-1
        while j>=0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        res = []
        for num in nums:
            res.append(str(num))
        res = int(''.join(res))
        if res > n and res < 2**31:
            return res
        else:
            return -1

    def nextGreaterElement_3d_best_speed(self, n: int) -> int:
        from bisect import bisect_right
        string = str(n)
        array, length, ans = [string[-1]], len(string), None
        for i in range(length - 2, -1, -1):
            if string[i] < array[-1]:
                index = bisect_right(array, string[i])
                ans = int(
                    ''.join(string[:i] + array[index] +
                    ''.join(array[:index]) + string[i] +
                    ''.join(array[index + 1:])))
                break
            array.append(string[i])
        return int(ans) if ans is not None and int(ans) <= 2 ** 31 - 1 else -1

    def nextGreaterElement_best_memory(self, n: int) -> int:
        s, s2, cap = str(n), '', (1 << 31) - 1
        
        for idx1, i in enumerate(s[::-1]):
            if not s2 or i >= s2[-1]:
                s2 += i
            else:
                for idx2, j in enumerate(s2):
                    if j > i: 
                        pj = j
                        pi = i
                        break
                res = int(
                    s[:len(s)-idx1-1] +
                    pj +
                    s2[:idx2] + pi + s2[idx2+1:])
                return -1 if res > cap else res
        return -1
