class Solution:
    def getAllElements(self, root1, root2) -> List[int]:  # 5.01% 7.10%
        def dfs(root):
            if not root:
                return
            for el in dfs(root.left):
                yield el
            yield root.val
            for el in dfs(root.right):
                yield el

        first = dfs(root1)
        second = dfs(root2)
        one = None
        two = None
        out = []
        while True:
            if one is None:
                one = next(first, float('inf'))
            if two is None:
                two = next(second, float('inf'))
            if one == float('inf') and two == float('inf'):
                break
            if one < two:
                out.append(one)
                one = None
            else:
                out.append(two)
                two = None
        return out

    def getAllElements_v2(self, root1, root2) -> List[int]:  # 93.28% 19.76%
        def dfs(root, res):
            if not root:
                return
            if root.left:
                dfs(root.left, res)
            res.append(root.val)
            if root.right:
                dfs(root.right, res)
        
        first = []
        dfs(root1, first)
        first.reverse()
        second = []
        dfs(root2, second)
        second.reverse()
        out = []
        while first and second:
            if first[-1] < second[-1]:
                out.append(first.pop())
            else:
                out.append(second.pop())
        if first:
            while first:
                out.append(first.pop())
        if second:
            while second:
                out.append(second.pop())
        return out

    def getAllElements_best_speed(
            self, root1: TreeNode, root2: TreeNode) -> List[int]:
        values = []
        def collect(root):
            if root:
                collect(root.left)
                values.append(root.val)
                collect(root.right)
        collect(root1)
        collect(root2)
        return sorted(values)

    def getAllElements_best_memory(self, root1, root2) -> List[int]:
        return self.merge_ordered(self.get_inorder(root1),
                                  self.get_inorder(root2))
    
    def merge_ordered(self, list1, list2):
        l1 = len(list1)
        l2 = len(list2)
        merged = []
        idx1 = idx2 = 0
        while idx1 < l1 and idx2 < l2:
            if list1[idx1] <= list2[idx2]:
                merged.append(list1[idx1])
                idx1 += 1
            else:
                merged.append(list2[idx2])
                idx2 += 1
        return merged + list1[idx1:] + list2[idx2:]
    
    def get_inorder(self, root):
        if not root:
            return []
        inorder = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                node.right = None
            
            if not node.left:
                inorder.append(node.val)
            else:
                stack.append(node)
                stack.append(node.left)
                node.left = None
        return inorder
