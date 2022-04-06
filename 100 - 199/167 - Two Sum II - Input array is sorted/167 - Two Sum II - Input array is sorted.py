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

    def twoSum_best_speed(self, numbers: List[int], target: int) -> List[int]:
        hashtable = collections.defaultdict(int)
        for i, elem in enumerate(numbers):
            a = target - elem
            if a in hashtable:
                return [hashtable[a] + 1, i + 1]
            else:
                hashtable[elem] = i

    def twoSum_3nd_best_speed(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total < target:
                old_low = numbers[low]
                low += 1
                while old_low == numbers[low]:
                    low += 1
            elif total > target:
                old_high = numbers[high]
                high -= 1
                while old_high == numbers[high]:
                    high -= 1
            else:
                return [low+1, high+1]

    def twoSum_4nd_best_speed(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [i+1, j+1]
