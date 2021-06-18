class Solution(object):
    def calPoints(self, ops):
        out = []
        for i in ops:
            if i.lstrip('-').isdigit():
                out.append(int(i))
            if i == 'C':
                out.pop()
            if i == 'D':
                out.append(2 * out[-1])
            if i == '+':
                out.append(out[-1] + out[-2])
        return sum(out)
    
    def calPoints_else(self, ops: List[str]) -> int:
        out = []
        for i in ops:
            if i == 'C':
                out.pop()
            elif i == 'D':
                out.append(2 * out[-1])
            elif i == '+':
                out.append(out[-1] + out[-2])
            else:            
                out.append(int(i))
        return sum(out)  

