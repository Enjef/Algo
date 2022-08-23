# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time Limit Exceeded
    def isPalindrome_v1(self, head: Optional[ListNode]) -> bool:
        return (f := (f := lambda node: ([node.val] if node else [])+(f(node.next) if node.next else []))(head)) == f[::-1]

    # 41.44% 47.91%
    def isPalindrome_v2(self, head: Optional[ListNode]) -> bool:
        arr = [] 
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]

    # 74.45% 84.51%
    def isPalindrome_v3(self, head: Optional[ListNode]) -> bool:
        prev = ListNode()
        prev.next = fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while prev and head:
            if prev.val != head.val:
                break
            if prev == head or prev.next == head and prev.val == head.val:
                return True
            prev = prev.next
            head = head.next
        return False

    def isPalindrome_best_speed(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            temp = rev
            rev = slow
            slow = slow.next
            rev.next = temp
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

    def isPalindrome_best_memory(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        prev = None
        odd = False
        while p2:
            if p2.next:
                p2 = p2.next.next
            else:
                odd = True
                p2 = None
            future = p1.next
            p1.next = prev
            prev = p1
            p1 = future
        p2 = prev.next if odd else prev
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
