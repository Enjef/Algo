class Solution:
    def findingUsersActiveMinutes(
            self,
            logs: List[List[int]],
            k: int) -> List[int]:  # Time Limit Exceeded
        x_map = {}
        out = [0] * k
        for user, time in logs:
            if user not in x_map:
                x_map[user] = set()
            x_map[user].add(time)
        for i in range(1, len(out)+1):
            count = 0
            for user in x_map:
                if i == len(x_map[user]):
                    count += 1
            out[i-1] += count
        return out

    def findingUsersActiveMinutes_my_second(
            self,
            logs: List[List[int]],
            k: int) -> List[int]:  # 96.56% 44.66%
        x_map = {}
        out = [0] * k
        for user, time in logs:
            if user not in x_map:
                x_map[user] = set()
            x_map[user].add(time)
        for user in x_map:
            out[len(x_map[user])-1] += 1
        return out

    def findingUsersActiveMinutes_best_speed(
            self,
            logs: List[List[int]],
            k: int) -> List[int]:
        hashmap = collections.defaultdict(set)
        result = [0] * k
        for log in logs:
            hashmap[log[0]].add(log[1])
        for time in hashmap.values():
            result[len(time)-1] += 1
        return result

    def findingUsersActiveMinutes_best_memory(
            self,
            logs: List[List[int]],
            k: int) -> List[int]:
        a = []
        for i in range(k):
            a.append(0)
        logs.sort(key=lambda x: (x[0], x[1]))
        i = 0
        while(i < len(logs)):
            j = i + 1
            if(j >= len(logs)):
                break
            if(logs[i] == logs[j]):
                logs.pop(j)
            else:
                i += 1 
        i = 0
        while(i < len(logs)):
            j = i
            count = 0
            while(logs[i][0] == logs[j][0]):
                count += 1
                j += 1
                if(j == len(logs)):
                    break
            a[count-1] = a[count-1]+1
            i = j
        return a
