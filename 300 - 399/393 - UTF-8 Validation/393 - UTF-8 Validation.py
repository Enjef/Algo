class Solution:
    # 88.30% 12.72%
    def validUtf8(self, data: List[int]) -> bool:
        def sub(arr):
            n = len(arr)
            return (
                arr[0].startswith('1'*n+'0') and
                (sum([x.startswith('10') for x in arr]) == (n-1))
            )

        arr = [bin(x)[2:].zfill(8) for x in data]
        m = len(data)
        i = 0
        while i < m:
            if arr[i].startswith('0'):
                i += 1
            else:
                j = count = 0
                while j < 8 and arr[i][j] == '1':
                    count += 1
                    j += 1
                if count > 4 or not sub(arr[i:i+j]):
                    return False
                i += j
        return True

    def validUtf8_best_speed_and_memory(self, data):
        n_bytes = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0

    def validUtf8_2nd_best_speed(self, data: List[int]) -> bool:
        count = 0
        for byte in data:
            if 128 <= byte <= 191:
                if count <= 0:
                    return False
                count -= 1
            else:
                if count:
                    return False
                if byte < 128:
                    continue
                elif byte < 224:
                    count = 1
                elif byte < 240:
                    count = 2
                elif byte < 248:
                    count = 3
                else:
                    return False
        return count == 0

    def validUtf8_3d_best_speed(self, data: List[int]) -> bool:
        cnt = 0
        for x in data:
            x = bin(x)[2:].zfill(8)
            if cnt:
                if x.startswith('10'):
                    cnt -= 1
                else:
                    return False
            else:
                cnt = x.find('0')
                if cnt not in {0, 2, 3, 4}:
                    return False
                if cnt:
                    cnt -= 1
        return cnt == 0
