# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k):  # 24.77% 53.21%
        first = second = end = head
        i = 0
        while end.next:
            if i < k-1:
                first = first.next
            if i > k-2:
                second = second.next
            end = end.next
            i += 1
        first.val, second.val = second.val, first.val
        return head

    def swapNodes_best_speed(self, head: ListNode, k: int) -> ListNode:
        first = last = head
        for i in range(1, k):
            first = first.next
        null_checker = first
        while null_checker.next:
            last = last.next
            null_checker = null_checker.next
        first.val, last.val = last.val, first.val
        return head

    def swapNodes_daily(self, head, k):  # 24.77%-83.61% 53.33%
        first = second = last = head
        idx = 1
        while last:
            if idx < k:
                first = first.next
            if idx > k:
                second = second.next
            last = last.next
            idx += 1
        first.val, second.val = second.val, first.val
        return head
