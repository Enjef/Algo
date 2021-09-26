class Solution:
    def isSubtree(
            self,
            root: TreeNode,
            subRoot: TreeNode) -> bool:  # 77.65% 98.93%
        def compare(root1, root2):
            stack = [(root1, root2)]
            while stack:
                cur1, cur2 = stack.pop()
                if not cur1 and not cur2:
                    continue
                if (
                        (not cur1 and cur2) or
                        (cur1 and not cur2) or
                        cur1.val != cur2.val):
                    return False
                stack.extend(
                    [(cur1.left, cur2.left), (cur1.right, cur2.right)]
                )
            return True
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            if cur.val == subRoot.val:
                if compare(cur, subRoot):
                    return True
            stack.extend([cur.left, cur.right])
        return False
