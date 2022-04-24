class Solution:
    def checkOnesSegment(self, s: str) -> bool:  # 46.81% 57.75%
        return '01' not in s

    def checkOnesSegment_best_speed(self, s: str) -> bool:
        c=0
        s=s+'0'
        for i in range(len(s)-1):
            if (s[i]=='1') & (s[i+1]=='0'):
                c+=1
                if c>1:
                    return False
        return True

    def checkOnesSegment_3d_speed(self, s: str) -> bool:
        return s.find('01') == -1
