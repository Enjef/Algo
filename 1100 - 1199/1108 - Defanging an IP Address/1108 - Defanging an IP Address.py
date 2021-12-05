class Solution:
    def defangIPaddr(self, address: str) -> str:  # 80.89% 87.67%
        return address.replace('.','[.]')
