# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):  # 10.63% 84.22%
        if not head or not head.next or not k:
            return head
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        n = len(arr)
        k = k % n
        arr[-1].next = arr[0]
        arr[-k-1].next = None
        return arr[-k]
