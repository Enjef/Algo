class Solution:
    def levelOrder(
            self,
            root: Optional[TreeNode]) -> List[List[int]]:  # 24.98% 9.20%
        def dfs(node, level, out):
            if not node:
                return out
            if level > len(out):
                out.append([node.val])
            else:
                out[level-1].append(node.val)
            dfs(node.left, level+1, out)
            return dfs(node.right, level+1, out)
        return dfs(root, 1, [])

    def levelOrder_stack(
            self,
            root: Optional[TreeNode]) -> List[List[int]]:  # 15.21% 45.00%
        if not root:
            return root
        stack = [(root, 1)]
        out = []
        while stack:
            cur, level = stack.pop()
            if len(out) < level:
                out.append([cur.val])
            else:
                out[level-1].append(cur.val)
            if cur.right:
                stack.append((cur.right, level+1))
            if cur.left:
                stack.append((cur.left, level+1))
        return out
