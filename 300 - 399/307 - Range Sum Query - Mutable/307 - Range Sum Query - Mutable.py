class NumArray:

    def __init__(self, nums: List[int]):  # 99.10% 91.54%
        self.nums = nums
        self.total = sum(nums)
        
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.total += diff
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if right + 1 - left < len(self.nums) // 2:
            return sum(self.nums[left: right+1])
        return self.total - sum(self.nums[:left]) - sum(self.nums[right+1:])


class NumArray_best_speed:
    def __init__(self, nums):
        self.nums=nums
        self.sums=sum(self.nums)
	
    def update(self, index, val):
        #if val >= self.nums[index]:
        #    self.sums += (val - self.nums[index])
        #else:
        #    self.sums -= (self.nums[index] - val)
        self.sums=self.sums-self.nums[index]+val
        self.nums[index] = val
    
    def sumRange(self, left, right):
        left_sum=sum(self.nums[:left])
        right_sum=sum(self.nums[right+1:])
        return self.sums-left_sum-right_sum


class NumArray_2nd_best_memory:

    def __init__(self, nums: List[int]):
        self.cache_sum = {}
        self.nums = nums[:]

    def update(self, index: int, val: int) -> None:
        prev_value = self.nums[index]
        self.nums[index] = val
        diff = prev_value - val
        for (left, right), value in self.cache_sum.items():
            if left <= index <= right:
                self.cache_sum[(left, right)] = value - diff

    def sumRange(self, left: int, right: int) -> int:
        if (left, right) not in self.cache_sum:
            self.cache_sum[(left, right)] = sum(self.nums[left:right + 1])
        return self.cache_sum[(left, right)]

