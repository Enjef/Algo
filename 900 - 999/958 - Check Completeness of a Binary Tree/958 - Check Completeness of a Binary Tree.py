class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:  # 65.05% 25.50%
        stack = [root]
        cur = 1
        final = False
        while stack:
            new = []
            new_nodes = 0
            for node in stack:
                if not node and cur or node and final and (node.left or node.right):
                    return False
                if not node:
                    continue
                cur -= 1
                if node.left:
                    new_nodes += 1
                if node.right:
                    new_nodes += 1
                if not node.right or not node.left:
                    final = True
                new.extend([node.left, node.right])
            stack = new
            cur = new_nodes
        return True

    def isCompleteTree_2nd_best_speed(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        isNull = False
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    isNull = True
                    continue
                if isNull:
                    return False
        return True

    def isCompleteTree_best_memory(self, root) -> bool:
        if not root:
            return True
        queue = deque([root])
        null_found = False
        while queue:
            node = queue.popleft()
            if node.left:
                if null_found:
                    return False
                queue.append(node.left)
            else:
                null_found = True
            if node.right:
                if null_found:
                    return False
                queue.append(node.right)
            else:
                null_found = True
        return True


class Solution_best_speed(object):
    node_count = 0
    max_position = 0

    def isCompleteTree(self, root):
        self.isCompleteTreeHelper(root, 1)
        return self.max_position == self.node_count

    def isCompleteTreeHelper(self, root, position):
        if root is None:
            return
        self.node_count += 1
        self.max_position = max(self.max_position, position)
        self.isCompleteTreeHelper(root.left, 2 * position)
        self.isCompleteTreeHelper(root.right, 2 * position + 1)
