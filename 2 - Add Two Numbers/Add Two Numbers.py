# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = l1
        while current is not None:
            if l2 is not None:
                current.val += l2.val
            if current.val > 9:
                if not current.next:
                    current.next = ListNode()
                current.next.val += current.val // 10
                current.val = current.val % 10

            if l2 is not None and l2.next is not None and current.next is None:
                current.next = ListNode()
            current = current.next
            if l2 is not None:
                l2 = l2.next
        return l1