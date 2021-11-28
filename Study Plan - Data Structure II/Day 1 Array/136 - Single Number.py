class Solution:
    def singleNumber(self, nums: List[int]) -> int:  # 85.04% 96.80%
        res = 0
        for num in nums:
            res = res ^ num
        return res

    def singleNumber(self, nums: List[int]) -> int:  # 99.99% 60.93%
        cart = set()
        for num in nums:
            if num in cart:
                cart.remove(num)
            else:
                cart.add(num)
        return list(cart)[0]
