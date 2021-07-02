class Solution:
    def interpret_my(self, command: str) -> str:
        command = command.replace('(al)', 'al')
        command = command.replace('()', 'o')
        return command

    def interpret_best(self, command: str) -> str:
        result = list()
        for i in range(len(command)):
            if command[i] == 'G':
                result.append('G')
            if command[i] in ('(', 'a', 'l'):
                continue
            if command[i] == ')':
                if command[i - 1] == 'l':
                    result.append('al')
                elif command[i - 1] == '(':
                    result.append('o')
        return ''.join(result)