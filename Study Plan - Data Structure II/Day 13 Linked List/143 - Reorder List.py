# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:  # 86.31% 48.42%
        """
        Do not return anything, modify head in-place instead.
        """
        start = head
        if not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = []
        temp = slow.next
        slow.next = None
        slow = temp
        while slow:
            fast.append(slow)
            slow = slow.next
        while fast:
            head_next = head.next
            slow = fast.pop()
            head.next = slow
            slow_next = slow.next
            slow.next = head_next
            head = head_next
            slow = slow_next
        return start
