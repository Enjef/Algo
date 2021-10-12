class Solution(object):
    def maximumWealth(self, accounts):
        return max([sum(x) for x in accounts])
