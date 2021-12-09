# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 67.75% 17.37%
        if not head or not head.next:
            return head
        dummy = prev = ListNode(next=head.next)
        while head and head.next:
            next_prev = head
            next_first = head.next.next
            cur_second = head.next
            prev.next = cur_second
            cur_second.next = head
            head.next = next_first
            prev = next_prev
            head = next_first
        return dummy.next
