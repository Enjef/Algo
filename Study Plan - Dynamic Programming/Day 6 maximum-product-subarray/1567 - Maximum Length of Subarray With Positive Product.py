class Solution:
    def getMaxLen(self, nums: List[int]) -> int:  # 5.20% 60.60%
        neg_len = pos_len = max_len = 0
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            if prod > 0:
                pos_len += 1
                neg_len += 1
                max_len = max(max_len, pos_len, neg_len, 1)
            elif prod == 0:
                prod = 1
                neg_len = pos_len = 0
                continue
            else:
                if nums[i] > 0:
                    pos_len = max(pos_len, 1)
                neg_len += 1
        neg_len = pos_len = 0
        max_len = max(max_len, pos_len)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            if prod > 0:
                pos_len += 1
                neg_len += 1
                max_len = max(max_len, pos_len, neg_len, 1)
            elif prod == 0:
                prod = 1
                neg_len = pos_len = 0
                continue
            else:
                if nums[i] > 0:
                    pos_len = max(pos_len, 1)
                neg_len += 1
        return max(max_len, pos_len)
