class Solution:
    def findLengthOfShortestSubarray(self, arr):  # 72.41% 23.75%
        n = len(arr)
        left, right, ans = -1, -1, 0
        def binarySearch(arr, x, l, r) :
            ans = r + 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] > x:
                    ans = m
                    r = m - 1
                else:
                    l = m + 1
            return ans 
                
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                left = i-1
                break
        i = n - 1
        while i >= 1:
            if arr[i-1] > arr[i]:
                right = i
                break
            i = i - 1
        if left == -1 or right == -1:
            return 0
        ans = left + 1
        for i in range(right, n):
            ind = binarySearch(arr, arr[i], 0, left)
            ans = max(ans, ind + n - i)
        return n - ans 

    def findLengthOfShortestSubarray_2nd_best_speed(self, arr):
        n = len(arr)
        left = 0
        for i in range(1, n):
            if arr[i] >= arr[i-1]:
                left = i
            else:
                break
        if left == n-1:
            return 0
        right = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                right = i
            else:
                break
        ans = min(n - left + 1, right)
        i = left
        j = right
        for i in range(left, -1, -1):
            j = right
            if arr[i] <= arr[right]:
                ans = min(ans, right - i - 1)
                break
            while j < n and arr[i] > arr[j]:
                j += 1
            ans = min(ans, j - i - 1)
        return ans
