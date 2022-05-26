# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:  # 64.91% 67.83%
        if not root:
            return ''
        left = right = ''
        if root.left:
            left = f'({self.tree2str(root.left)})'
        if not root.left and root.right:
            left = '()'
        if root.right:
            right = f'({self.tree2str(root.right)})'
        return f'{root.val}{left}{right}' if (left or right) else f'{root.val}'

    def tree2str(self, root: TreeNode) -> str:  # 73.54% 67.83%
        return str(root.val)+ (f'({self.tree2str(root.left)})' if root.left else '()' if root.right else '') + (f'({self.tree2str(root.right)})' if root.right else '')

    def tree2str_best_speed(self, root: Optional[TreeNode]) -> str:
        def dfs(root: Optional[TreeNode]) -> str:
            if not root:
                return ''
            if root.right:
                return str(root.val) + '(' + dfs(root.left) +')(' + dfs(root.right) + ')'
            if root.left:
                return str(root.val) + '(' + dfs(root.left) + ')'
            return str(root.val)
        return dfs(root)

    def tree2str_2nd_best_speed(self, root: Optional[TreeNode]) -> str:
        
        def preorder(node):
            if not node:
                return ''
            else:
                l = preorder(node.left)
                r = preorder(node.right)
                if l == '' and r == '':
                    return str(node.val)
                elif r == '':
                    return str(node.val) + '(' + l + ')'
                else:
                    return str(node.val) + '(' + l + ')' + '(' + r + ')'
        return preorder(root)     

    def tree2str_best_memory(self, root: Optional[TreeNode]) -> str:
        ans = ''
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node in {'(', ')'}:
                    ans += node
                    continue
                ans += str(node.val)
                if node.left or node.right:
                    if node.right:
                        stack.append(')')
                        stack.append(node.right)
                        stack.append('(')
                    stack.append(')')
                    stack.append(node.left)
                    stack.append('(')
        return ans


class Solution_3d_best_speed:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root).replace('None', '')[1:-1]
    
    def dfs(self, node):
        if not node:
            return 
        if node.right and not node.left:
            return f'({node.val}(){self.dfs(node.right)})'
        return f'({node.val}{self.dfs(node.left)}{self.dfs(node.right)})'
