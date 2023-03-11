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


# 55.25% 61.21% (46.07% 26.39%)
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def list_to_tree(arr):
            if not arr:
                return None
            n = len(arr)
            return TreeNode(
                val=arr[n//2],
                left=list_to_tree(arr[:n//2]),
                right=list_to_tree(arr[n//2+1:]))
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return list_to_tree(arr)


class Solution_best_speed:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root


class Solution_best_memory:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.rec(head)

    def rec(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast, prev = head, head, head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        node = TreeNode(slow.val)
        node.right = self.rec(slow.next)
        node.left = self.rec(head)
        return node
