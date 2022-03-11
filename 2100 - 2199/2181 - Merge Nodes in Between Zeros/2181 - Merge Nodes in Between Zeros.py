# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):  # 99.26% 97.22%
        cur = prev = head
        while cur:
            while cur and cur.val:
                prev.val += cur.val
                cur.val = 0
                cur = cur.next
            if prev.val:
                prev = prev.next
            if cur:     
                cur = cur.next
        cur = head
        while cur and cur.next and cur.next.val:
            cur = cur.next
        cur.next = None
        return head

    def mergeNodes_best_speed(self, head):
        ptr1 = head
        ptr2 = head.next
        s = 0
        while ptr2:
            if ptr2.val == 0:
                ptr1 = ptr1.next
                ptr1.val = s
                s = 0
            else:
                s += ptr2.val
            ptr2 = ptr2.next
        ptr1.next = None
        return head.next

    def mergeNodes_best_memory(self, head):
        arr = []
        cur = head
        while cur:
            if cur.val == 0:
                arr.insert(0, 0)
            else:
                arr[0] += cur.val
            cur = cur.next
        arr = arr[::-1]
        sentinel = ListNode(0)
        cur = sentinel
        for i in range(len(arr) - 1):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return sentinel.next
