class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:  # 20.40% 59.75%
        left = 0
        way = 0
        for i in range(len(nums)):
            if not nums[i]:
                if k:
                    nums[i] = 2
                    k -= 1
                else:
                    while left < i and nums[left] != 2:
                        left += 1
                    if nums[left] == 2:
                        nums[i] = 2
                    left += 1
            way = max(way, i-left+1 if nums[i] else 0)
        return way

    def longestOnes_best_speed(self, A: List[int], K: int) -> int:
        left = right = 0
        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
        return right - left + 1

    def longestOnes_best_memory(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1

    def longestOnes_2nd_best_memory(self, A: List[int], K: int) -> int:
      count, j = 0, 0
      res = float('-inf')
      for i in range(len(A)):
        if A[i] == 0:
          count += 1
        while count > K and j < len(A):
          if A[j] == 0:
            count -= 1
          j += 1
        res = max(res, i-j+1)
      if res == float('-inf'):
        if count <= K:
          return len(A)
        else:
          return 0
      return res
