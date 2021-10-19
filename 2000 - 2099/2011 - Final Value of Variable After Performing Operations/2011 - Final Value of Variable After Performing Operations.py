class Solution:
    def finalValueAfterOperations(
            self,
            operations: List[str]) -> int:  # 10.78% 91.84%
        return sum([1 if op in ['++X', 'X++'] else -1 for op in operations])
