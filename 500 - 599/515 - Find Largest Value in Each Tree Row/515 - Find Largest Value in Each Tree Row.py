# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues_mock(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 34.89% 57.73%
        out = []
        stack = [root]
        while stack:
            next_level = []
            level_max = float('-inf')
            while stack:
                cur = stack.pop()
                if not cur:
                    continue
                level_max = max(level_max, cur.val)
                next_level.extend([cur.left, cur.right])
            out.append(level_max)
            stack = next_level
        out.pop()
        return out

    def largestValues_mock_v2(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 94.56% 57.73%
        if not root:
            return root
        out = []
        stack = [root]
        while stack:
            next_level = []
            level_max = float('-inf')
            while stack:
                cur = stack.pop()
                if not cur:
                    continue
                level_max = max(level_max, cur.val)
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            out.append(level_max)
            stack = next_level
        return out

    def largestValues_best_speed(
           self,
           root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            levelMax = float('-inf')
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if node:
                    levelMax = max(levelMax,node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(levelMax)
        return result             

    def largestValues_mock(
            self, root: Optional[TreeNode]) -> List[int]:  # 94.18% 58.00%
        if not root:
            return None
        stack = [root]
        out = []
        while stack:
            temp = []
            row_max = float('-inf')
            while stack:
                cur = stack.pop()
                row_max = max(row_max, cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            out.append(row_max)
            stack = temp
        return out
