class Solution(object):
    def maximumWealth(self, accounts):  # 92.69% 24.55%
        return max([sum(x) for x in accounts])

    def maximumWealth_study_plan(self, accounts):  # 74.95% 81.46%
        return sum(max(accounts, key=lambda x: sum(x)))

    def maximumWealth_best_speed(self, accounts: List[List[int]]) -> int:
        new_list = max([*map(sum, accounts)])
        return new_list
