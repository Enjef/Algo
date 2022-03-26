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

    def rotateRight_best_speed(self, head, k):
        if not head:
            return None
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        n = len(vals)
        k = k % n
        new_vals = vals[-k:] + vals[:-k]
        new_root = ListNode(new_vals[0])
        curr = new_root
        for i in range(1, n):
            curr.next = ListNode(new_vals[i])
            curr = curr.next
        return new_root    

    def rotateRight_best_memory(self, head, k):
        if not head:
            return None
        if not head.next:
            return head
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        new_tail = head
        for _ in range(n- k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
