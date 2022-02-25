"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node': # 5.51% 12.74%
        if not node:
            return node
        
        def create_node(root):
            if not root or root.val in nodes:
                return None
            nodes[root.val] = Node(root.val, [])
            for neighbor in root.neighbors:
                create_node(neighbor)
            return

        def link_node(root):
            if not root:
                return
            cur = nodes[root.val]
            for neighbor in root.neighbors:
                candidate = nodes[neighbor.val]
                if candidate not in cur.neighbors:
                    cur.neighbors.append(candidate)
                    link_node(neighbor)
            return
        
        nodes = {}
        create_node(node)
        link_node(node)
        return nodes[node.val]

class Solution_best_speed:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        return self.clone(node, {})
    
    def clone(self, nd, visited):
        if nd not in visited:
            cl = Node(nd.val)
            visited[nd] = cl
            for n in nd.neighbors:
                cl.neighbors.append(self.clone(n, visited))
        return visited[nd]

class Solution_best_memory:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node
