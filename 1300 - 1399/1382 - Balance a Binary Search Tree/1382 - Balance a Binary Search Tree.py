class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:  # 27.75% 11.59%
        def create_tree(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            mid_node = TreeNode(arr[mid])
            mid_node.left = create_tree(arr[:mid])
            mid_node.right = create_tree(arr[mid+1:])
            return mid_node

        def dfs(root):
            if not root.left and not root.right:
                values.append(root.val)
                return
            if root.left:
                dfs(root.left)
            values.append(root.val)
            if root.right:
                dfs(root.right)
            return

        values = []
        dfs(root)
        new_root = TreeNode(left=create_tree(values))
        return new_root.left

    def balanceBST_not_root_check(self, root) -> TreeNode:  # 65.25% 11.59%
        def create_tree(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            mid_node = TreeNode(arr[mid])
            mid_node.left = create_tree(arr[:mid])
            mid_node.right = create_tree(arr[mid+1:])
            return mid_node

        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                values.append(root.val)
                return
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)
            return

        values = []
        dfs(root)
        new_root = TreeNode(left=create_tree(values))
        return new_root.left

    def in_order_traversal(self, root: TreeNode) -> List[TreeNode]:
        stack = []
        in_order_traversal = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            in_order_traversal.append(root)
            root = root.right
        for node in in_order_traversal:
            node.left = None
            node.right = None
        return in_order_traversal

    def balance_dc(self, sorted_nodes, l: int, r: int) -> TreeNode:
        if l > r:
            return None
        if l == r:
            return sorted_nodes[l]
        m = l + (r - l) // 2
        root = sorted_nodes[m]
        root.left = self.balance_dc(sorted_nodes, l, m-1)
        root.right = self.balance_dc(sorted_nodes, m+1, r)
        return root
        
    def balanceBST_best_speed(self, root: TreeNode) -> TreeNode:
        sorted_nodes = self.in_order_traversal(root)
        n = len(sorted_nodes)
        return self.balance_dc(sorted_nodes, 0, n-1)

    def balanceBST_best_memory(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
        
        def build_BST(left,right):
            if left> right: return None
            mid = left +(right - left)//2
            root = nodes[mid]
            root.left = build_BST(left,mid - 1)
            root.right = build_BST(mid + 1, right)
            return root
            
        inorder(root)
        return build_BST(0 , len(nodes) -1)


