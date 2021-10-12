class Solution:
    def findCircleNum(
            self,
            isConnected: List[List[int]]) -> int:  # 54.09% 73.49%
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

    def findCircleNum_best_speed(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        count = 0
        visited = set()
        for start in range(len(isConnected)):
            if start not in visited:
                count += 1
                dfs(start)
        return count

    def findCircleNum_3d_to_best_memory(
            self,
            isConnected: List[List[int]]) -> int:
        isVisited = []
        queue = collections.deque()
        numPro = 0
        for city in range(len(isConnected)):
            if city in isVisited:
                continue
            numPro += 1
            queue.append(city)
            while queue:
                targetCity = queue.popleft()
                isVisited.append(targetCity)

                for secondCity in range(len(isConnected)):
                    if (
                            isConnected[targetCity][secondCity] == 1 and
                            secondCity not in isVisited):
                        queue.append(secondCity)
        return numPro
