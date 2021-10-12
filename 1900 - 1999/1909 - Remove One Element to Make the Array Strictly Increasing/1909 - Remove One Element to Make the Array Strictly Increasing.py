class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:  # 99.21% 92.28% 
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
            if nums[i-1] > nums[i]:
                count += 1
                if i <= len(nums)-2:
                    if nums[i-1] < nums[i+1]:
                        continue
                    if nums[i-1] == nums[i+1] and len(nums) > 3:
                        return False
                    else:
                        if i >= 2:
                            if nums[i-2] >= nums[i]:
                                return False
            if count > 1:
                return False
        return True

    def canBeIncreasing_best(self, nums: List[int]) -> bool:  # 96.80% 92.28%
        stack = []
        remove = False
        for i in nums:
            if not stack:
                stack.append(i)
                continue
            if stack[-1] < i:
                stack.append(i)
                continue
            if remove:
                return False
            else:
                remove = True
            if len(stack) > 1:
                if i > stack[-2]:
                    stack.pop()
                    stack.append(i)
                else:
                    continue
            else:
                stack.pop()
                stack.append(i)
        return True
