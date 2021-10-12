class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(len(encoded)):
            arr.append(arr[-1] ^ encoded[i])  # better: encoded[i] ^ res[i]
        return arr
