class Solution:
    def twoSum(self, numbers, target):  # 5.03% 13.06%
        n = len(numbers)
        for i in range(n-1):
            left, right = i+1, n-1
            while left <= right:
                mid = left + (right-left)//2
                if numbers[i] + numbers[mid] == target:
                    return i+1, mid+1
                if numbers[i] + numbers[mid] > target:
                    right = mid-1
                else:
                    left = mid+1

    def twoSum(self, numbers, target):  # 5.03% 46.00%
        n = len(numbers)
        for i in range(n-1):
            left, right = i+1, n-1
            cur = target - numbers[i]
            while left <= right:
                mid = left + (right-left)//2
                if cur == numbers[mid]:
                    return i+1, mid+1
                if cur < numbers[mid]:
                    right = mid-1
                else:
                    left = mid+1


