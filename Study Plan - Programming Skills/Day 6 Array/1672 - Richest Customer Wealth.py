class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:  # 74.95% 81.46%
        return sum(max(accounts, key=lambda x: sum(x)))
