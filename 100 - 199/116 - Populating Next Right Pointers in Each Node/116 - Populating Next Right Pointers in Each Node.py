class Solution:
    def connect(self, root: 'Node') -> 'Node':  # 40.60% 32.29%
        if not root:
            return root
        stack = [[root, 1]]
        levels = []
        while stack:
            cur, level = stack.pop(0)
            if len(levels) < level:
                levels.append([])
            if cur.left:
                levels[level-1].append(cur.left)
                stack.append([cur.left, level+1])
            if cur.right:
                levels[level-1].append(cur.right)
                stack.append([cur.right, level+1])
        levels.pop()
        for level in levels:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root

    def connect_mock(self, root) -> 'Optional[Node]':  # 95.73% 34.93%
        if not root:
            return root
        stack = [root]
        while stack:
            temp = []
            while stack:
                cur = stack.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            for i in range(len(temp)-1):
                temp[i].next = temp[i+1]
            stack = temp
        return root

    def connect_best_speed(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect_best_speed(root.left)
        self.connect_best_speed(root.right)
        return root

    def connect_third_best_memory(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = collections.deque([root])
        while queue:
            nextt = None
            for _ in range(len(queue)):
                node = queue.popleft()
                node.next = nextt
                nextt = node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return root

    def connect_best_speed_new(self, root) -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.appendleft(root)
        while q:
            sz = len(q)
            prev = None
            for _ in range(sz):
                curr = q.pop()
                if prev:
                    prev.next = curr
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
                prev = curr
        return root
