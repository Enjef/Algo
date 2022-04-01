class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:  # 57.72% 97.05%
        max_index = arr.index(max(arr))
        if max_index == 0:
            arr[0] = 0
        return arr.index(max(arr))

    def peakIndexInMountainArray_v2(self, arr):  # 5.07% 61.14%
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

    def peakIndexInMountainArray_best_speed(self, arr: List[int]) -> int:
        beg = 1
        end = len(arr) - 2
        while beg <= end:
            mid = (beg + end) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                beg = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                end = mid - 1
            elif arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
                return -1
        return -1

    def peakIndexInMountainArray_2nd_best_speed(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            elif l == m:
                break
            else:
                r = m
        return l
