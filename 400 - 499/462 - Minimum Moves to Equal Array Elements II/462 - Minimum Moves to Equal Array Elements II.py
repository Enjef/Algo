class Solution:
    def minMoves2(self, nums: List[int]) -> int: # 79.57% 35.77%
        nums.sort()
        avg = nums[len(nums)//2]
        return sum([abs(avg-num) for num in nums])

    def minMoves2_best_speed(self, nums: List[int]) -> int:
        answer = 0
        N = len(nums)
        nums.sort()
        mxcnt = N // 2
        small = nums[:mxcnt]
        big = nums[mxcnt:]
        mid = nums[mxcnt]
        answer += mid * len(small) - sum(small)
        answer += sum(big) - mid * len(big)
        return answer

    def minMoves2_2nd_best_speed(self, arr: List[int]) -> int:
        arr.sort()
        tot = 0
        i,j = 0,len(arr) - 1
        while i < j:
            tot += arr[j] - arr[i]
            j -= 1;i += 1
        return tot

    def minMoves2_best_memory(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        result = 0
        for i in range(len(nums)):
            result = result + abs(nums[i] - nums[mid])
        return result
