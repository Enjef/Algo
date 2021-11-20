class Solution:
    def mergeTwoLists(self, l1, l2):  # 92.88% 86.84%
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next

    def mergeTwoLists_v2(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:  # 92.88% 86.84%
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next
        dummy = ListNode(next=start)
        cur = start
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next