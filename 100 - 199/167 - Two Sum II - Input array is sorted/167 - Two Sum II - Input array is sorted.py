class Solution:
    def twoSum(self, numbers, target: int):  # 88.69% 5.00%
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
        return([l+1, r+1])

    def twoSum_bin_search(
            self,
            numbers: List[int],
            target: int) -> List[int]:  # 28.86% 5.00%
        for i in range(len(numbers)):
            left, right = i+1, len(numbers) - 1
            cur = target - numbers[i]
            while left <= right:
                mid = left + (right - left) // 2
                if cur == numbers[mid]:
                    return [i+1, mid+1]
                elif numbers[mid] > cur:
                    right = mid - 1
                else:
                    left = mid + 1
