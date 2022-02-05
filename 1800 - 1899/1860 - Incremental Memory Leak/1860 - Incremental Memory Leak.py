class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]: # 21.61% 82.41%
        time = 1
        out = [1, memory1, memory2]
        while out[1] >= 0 and  out[2] >= 0:
            if out[1] >= out[2]:
                if out[1]-out[0] < 0:
                    break
                out[1] -= out[0]
            else:
                if out[2]-out[0] < 0:
                    break
                out[2] -= out[0]
            out[0] += 1
        return out

    def memLeak_best_speed(self, memory1: int, memory2: int) -> List[int]:
        def terms(start, sums):
            if start > sums:
                return 0
            return int(((1-start) + math.sqrt((start-1)**2 + 4*sums)) // 2)
        mem1, mem2 = min(memory1, memory2), max(memory1, memory2)
        comp = memory1 >= memory2
        diff = mem2 - mem1
        a = int((-1 + math.sqrt(1 + 8 * diff)) // 2)
        mem2 -= (1+a)*a // 2
        if mem2 > mem1 or (mem2 == mem1 and comp):
            t2 = terms(a+1, mem2)
            mem2 -= (a+t2)*t2
            t1 = terms(a+2, mem1)
            mem1 -= (a+t1+1)*t1
        else:
            t1 = terms(a+1, mem1)
            mem1 -= (a+t1)*t1
            t2 = terms(a+2, mem2)
            mem2 -= (a+t2+1)*t2
        if comp:
            return [a + t1 + t2 + 1, mem2, mem1]
        else:
            return [a + t1 + t2 + 1, mem1, mem2]

    def memLeak_best_memory(self, memory1: int, memory2: int) -> List[int]:
        crashTime = 1
        while True:
            if memory1 >= memory2:
                if memory1 < crashTime:
                    break
                memory1 -= crashTime
            else:
                if memory2 < crashTime:
                    break
                memory2 -= crashTime
            crashTime = crashTime + 1
        return(crashTime, memory1, memory2)

