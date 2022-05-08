class Solution:
    # 10.07% 5.22%
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        if n == 1:
            if nums[0] == '1':
                return '0'
            else:
                return '1'
        start = int('0b'+'1'*(n-1), 2)+1
        end = int('0b'+'1'+'0'*n, 2)
        seen = {'0b'+x for x in nums}
        candidates = set(str(bin(x)) for x in range(start, end))
        candidates.add('0b'+'0'*n)
        return (candidates-seen).pop()[2:]

    def findDifferentBinaryString_best_speed(self, nums: List[str]) -> str:
        decNums = [int(z, 2) for z in nums]
        n = len(nums)
        for i in range(2**n):
            if i not in decNums:
                return bin(i)[2:].zfill(n)

    def findDifferentBinaryString_best_memory(self, nums: List[str]) -> str:
        a = ['0', '1']
        r = [a]*len(nums)
        for l in itertools.product(*r):
            t = ''.join(l)
            if t not in nums:
                return t
