# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 29.47% 41.48% (31.38% 55.21%)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def push_heap(heap_list, x):
            heap_list.append(x)
            pos = len(heap_list) - 1
            while pos > 0 and heap_list[pos].val < heap_list[(pos-1)//2].val:
                heap_list[pos], heap_list[(pos-1)//2] = heap_list[(pos-1)//2], heap_list[pos]
                pos = (pos-1)//2

        def pop_heap(heap_list):
            ans = heap_list[0]
            heap_list[0] = heap_list[-1]
            pos = 0
            while pos * 2 + 2 < len(heap_list):
                min_son_index = pos * 2 + 1
                if heap_list[pos * 2 + 2].val < heap_list[min_son_index].val:
                    min_son_index = pos * 2 + 2
                if heap_list[pos].val > heap_list[min_son_index].val:
                    heap_list[pos], heap_list[min_son_index] = heap_list[min_son_index], heap_list[pos]
                    pos = min_son_index
                else:
                    break
            heap_list.pop()
            if len(heap_list) == 2 and heap_list[0].val > heap_list[1].val:
                heap_list[0], heap_list[1] = heap_list[1], heap_list[0]
            return ans

        dummy = cur = ListNode()
        heap = []
        for el in lists:
            if el:
                push_heap(heap, el)
        while heap:
            new = pop_heap(heap)
            cur.next = new
            new = new.next
            if new:
                push_heap(heap, new)
            cur = cur.next
        return dummy.next


# Best speed and memory
'''
f = open("user.out", 'w')
for s in sys.stdin:
    print('[', ','.join(
        map(str, sorted(int(v) for v in s.rstrip().replace('[', ',').replace(']', ',').split(',') if v))), ']', sep='',
          file=f)
exit(0)
'''


class Solution_2nd_best_speed:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list1 = []
        temp1 = temp2 = ListNode(0)
        for num in lists:
            while num:
                list1.append(num)
                num = num.next
        list1.sort(key=lambda x: x.val)
        for i in list1:
            temp1.next = i
            temp1 = temp1.next
        return temp2.next


class Solution_2nd_best_memory:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            h1 = lists.pop()
            h2 = lists.pop()
            head = tail = ListNode()
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next = h1
                    tail = tail.next
                    h1 = h1.next
                else:
                    tail.next = h2
                    tail = tail.next
                    h2 = h2.next
                tail.next = None
            if h1:
                tail.next = h1
            elif h2:
                tail.next = h2
            lists.append(head.next)
        if lists:
            return lists[0]
        else:
            return None
