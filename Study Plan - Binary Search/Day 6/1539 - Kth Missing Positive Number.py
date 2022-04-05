class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:  # 24.28% 14.78%
        return sorted(set(range(1, arr[-1]+k+1))-set(arr))[k-1]
        
    def findKthPositive_binary_search(self, arr, k):  # 26.82% 52.38%
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] - mid > k:
                right = mid
            else:
                left = mid + 1
        return right + k
