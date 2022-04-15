class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:  # 92.54% 51.77%
        arr = []
        for num in nums:
            if not arr or arr[-1] < num:
                arr.append(num)
            left, right = 0, len(arr)-1
            while left < right:
                mid = left + (right-left)//2
                if arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            arr[left] = num
        return len(arr)
