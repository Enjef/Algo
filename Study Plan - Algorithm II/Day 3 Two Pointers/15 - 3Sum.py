class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        diff_d = {}
        plus = set()
        minus = set()
        out = set()
        for num in nums:
            diff_d[num] = diff_d.get(num, 0) + 1
            if num < 0:
                minus.add(num)
            elif num > 0:
                plus.add(num)
        if 0 in diff_d and diff_d[0] > 2:
            out.add((0, 0, 0))
        for first in plus:
            for second in minus:
                diff = first + second
                if (
                        -diff in diff_d and (
                            -diff != first and
                            -diff != second or diff_d[-diff] > 1)):
                    out.add(tuple(sorted([-diff, first, second])))
        return out
