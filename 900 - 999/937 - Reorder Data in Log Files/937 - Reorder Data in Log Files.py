class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:  # 22.11% 88.85%
        dig = []
        let = []
        for i, log in enumerate(logs):
            title, *content = log.split()
            if content[0].isalpha():
                let.append([title, content])
            else:
                dig.append(log)
        let.sort(key=lambda x: x[0])
        let.sort(key=lambda x: x[1])
        for i, x in enumerate(let):
            let[i] = ' '.join([x[0], ' '.join(x[1])])
        logs = let + dig
        return logs

    def reorderLogFiles_best_speed(self, logs: List[str]) -> List[str]:
        def sorting_algorithm(log):
            left_side, right_side = log.split(" ", 1)
            if right_side[0].isalpha():
                return (0, right_side, left_side)
            else:
                return (1,)
        return sorted(logs, key=sorting_algorithm)

    def reorderLogFiles_2nd_to_best(self, logs: List[str]) -> List[str]:
        letter_logs = []
        dig_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                dig_logs.append(log)
            else:
                letter_logs.append(log)
                
        def sort_function(entry):
            splitted_entry = entry.split()
            return (splitted_entry[1:], splitted_entry[0])
        letter_logs.sort(key=sort_function)
        return letter_logs + dig_logs

    def reorderLogFiles_best_memory(self, logs: List[str]) -> List[str]:
        return sorted(logs,key=self.sor)

    def sor(self,logs):
        a, b = logs.split(' ', 1)
        if b[0].isalpha():
            return (0, b, a)
        else:
            return (1, None, None)
