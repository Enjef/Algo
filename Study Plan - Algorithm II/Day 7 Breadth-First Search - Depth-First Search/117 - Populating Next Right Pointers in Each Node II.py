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

    def connect_second_try(self, root: 'Node') -> 'Node':  # 93.23% 82.41%
        if not root:
            return root
        stack = [root.left, root.right]
        while stack:
            temp = []
            for i in range(len(stack)):
                cur = stack[i]
                if not cur:
                    continue
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                if i == len(stack)-1:
                    continue
                cur.next = stack[i+1]
            stack = temp
        return root

    def connect_refactored(self, root: 'Node') -> 'Node':  # 97.93% 82.41%
        if not root:
            return root
        stack = [root]
        while stack:
            temp = []
            for i in range(len(stack)):
                cur = stack[i]
                if i < len(stack)-1:
                    cur.next = stack[i+1]
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            stack = temp
        return root
