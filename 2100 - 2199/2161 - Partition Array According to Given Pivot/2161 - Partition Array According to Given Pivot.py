class Solution: # unstable test results with the same code 77.69% 99.09%
    def pivotArray(self, nums, pivot: int): # 7.06% 89.73% (84.45% 89.73%)
        more, eq, less = [], [], []
        for num in nums:
            if num > pivot:
                more.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                less.append(num)
        nums[:] = less + eq + more
        return nums
