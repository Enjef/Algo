class Solution:
    def makeConnected(self, n: int, connections):  # 5.04% 62.28%
        m = len(connections)
        if n - m - 1  > 0:
            return -1
        networks = []
        for host, target in connections:
            found = [-1, -2]
            for i, net in enumerate(networks):
                if host in net:
                    found[0] = i
                if target in net:
                    found[1] = i
            if found[0] == found[1]:
                networks[found[0]].update([host, target])
            elif found == [-1, -2]:
                networks.append(set([host, target]))
            elif found[0] != -1 and found[1] != -2:
                networks[found[0]].update(networks[found[1]])
                networks.pop(found[1])
            elif found[0] != -1:
                networks[found[0]].add(target)
            else:
                networks[found[1]].add(host)
        return n - sum([len(x)-1 for x in networks]) - 1
