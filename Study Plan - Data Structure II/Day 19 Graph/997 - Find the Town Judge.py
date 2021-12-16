class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:  # 7.62% 97.78%
        town = [0] * n
        for item in trust:
            town[item[1]-1] += 1
            town[item[0]-1] -= 1
        return -1 if n-1 not in town else town.index(n-1)+1
