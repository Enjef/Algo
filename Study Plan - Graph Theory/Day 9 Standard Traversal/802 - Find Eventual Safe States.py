class Solution:
    def eventualSafeNodes(self, graph):  # 5.11% 5.35%
        def dfs(idx, seen):
            if not graph[idx]:
                mem[idx] = set([idx])                
            if idx in mem:
                return mem[idx]
            if idx in seen:
                return 'cycle'
            seen.add(idx)
            cur = set()
            for i in graph[idx]:
                temp = dfs(i, seen.copy())
                if temp == 'cycle':
                    return 'cycle'
                else:
                    cur.update(temp)
            mem[idx] = cur
            return cur
        
        terminal = set()
        mem = {}

        out = set()
        for index in range(len(graph)):
            test = dfs(index, set())
            if test != 'cycle':
                out.add(index)
        return sorted(terminal | out)


    def eventualSafeNodes_best_speed(self, graph):
        seen = ['new'] * len(graph)

        def hasCycle(node):
            seen[node] = 'unsafe'
            for adj_node in graph[node]:
                if (seen[adj_node] == 'unsafe') or (seen[adj_node] == 'new' and hasCycle(adj_node)):
                    return True
            seen[node] = 'safe'
            return False
                        
        res = []
        for i in range(len(graph)):
            if seen[i] == 'new':
                hasCycle(i)
            if seen[i] == 'safe':
                res.append(i)
        return res

    def eventualSafeNodes_2nd_best_speed(self, graph):
        res= []
        def dfs(node):
            if color[node]: return color[node] == 1
            color[node] = 2
            for ch in graph[node]:
                if not dfs(ch):
                    return False
            color[node] = 1
            return True
        
        color = [0]*len(graph)
        for i in range(len(graph)):
            if dfs(i): res.append(i)
        return res              


class Solution_best_memory:
    def explore(self, visited, index, graph):
        if index in visited:
            graph[index] = False
            return False
        if graph[index] == True:
            return True
        elif graph[index] == False:
            return False
        for j in range(len(graph[index])):
            visited.add(index)
            next_visited = visited.copy()
            is_safe = self.explore(next_visited, graph[index][j], graph)
            if not is_safe:
                graph[index] = False
                return False
        if not graph[index] == False:
            graph[index] = True
            return True
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        for i in range(len(graph)):
            visited = {i}
            is_safe = True
            if graph[i] == True:
                pass
            elif graph[i] == False:
                pass
            else:
                for j in range(len(graph[i])):
                    is_safe = self.explore(visited, graph[i][j], graph)
                    if not is_safe:
                        graph[i] = False
                        break
            if not graph[i] == False:
                graph[i] = True
        solution = []
        for i in range(len(graph)):
            if graph[i]:
                solution.append(i)
        return solution
