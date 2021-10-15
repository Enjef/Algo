class Solution:
    def connect(self, root: 'Node') -> 'Node':  # 50.30% 31.59%
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

    def connect_second_sp_run(self, root: 'Node') -> 'Node':  # 24.74% 31.59%
        if not root:
            return root
        stack = [root]
        while stack:
            new = []
            for i in range(len(stack)):
                if stack[i].left:
                    new.extend([stack[i].left, stack[i].right])
                if i < len(stack)-1:
                    stack[i].next = stack[i+1]
            stack = new
        return root
