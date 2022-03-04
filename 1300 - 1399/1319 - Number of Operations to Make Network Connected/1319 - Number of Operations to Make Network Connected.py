class Solution:
    def makeConnected(self, n: int, connections):  # 5.04% 62.28%
        m = len(connections)
        if n - m - 1  > 0:
            return -1
        networks = []
        for host, target in connections:
            found = [-1, -2]
            for i, net in enumerate(networks):
                if host in net:
                    found[0] = i
                if target in net:
                    found[1] = i
            if found[0] == found[1]:
                networks[found[0]].update([host, target])
            elif found == [-1, -2]:
                networks.append(set([host, target]))
            elif found[0] != -1 and found[1] != -2:
                networks[found[0]].update(networks[found[1]])
                networks.pop(found[1])
            elif found[0] != -1:
                networks[found[0]].add(target)
            else:
                networks[found[1]].add(host)
        return n - sum([len(x)-1 for x in networks]) - 1


class Solution_best_speed:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        def find_root(node, roots):
            while (node != roots[node]):
                roots[node] = roots[roots[node]]
                node = roots[node]
            return node
        
        roots = list(range(n))
        n_components = n
        for c in connections:
            node1 = find_root(c[0], roots)
            node2 = find_root(c[1], roots)
            if node1 != node2:
                roots[node1] = node2
                n_components -= 1
        return n_components-1


class UnionFind_best_speed_v2:
    def __init__(self, sz):
        self.size = [0] * sz
        self.parent = [i for i in range(sz)]
        
    def root(self, index):
        root = index
        while self.parent[root] != root:
            root = self.parent[root]
        self.parent[index] = root
        return root
    
    def union(self, index_1, index_2):
        root_1 = self.root(index_1)
        root_2 = self.root(index_2)
        if root_1 == root_2:
            return
        if self.size[root_1] > self.size[root_2]:
            self.parent[root_2] = root_1
            self.size[root_1] += self.size[root_2]
        else:
            self.parent[root_1] = root_2
            self.size[root_2] += self.size[root_1]


class Solution_best_memory:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [idx for idx in range(n)]
        extraCable = 0
        group = n
        
        def getParent(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        for connection in connections:
            parent1 = getParent(connection[0])
            parent2 = getParent(connection[1])
            if parent1 != parent2:
                group -= 1
                parent[parent1] = parent2
            else:
                extraCable += 1
        if extraCable >= group-1:
            return group-1
        return -1
