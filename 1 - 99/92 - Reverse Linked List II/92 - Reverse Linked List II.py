class Solution:
    # 32.79% 51.75% (87.22% 51.75%)
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        arr[left-1:right] = arr[left-1:right][::-1]
        arr[-1].next = None
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        return arr[0]

    def reverseBetween_best_speed(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        prev = None
        curr = head
        i = 0
        while (i < left-1):
            prev = curr
            curr = curr.next
            i += 1

        preStart = prev
        start = curr

        while i < right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        start.next = curr
        if preStart:
            preStart.next = prev

        return head if left > 1 else prev

    def reverseBetween_best_memory(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        x = head
        y = head
        l = []
        c = 1
        while c < left:
            x = x.next
            c += 1
        y = x
        while c <= right:
            l.append(y.val)
            y = y.next
            c += 1
        m = len(l)-1
        for i in range(len(l)):
            x.val = l[m]
            m -= 1
            x = x.next
        return head

    def reverseBetween_2nd_best_speed(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        if left == right:
            return head
        curr, prev = head, None
        for i in range(left - 1):
            prev = curr
            curr = curr.next
        con, tail = prev, curr
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tail.next = curr
        if con:
            con.next = prev
        else:
            head = prev
        return head

    def reverseBetween_3d_best_speed(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prevLeft, current = dummy, head
        for i in range(left - 1):
            prevLeft, current = current, current.next
        prevNode = None
        for i in range(right - left + 1):
            nextNode = current.next
            current.next, prevNode = prevNode, current
            current = nextNode
        prevLeft.next.next = current
        prevLeft.next = prevNode
        return dummy.next
