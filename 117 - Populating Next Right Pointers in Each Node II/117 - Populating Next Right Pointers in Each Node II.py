class Solution:
    def connect(self, root: 'Node') -> 'Node':  # 78.19% 48.24%
        if not root:
            return root
        stack = [root]
        while stack:
            level = []
            for i, node in enumerate(stack):
                if i < len(stack)-1:
                    node.next = stack[i+1]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            stack = level
        return root

    def connect_best_speed(self, root: 'Node') -> 'Node':
        queue = collections.deque()
        if not root:
            return root
        queue.append((root, 0))
        prev, prevlevel = None, -1
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            if level == prevlevel:
                prev.next = node
            prev, prevlevel = node, level
        return root

    def connect_best_memory(self, root: 'Node') -> 'Node':
        pre = root
        while pre:
            cur = pre
            node1 = None
            first = None
            while cur:
                if cur.left:
                    first = cur.left
                    break
                if cur.right:
                    first = cur.right
                    break
                cur = cur.next
            node1 = first
            while cur:
                if cur.left and node1 != cur.left:
                    node1.next = cur.left
                    node1 = cur.left
                if cur.right and node1 != cur.right:
                    node1.next = cur.right
                    node1 = cur.right
                cur = cur.next
            pre = first
        return root
