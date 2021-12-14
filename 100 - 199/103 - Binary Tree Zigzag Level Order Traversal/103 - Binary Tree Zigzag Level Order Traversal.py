# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(
            self,
            root: Optional[TreeNode]) -> List[List[int]]:  # 24.43% 45.03%
        if not root:
            return None
        stack = [root]
        out = []
        left = True
        while stack:
            temp = []
            level = []
            while stack:
                cur = stack.pop(0)
                level.append(cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            if left:
                out.append(level)
                left = False
            else:
                out.append(level[::-1])
                left = True
            stack = temp
        return out

    def zigzagLevelOrder_vest_speed(
            self,
            root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = [[root.val]]
        level = [root]
        i = 1
        while(level):
            this_level = []
            for node in level:
                if node.left:
                    this_level.append(node.left)
                if node.right:
                    this_level.append(node.right)
            if this_level:
                if i % 2 == 0:
                    ret.append([node.val for node in this_level])
                else:
                    ret.append([node.val for node in this_level[::-1]])
            level = this_level
            i += 1
        return ret

    def zigzagLevelOrder_2nd_best_speed(
            self,
            root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        leftDirection = True
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                currentNode = queue.pop(0)
                if leftDirection :
                    level.append(currentNode.val)
                else:
                    level.insert(0, currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(level)
            leftDirection = not leftDirection
        return result
