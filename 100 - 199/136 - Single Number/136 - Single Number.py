class Solution(object):
    def singleNumber(self, nums):  # 64.33% 13.97%
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count.pop(num)
        return count.keys()[0]

    def singleNumber_ds_2_v1(self, nums: List[int]) -> int:  # 85.04% 96.80%
        res = 0
        for num in nums:
            res = res ^ num
        return res

    def singleNumber_ds_2_v2(self, nums: List[int]) -> int:  # 99.99% 60.93%
        cart = set()
        for num in nums:
            if num in cart:
                cart.remove(num)
            else:
                cart.add(num)
        return list(cart)[0]

    def singleNumber_best_speed(self, nums):
        return 2 * sum(set(nums)) - sum(nums)
