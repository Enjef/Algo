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
