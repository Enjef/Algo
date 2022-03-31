class Solution:
    def validateStackSequences(self, pushed, popped):  # 41.47% 8.55%
        stack = []
        i = 0
        n = len(popped)
        for push in pushed:
            stack.append(push)
            while stack and i < n and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack

    def validateStackSequences_best_speed(self, pushed, popped):
        stack = []
        n, i, j = len(pushed), 0, 0

        while i < n or j < n:
            if stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            elif i < n:
                stack.append(pushed[i])
                i += 1
            else: return False

        return not stack 

    def validateStackSequences_2nd_best_speed(self, pushed, popped):
        i = 0
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(popped)
