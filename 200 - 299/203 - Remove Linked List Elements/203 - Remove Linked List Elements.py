# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):  # 72.88 % 26.95%
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head and head.val == val:
            head = head.next
        cur, prev = head, ListNode(next=head)
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

    def removeElements_sp_day_7(self, head, val):  # 51.03% 26.95%
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        while head.val == val:
            if not head.next:
                return None
            head = head.next
        prev = ListNode(next=head)
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return head

    def removeElements_best_memory(
            self,
            head: Optional[ListNode],
            val: int) -> Optional[ListNode]:
        dummynode=ListNode()
        dummynode.next=head
        travelnode=dummynode
        while(travelnode.next!=None):
            if travelnode.next.val!=val:
                travelnode=travelnode.next
            else:
                temp=ListNode()
                temp=travelnode.next
                travelnode.next=temp.next
        return dummynode.next
