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

    def isSubtree_best_second_speed(self, s, t):
        def sy(nd):
            return f"A{nd.val}#{sy(nd.left)}{sy(nd.right)}"if nd else"Z"
        return sy(t) in sy(s)

    def isSubtree_best_third_speed(
            self,
            root: Optional[TreeNode],
            subRoot: Optional[TreeNode]) -> bool:
        main_str = self.recurse(root)
        sub_str = self.recurse(subRoot)
        return sub_str in main_str

    def recurse(self, root):
        if not root:
            return None
        left_str = self.recurse(root.left)
        right_str = self.recurse(root.right)
        return (
            "# " + str(root.val) + " " + str(left_str) + " " + str(right_str)
        )

    def isSubtree_memory(
            self,
            root: Optional[TreeNode],
            subRoot: Optional[TreeNode]) -> bool:
        def generateString(rootNode):
            string = []
            stack = [rootNode]
            while stack:
                node = stack.pop()
                if node:
                    string.append('^'+str(node.val))
                    stack.append(node.right)
                    stack.append(node.left)
                else:
                    string.append('#')
            return '_'.join(string)
        return generateString(subRoot) in generateString(root)
