class Solution:
    def criticalConnections(self, n, connections):  # 25.12% 39.08%
        def dfs(node, level, prev):
            seen.add(node)
            ranks[node] = level
            for child in server[node]:
                if child == prev:
                    continue
                if child not in seen:
                    dfs(child, level+1, node)
                ranks[node] = min(ranks[child], ranks[node])
                if ranks[child] >= level+1:
                    result.append([node, child])

        ranks = list(range(n))
        server = defaultdict(list)
        for first, second in connections:
            server[first].append(second)
            server[second].append(first)
        seen = set()
        result = []
        dfs(0, 0, -1)
        return result

    def criticalConnections_best_speed(
            self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        arrives, crits = [None]*n, []

        def dfs(node=0, parent=-1, time=1):
            if arrives[node]:
                return
            arrives[node] = time
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node, time + 1)
                if arrives[neighbor] == time + 1:
                    crits.append((node, neighbor))
                else:
                    arrives[node] = min(arrives[node], arrives[neighbor])
            return crits
        return dfs()

    def criticalConnections_best_memory(
            self, n, connections):
        depth_first_search_order = [-1] * n
        back_earliest = [float("inf")] * n
        graph = collections.defaultdict(list)
        for s_edge, e_edge in connections:
            graph[s_edge].append(e_edge)
            graph[e_edge].append(s_edge)

        stack = []
        current_node = 0
        depth_first_search_order[0] = 0
        back_earliest[0] = 0
        current_list = graph[0]
        node_num = 1
        res = []
        while current_list:
            next_node = current_list.pop()
            if depth_first_search_order[next_node] == -1:
                stack.append(current_node)
                current_node = next_node
                depth_first_search_order[current_node] = node_num
                back_earliest[current_node] = depth_first_search_order[current_node]
                current_list = graph[current_node]
                node_num += 1
            else:
                if not stack or (stack and stack[-1] != next_node):
                    back_earliest[current_node] = min(
                        back_earliest[current_node], depth_first_search_order[next_node])

            while stack and not current_list:
                next_node = current_node
                current_node = stack.pop()
                back_earliest[current_node] = min(
                    back_earliest[current_node], back_earliest[next_node])
                if back_earliest[next_node] > depth_first_search_order[current_node]:
                    res.append((next_node, current_node))
                current_list = graph[current_node]
        return res
