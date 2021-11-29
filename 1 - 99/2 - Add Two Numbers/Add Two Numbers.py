# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
            self,
            l1: ListNode,
            l2: ListNode) -> ListNode:  # 91.21% 73.50%
        current = l1
        while current is not None:
            if l2 is not None:
                current.val += l2.val
            if current.val > 9:
                if not current.next:
                    current.next = ListNode()
                current.next.val += current.val // 10
                current.val = current.val % 10

            if l2 is not None and l2.next is not None and current.next is None:
                current.next = ListNode()
            current = current.next
            if l2 is not None:
                l2 = l2.next
        return l1

    def addTwoNumbers_mock(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:  # 41.88% 12.38%
        s1 = ''
        s2 = ''
        head = l3 = ListNode()
        while l1 and l2:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)   
            l2 = l2.next
        s1 = str(int(s1[::-1]) + int(s2[::-1]))
        i = len(s1) - 1
        while i > 0:
            l3.val = int(s1[i])
            l3.next = ListNode()
            l3 = l3.next
            i -= 1
        l3.val = s1[0]
        return head

    def addTwoNumbers_best_memory(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        carry = 0
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            total = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            res.next = ListNode(total)
            res = res.next
        if carry > 0:
            res.next = ListNode(carry)
        return dummy.next
