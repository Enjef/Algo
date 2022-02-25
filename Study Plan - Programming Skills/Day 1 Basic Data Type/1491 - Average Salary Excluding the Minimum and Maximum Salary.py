class Solution:
    def average(self, salary: List[int]) -> float: # 18.97% 50.86% 
        salary.sort()
        sub = salary[1:-1]
        return sum(sub)/len(sub)
