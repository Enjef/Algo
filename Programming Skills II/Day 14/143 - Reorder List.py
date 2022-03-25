# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:  #  92.56% 39.85%
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        fast = slow = head
        prev = ListNode(next=head)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        prev.next = None
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        x = first = head
        y = second = prev
        while first and second:
            prev = second
            first_temp = first.next
            first.next = second
            second_temp = second.next
            second.next = first_temp
            first = first_temp
            second = second_temp
        if second:
            prev.next = second
        return
