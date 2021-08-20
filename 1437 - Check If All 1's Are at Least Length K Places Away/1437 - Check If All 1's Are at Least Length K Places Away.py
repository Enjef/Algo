class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:  # 16.33% 8.76%
        if 1 not in nums:
            return True
        out = []
        nums = nums[nums.index(1):len(nums)-nums[::-1].index(1)-1]
        for num in nums:
            if num == 1:
                out.append([])
            else:
                out[-1].append(num)
        for el in out:
            if len(el) < k:
                return False
        return True

    def kLengthApart_refactored(
            self,
            nums: List[int],
            k: int) -> bool:  # 50.80% 95.22%
        if 1 not in nums:
            return True
        cur = 0
        for num in nums[nums.index(1)+1:len(nums)-nums[::-1].index(1)]:
            if num == 0:
                cur += 1
            else:
                if cur < k:
                    return False
                cur = 0
        return True

    def kLengthApart_best_speed(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        idx = nums.index(1)
        ans, n, l = True, len(nums), 0
        for i in range(idx + 1, n):
            if nums[i] == 0:
                l += 1
            else:
                if (l < k):
                    ans = False
                    break
                l = 0
        return ans

    def kLengthApart_best_memory(self, nums: List[int], k: int) -> bool:
        prev=-1
        for idx,num in enumerate(nums):
            if num==1:
                if prev!=-1 and idx-prev<k+1:
                    return False
                prev=idx
        return True
