class Solution:
    def findCircleNum(self, isConnected):  # 59.64% 25.88%
        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            for idx in range(n):
                if isConnected[cur][idx]:
                    dfs(idx)
            return
        
        n = len(isConnected)
        res = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
