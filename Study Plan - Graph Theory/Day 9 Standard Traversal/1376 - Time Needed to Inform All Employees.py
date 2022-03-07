class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):  # 32.97% 31.67%
        def dfs(idx):
            cur_time = informTime[idx]
            next_level = 0
            for employee in ways[idx]:
                next_level = max(next_level, dfs(employee))
            return cur_time + next_level
        
        ways = defaultdict(list)
        for i, man in enumerate(manager):
            ways[man].append(i)
        return dfs(headID)

    def numOfMinutes_best_speed(self, n, headID, manager, informTime):
        def findTime(c):
            if manager[c] != -1:
                informTime[c] += findTime(manager[c])
                manager[c] = -1
            return informTime[c]
        
        return max(map(findTime, manager))

    def numOfMinutes_best_memory(self, n, headID, manager, informTime):
        time = 0
        for i in range(n):
            if informTime[i] == 0:
                curtime = 0
                j = i
                while manager[j] != -1:
                    curtime += informTime[manager[j]]
                    j = manager[j]
                time = max(time,curtime)
        return time
