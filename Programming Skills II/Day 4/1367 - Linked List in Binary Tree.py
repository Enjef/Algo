# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head, root) -> bool:  # 98.47% 94.08%
        def dfs(cur_tree, cur_list):
            if not cur_list:
                return True
            if not cur_tree or (cur_tree and cur_tree.val != cur_list.val):
                return False
            return (
                dfs(cur_tree.left, cur_list.next) or
                dfs(cur_tree.right, cur_list.next))
        
        stack = [root]
        while stack:
            temp = []
            for cur in stack:
                if cur: 
                    if cur.val == head.val and dfs(cur, head):
                        return True
                    temp.extend([cur.left, cur.right])
            stack = temp
        return False
