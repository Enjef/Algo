class Solution:
    def balancedStringSplit(self, s: str) -> int:  # 18.28% 97.37%
        out = 0                                    # 95.84% 9.85% new
        count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                out += 1
        return out

    def balancedStringSplit_mock(self, s: str) -> int:  # 95.84% 68.80%
        left = 0
        right = 0
        out = 0
        for char in s:
            if char == 'L':
                if not right:
                    left += 1
                else:
                    right -= 1
            else:
                if not left:
                    right += 1
                else:
                    left -= 1
            if not left and not right:
                out += 1
        return out        

    def balancedStringSplit_best_speed(self, s: str) -> int:
        stackS = collections.deque()
        stackS.append(s[0])
        count = 0
        c = ''
        for i in s[1:]:
            if len(stackS)==0:
                stackS.append(i)
                c = stackS[-1]
            elif len(stackS)>0:
                c = stackS[-1]
                if i == c:
                    stackS.append(i)
                else:
                    stackS.pop()
                    if len(stackS)==0:
                        count = count +1
        return count

    def balancedStringSplit_2nd_best_speed(self, s: str) -> int:
        ans = 0
        rcount = 0
        lcount = 0
        for ch in s:
            if ch == 'R':
                rcount += 1
            else:
                lcount += 1
            
            if rcount == lcount:
                rcount = 0
                lcount = 0
                ans += 1
        return ans

    def balancedStringSplit_best_memory(self, s: str) -> int:
        balance = 0
        ans = 0
        for i in s:
            if i == 'R':
                balance -= 1
            else:
                balance += 1
            if balance == 0:
                    ans += 1
        return ans
