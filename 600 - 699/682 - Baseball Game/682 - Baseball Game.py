class Solution(object):
    def calPoints(self, ops):
        out = []
        for i in ops:
            if i.lstrip('-').isdigit():
                out.append(int(i))
            if i == 'C':
                out.pop()
            if i == 'D':
                out.append(2 * out[-1])
            if i == '+':
                out.append(out[-1] + out[-2])
        return sum(out)

    def calPoints_daily(self, ops: List[str]) -> int:  # 84.23% 74.69%
        stack = []
        for operation in ops:
            if operation == '+':
                stack.append(stack[-2]+stack[-1])
            elif operation == 'D':
                stack.append(stack[-1]*2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)

    def calPoints_best_memory(self, ops: List[str]) -> int:
        if not ops:
            return 0
        stack = []
        for op in ops:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
                if op[0] == '-':
                    stack.append(-int(op[1:]))
                else:
                    stack.append(int(op))
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                new_value = stack[-1] * 2
                stack.append(new_value)
            elif op == '+':
                new_value = stack[-1] + stack[-2]
                stack.append(new_value)
        return sum(stack)
