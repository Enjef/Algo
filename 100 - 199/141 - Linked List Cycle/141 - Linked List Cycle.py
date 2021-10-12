# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:  # 99.72% 23.43%
        if not head:
            return False
        slow = head
        fast = head.next
        while fast:
            if slow == fast:
                return True
            if fast.next is None:
                break
            slow = slow.next
            fast = fast.next.next
        return False

    def hasCycle_sp_day_7(self, head: ListNode) -> bool:  # 6.20% 6.84%
        if not head:
            return False
        unique = set()
        while head:
            if head in unique:
                return True
            else:
                unique.add(head)
                head = head.next
        return False
