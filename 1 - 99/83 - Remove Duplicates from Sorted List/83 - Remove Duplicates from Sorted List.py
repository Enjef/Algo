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

    def deleteDuplicates_best_speed(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode()
        dummy.next = head
        node = head
        prev = dummy
        while node:
            if node.val in seen:
                prev.next = node.next
                node = node.next
                continue
            seen.add(node.val)
            prev = node
            node = node.next
        return dummy.next

    def deleteDuplicates_2nd_best_speed(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next 
            else:
                cur = cur.next 
        return head

    def deleteDuplicates_best_memory(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
