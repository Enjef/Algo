# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:  # 86.98% 
        num = []
        while head:
            num.append(head.val)
            head = head.next
        num = ''.join(str(i) for i in num)
        return int(num, 2)
