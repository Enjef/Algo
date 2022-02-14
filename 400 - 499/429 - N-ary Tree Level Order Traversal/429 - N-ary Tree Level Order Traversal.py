"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]: # 39.79% 91.02%
        if not root:
            return []
        out = []
        stack = [root]
        while stack:
            temp = []
            out.append([])
            while stack:
                cur = stack.pop(0)
                out[-1].append(cur.val)
                temp.extend(cur.children)
            stack = temp
        return out

    def levelOrder_best_speed(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            queue_len = len(queue)
            curr_level = []
            for _ in range(queue_len):
                curr = queue.popleft()
                curr_level.append(curr.val)
                for child in curr.children:
                    if child:
                        queue.append(child)
            ans.append(curr_level)
        return ans
