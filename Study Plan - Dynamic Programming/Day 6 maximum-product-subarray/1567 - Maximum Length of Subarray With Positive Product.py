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

    def getMaxLen_pos_neg_dp(self, nums: List[int]) -> int:  # 70.30% 60.74%%
        pos = [0]*len(nums)
        neg = [0]*len(nums)
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = 1 + pos[i-1]
                neg[i] = 1 + neg[i-1] if neg[i-1] else 0
            elif nums[i] < 0:
                neg[i] = 1 + pos[i-1]
                pos[i] = 1 + neg[i-1] if neg[i-1] else 0
        return max(pos)

    def getMaxLen_vars_dp(self, nums: List[int]) -> int:  # 84.27% 92.70%
        pos = neg = 0
        res = -1
        pos = 1 if nums[0] > 0 else 0
        neg = 1 if nums[0] < 0 else 0
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0
            elif nums[i] < 0:
                neg, pos = 1 + pos, 1 + neg if neg else 0
            else:
                pos = neg = 0
            res = max(res, pos)
        res = max(res, pos)
        return res if res > 0 else 0
