class Solution:  # 70.62% 94.31%
    def checkArithmeticSubarrays(
            self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True
        
        out = []
        for i in range(len(l)):
            out.append(check(nums[l[i]:r[i]+1]))
        return out
