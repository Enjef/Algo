class Solution:
    def capitalizeTitle(self, title: str) -> str:  # 87.24% 94.80%
        return ' '.join(
            word.capitalize() if len(word)>2 else word
            for word in title.lower().split()
        )

    def capitalizeTitle_best_speed(self, title: str) -> str:
        x = title.split()
        st = ''
        for i in x :
            if len(i) > 2 :
                st = st + i.capitalize() + ' '
            else : 
                st = st + i.lower() + ' '
        return st[:len(st)-1]
