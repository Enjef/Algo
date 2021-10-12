class Solution:
    def getLucky(self, s: str, k: int) -> int:  # 97.00% 58.58%
        alf = 'abcdefghijklmnopqrstuvwxyz'
        cur = ''.join([str(alf.index(x)+1) for x in list(s)])
        while k:
            cur = sum([int(x) for x in list(str(cur))])
            k -= 1
        return cur

    def getLucky_memory_best(self, s, k):
        dic = {}
        for i in range(1, 27):
            dic[chr(i+96)] = i
        nums = ''
        for i in s:
            nums += str(dic[i])
        x = 0
        while k:
            for i in nums:
                x += int(i)
            nums = str(x)
            x = 0
            k -= 1
        return nums
