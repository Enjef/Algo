# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        while head.next:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next
        head.next = prev
        return head

    def short(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

    def reverseList_sp_day_8(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 10.73% 46.12%
        if not head:
            return head
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
