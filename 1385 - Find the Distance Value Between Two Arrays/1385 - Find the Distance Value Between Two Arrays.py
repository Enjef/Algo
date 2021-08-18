class Solution:
    def findTheDistanceValue(
            self,
            arr1: List[int],
            arr2: List[int],
            d: int) -> int:  # 74.10% 73.02%
        out = len(arr1)
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    out -= 1
                    break
        return out

    def findTheDistanceValue_best_speed(
            self,
            arr1: List[int],
            arr2: List[int],
            d: int) -> int:
        from bisect import bisect, bisect_left
        arr2.sort()
        ans = 0
        for val in arr1:
            left = bisect_left(arr2, val-d)
            right = bisect(arr2, val+d)
            ans += left == right
        return ans
