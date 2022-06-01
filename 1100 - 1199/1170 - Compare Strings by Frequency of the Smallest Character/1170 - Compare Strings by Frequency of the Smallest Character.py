class Solution:
    def numSmallerByFrequency(
            self, queries: List[str],
            words: List[str]) -> List[int]:  # 98.07% 17.76%
        def weight(el):
            el_min = 'z'
            count = 0
            for char in el:
                if char < el_min:
                    el_min = char
                    count = 1
                elif char == el_min:
                    count += 1
            return count

        def bin_search(target):
            left, right = 0, len(words)
            while left < right:
                mid = (left+right)//2
                if words[mid] > target:
                    left = mid + 1
                else:
                    right = mid
            return left

        words = sorted([weight(word) for word in words], reverse=True)
        out = []
        for query in queries:
            out.append(bin_search(weight(query)))
        return out

    def numSmallerByFrequency_best_speed(self, queries: List[str], words: List[str]) -> List[int]:
        W = sorted([w.count(min(w)) for w in words])
        res = []
        for q in queries:
            cnt = q.count(min(q))
            idx = bisect.bisect(W, cnt)
            res.append(len(words) - idx)
        return res

    def numSmallerByFrequency_best_memory(self, queries: List[str], words: List[str]) -> List[int]:
        for i, q in enumerate(queries):
            queries[i] = q.count(min(q))
        for i, l in enumerate(words):
            words[i] = l.count(min(l))
        result = []
        for q in queries:
            counter = 0
            for w in words:
                if w > q:
                    counter += 1
            result.append(counter)
        return result
