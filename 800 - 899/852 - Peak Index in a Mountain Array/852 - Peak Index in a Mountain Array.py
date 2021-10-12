class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:  # 57.72% 97.05%
        max_index = arr.index(max(arr))
        if max_index == 0:
            arr[0] = 0
        return arr.index(max(arr))

    def peakIndexInMountainArray_best(self, arr: List[int]) -> int:
        l, r, peak = 0, len(arr)-1, 0
        while l <= r:
            m = (l + r) // 2
            if arr[m-1] < arr[m] > arr[m+1]:
                peak = m
                break
            elif arr[m-1] < arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m-1
        return peak
