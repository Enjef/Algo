class Solution:
    def suggestedProducts(self, products, searchWord):  # 12.51% 98.81%
        n = len(searchWord)
        products.sort()
        out = []
        for i in range(1, n+1):
            cur_char = []
            for word in products:
                if word.startswith(searchWord[:i]):
                    cur_char.append(word)
                    if len(cur_char) == 3:
                        break
            out.append(cur_char)
        return out

    def suggestedProducts_best_speed(self, products, searchWord):
        products = sorted(products)
        l, r = 0, len(products)-1
        output = [[] for _ in searchWord]
        for i in range(len(searchWord)):
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r -= 1
            output[i] = products[l:min(l+3, r+1)]
        return output

    def suggestedProducts_best_memory(self, products, searchWord):
        products.sort()
        res, cur = [], ''
        for c in searchWord:
            cur += c
            i = bisect.bisect_left(products, cur)
            res.append([w for w in products[i:i+3] if w.startswith(cur)])
        return res
