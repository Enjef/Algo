class Solution:
    def average(self, salary: List[int]) -> float: # 99.23% 54.56%
        n = len(salary)
        s_min, s_max, total = float('inf'), -1, 0
        for el in salary:
            s_min, s_max = min(s_min, el), max(s_max, el)
            total += el
        return (total - s_min - s_max)/(n-2)

    def average_best_speed(self, salary: List[int]) -> float:
        salaryarray = []
        for x in salary:
            salaryarray.append(x)
        salaryarray.sort()
        salaryarray.pop(0)
        salaryarray.pop(len(salaryarray)-1)
        average = sum(salaryarray) / len(salaryarray)
        return average    

    def average_best_memory(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(-1)
        salary.pop(0)
        return sum(salary)/len(salary)
