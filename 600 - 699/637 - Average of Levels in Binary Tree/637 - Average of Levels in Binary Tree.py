# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(
            self,
            root: Optional[TreeNode]) -> List[float]:  # 55.01% 5.72%
        arr = []
        def helper(root, index):
            if not root:
                return arr
            if len(arr)-1 < index:
                arr.append([])
            arr[index].append(root.val)
            helper(root.left, index+1)
            helper(root.right,index+1)
            return arr
        return [sum(x)/len(x) for x in helper(root, 0)]

    def averageOfLevels_stack(
            self,
            root: Optional[TreeNode]) -> List[float]:  # 92.81% 66.71%
        arr = []
        stack = [(root, 0)]
        while stack:
            cur, index = stack.pop()
            if not cur:
                continue
            stack.extend([(cur.left, index+1), (cur.right, index+1)])
            if len(arr)-1 < index:
                arr.append([])
            arr[index].append(cur.val)
        return [sum(x)/len(x) for x in arr]

    def averageOfLevels_best(self, root: TreeNode) -> List[float]:
        queue = deque()
        queue.append(root)
        avg = []
        while queue:
            level_size = len(queue)
            total = 0
            for _ in range(level_size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg.append(total/level_size)
        return avg
