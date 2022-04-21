class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:  # 22.73% 87.11%
        def helper(node):
            if not node:
                return
            helper(node.left)
            arr.append(1)
            helper(node.right)
            return
        arr = []
        helper(root)
        return len(arr)

    def countNodes_v2(self, root: Optional[TreeNode]) -> int:  # 57.17% 47.44%
        def helper(node):
            if not node:
                return 0
            return 1 + helper(node.left) + helper(node.right)

        return  helper(root)

    def countNodes_v3(self, root: Optional[TreeNode]) -> int:  # 11.38% 87.11%
        if not root:
            return 0
        return  1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def nodeExist(idx):
            node = root
            left = 0
            right = 2 ** height - 1
            count = 0
            while count < height:
                mid = math.ceil((left + right)/2)
                if (idx >= mid):
                    node = node.right
                    left = mid                    
                else:
                    node = node.left
                    right = mid - 1
                count += 1
            return  node != None
            
        if not root:
            return 0
        node = root
        height = 0
        while node.left:
            height += 1
            node = node.left
        if height == 0 :
            return 1
        node = root
        left , right = 1 , 2 ** height - 1
        idx = None
        while left <= right:
            idx = left + (right - left) // 2
            if nodeExist(idx):
                left = idx + 1
            else:
                right = idx - 1
        return (2 ** height - 1)  + left 
