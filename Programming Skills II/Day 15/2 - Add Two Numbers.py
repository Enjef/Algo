# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):  # 80.95% 16.63%
        def list_to_int(node):
            result = 0
            i = 0
            while node:
                result += node.val*10**i
                node = node.next
                i += 1
            return result
        
        num = list_to_int(l1) + list_to_int(l2)
        arr = []
        while num:
            arr.append(num%10)
            num //= 10
        arr.reverse()
        head = cur = ListNode()
        while arr:
            cur.val = arr.pop()
            if arr:
                cur.next = ListNode()
            cur = cur.next
        return head
        