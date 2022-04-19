# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:  # 47.51% 94.87%
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            dfs(node.right)            
        self.first = self.second = self.prev = None
        dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return


class Solution_best_speed:
    def inorder(self,root,arr):
        if root==None:
            return
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
        
    def solve(self,root,arr,idx):
        if root==None:
            return
        self.solve(root.left,arr,idx)
        root.val=arr[idx[0]]
        idx[0]+=1
        self.solve(root.right,arr,idx)
        
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr=[]
        self.inorder(root,arr)
        arr.sort()
        idx=[0]
        self.solve(root,arr,idx)


class Solution_2nd_best_speed:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []     
        startnode = None
        prev = None
        lastnode = None

        def dfs(root):
            nonlocal res, startnode, prev, lastnode
            if not root:
                return 
            dfs(root.left)
            if prev and prev.val > root.val:
                if not startnode:
                    startnode = prev
                lastnode = root            
            prev = root
            dfs(root.right)

        dfs(root)
        if startnode and lastnode:
            startnode.val, lastnode.val = lastnode.val, startnode.val


class Solution_3d_best_speed(object): 
    def recoverTree(self, root):
        res = []
        self.dfs(root, res)
        first, second = None, None
        for i in range(len(res)-1):
            if res[i].val > res[i+1].val and not first:
                first = res[i]
            if res[i].val > res[i+1].val and first:
                second = res[i+1]
        first.val, second.val = second.val, first.val

    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root)
            self.dfs(root.right, res)
