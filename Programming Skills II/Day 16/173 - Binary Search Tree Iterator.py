# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):  # 76.63% 91.56%
        self.arr = []
        self.index = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        self.size = len(self.arr)
        
    def next(self) -> int:
        res = self.arr[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index < self.size


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()