# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 25.76% 44.72%
        prev = None
        cur = head
        while cur:
            new = cur.next
            cur.next = prev
            prev = cur
            cur = new
        return prev