class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):  # 43.95% 86.96%
        layers = defaultdict(list)
        for i in range(n):
            layers[manager[i]].append(i)
        res = 0
        stack = [(-1, 0)]
        while stack:
            next_row = set()
            for el, cur_time in stack:
                if el not in layers:
                    res = max(res, cur_time)
                    continue
                next_row.update(
                    tuple((x, cur_time+informTime[x])) for x in layers[el]
                )
            stack = next_row
        return res

    def numOfMinutes_best_speed(self, n, headID, manager, informTime):
        def findTime(c):
            if manager[c] != -1:
                informTime[c] += findTime(manager[c])
                manager[c] = -1
            return informTime[c]

        return max(map(findTime, manager))

    def numOfMinutes_2nd_best_speed(self, n, headID, manager, informTime):
        time = [-1]*n

        def calculate(idx):
            mgr = manager[idx]
            if mgr == -1:
                return 0
            if time[mgr] != -1:
                mgr_time = time[mgr]
            else:
                mgr_time = calculate(mgr)
                time[mgr] = mgr_time
            return mgr_time + informTime[mgr]
        for idx in range(n):
            if(time[idx] != -1):
                continue
            time[idx] = calculate(idx)
        return max(time)

    def numOfMinutes_best_memory(self, n, headID, manager, informTime):
        res = 0
        for i in range(len(manager)):
            if informTime[i] == 0:
                temp = 0
                index = i
                while index != -1:
                    temp += informTime[index]
                    index = manager[index]
                res = max(res, temp)
        return res
