# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:  # 98.83% 24.07%
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head

    def deleteDuplicates_sp_day_8(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 5.51% 55.88%
        if not head:
            return head
        cur = head
        while cur:
            if cur.next:
                if cur.next.val == cur.val:
                    cur.next = cur.next.next
                    continue
            cur = cur.next
        return head
