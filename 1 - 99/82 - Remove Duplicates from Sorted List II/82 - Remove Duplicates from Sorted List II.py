# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        unique = True
        last_unique = None
        first = head
        second = first.next
        while second:
            if second.val == first.val:
                second = second.next
                unique = False
                continue
            elif second.val != first.val and not unique:
                first = second
                second = second.next
                continue
            else:
                unique = True
                if not last_unique:
                    last_unique = first
                    head = last_unique
                    second = second.next
                else:
                    last_unique.next = first
                    second = second.next
        return head
