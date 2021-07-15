class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:  # 7.27%
        out = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left, right = i + 1, j - 1
                while left < right:
                    temp = [nums[i], nums[j], nums[left], nums[right]]
                    if sum(temp) == target:
                        out.add(sorted(temp))
                        right -= 1
                        left += 1
                    elif sum(temp) > target:
                        right -= 1
                    else:
                        left += 1
        return out

    def fourSum_2(self, n: List[int], t: int) -> List[List[int]]:  # 61.41% 92.82%
        out = []
        count = 0
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            if int(nums[i]) + int(nums[len(nums) - 1]) * 3 < target:
                continue
            if int(nums[i]) * 4 > target:
                break
            for j in range(i + 1, len(nums) - 2):
                if int(nums[i]) + int(nums[j]) + int(nums[len(nums) - 1]) * 2 < target:
                    continue
                if int(nums[i]) + int(nums[j]) * 3 > target:
                    break
                for k in range(j + 1, len(nums) - 1):
                    if int(nums[i]) + int(nums[j]) + int(nums[k]) + int(nums[len(nums) - 1]) < target:
                        continue
                    if int(nums[i]) + int(nums[j]) + int(nums[k]) * 2 > target:
                        break
                    for z in range(k + 1, len(nums)):
                        temp = [
                            int(nums[i]), int(nums[j]),
                            int(nums[k]), int(nums[z])
                        ]
                        if sum(temp) < target:
                            continue
                        if sum(temp) > target:
                            break
                        if sum(temp) == target:
                            if temp not in out:
                                count += 1
                                out.append(sorted(temp))
        return out
