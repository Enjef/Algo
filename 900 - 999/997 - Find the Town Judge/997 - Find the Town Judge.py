class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:  # 7.62% 97.78%
        town = [0] * n
        for item in trust:
            town[item[1]-1] += 1
            town[item[0]-1] -= 1
        return -1 if n-1 not in town else town.index(n-1)+1

    def findJudge_study_plan(self, n: int, trust):  # 69.58% 91.83%
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        town = defaultdict(set)
        for start, end in trust:
            town[start].add(end)
        out = set.intersection(*town.values()) - set(town)
        if not out or len(town) < n-1:
            return -1
        out = out.pop()
        return out if out not in town else -1

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

    def findJudge_best_memory(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1
