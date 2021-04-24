class Solution:
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
        return([l+1, r+1])


x = Solution()
print(x.twoSum([2,7,11,15], 9))
print(x.twoSum([2,3,4], 6))
print(x.twoSum([-1,0], -1))
print(x.twoSum([1,2,3,4,5,6,7,8,9,10], 13))
print(x.twoSum([5,25,75], 100))
print(x.twoSum([3,24,50,79,88,150,345], 200))
