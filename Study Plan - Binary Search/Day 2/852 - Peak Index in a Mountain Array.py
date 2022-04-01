class Solution:
    def peakIndexInMountainArray_best(self, arr):  # 5.07% 61.14%
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

    def peakIndexInMountainArray(self, arr: List[int]) -> int:  # 94.23% 93.02%
        return arr.index(max(arr))
