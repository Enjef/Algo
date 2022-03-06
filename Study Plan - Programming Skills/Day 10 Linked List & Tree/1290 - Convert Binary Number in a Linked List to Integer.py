# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:  # 73.71% 74.58%
        num = []
        while head:
            num.append(str(head.val))
            head = head.next
        return int(''.join(num), 2)
