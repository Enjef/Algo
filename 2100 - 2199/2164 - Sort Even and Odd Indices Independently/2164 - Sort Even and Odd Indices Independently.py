class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:  # 71.60% 75.66%
        odd = sorted([x for i, x in enumerate(
            nums) if not i % 2], reverse=True)
        even = sorted([x for i, x in enumerate(nums) if i % 2])
        res = []
        while odd or even:
            if odd:
                res.append(odd.pop())
            if even:
                res.append(even.pop())
        return res

    def sortEvenOdd_best_speed(self, nums: List[int]) -> List[int]:
        odds = sorted(nums[1::2], reverse=True)
        evens = sorted(nums[::2])
        return [
            item for sublist in zip_longest(evens, odds)
            for item in sublist if item]

    def sortEvenOdd_2nd_best_speed(self, nums: List[int]) -> List[int]:
        lst = []
        pst = []
        for i in range(len(nums)):
            if(i % 2 == 0):
                lst.append(nums[i])
            else:
                pst.append(nums[i])
        lst.sort()
        pst.sort(reverse=True)
        ctr = 0
        ptr = 0
        nums.clear()
        for i in range(len(lst)+len(pst)):
            if(i % 2 == 0):
                nums.append(lst[ctr])
                ctr += 1
            else:
                nums.append(pst[ptr])
                ptr += 1
        return nums
