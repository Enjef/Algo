class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = set()  # 7.27%
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

    def fourSum_2(self, nums: List[int], target: int) -> List[List[int]]:
        out = []  # 64.15% 98.56%
        count = 0
        nums = sorted(nums)
        n = len(nums)
        last = int(nums[-1])
        for i in range(n - 3):
            first = int(nums[i])
            if first + last * 3 < target:
                continue
            if first * 4 > target:
                break
            for j in range(i + 1, n - 2):
                second = int(nums[j])
                if (first +
                   second +
                   last * 2 < target):
                    continue
                if first + second * 3 > target:
                    break
                for k in range(j + 1, n - 1):
                    third = int(nums[k])
                    if (first + second + third + last < target):
                        continue
                    if first + second + third * 2 > target:
                        break
                    for z in range(k + 1, n):
                        fourth = int(nums[z])
                        temp = [
                            first, second,
                            third, fourth
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

    def fourSum_3(self, nums: List[int], target: int) -> List[List[int]]:
        pair_map = {}  # 75.82% 5.06%
        result = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                cur = nums[i] + nums[j]
                diff = target - cur
                if cur not in pair_map:
                    pair_map[cur] = [[i, j]]
                if diff in pair_map:
                    for pair in pair_map[diff]:
                        x, y = pair
                        if (i!=x and i!=y) and (j!=x and j!=y):
                            temp = [nums[i],nums[j],nums[x],nums[y]]
                            result.add(tuple(sorted(temp)))
                pair_map[cur].append((i, j))
        result = sorted(list(result))
        return result
