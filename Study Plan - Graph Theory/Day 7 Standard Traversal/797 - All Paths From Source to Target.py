class Solution:
    def allPathsSourceTarget(self, graph):  # 97.19% 38.24%
        def dfs(cur, idx):
            if cur[-1] == n-1:
                out.append(cur)
                return
            if idx == n-1:
                return
            for num in graph[idx]:
                dfs(cur+[num], num)
            return
        
        n = len(graph)
        out = []
        dfs([0], 0)
        return out
