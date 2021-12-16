class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:  # 7.62% 97.78%
        town = [0] * n
        for item in trust:
            town[item[1]-1] += 1
            town[item[0]-1] -= 1
        return -1 if n-1 not in town else town.index(n-1)+1

    def findJudge_best_speed(self, n: int, trust: List[List[int]]) -> int:
        people = [-1] + [0] * (n) 
        for source, target in trust:
            people[source] = -1
            if people[target] != -1:
                people[target] += 1 
        judges = [p for p, score in enumerate(people) if score==n-1]
        if len(judges) == 1:
            return judges.pop()
        else:
            return -1 
