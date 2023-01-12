class Solution:
    # 86.54% 82.69% (89.10% 83.33%)
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node, prev):
            if node not in root:
                res[node] = 1
                return dict((labels[node], 1))
            new = defaultdict(int)
            for child in root[node]:
                if child == prev:
                    continue
                cur = dfs(child, node)
                for key in cur:
                    new[key] += cur[key]
            new[labels[node]] += 1
            res[node] = new[labels[node]]
            return new

        root = defaultdict(list)
        for x, y in edges:
            root[x].append(y)
            root[y].append(x)

        res = [0] * n
        dfs(0, -1)
        return res


class Solution_best_speed:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        response = [0] * n
        node2edges = [[] for _ in range(n)]
        for edge in edges:
            node2edges[edge[0]].append(edge[1])
            node2edges[edge[1]].append(edge[0])

        def dfs(nodeId: int, parentNodeId: int, labelCounter: List[int]) -> None:
            nodeLabelId = ord(labels[nodeId]) - 97
            before = labelCounter[nodeLabelId]
            labelCounter[nodeLabelId] += 1
            for nextNodeId in node2edges[nodeId]:
                if nextNodeId == parentNodeId:
                    continue
                dfs(nextNodeId, nodeId, labelCounter)
            response[nodeId] = labelCounter[nodeLabelId] - before

        dfs(0, -1, [0] * 26)
        return response


class Solution_best_memory:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        seen = [False] * n
        count = [0] * 26
        ans = [0] * n

        def postOrder(i):
            if seen[i]:
                return
            seen[i] = True
            before = count[ord(labels[i]) - ord('a')]
            for j in g[i]:
                postOrder(j)
            count[ord(labels[i]) - ord('a')] += 1
            ans[i] = count[ord(labels[i]) - ord('a')] - before
        postOrder(0)
        return ans
