# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):  # 92.27%  61.84%
        l3 = ListNode()
        out = l3
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 or l2
        return out.next

    def mergeTwoLists_sp_day_7(self, l1, l2):  # 92.27% 31.47%
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
