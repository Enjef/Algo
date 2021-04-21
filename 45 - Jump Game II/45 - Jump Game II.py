class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0
        i = 0
        count = 0
        while i < len(nums) - 1:
            count += 1
            if i + nums[i] >= len(nums) - 1:
                return count
            if nums[i] > 1:
                if nums[nums[i]] == 0:
                    check = [
                        j + x for j, x in enumerate(nums[i+1:i + nums[i]+1])
                    ]
                    index = check.index(max(check))
                    i += index + 1
                    continue
                check = [j + x for j, x in enumerate(nums[i:i + nums[i]+1])]
                index = check.index(max(check))
                if nums[i+index] == 1:
                    i += nums[i]
                    continue
                i += index
            else:
                i += 1
        return count


x = Solution()
print(x.jump([1,1,1,1,1]), 'Expected: 4')
print(x.jump([1,2,1,1,1]), 'Expected: 3')
print(x.jump([4,1,1,3,1,1,1]), 'Expected: 2')
print(x.jump([2,0,2,0,1]), 'Expected: 2')
print(x.jump([2,3,1,1,4]), 'Expected: 2')
print(x.jump([2,3,0,1,4]), 'Expected: 2')
print(x.jump([2,3,1,1,4]), 'Expected: 2')
print(x.jump([1,2,3]), 'Expected: 2')
print(x.jump([3,4,3,2,5,4,3]), 'Expected: 3')
print(x.jump([2,0,2,4,6,0,0,3]), 'Expected: ?')
print(x.jump([9,4,5,4,1,8,1,2,0,7,8,7,0,6,6,1,1,2,5,0,9,8,4,7,9,6,8,1,4,0,8,5,5,3,9,8,1,2,2,3,0,1,3,2,7,9,3,0,1]), 'Expected: 8')
