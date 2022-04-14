class Solution:
    def findClosestElements_heap(self, arr, k, x):  # 50.05% 5.35%
        arr = [(abs(num-x), idx, num) for idx, num in enumerate(arr)]
        heapify(arr)
        return sorted([heappop(arr)[2] for _ in range(k)])

    def findClosestElements_bin(self, arr, k, x):  # 71.00% 43.66%
        n = len(arr)
        left, right = 0, n-1
        res = -1
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        left = max(0, res)
        if arr[left] != x and n > 1:
            left = min((abs(x-arr[left]), left),
                       (abs(x-arr[left+1]), left+1))[1]
        k -= 1
        right = left
        while k:
            if left > 0 and right < n-1:
                if abs(x-arr[left-1]) <= abs(x-arr[right+1]):
                    left -= 1
                else:
                    right += 1
            elif left == 0:
                right += 1
            elif right == n-1:
                left -= 1
            k -= 1
        return arr[left:right+1]

    def findClosestElements_best_speed(self, arr, k, x):
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left+k]
