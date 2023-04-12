class Solution:
    # 21.51% 69.41% (51.06% 69.41%)
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = path.split('/')
        for el in cur:
            if not el or el == '.':
                continue
            if el == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(el)
        if not stack:
            return '/'
        return '/' + '/'.join(stack)

    # 86.71% 69.41% (97.26% 69.41%)
    def simplifyPath_v2(self, path: str) -> str:
        stack = []
        cur = path.split('/')
        for el in cur:
            if not el or el=='.':
                continue
            if el == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(el)
        return '/' + '/'.join(stack)
