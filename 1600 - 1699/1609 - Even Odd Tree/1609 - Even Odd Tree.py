# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:  # 19.42% 86.47%
        odd = True
        stack = [root]
        while stack:
            new = []
            if bool(stack[0].val % 2) != odd:
                return False
            if stack[0].left:
                new.append(stack[0].left)
            if stack[0].right:
                new.append(stack[0].right)
            if len(stack) > 1:
                for i in range(1, len(stack)):
                    if (
                        bool(stack[i].val % 2) != odd or
                        stack[i-1].val == stack[i].val or
                        (stack[i-1].val > stack[i].val)*odd or
                            (stack[i-1].val < stack[i].val)*bool(not(odd))):
                        return False
                    if stack[i].left:
                        new.append(stack[i].left)
                    if stack[i].right:
                        new.append(stack[i].right)
            odd = not odd
            stack = new
        return True

    def isEvenOddTree_best_speed(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        is_even_row = True
        while queue:
            if is_even_row:
                pre_val = float("-inf")
            else:
                pre_val = float("inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                if is_even_row:
                    if node.val <= pre_val or node.val & 1 == 0:
                        return False
                else:
                    if node.val >= pre_val or node.val & 1 == 1:
                        return False
                pre_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            is_even_row = not is_even_row
        return True

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = []
        is_even = False
        if root:
            queue.append(root)
        while queue:
            is_even = not is_even
            nodes = 0
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                nodes += 1
                if is_even:
                    if node.val & 1 == 0:
                        return False
                    if level == []:
                        level.append(node.val)
                    else:
                        if level and node.val <= level[-1]:
                            return False
                        level.append(node.val)
                if is_even == False:
                    if node.val & 1 == 1:
                        return False
                    if level == []:
                        level.append(node.val)
                    else:
                        if level and node.val >= level[-1]:
                            return False
                        level.append(node.val)
        return True
