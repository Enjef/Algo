class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        out = 0
        seen = []

        def dfs(node):
            stack = [isConnected[node]]
            while stack:
                cur = stack.pop()
                for j in range(len(cur)):
                    if cur[j] == 1 and j not in seen:
                        stack.append(isConnected[j])
                        seen.append(j)
            return

        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                out += 1
        return out
