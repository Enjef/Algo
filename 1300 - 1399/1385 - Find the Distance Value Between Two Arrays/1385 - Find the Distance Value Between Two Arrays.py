class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):  # 74.10% 73.02%
        out = len(arr1)
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    out -= 1
                    break
        return out

    def findTheDistanceValue_v2(self, arr1, arr2, d):  # 99.15% 85.90%
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

    def findTheDistanceValue_best_speed(self, arr1, arr2, d):
        from bisect import bisect, bisect_left
        arr2.sort()
        ans = 0
        for val in arr1:
            left = bisect_left(arr2, val-d)
            right = bisect(arr2, val+d)
            ans += left == right
        return ans

    def findTheDistanceValue_3d_best_speed(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist
