class Solution:
    def checkArithmeticSubarrays(self, nums, left, right):  # 97.12% 88.01%
        def is_arithmetic(arr):
            arr.sort()
            if len(arr) <= 2:
                return True
            diff = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True
        out = [False] * len(left)
        for j in range(len(left)):
            if is_arithmetic(nums[left[j]:right[j]+1]):
                out[j] = True
        return out

    def checkArithmeticSubarrays_best_memory(self, nums, l, r):
        results = [False]*len(l)
        for i in range(len(l)):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort()
            diff = subarray[1] - subarray[0]
            j = 2
            while j < len(subarray) and subarray[j] - subarray[j-1] == diff:
                j += 1
            results[i] = j == len(subarray)
        return results
