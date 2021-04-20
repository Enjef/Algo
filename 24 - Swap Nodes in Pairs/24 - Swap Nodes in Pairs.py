# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        first = head.next
        second = head
        head = first
        second.next = first.next
        first.next = second
        prev = second
        if second.next:
            while prev.next.next:
                first = prev.next.next
                second = prev.next
                prev.next = first
                second.next = first.next
                first.next = second
                if second.next:
                    prev = second
                else:
                    break
        return head
