class Solution:
    def countStudents(self, students, sandwiches) -> int: # 66.14% 68.34%
        total = len(students)
        counter = {}
        amt = 0
        for el in students:
            counter[el] = counter.get(el, 0) + 1
        for el in sandwiches:
            if el not in counter or not counter[el]:
                break
            amt += 1
            counter[el] -= 1
        return total - amt

    def countStudents_best_speed(self, students, sandwiches) -> int:
        circular, square = students.count(0), students.count(1)
        for s in sandwiches:
            if s == 0 and circular:
                circular -= 1
            elif s == 1 and square:
                square -= 1
            else:
                break
        return circular + square

    def countStudents_2nd_best_speed(self, students, sandwiches) -> int:
        unchanged=1
        changed=0
        i=0
        j=0
        total=len(students)+len(sandwiches)
        while(unchanged<total):
            if students[0]==sandwiches[0]:
                students=students[:i]+students[i+1:]
                sandwiches=sandwiches[1:]
                unchanged=0
                if len(sandwiches)==0:
                    return 0
            else:
                students=students[1:]+[students[0]]
                unchanged+=1
        return len(sandwiches)

    def countStudents_best_memory(self, students, sandwiches) -> int:
        from collections import Counter 
        c = Counter(students)
        n = len(sandwiches)
        k = 0
        while k < n and c[sandwiches[k]]:
            c[sandwiches[k]] -= 1
            k += 1
        return n-k
