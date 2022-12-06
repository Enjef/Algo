# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 85.69% 78.70% (78.38% 31.02%)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = even = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
            if n % 2:
                even = cur
        last = None
        if not n % 2:
            last = even.next
        n = n // 2 - int(not n % 2)
        cur = head
        while n:
            even.next = cur.next
            even = even.next
            cur.next = cur.next.next
            cur = cur.next
            n -= 1
        even.next = last
        return head


class Solution_best_speed:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        so = odd = head
        se = even = head.next
        while odd and odd.next and even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = se
        return so

    def oddEvenList_2nd(self, head):
        if not head:
            return head
        odd = head
        even_head, even = head.next, head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head
