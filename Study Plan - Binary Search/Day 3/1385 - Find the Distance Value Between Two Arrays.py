class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):  # 99.15% 85.90%
        arr2.sort()
        count = 0
        for num in arr1:
            left, right = 0, len(arr2)
            while left < right:
                mid = left + (right-left)//2 
                if abs(arr2[mid] - num) <= d:
                    count -= 1
                    break
                elif arr2[mid] > num:
                    right = mid
                else:
                    left = mid + 1
            count += 1
        return count
