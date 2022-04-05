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

    def findKthPositive_best_speed(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l < r:
            m = (l+r+1)//2
            if (arr[m]-1)-m < k:
                l = m
            else:
                r = m-1
        if k < arr[0]:
            return k
        return arr[l]+(k-(arr[l]-l-1))

    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        i = 1
        cur_k = arr[0] - 1
        while i < n and cur_k < k:
            cur_k += arr[i] - arr[i - 1] - 1
            i += 1
        if cur_k >= k:
            return arr[i-1] - (cur_k - k) - 1
        else:
            return arr[i-1] + (k - cur_k) 
