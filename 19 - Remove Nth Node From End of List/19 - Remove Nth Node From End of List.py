# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        current = head
        x_prev = None
        x_node = head
        if not head.next:
            return None
        while n:
            n -= 1
            current = current.next
        while current:
            current = current.next
            x_prev = x_node
            x_node = x_node.next
        if x_prev == None:
            return head.next
        x_prev.next = x_node.next
        return head
