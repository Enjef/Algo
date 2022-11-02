# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 43.37% 83.41% (58.86% 63.27%)
import copy


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left, up, right, down = 0, 0, n, m
        grid = [[-1]*n for _ in range(m)]
        while left <= right and up <= down:
            for i in range(left, right):
                if not head:
                    return grid
                grid[up][i] = head.val
                head = head.next
            up += 1
            for i in range(up, down):
                if not head:
                    return grid
                grid[i][right-1] = head.val
                head = head.next
            right -= 1
            for i in range(right-1, left-1, -1):
                if not head:
                    return grid
                grid[down-1][i] = head.val
                head = head.next
            down -= 1
            for i in range(down-1, up-1, -1):
                if not head:
                    return grid
                grid[i][left] = head.val
                head = head.next
            left += 1
        return grid


class Solution_best_speed:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for _ in range(m)]
        left = 0
        right = n
        top = 0
        down = m
        while left < right and top < down:
            for c in range(left, right):
                grid[top][c] = head.val
                head = head.next
                if head is None:
                    return grid
            top += 1
            if top == down:
                break
            for r in range(top, down):
                grid[r][right - 1] = head.val
                head = head.next
                if head is None:
                    return grid
            right -= 1
            if left == right:
                break
            for c in range(right - 1, left - 1, -1):
                grid[down - 1][c] = head.val
                head = head.next
                if head is None:
                    return grid
            down -= 1
            if down == top:
                break
            for r in range(down - 1, top - 1, -1):
                grid[r][left] = head.val
                head = head.next
                if head is None:
                    return grid
            left += 1
        return grid


class Solution_best_memory:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [-1] * n
        mastermatrix = []
        for i in range(m):
            mastermatrix.append(copy.deepcopy(matrix))

        def travelside(distance, direction, matrix, node, height, width):
            for i in range(distance[0]):
                matrix[height][width] = node.val
                if node.next == None:
                    return 1
                width += direction
                node = node.next
            width -= direction
            distance[0] -= 1
            traveldown(distance, direction, matrix,
                       node, height+1*direction, width)

        def traveldown(distance, direction, matrix, node, height, width):
            for i in range(distance[1]):
                matrix[height][width] = node.val
                if node.next == None:
                    return 1
                height += direction
                node = node.next
            height -= direction
            distance[1] -= 1
            travelside(distance, direction * -1, matrix,
                       node, height, width-1*direction)

        travelside([n, m-1], 1, mastermatrix, head, 0, 0)
        return mastermatrix
