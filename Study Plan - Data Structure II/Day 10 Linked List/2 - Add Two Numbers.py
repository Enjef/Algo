# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:  # 17.73% 46.12%
        dummy = ListNode(next=l1)
        extra = 0
        while l1 and l2:
            l1.val += l2.val
            if l1.val > 9:
                extra = 1
                l1.val %= 10
            if l1.next and not l2.next:
                l2.next = ListNode()
            if not l1.next and l2.next:
                l1.next = ListNode()
            if extra:
                if not(l1.next and l2.next):
                    l1.next = ListNode(val=extra)
                else:
                    l1.next.val += extra
            l1 = l1.next
            l2 = l2.next
            extra = 0
        return dummy.next
