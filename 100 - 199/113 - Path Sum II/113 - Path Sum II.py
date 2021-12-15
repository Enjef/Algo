# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(
            self,
            root: Optional[TreeNode],
            targetSum: int) -> List[List[int]]:  # 53.46% 30.89%
        def dfs(root, cur, target, out):
            if not root.left and not root.right and target-root.val == 0:
                out.append(cur+[root.val])
            if root.left:
                dfs(root.left, cur+[root.val], target-root.val, out)
            if root.right:
                dfs(root.right, cur+[root.val], target-root.val, out)
            return out
        if not root:
            return root
        return dfs(root, [], targetSum, [])

    def pathSum_best_speed(
            self,
            root: Optional[TreeNode],
            targetSum: int) -> List[List[int]]:
        ans = []
        if root: 
            mp = {root: None}
            stack = [(root, 0)]
            while stack: 
                node, val = stack.pop()
                val += node.val 
                if node.left: 
                    mp[node.left] = node
                    stack.append((node.left, val))
                if node.right: 
                    mp[node.right] = node 
                    stack.append((node.right, val))
                if not node.left and not node.right and val == targetSum: 
                    path = []
                    while node: 
                        path.append(node.val)
                        node = mp[node]
                    ans.append(path[::-1])
        return ans 

    def isLeaf(self, node):
        return True if node and not node.left and not node.right else False
    
    def pathSum_2nd_best_speed(
            self,
            root: Optional[TreeNode],
            targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        def generate(node, targetSum, path):
            if node:
                if self.isLeaf(node) and targetSum == node.val:
                    self.ans.append(path[:] + [node.val])
                path.append(node.val)
                generate(node.left, targetSum - node.val, path)
                generate(node.right, targetSum - node.val, path)
                path.pop()
        generate(root, targetSum, [])
        return self.ans

    def pathSum_best_memory(
            self,
            root: Optional[TreeNode],
            targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val])]
        sum_paths = []
        while stack:
            node, path = stack.pop()
            if not node.right and not node.left and targetSum == sum(path):
                sum_paths.append(path)
            if node.left:
                stack.append((node.left, path + [node.left.val]))
            if node.right:
                stack.append((node.right, path + [node.right.val]))
        return sum_paths
