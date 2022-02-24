# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: # 26.92% 17.60%
        arr = []
        while head:
            arr.append(head)
            head = head.next
        start = cur = ListNode()
        while arr:
            cur.next = arr.pop(0)
            cur = cur.next
            if arr:
                cur.next = arr.pop()
                cur = cur.next
        cur.next = None
        return start.next

    def reorderList_best_speed(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        head2 = prev
        slow.next = None
        curr1 = head
        curr2 = head2
        while curr1 and curr2:
            next_curr1 = curr1.next
            next_curr2 = curr2.next
            curr1.next = curr2
            curr2.next = next_curr1
            curr1 = next_curr1
            curr2 = next_curr2
