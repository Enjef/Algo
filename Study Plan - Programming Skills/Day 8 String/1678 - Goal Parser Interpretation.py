class Solution:
    def interpret(self, command: str) -> str:  # 69.02% 45.27%
        return command.replace('()', 'o').replace('(al)', 'al')