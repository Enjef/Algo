class Solution:
    # 97.64% 22.27% (93.58% 16.70%)
    def discountPrices(self, sentence: str, discount: int) -> str:
        discounted = (100 - discount) / 100
        res = []
        for word in sentence.split():
            if word[0] == '$':
                if word[1:].isdigit():
                    res.append(f'${int(word[1:])*discounted:.2f}')
                    continue
            res.append(word)
        return ' '.join(res)

    # 61.24% 96.36% (70.24% 96.36%)
    def discountPrices_v2(self, sentence: str, discount: int) -> str:
        discounted = (100 - discount) / 100
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            if word[0] == '$':
                if word[1:].isdigit():
                    sentence[i] = f'${int(word[1:])*discounted:.2f}'
        return ' '.join(sentence)


class Solution_best_speed:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for i, w in enumerate(words):
            if w[0] != '$':
                continue
            try:
                ii = int(w[1:])
            except:
                continue
            if ii < 0:
                continue
            words[i] = f'${ii*(100-discount)/100:.2f}'
        return ' '.join(words)


class Solution_best_memory:
    def discountPrices_2nd_best(self, sentence: str, discount: int) -> str:
        self.discount = discount
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            word = sentence[i]
            check, price = self.is_price(word)
            if check:
                sentence[i] = '$' + str(self.apply_discount(price))
        return ' '.join(sentence)

    def is_price(self, word):
        digits = set(str(i) for i in range(10))
        price = ''
        if len(word) < 2:
            return False, 0
        if word[0] != '$':
            return False, 0
        for el in word[1:]:
            if el not in digits:
                return False, 0
            price += el
        return True, int(price)

    def apply_discount(self, price):
        ans = price - (self.discount * price / 100)
        return f'{ans:0.2f}'
